```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/xml/tcp_445_smb_nmap.xml" 172.16.185.82
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:32:57 2024 as: nmap -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/xml/tcp_445_smb_nmap.xml 172.16.185.82
Nmap scan report for 172.16.185.82
Host is up, received user-set (0.23s latency).
Scanned at 2024-07-31 12:32:58 EDT for 49s

PORT    STATE SERVICE       REASON         VERSION
445/tcp open  microsoft-ds? syn-ack ttl 64
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
|_smb-print-text: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: EOF
| nbstat: NetBIOS name: CLIENT01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:0c:26 (VMware)
| Names:
|   CLIENT01<20>         Flags: <unique><active>
|   CLIENT01<00>         Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:0c:26:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
| smb2-time: 
|   date: 2024-07-31T16:33:18
|_  start_date: N/A
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
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: EOF
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 12:33:47 2024 -- 1 IP address (1 host up) scanned in 50.24 seconds

```
