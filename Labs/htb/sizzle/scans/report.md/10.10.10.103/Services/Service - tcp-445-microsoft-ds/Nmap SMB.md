```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:21:29 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp445/xml/tcp_445_smb_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.056s latency).
Scanned at 2025-02-11 10:21:29 EST for 52s

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
| smb2-time: 
|   date: 2025-02-11T15:21:56
|_  start_date: 2025-02-11T15:17:56
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-print-text: false

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:22:21 2025 -- 1 IP address (1 host up) scanned in 52.29 seconds

```
