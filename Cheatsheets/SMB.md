## NMAP 
### Enum
```
nmap --script smb-enum-domains.nse,smb-enum-groups.nse,smb-enum-processes.nse,smb-enum-services.nse,smb-enum-sessions.nse,smb-enum-shares.nse,smb-enum-users.nse -p 445 <target>
```
```
nmap --script "safe or smb-enum-*" -p 445 <IP>
```
### Vulnerability Detection
```
nmap --script smb-vuln-conficker.nse,smb-vuln-cve2009-3103.nse,smb-vuln-cve-2017-7494.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse,smb-vuln-regsvc-dos.nse,smb-vuln-webexec.nse -p 445 <target>
```
## Enum4linux
### Dump interesting information
```
enum4linux -a [-u "<username>" -p "<password"] <IP>
```
```
enum4linux-ng -A [-u "<username>" -p "<password>"] <IP>
```
## RPCclient
### Connect to the RPC
- No creds
```
rpcclient -U "" -N <IP>
```
- Hash login
```
rpcclient //SHARE -U domain.local/USERNAME%HASH --pw-nt-hash
```
- With creds 
```
rpcclient -U "username%password" <IP>
```
## Impacket
### Dump User Information
```
/usr/share/doc/python3-impacket/examples/samrdump.py -port 139 [[domain/]username[:password]@]<targetName or address>
```
```
/usr/share/doc/python3-impacket/examples/samrdump.py -port 445 [[domain/]username[:password]@]<targetName or address>
```
### Map possible RPC endpoints
```
/usr/share/doc/python3-impacket/examples/rpcdump.py -port 135 [[domain/]username[:password]@]<targetName or address>
```
```
/usr/share/doc/python3-impacket/examples/rpcdump.py -port 139 [[domain/]username[:password]@]<targetName or address>
```
```
/usr/share/doc/python3-impacket/examples/rpcdump.py -port 445 [[domain/]username[:password]@]<targetName or address>
```
### Anonymous login
```
smbclient --no-pass <IP>
```
