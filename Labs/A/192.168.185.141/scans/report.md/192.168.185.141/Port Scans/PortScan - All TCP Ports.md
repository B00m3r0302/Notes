```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_full_tcp_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:07:56 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_full_tcp_nmap.xml 192.168.185.141
Increasing send delay for 192.168.185.141 from 5 to 10 due to 11 out of 12 dropped probes since last increase.
Warning: Hit PCRE_ERROR_MATCHLIMIT when probing for service http with the regex '^HTTP/1\.1 \d\d\d (?:[^\r\n]*\r\n(?!\r\n))*?.*\r\nServer: Virata-EmWeb/R([\d_]+)\r\nContent-Type: text/html; ?charset=UTF-8\r\nExpires: .*<title>HP (Color |)LaserJet ([\w._ -]+)&nbsp;&nbsp;&nbsp;'
adjust_timeouts2: packet supposedly had rtt of -163683 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -163683 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -127968 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -127968 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -136284 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -136284 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -195870 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -195870 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -153880 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -153880 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -176800 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -176800 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -184133 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -184133 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -160126 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -160126 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -149418 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -149418 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -137012 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -137012 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -198018 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -198018 microseconds.  Ignoring time.
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.084s latency).
Scanned at 2024-08-05 22:07:57 EDT for 676s
Not shown: 65516 closed tcp ports (reset)
PORT      STATE SERVICE         REASON          VERSION
22/tcp    open  ssh             syn-ack ttl 125 OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 e0:3a:63:4a:07:83:4d:0b:6f:4e:8a:4d:79:3d:6e:4c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHi6qqQGQteAgLLakGf2MPORvtZSeF1gAL03sfUo/E/jsObuAOjzHPfw1OIfAyctU/gv17d0sz17kGDXbg4In4vxlnavXxnB/L2ipQLhAkFLo1YZLLwyUs0j1jiSW65Ax12A20nH0F3hbuqKsuWIPywR9XXc0cwhyY3ET06ZCbVVvP8ChGMd97uZTDeZtrnskYMXmqnfQpOGPL6e022+K5ud3MboyYXTlD0rGyVHyLCCXeg9QdxsVR5mZ8hSVCrwdX8Q4tb4kLYi+wpPx1KCirHEk/8O8I7YuA5KR4AeaMVSlqUhlm9MXaNw+5WZD2xOue0ZPCx2gxgKgndoUDfAagZrHr3dzgMUDgUnKTbtL/EIZdyzKh5C1TrN+yplSpqYjK975Q1qas7SUmzanN9S/PnhFFer/0j6hTtGlRalbxX12i2ifC0314ifnHY3Zz+2VD49RARArwvZR+7KcGKP+5tpCl9IyVf1xSKFFnJ0cQdhuAgJnkCfQXaQLHTzqSbys=
|   256 3f:16:ca:33:25:fd:a2:e6:bb:f6:b0:04:32:21:21:0b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOpOTM37eUD8SUKAqFVSNV8ECDl5yUqV7a41c39cXyPE6EMeNbKxWvQDoTw+WEYArHFAEj3SZbFupIZoZmvjFuA=
|   256 fe:b0:7a:14:bf:77:84:9a:b3:26:59:8d:ff:7e:92:84 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICyZUVdHOqTpEFyvELlmc7sCN1XFXQo7RdZdTRTPO2uJ
80/tcp    open  http            syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-generator: Nicepage 4.8.2, nicepage.com
|_http-title: Home
81/tcp    open  http            syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-title: Attendance and Payroll System
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
135/tcp   open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open  netbios-ssn     syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?   syn-ack ttl 125
3306/tcp  open  mysql           syn-ack ttl 125 MySQL (unauthorized)
3307/tcp  open  opsession-prxy? syn-ack ttl 125
| fingerprint-strings: 
|   Arucer, DistCCD, FourOhFourRequest, NJE, NoMachine, OpenVPN, Radmin, Socks4, metasploit-xmlrpc, ms-sql-s, oracle-tns, tarantool: 
|_    Host '192.168.45.166' is not allowed to connect to this MariaDB server
5040/tcp  open  unknown         syn-ack ttl 125
5985/tcp  open  http            syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http            syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
49665/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
49666/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
49667/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
49668/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
49669/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
49670/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
52783/tcp open  msrpc           syn-ack ttl 125 Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3307-TCP:V=7.94SVN%I=9%D=8/5%Time=66B185EB%P=x86_64-pc-linux-gnu%r(
SF:FourOhFourRequest,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20
SF:is\x20not\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20serve
SF:r")%r(DistCCD,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x
SF:20not\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%
SF:r(Radmin,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not
SF:\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(ora
SF:cle-tns,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\
SF:x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(Sock
SF:s4,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20al
SF:lowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(ms-sql-s,
SF:4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20allow
SF:ed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(Arucer,4D,"I
SF:\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20allowed\x2
SF:0to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(metasploit-xmlrpc
SF:,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20allo
SF:wed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(tarantool,4
SF:D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20allowe
SF:d\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(NJE,4D,"I\0\0
SF:\x01\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20allowed\x20to\
SF:x20connect\x20to\x20this\x20MariaDB\x20server")%r(OpenVPN,4D,"I\0\0\x01
SF:\xffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20allowed\x20to\x20c
SF:onnect\x20to\x20this\x20MariaDB\x20server")%r(NoMachine,4D,"I\0\0\x01\x
SF:ffj\x04Host\x20'192\.168\.45\.166'\x20is\x20not\x20allowed\x20to\x20con
SF:nect\x20to\x20this\x20MariaDB\x20server");
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows XP|2008|2019|7 (87%)
OS CPE: cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_server_2008 cpe:/o:microsoft:windows_7
Aggressive OS guesses: Microsoft Windows XP SP3 (87%), Microsoft Windows Server 2008 (85%), Microsoft Windows Server 2019 (85%), Microsoft Windows 7 (85%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=8/5%OT=22%CT=1%CU=44570%PV=Y%DS=4%DC=T%G=Y%TM=66B18
OS:821%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=10C%TS=U)SEQ(SP=102%GCD=1
OS:%ISR=10C%TI=I%TS=U)OPS(O1=M551NW8NNS%O2=M551NW8NNS%O3=M551NW8%O4=M551NW8
OS:NNS%O5=M551NW8NNS%O6=M551NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF
OS:%W6=FF70)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M551NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=80%
OS:S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+
OS:%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=
OS:G%RIPCK=G%RUCK=53FB%RUD=G)IE(R=N)

Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: -2s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 60269/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 59619/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 62215/udp): CLEAN (Failed to receive data)
|   Check 4 (port 46131/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time: 
|   date: 2024-08-06T02:18:46
|_  start_date: N/A

TRACEROUTE (using port 1723/tcp)
HOP RTT      ADDRESS
1   68.70 ms 192.168.45.1
2   68.58 ms 192.168.45.254
3   68.86 ms 192.168.251.1
4   68.51 ms 192.168.185.141

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:19:13 2024 -- 1 IP address (1 host up) scanned in 677.94 seconds

```
