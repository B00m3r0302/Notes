```bash
nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/xml/tcp_139_smb_nmap.xml" 172.16.185.10
```

[/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/tcp_139_smb_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/tcp_139_smb_nmap.txt):

```
# Nmap 7.94SVN scan initiated Thu Aug  1 10:35:42 2024 as: nmap -vv --reason -Pn -T4 -sV -p 139 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/tcp_139_smb_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/xml/tcp_139_smb_nmap.xml 172.16.185.10
Nmap scan report for 172.16.185.10
Host is up, received user-set (0.088s latency).
Scanned at 2024-08-01 10:35:42 EDT for 19s

PORT    STATE SERVICE     REASON         VERSION
139/tcp open  netbios-ssn syn-ack ttl 64 Microsoft Windows netbios-ssn
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:2d:3a (VMware)
| Names:
|   DC01<20>             Flags: <unique><active>
|   DC01<00>             Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
|   MEDTECH<1c>          Flags: <group><active>
|   MEDTECH<1b>          Flags: <unique><active>
| Statistics:
|   00:50:56:bf:2d:3a:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_smb-print-text: false
| smb2-time: 
|   date: 2024-08-01T14:35:51
|_  start_date: N/A
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: EOF
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: EOF
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
# Nmap done at Thu Aug  1 10:36:01 2024 -- 1 IP address (1 host up) scanned in 19.09 seconds

```
