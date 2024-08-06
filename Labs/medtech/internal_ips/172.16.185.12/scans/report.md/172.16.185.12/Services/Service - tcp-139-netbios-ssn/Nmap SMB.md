```bash
nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/xml/tcp_139_smb_nmap.xml" 172.16.185.12
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/tcp_139_smb_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/tcp_139_smb_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:33:11 2024 as: nmap -vv --reason -Pn -T4 -sV -p 139 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/tcp_139_smb_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/xml/tcp_139_smb_nmap.xml 172.16.185.12
Nmap scan report for 172.16.185.12
Host is up, received user-set (0.19s latency).
Scanned at 2024-07-31 12:33:12 EDT for 18s

PORT    STATE SERVICE     REASON         VERSION
139/tcp open  netbios-ssn syn-ack ttl 64 Microsoft Windows netbios-ssn
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: EOF
|_smb-print-text: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: EOF
| nbstat: NetBIOS name: DEV04, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:7b:40 (VMware)
| Names:
|   DEV04<00>            Flags: <unique><active>
|   DEV04<20>            Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:7b:40:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
| smb-protocols: 
|   dialects: 
|     2:0:2
|     2:1:0
|     3:0:0
|     3:0:2
|_    3:1:1
| smb2-time: 
|   date: 2024-07-31T16:33:19
|_  start_date: N/A
| smb2-capabilities: 
|   2:0:2: 
|     Distributed File System
|   2:1:0: 
|     Distributed File System
|     Leasing
|   3:0:0: 
|     Distributed File System
|     Leasing
|   3:0:2: 
|     Distributed File System
|     Leasing
|   3:1:1: 
|     Distributed File System
|_    Leasing

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 12:33:30 2024 -- 1 IP address (1 host up) scanned in 19.07 seconds

```
