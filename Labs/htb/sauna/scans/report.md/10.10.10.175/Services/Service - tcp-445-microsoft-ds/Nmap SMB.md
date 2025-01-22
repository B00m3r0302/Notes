```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.175
```

[/home/kali/Notes/Labs/htb/sauna/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.95 scan initiated Wed Jan 22 09:52:00 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/sauna/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/kali/Notes/Labs/htb/sauna/scans/tcp445/xml/tcp_445_smb_nmap.xml 10.10.10.175
Nmap scan report for 10.10.10.175
Host is up, received user-set (0.052s latency).
Scanned at 2025-01-22 09:52:11 EST for 51s

PORT    STATE SERVICE       REASON          VERSION
445/tcp open  microsoft-ds? syn-ack ttl 127
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-print-text: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb-protocols: 
|   dialects: 
|     2:0:2
|     2:1:0
|     3:0:0
|     3:0:2
|_    3:1:1
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-01-22T22:52:46
|_  start_date: N/A
| smb2-capabilities: 
|   2:0:2: 
|     Distributed File System
|   2:1:0: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3:0:0: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3:0:2: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3:1:1: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan 22 09:53:02 2025 -- 1 IP address (1 host up) scanned in 62.27 seconds

```
