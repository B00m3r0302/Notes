```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/blackfield/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/blackfield/scans/xml/_full_tcp_nmap.xml" 10.10.10.192
```

[/home/kali/Notes/Labs/htb/blackfield/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/htb/blackfield/scans/_full_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Sat Jan 25 10:52:23 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/htb/blackfield/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/htb/blackfield/scans/xml/_full_tcp_nmap.xml 10.10.10.192
Nmap scan report for 10.10.10.192
Host is up, received user-set (0.053s latency).
Scanned at 2025-01-25 10:52:24 EST for 648s
Not shown: 65527 filtered tcp ports (no-response)
PORT     STATE SERVICE       REASON          VERSION
53/tcp   open  domain        syn-ack ttl 127 (generic dns response: SERVFAIL)
| fingerprint-strings: 
|   DNS-SD-TCP: 
|     _services
|     _dns-sd
|     _udp
|_    local
88/tcp   open  kerberos-sec  syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-01-25 22:54:16Z)
135/tcp  open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
389/tcp  open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds? syn-ack ttl 127
593/tcp  open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
3268/tcp open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
5985/tcp open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.95%I=9%D=1/25%Time=67950938%P=x86_64-pc-linux-gnu%r(DNS-
SF:SD-TCP,30,"\0\.\0\0\x80\x82\0\x01\0\0\0\0\0\0\t_services\x07_dns-sd\x04
SF:_udp\x05local\0\0\x0c\0\x01");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10 (97%)
OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Windows Server 2019 (97%), Microsoft Windows 10 1903 - 21H1 (91%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.95%E=4%D=1/25%OT=53%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=67950B40%P=x86_64-pc-linux-gnu)
SEQ(SP=104%GCD=1%ISR=10A%TI=I%II=I%SS=S%TS=U)
SEQ(SP=F8%GCD=1%ISR=10D%TI=I%II=I%SS=S%TS=U)
OPS(O1=M53CNW8NNS%O2=M53CNW8NNS%O3=M53CNW8%O4=M53CNW8NNS%O5=M53CNW8NNS%O6=M53CNNS)
WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)
ECN(R=Y%DF=Y%TG=80%W=FFFF%O=M53CNW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-01-25T23:02:32
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: 6h59m59s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 48702/tcp): CLEAN (Timeout)
|   Check 2 (port 34369/tcp): CLEAN (Timeout)
|   Check 3 (port 53637/udp): CLEAN (Timeout)
|   Check 4 (port 56656/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE (using port 53/tcp)
HOP RTT      ADDRESS
1   54.78 ms 10.10.14.1
2   54.97 ms 10.10.10.192

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jan 25 11:03:12 2025 -- 1 IP address (1 host up) scanned in 648.52 seconds

```
