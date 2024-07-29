```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/xml/_full_tcp_nmap.xml" 192.168.227.121
```

[/home/kali/Notes/Labs/medtech/192.168.227.121/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.121/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Jul 29 07:55:21 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/medtech/192.168.227.121/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/192.168.227.121/scans/xml/_full_tcp_nmap.xml 192.168.227.121
Increasing send delay for 192.168.227.121 from 0 to 5 due to 418 out of 1044 dropped probes since last increase.
Increasing send delay for 192.168.227.121 from 5 to 10 due to 13 out of 31 dropped probes since last increase.
Warning: 192.168.227.121 giving up on port because retransmission cap hit (6).
Warning: Hit PCRE_ERROR_MATCHLIMIT when probing for service http with the regex '^HTTP/1\.1 \d\d\d (?:[^\r\n]*\r\n(?!\r\n))*?.*\r\nServer: Virata-EmWeb/R([\d_]+)\r\nContent-Type: text/html; ?charset=UTF-8\r\nExpires: .*<title>HP (Color |)LaserJet ([\w._ -]+)&nbsp;&nbsp;&nbsp;'
adjust_timeouts2: packet supposedly had rtt of -167097 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -167097 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -276771 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -276771 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -176848 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -176848 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -174514 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -174514 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -176279 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -176279 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -179708 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -179708 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -174052 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -174052 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -504411 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -504411 microseconds.  Ignoring time.
Nmap scan report for 192.168.227.121
Host is up, received user-set (0.078s latency).
Scanned at 2024-07-29 07:55:22 EDT for 978s
Not shown: 65515 closed tcp ports (reset)
PORT      STATE    SERVICE       REASON          VERSION
80/tcp    open     http          syn-ack ttl 125 Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: MedTech
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
135/tcp   open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open     netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp   open     microsoft-ds? syn-ack ttl 125
5985/tcp  open     http          syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
17042/tcp filtered unknown       no-response
36082/tcp filtered unknown       no-response
39874/tcp filtered unknown       no-response
47001/tcp open     http          syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47113/tcp filtered unknown       no-response
47820/tcp filtered unknown       no-response
49664/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
49665/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
49666/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
49667/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
49668/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
49669/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
49670/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
49671/tcp open     msrpc         syn-ack ttl 125 Microsoft Windows RPC
58844/tcp filtered unknown       no-response
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2022 (87%)
Aggressive OS guesses: Microsoft Windows Server 2022 (87%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/29%OT=80%CT=1%CU=42855%PV=Y%DS=4%DC=T%G=Y%TM=66A7
OS:86FC%P=x86_64-pc-linux-gnu)SEQ(SP=103%GCD=1%ISR=10E%TS=A)OPS(O1=M551NW8S
OS:T11%O2=M551NW8ST11%O3=M551NW8NNT11%O4=M551NW8ST11%O5=M551NW8ST11%O6=M551
OS:ST11)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFDC)ECN(R=Y%DF=Y%T=
OS:80%W=FFFF%O=M551NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2
OS:(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)
OS:T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=81D3%RUD=
OS:G)IE(R=N)

Uptime guess: 0.024 days (since Mon Jul 29 07:37:16 2024)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 18369/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 19543/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 26084/udp): CLEAN (Failed to receive data)
|   Check 4 (port 24583/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time: 
|   date: 2024-07-29T12:11:32
|_  start_date: N/A
|_clock-skew: 0s

TRACEROUTE (using port 8080/tcp)
HOP RTT      ADDRESS
1   81.70 ms 192.168.45.1
2   80.60 ms 192.168.45.254
3   80.79 ms 192.168.251.1
4   73.70 ms 192.168.227.121

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 29 08:11:40 2024 -- 1 IP address (1 host up) scanned in 979.24 seconds

```
