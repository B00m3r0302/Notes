```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/forest/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/xml/_full_tcp_nmap.xml" 10.10.10.161
```

[/home/kali/Notes/Labs/htb/forest/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/htb/forest/scans/_full_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 20 12:43:04 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/htb/forest/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/htb/forest/scans/xml/_full_tcp_nmap.xml 10.10.10.161
Nmap scan report for forest.htb.local (10.10.10.161)
Host is up, received user-set (0.053s latency).
Scanned at 2025-01-20 12:43:04 EST for 579s
Not shown: 65456 closed tcp ports (reset)
PORT      STATE    SERVICE       REASON          VERSION
53/tcp    open     domain        syn-ack ttl 127 (generic dns response: SERVFAIL)
| fingerprint-strings: 
|   DNS-SD-TCP: 
|     _services
|     _dns-sd
|     _udp
|_    local
88/tcp    open     kerberos-sec  syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-01-20 17:51:02Z)
135/tcp   open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open     netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp   open     ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp   open     microsoft-ds  syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
464/tcp   open     kpasswd5?     syn-ack ttl 127
593/tcp   open     ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open     tcpwrapped    syn-ack ttl 127
3268/tcp  open     ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
3269/tcp  open     tcpwrapped    syn-ack ttl 127
4028/tcp  filtered dtserver-port no-response
5985/tcp  open     http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9056/tcp  filtered unknown       no-response
9157/tcp  filtered unknown       no-response
9389/tcp  open     mc-nmf        syn-ack ttl 127 .NET Message Framing
10459/tcp filtered unknown       no-response
11177/tcp filtered unknown       no-response
13295/tcp filtered unknown       no-response
14226/tcp filtered unknown       no-response
14382/tcp filtered unknown       no-response
15109/tcp filtered unknown       no-response
15272/tcp filtered unknown       no-response
16430/tcp filtered unknown       no-response
18248/tcp filtered unknown       no-response
18817/tcp filtered unknown       no-response
21397/tcp filtered unknown       no-response
21735/tcp filtered unknown       no-response
22732/tcp filtered unknown       no-response
22973/tcp filtered unknown       no-response
23611/tcp filtered unknown       no-response
23727/tcp filtered unknown       no-response
24569/tcp filtered unknown       no-response
25438/tcp filtered unknown       no-response
25492/tcp filtered unknown       no-response
25985/tcp filtered unknown       no-response
26340/tcp filtered unknown       no-response
26627/tcp filtered unknown       no-response
26871/tcp filtered unknown       no-response
27225/tcp filtered unknown       no-response
27971/tcp filtered unknown       no-response
28723/tcp filtered unknown       no-response
28774/tcp filtered unknown       no-response
29550/tcp filtered unknown       no-response
31395/tcp filtered unknown       no-response
31963/tcp filtered unknown       no-response
33071/tcp filtered unknown       no-response
35110/tcp filtered unknown       no-response
36504/tcp filtered unknown       no-response
36624/tcp filtered unknown       no-response
37465/tcp filtered unknown       no-response
37508/tcp filtered unknown       no-response
39390/tcp filtered unknown       no-response
39812/tcp filtered unknown       no-response
40929/tcp filtered unknown       no-response
41987/tcp filtered unknown       no-response
46565/tcp filtered unknown       no-response
46589/tcp filtered unknown       no-response
47001/tcp open     http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
48293/tcp filtered unknown       no-response
49664/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49666/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49671/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49676/tcp open     ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49677/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49684/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49706/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
49979/tcp open     msrpc         syn-ack ttl 127 Microsoft Windows RPC
51546/tcp filtered unknown       no-response
56620/tcp filtered unknown       no-response
58791/tcp filtered unknown       no-response
59266/tcp filtered unknown       no-response
59413/tcp filtered unknown       no-response
60556/tcp filtered unknown       no-response
60811/tcp filtered unknown       no-response
60891/tcp filtered unknown       no-response
64529/tcp filtered unknown       no-response
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.95%I=9%D=1/20%Time=678E8B79%P=x86_64-pc-linux-gnu%r(DNS-
SF:SD-TCP,30,"\0\.\0\0\x80\x82\0\x01\0\0\0\0\0\0\t_services\x07_dns-sd\x04
SF:_udp\x05local\0\0\x0c\0\x01");
Aggressive OS guesses: Microsoft Windows Server 2012 or 2012 R2 (97%), Microsoft Windows Server 2016 or Server 2019 (96%), Microsoft Windows Server 2012 (95%), Microsoft Windows Vista SP2 or Windows 7 or Windows Server 2008 R2 or Windows 8.1 (94%), Microsoft Windows 10 1703 or Windows 11 21H2 (94%), Microsoft Windows 10 1507 (93%), Microsoft Windows 10 1507 - 1607 (93%), Microsoft Windows Server 2012 R2 (93%), Microsoft Windows Server 2012 R2 Update 1 (93%), Microsoft Windows 7, Windows Server 2012, or Windows 8.1 Update 1 (93%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.95%E=4%D=1/20%OT=53%CT=1%CU=38905%PV=Y%DS=2%DC=T%G=Y%TM=678E8D6
OS:B%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=110%TI=I%CI=I%II=I%SS=S%TS=
OS:A)SEQ(SP=103%GCD=1%ISR=106%TI=I%CI=I%II=I%SS=S%TS=A)SEQ(SP=105%GCD=1%ISR
OS:=10D%TI=I%CI=I%II=I%SS=S%TS=A)SEQ(SP=105%GCD=2%ISR=108%TI=I%CI=I%II=I%SS
OS:=S%TS=A)SEQ(SP=106%GCD=2%ISR=10B%TI=I%CI=I%II=I%SS=S%TS=A)OPS(O1=M53CNW8
OS:ST11%O2=M53CNW8ST11%O3=M53CNW8NNT11%O4=M53CNW8ST11%O5=M53CNW8ST11%O6=M53
OS:CST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=2000)ECN(R=Y%DF=Y%T
OS:=80%W=2000%O=M53CNW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T
OS:2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O
OS:%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y
OS:%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%R
OS:D=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IP
OS:L=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Uptime guess: 3.193 days (since Fri Jan 17 08:15:11 2025)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: FOREST; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-01-20T17:59:26
|_  start_date: 2025-01-17T13:22:26
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 32753/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 5568/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 44587/udp): CLEAN (Failed to receive data)
|   Check 4 (port 51719/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: FOREST
|   NetBIOS computer name: FOREST\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: FOREST.htb.local
|_  System time: 2025-01-20T09:59:25-08:00
|_clock-skew: mean: 2h46m52s, deviation: 4h37m09s, median: 6m51s
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   51.70 ms 10.10.14.1
2   51.77 ms forest.htb.local (10.10.10.161)

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 20 12:52:43 2025 -- 1 IP address (1 host up) scanned in 579.35 seconds

```
