## Section 2 Passive Information Gathering

### Subsection 6.2.1 Whois Enumeration
```
whois DOMAIN-NAME
```
```
whois IP
```
```
whois DOMAIN-NAME -h DNS-IP
```
- To get an IP address from the A record of the domain host 
```
host DOMAIN-NAME
```
- To get additional records or specific types like the following add the -t flag
	- NS
	- MX
	- etc.
```
host -t TYPE_OF_RECORD DOMAIN-NAME
```
- One-liner reverse loopup to request the hostname for an IP in a range of IPs
```
for ip in $(seq IP-RANGE ex. 200 254); do xxx.xxx.xxx.$ip; done | grep -v "not found"
```
- dnsenum regular
```
dnsenum DOMAIN_NAME
```
- dnsrecon standard scan
```
dnsrecon -d DOMAIN_NAME -t std
```
- dnsrecon brute force subdomains one-liner
```
dnsrecon -d DOMAIN_NAME -D SUBDOMAIN_WORD_LIST -t brt
```
- Windows dns enumeration == nslookup
```
nslookup DOMAIN_NAME
```
```
nslookup -t TYPE_OF_RECORD DOMAIN_NAME DNS_OR_DC_IP
```
- Reverse lookup whois for an internal IP
```
whois InternalIP -h DNS-IP OR DC
```

## Section 3 Active Information Gathering
### Subsection 6.3.2 TCP/UDP Port Scanning Theory
- nc tcp scan
```
nc -nvv -w 1 -z IP PORT-RANGE
```
### Subsection  6.3.3 Port Scanning With NMAP
- The -A option on nmap does the following 
	- OS and version detection
	- Traceroute
	- Script scanning
- OS guessing with nmap
```
nmap -O IP --osscan-guess
```
- To get more information on an NMAP NSE scripts use the following 
```
nmap --script-help SCRIPT_NAME
OR 
cat the script file and read the description
```
- NMAP NSE scripts are located in /usr/share/nmap/scripts
```
ls -l /usr/share/nmap/scripts/SERVICE_OR_KEYWORD
```
- Update the NMAP script database with 
```
sudo nmap --script-updatedb
```
- In powershell the following command can be used to see if a port is active 
```
Test-NetConnection -Port PORT IP
```
- One-liner to find top 1024 open ports in powershell 
```
powershell 1..1024| %{echo ((New-Object Net.Sockets.TcpClient).Connect("IP", $_)) "TCP port $_ is open"}2>$null
```
- Another way to do this which could be used on a domain controller
```
foreach ($port in 1..1024) {if (($a=Test-NetConnection IP -Port $port -WarningAction SilentlyContinue).tcpTestSucceded -eq $true){ "TCP port $port is open"}
```
### Subsection 6.3.4 SMB Enumeration
- view shares on dc01 (domain controller 01) in windows cmd or powershell
```
net view \\dc01 /all
```
- To query NetBIOS name service for valid NetBIOS names
```
sudo nbtscan -r IP/24OR_IP_RANGE_CIDR
```
- python script to find user alfred using enum4linux for multiple IP addresses
```
import subprocess 

# smb_list.txt is a file with one ip on each line

def run_enum4linux(file_path):
	with open(file_path, 'r') as file:
		for line in file:
			ip = line.strip()
			if ip:
				subprocess.run(["enum4linux", "-u", "alfred", "-S", ip])
if __name__ = "__main__"
	run_enum4linux(smb_list.txt)
```
### Subsection 6.3.5 SMTP Enumration
- Two types of requests 
	- VRFY asks the server to verify an email address
		- 252 == exists
		- 550 == does not exist
	- EXPN asks the server for the membership of a mailing list 
- Python script to connect to a socket and verify a user
```
#! /usr/bin/python3

import socket
import sys

if len(sys.argv) != 3:
	Print("Usage: verfy.py <username> <target_ip>")
	sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = sys.argv[2]
connect = s.connect((ip,25))
banner = s.recv(1024)

Print(banner)

user = (sys.argv[1].encode())

s.send(b'VRFY ' + user + b'\r\n')

result = s.recv(1024)

Print(result)

s.close()
```
- Windows: if you are a high privileged user you can install the Windows version of telnet to work with SMTP in the command line with the following commands 
```
dism /online /Enable-Feature /FeatureName:TelnetClient
```
```
telnet IP PORT
```
### Subsection 6.3.6 SNMP Enumeration
- protocols 1,2, and 2c offer no traffic encryption
	- This means SNMP information on these protocols can be easily intercepted over a local network
- Traditional SNMP protocols often have weak authentication schemas and are commonly left configured with default public and private community strings
	- Because of this they should be a favored enumeration protocol
- onesixtyone will attempt a brute force attack against a list of IP addresses with a text file of community strings and a text file of ip addresses 
```
# can also use a wordlist from seclists 
echo public > community
echo private >> community
echo manager >> community
```
```
for ip in $(seq 1 254); do echo xxx.xxx.xxx.$ip; done > ips
```
```
onesixtyone -c community -i ips
```
- snmpwalk requires that we know the read-only community string and can give additional information like target email addresses
```
snmpwalk -c COMMUNITY_STRING -v VERSION -t 10 IP
```
- Further enumeration with snmpwalk using MIB Values
```
snmpwalk -c COMMUNITY_STRING -v VERSION IP MIB_VALUE
```
## Exercises To-Do

- [x] 1.1.1 (page 10)
- [ ] 1.1.2 (page 12)