```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/xml/_full_tcp_nmap.xml" 192.168.196.145
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:44 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/xml/_full_tcp_nmap.xml 192.168.196.145
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
adjust_timeouts2: packet supposedly had rtt of 8418312 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8418312 microseconds.  Ignoring time.
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
adjust_timeouts2: packet supposedly had rtt of 8201492 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8201492 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9750297 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9750297 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8289380 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8289380 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -1772700 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -2956055 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -2956055 microseconds.  Ignoring time.
Nmap scan report for 192.168.196.145
Host is up, received user-set (1.00s latency).
Scanned at 2024-08-21 13:00:45 EDT for 2514s
Not shown: 65527 filtered tcp ports (no-response)
PORT     STATE SERVICE       REASON          VERSION
21/tcp   open  ftp           syn-ack ttl 125 Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
80/tcp   open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
|_http-title: Samuel's Personal Site
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-favicon: Unknown favicon MD5: 556F31ACD686989B1AFCF382C05846AA
135/tcp  open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack ttl 125
1978/tcp open  unisql?       syn-ack ttl 125
| fingerprint-strings: 
|   GenericLines, GetRequest, HTTPOptions, NULL: 
|_    system windows 6.2
3389/tcp open  ms-wbt-server syn-ack ttl 125 Microsoft Terminal Services
| ssl-cert: Subject: commonName=oscp
| Issuer: commonName=oscp
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-06-01T17:05:40
| Not valid after:  2024-12-01T17:05:40
| MD5:   6309:abf7:43ed:e13c:17e9:a283:69a9:be3b
| SHA-1: 312e:8c85:4523:5112:d449:e540:131c:0537:c681:8035
| -----BEGIN CERTIFICATE-----
| MIICzDCCAbSgAwIBAgIQFn6cU7xPqoFBR9Ur1G7qgDANBgkqhkiG9w0BAQsFADAP
| MQ0wCwYDVQQDEwRvc2NwMB4XDTI0MDYwMTE3MDU0MFoXDTI0MTIwMTE3MDU0MFow
| DzENMAsGA1UEAxMEb3NjcDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
| AMD9K+YsLeBS1LRz547xDIZAoQ1frDd/MJmUqkHtu7hpTnTMLuodk0TKJNwctYjK
| A/M4blu/k5MO4bKF5+jY38CUR8xUfGLhb6ujNIjxmk7pbGbZ7ri9JdQODHhZHYsp
| 22tRO8ndivctBR7VVRQrQYVk8S3LJeYJvCHq9HN0RYWSCqOUMmLksUpZHg4Fjhci
| 4WH5nLE2C8v6HK2ZHhc0+0l/GCAEzn73qY7QCa61nxbYQrtX6nZXzWxc4PI/FuQL
| 8u+u4qz2FjxBJffUA+sbFRO0erD5QbIwckwkWtDoCx6bJ7X0X10mDEJNAhA+YDU2
| SQZdKGuy6BaDDY1nWZEFti0CAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEw
| CwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQAhA9ETadHx5hcg6Prp0frB
| lJBDU0BI9SP8F1uoxrA95NKL62UzPKvPmAvsxBIsq/DAI+tcgA01xhHRvFP1m+PY
| HXakGGHADMbseQps+bk4TWwOd0idPW6tA6z+tMrESPCgSnEMoXntTiDYRD59KzXo
| GzUgjFqgcshQuCqiuYxVFQKBLubHUmvu9ZlAQndKZGiXSNRQpWAbqJGbR/BUqVl0
| mABTRrvbPgNp7cHgeVXyvlh/mh6ClqOYx4ZsRlGhaW0jCqPUoDhmu6towHPss1qc
| GAZzfUBPTrd8BYLDSoVzW4ftAs9/I44EtotqKahOt3YhgROY97gIvF64cvKlmDRe
|_-----END CERTIFICATE-----
|_ssl-date: 2024-08-21T17:42:26+00:00; -2s from scanner time.
7680/tcp open  tcpwrapped    syn-ack ttl 125
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1978-TCP:V=7.94SVN%I=9%D=8/21%Time=66C6267B%P=aarch64-unknown-linux
SF:-gnu%r(NULL,14,"system\x20windows\x206\.2\n\n")%r(GenericLines,14,"syst
SF:em\x20windows\x206\.2\n\n")%r(GetRequest,14,"system\x20windows\x206\.2\
SF:n\n")%r(HTTPOptions,14,"system\x20windows\x206\.2\n\n");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows XP (89%)
OS CPE: cpe:/o:microsoft:windows_xp::sp3
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows XP SP3 (89%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=21%CT=%CU=%PV=Y%DS=4%DC=T%G=N%TM=66C6270F%P=aarch64-unknown-linux-gnu)
SEQ(SP=103%GCD=1%ISR=106%TS=U)
SEQ(SP=104%GCD=1%ISR=10A%TI=I%TS=U)
OPS(O1=M551NW8NNS%O2=M551NW8NNS%O3=M551NW8%O4=M551NW8NNS%O5=M551NW8NNS%O6=M551NNS)
WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)
ECN(R=Y%DF=Y%TG=80%W=FFFF%O=M551NW8NNS%CC=N%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=N)

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
|   Check 1 (port 57021/tcp): CLEAN (Timeout)
|   Check 2 (port 50019/tcp): CLEAN (Timeout)
|   Check 3 (port 57666/udp): CLEAN (Timeout)
|   Check 4 (port 41784/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_clock-skew: mean: -1s, deviation: 1s, median: -2s
| smb2-time: 
|   date: 2024-08-21T17:41:45
|_  start_date: N/A

TRACEROUTE (using port 21/tcp)
HOP RTT       ADDRESS
1   812.77 ms 192.168.45.1
2   812.54 ms 192.168.45.254
3   813.11 ms 192.168.251.1
4   813.19 ms 192.168.196.145

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:42:39 2024 -- 1 IP address (1 host up) scanned in 2515.11 seconds

```
