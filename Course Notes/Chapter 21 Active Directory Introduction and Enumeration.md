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
## Exercises To-Do

- [ ] 2.1.1 (page 20)