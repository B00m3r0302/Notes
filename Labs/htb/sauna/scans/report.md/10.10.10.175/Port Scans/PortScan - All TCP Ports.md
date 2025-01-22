```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/sauna/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/xml/_full_tcp_nmap.xml" 10.10.10.175
```

[/home/kali/Notes/Labs/htb/sauna/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/_full_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Wed Jan 22 09:48:47 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/htb/sauna/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/htb/sauna/scans/xml/_full_tcp_nmap.xml 10.10.10.175
Increasing send delay for 10.10.10.175 from 0 to 5 due to 31 out of 77 dropped probes since last increase.
Increasing send delay for 10.10.10.175 from 5 to 10 due to 11 out of 11 dropped probes since last increase.
Warning: Hit PCRE_ERROR_MATCHLIMIT when probing for service http with the regex '^HTTP/1\.1 \d\d\d (?:[^\r\n]*\r\n(?!\r\n))*?.*\r\nServer: Virata-EmWeb/R([\d_]+)\r\nContent-Type: text/html; ?charset=UTF-8\r\nExpires: .*<title>HP (Color |)LaserJet ([\w._ -]+)&nbsp;&nbsp;&nbsp;'
Nmap scan report for 10.10.10.175
Host is up, received user-set (0.058s latency).
Scanned at 2025-01-22 09:48:58 EST for 1839s
Not shown: 65516 filtered tcp ports (no-response)
PORT      STATE SERVICE       REASON          VERSION
53/tcp    open  domain        syn-ack ttl 127 Simple DNS Plus
80/tcp    open  http          syn-ack ttl 127 Microsoft IIS httpd 10.0
88/tcp    open  kerberos-sec  syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-01-22 23:16:35Z)
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: EGOTISTICAL-BANK.LOCAL0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack ttl 127
464/tcp   open  kpasswd5?     syn-ack ttl 127
593/tcp   open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped    syn-ack ttl 127
3269/tcp  open  tcpwrapped    syn-ack ttl 127
5985/tcp  open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        syn-ack ttl 127 .NET Message Framing
49667/tcp open  unknown       syn-ack ttl 127
49673/tcp open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49674/tcp open  unknown       syn-ack ttl 127
49677/tcp open  unknown       syn-ack ttl 127
49695/tcp open  unknown       syn-ack ttl 127
49718/tcp open  unknown       syn-ack ttl 127
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.95%E=4%D=1/22%OT=53%CT=%CU=%PV=Y%G=N%TM=67910C89%P=x86_64-pc-linux-gnu)
SEQ()
ECN(R=N)
T1(R=N)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=N)

Service Info: Host: SAUNA; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 35558/tcp): CLEAN (Timeout)
|   Check 2 (port 50490/tcp): CLEAN (Timeout)
|   Check 3 (port 57297/udp): CLEAN (Timeout)
|   Check 4 (port 32549/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_smb2-security-mode: Couldn't establish a SMBv2 connection.

TRACEROUTE (using port 139/tcp)
HOP RTT    ADDRESS
1   ... 30

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan 22 10:19:37 2025 -- 1 IP address (1 host up) scanned in 1849.45 seconds

```
