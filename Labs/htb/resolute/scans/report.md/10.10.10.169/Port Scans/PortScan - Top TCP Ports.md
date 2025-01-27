```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/resolute/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/xml/_quick_tcp_nmap.xml" 10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Sun Jan 26 20:13:35 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/htb/resolute/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/htb/resolute/scans/xml/_quick_tcp_nmap.xml 10.10.10.169
Increasing send delay for 10.10.10.169 from 0 to 5 due to 175 out of 437 dropped probes since last increase.
Increasing send delay for 10.10.10.169 from 5 to 10 due to 11 out of 17 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -140343 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -140343 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -95190 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -95190 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -121994 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -121994 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -122984 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -122984 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120413 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120413 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -96470 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -96470 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -124122 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -124122 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120110 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120110 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120907 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120907 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -97472 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -97472 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -124200 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -124200 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -122592 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -122592 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -123583 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -123583 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -98442 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -98442 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -122545 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -122545 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -124428 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -124428 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -123123 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -123123 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.169
Host is up, received user-set (0.052s latency).
Scanned at 2025-01-26 20:13:36 EST for 124s
Not shown: 988 closed tcp ports (reset)
PORT     STATE SERVICE      REASON          VERSION
53/tcp   open  domain       syn-ack ttl 127 Simple DNS Plus
88/tcp   open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-01-27 01:21:57Z)
135/tcp  open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp  open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp  open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: megabank.local, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds (workgroup: MEGABANK)
464/tcp  open  kpasswd5?    syn-ack ttl 127
593/tcp  open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped   syn-ack ttl 127
3268/tcp open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: megabank.local, Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped   syn-ack ttl 127
5985/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Aggressive OS guesses: Microsoft Windows Server 2012 or 2012 R2 (97%), Microsoft Windows Server 2016 or Server 2019 (96%), Microsoft Windows Server 2016 (95%), Microsoft Windows Server 2012 (94%), Microsoft Windows Vista SP2 or Windows 7 or Windows Server 2008 R2 or Windows 8.1 (94%), Microsoft Windows 10 1703 or Windows 11 21H2 (94%), Microsoft Windows 10 (93%), Microsoft Windows 10 1507 (93%), Microsoft Windows 10 1507 - 1607 (93%), Microsoft Windows 10 1511 (93%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.95%E=4%D=1/26%OT=53%CT=1%CU=40066%PV=Y%DS=2%DC=T%G=Y%TM=6796DE3
OS:C%P=x86_64-pc-linux-gnu)SEQ(SP=103%GCD=1%ISR=108%CI=I%II=I%TS=A)SEQ(SP=1
OS:05%GCD=1%ISR=10A%CI=I%II=I%TS=A)SEQ(SP=107%GCD=1%ISR=109%CI=I%II=I%TS=A)
OS:SEQ(SP=FD%GCD=1%ISR=107%CI=I%II=I%TS=A)SEQ(SP=FF%GCD=1%ISR=10D%CI=I%II=I
OS:%TS=A)OPS(O1=M53CNW8ST11%O2=M53CNW8ST11%O3=M53CNW8NNT11%O4=M53CNW8ST11%O
OS:5=M53CNW8ST11%O6=M53CST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6
OS:=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M53CNW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O
OS:%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%D
OS:F=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=
OS:%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%
OS:W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=
OS:)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%
OS:DFI=N%T=80%CD=Z)

Uptime guess: 0.006 days (since Sun Jan 26 20:06:34 2025)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: Host: RESOLUTE; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Resolute
|   NetBIOS computer name: RESOLUTE\x00
|   Domain name: megabank.local
|   Forest name: megabank.local
|   FQDN: Resolute.megabank.local
|_  System time: 2025-01-26T17:22:29-08:00
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
|_clock-skew: mean: 2h47m01s, deviation: 4h37m09s, median: 7m00s
| smb2-time: 
|   date: 2025-01-27T01:22:30
|_  start_date: 2025-01-27T01:13:52
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 52471/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 47337/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 55070/udp): CLEAN (Timeout)
|   Check 4 (port 30335/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE (using port 10628/tcp)
HOP RTT      ADDRESS
1   51.05 ms 10.10.14.1
2   51.11 ms 10.10.10.169

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jan 26 20:15:40 2025 -- 1 IP address (1 host up) scanned in 124.49 seconds

```
