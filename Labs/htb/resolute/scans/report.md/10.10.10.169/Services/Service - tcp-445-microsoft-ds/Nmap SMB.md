```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.95 scan initiated Sun Jan 26 20:15:40 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/resolute/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/kali/Notes/Labs/htb/resolute/scans/tcp445/xml/tcp_445_smb_nmap.xml 10.10.10.169
Nmap scan report for 10.10.10.169
Host is up, received user-set (0.052s latency).
Scanned at 2025-01-26 20:15:41 EST for 119s

PORT    STATE SERVICE      REASON          VERSION
445/tcp open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds (workgroup: MEGABANK)
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
Service Info: Host: RESOLUTE; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb-mbenum: 
|_  ERROR: Call to Browser Service failed with status = 2184
| smb2-time: 
|   date: 2025-01-27T01:22:59
|_  start_date: 2025-01-27T01:13:52
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2:0:2
|     2:1:0
|     3:0:0
|     3:0:2
|_    3:1:1
|_smb-print-text: false
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
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
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Resolute
|   NetBIOS computer name: RESOLUTE\x00
|   Domain name: megabank.local
|   Forest name: megabank.local
|   FQDN: Resolute.megabank.local
|_  System time: 2025-01-26T17:23:03-08:00
| smb-enum-domains: 
|   MEGABANK
|     Groups: Cert Publishers, RAS and IAS Servers, Allowed RODC Password Replication Group, Denied RODC Password Replication Group, DnsAdmins
|     Users: Administrator, Guest, krbtgt, DefaultAccount, ryan, marko, sunita, abigail, marcus, sally, fred, angela, felicia, gustavo, ulf, stevie
|     Creation time: 2025-01-27T01:13:42
|     Passwords: min length: 7; min age: 1.0 days; max age: n/a days; history: 24 passwords
|     Account lockout disabled
|   Builtin
|     Groups: Account Operators, Pre-Windows 2000 Compatible Access, Incoming Forest Trust Builders, Windows Authorization Access Group, Terminal Server License Servers, Administrators, Users, Guests, Print Operators, Backup Operators, Replicator, Remote Desktop Users, Network Configuration Operators, Performance Monitor Users, Performance Log Users, Distributed COM Users, IIS_IUSRS, Cryptographic Operators, Event Log Readers, Certificate Service DCOM Access, RDS Remote Access Servers, RDS Endpoint Servers, RDS Management Servers, Hyper-V Administrators, Access Control Assistance Operators, Remote Management Users, System Managed Accounts Group, Storage Replica Administrators, Server Operators
|     Users: n/a
|     Creation time: 2016-07-16T13:19:09
|     Passwords: min length: n/a; min age: n/a days; max age: 42 days; history: n/a passwords
|_    Account lockout disabled
| smb-enum-users: 
|   MEGABANK\abigail (RID: 6602)
|     Flags:       Normal user account
|   MEGABANK\Administrator (RID: 500)
|     Description: Built-in account for administering the computer/domain
|     Flags:       Normal user account, Password does not expire
|   MEGABANK\angela (RID: 6606)
|     Flags:       Normal user account
|   MEGABANK\annette (RID: 6614)
|     Flags:       Normal user account
|   MEGABANK\annika (RID: 6615)
|     Flags:       Normal user account
|   MEGABANK\claire (RID: 6611)
|     Flags:       Normal user account
|   MEGABANK\claude (RID: 6617)
|     Flags:       Normal user account
|   MEGABANK\DefaultAccount (RID: 503)
|     Description: A user account managed by the system.
|     Flags:       Password not required, Normal user account, Account disabled, Password does not expire
|   MEGABANK\felicia (RID: 6607)
|     Flags:       Normal user account
|   MEGABANK\fred (RID: 6605)
|     Flags:       Normal user account
|   MEGABANK\Guest (RID: 501)
|     Description: Built-in account for guest access to the computer/domain
|     Flags:       Password not required, Normal user account, Account disabled, Password does not expire
|   MEGABANK\gustavo (RID: 6608)
|     Flags:       Normal user account
|   MEGABANK\krbtgt (RID: 502)
|     Description: Key Distribution Center Service Account
|     Flags:       Normal user account, Account disabled
|   MEGABANK\marcus (RID: 6603)
|     Flags:       Normal user account
|   MEGABANK\marko (RID: 1111)
|     Full name:   Marko Novak
|     Description: Account created. Password set to Welcome123!
|     Flags:       Normal user account, Password does not expire
|   MEGABANK\melanie (RID: 10101)
|     Flags:       Normal user account
|   MEGABANK\naoki (RID: 10104)
|     Flags:       Normal user account
|   MEGABANK\paulo (RID: 6612)
|     Flags:       Normal user account
|   MEGABANK\per (RID: 6616)
|     Flags:       Normal user account
|   MEGABANK\ryan (RID: 1105)
|     Full name:   Ryan Bertrand
|_    Flags:       Normal user account, Password does not expire

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jan 26 20:17:40 2025 -- 1 IP address (1 host up) scanned in 119.28 seconds

```
