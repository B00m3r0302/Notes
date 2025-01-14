```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/flight/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/flight/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.11.187
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 18:21:21 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/flight/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/kali/Notes/Labs/htb/flight/scans/tcp445/xml/tcp_445_smb_nmap.xml 10.10.11.187
Nmap scan report for 10.10.11.187
Host is up, received user-set (0.090s latency).
Scanned at 2025-01-13 18:21:22 EST for 51s

PORT    STATE SERVICE       REASON          VERSION
445/tcp open  microsoft-ds? syn-ack ttl 127
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
| smb-protocols: 
|   dialects: 
|     2:0:2
|     2:1:0
|     3:0:0
|     3:0:2
|_    3:1:1
|_smb-print-text: false
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
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-01-14T06:21:48
|_  start_date: N/A
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 18:22:13 2025 -- 1 IP address (1 host up) scanned in 52.96 seconds

```
