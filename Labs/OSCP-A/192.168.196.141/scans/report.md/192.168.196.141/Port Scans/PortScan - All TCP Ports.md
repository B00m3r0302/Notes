```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/xml/_full_tcp_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/xml/_full_tcp_nmap.xml 192.168.196.141
Warning: 192.168.196.141 giving up on port because retransmission cap hit (6).
adjust_timeouts2: packet supposedly had rtt of -4157428 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -4219356 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -4219356 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -7496642 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -7496642 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -10707101 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -10707101 microseconds.  Ignoring time.
Nmap scan report for 192.168.196.141
Host is up, received user-set (0.68s latency).
Scanned at 2024-08-21 13:00:02 EDT for 2270s
Not shown: 65483 closed tcp ports (reset)
PORT      STATE    SERVICE         REASON          VERSION
22/tcp    open     ssh             syn-ack ttl 125 OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 e0:3a:63:4a:07:83:4d:0b:6f:4e:8a:4d:79:3d:6e:4c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHi6qqQGQteAgLLakGf2MPORvtZSeF1gAL03sfUo/E/jsObuAOjzHPfw1OIfAyctU/gv17d0sz17kGDXbg4In4vxlnavXxnB/L2ipQLhAkFLo1YZLLwyUs0j1jiSW65Ax12A20nH0F3hbuqKsuWIPywR9XXc0cwhyY3ET06ZCbVVvP8ChGMd97uZTDeZtrnskYMXmqnfQpOGPL6e022+K5ud3MboyYXTlD0rGyVHyLCCXeg9QdxsVR5mZ8hSVCrwdX8Q4tb4kLYi+wpPx1KCirHEk/8O8I7YuA5KR4AeaMVSlqUhlm9MXaNw+5WZD2xOue0ZPCx2gxgKgndoUDfAagZrHr3dzgMUDgUnKTbtL/EIZdyzKh5C1TrN+yplSpqYjK975Q1qas7SUmzanN9S/PnhFFer/0j6hTtGlRalbxX12i2ifC0314ifnHY3Zz+2VD49RARArwvZR+7KcGKP+5tpCl9IyVf1xSKFFnJ0cQdhuAgJnkCfQXaQLHTzqSbys=
|   256 3f:16:ca:33:25:fd:a2:e6:bb:f6:b0:04:32:21:21:0b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOpOTM37eUD8SUKAqFVSNV8ECDl5yUqV7a41c39cXyPE6EMeNbKxWvQDoTw+WEYArHFAEj3SZbFupIZoZmvjFuA=
|   256 fe:b0:7a:14:bf:77:84:9a:b3:26:59:8d:ff:7e:92:84 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICyZUVdHOqTpEFyvELlmc7sCN1XFXQo7RdZdTRTPO2uJ
80/tcp    open     http            syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-generator: Nicepage 4.8.2, nicepage.com
|_http-title: Home
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
81/tcp    open     http            syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
| http-methods: 
|_  Supported Methods: OPTIONS
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
|_http-title: Attendance and Payroll System
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
135/tcp   open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open     netbios-ssn     syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp   open     microsoft-ds?   syn-ack ttl 125
3306/tcp  open     mysql           syn-ack ttl 125 MySQL (unauthorized)
3307/tcp  open     opsession-prxy? syn-ack ttl 125
| fingerprint-strings: 
|   NCP, NessusTPv12, RPCCheck, Radmin, TLSSessionReq: 
|_    Host '192.168.45.234' is not allowed to connect to this MariaDB server
4054/tcp  filtered ccu-comm-2      no-response
5040/tcp  open     unknown         syn-ack ttl 125
5985/tcp  open     http            syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
7181/tcp  filtered janus-disc      no-response
7805/tcp  filtered unknown         no-response
8298/tcp  filtered unknown         no-response
9408/tcp  filtered unknown         no-response
14229/tcp filtered unknown         no-response
26448/tcp filtered unknown         no-response
26907/tcp filtered unknown         no-response
29027/tcp filtered unknown         no-response
29062/tcp filtered unknown         no-response
29387/tcp filtered unknown         no-response
31244/tcp filtered unknown         no-response
32585/tcp filtered unknown         no-response
33901/tcp filtered unknown         no-response
34809/tcp filtered unknown         no-response
37609/tcp filtered unknown         no-response
39152/tcp filtered unknown         no-response
41985/tcp filtered unknown         no-response
43056/tcp filtered unknown         no-response
44146/tcp filtered unknown         no-response
44934/tcp filtered unknown         no-response
46246/tcp filtered unknown         no-response
46833/tcp filtered unknown         no-response
47001/tcp open     http            syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
48716/tcp filtered unknown         no-response
49664/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
49665/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
49666/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
49667/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
49668/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
49669/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
49670/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
49805/tcp filtered unknown         no-response
51462/tcp filtered unknown         no-response
52783/tcp open     msrpc           syn-ack ttl 125 Microsoft Windows RPC
53228/tcp filtered unknown         no-response
55597/tcp filtered unknown         no-response
55941/tcp filtered unknown         no-response
57180/tcp filtered unknown         no-response
62548/tcp filtered unknown         no-response
62788/tcp filtered unknown         no-response
64129/tcp filtered unknown         no-response
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3307-TCP:V=7.94SVN%I=9%D=8/21%Time=66C62519%P=aarch64-unknown-linux
SF:-gnu%r(RPCCheck,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.234'\x20is
SF:\x20not\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server"
SF:)%r(TLSSessionReq,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.234'\x20
SF:is\x20not\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20serve
SF:r")%r(NCP,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.234'\x20is\x20no
SF:t\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(Ra
SF:dmin,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.234'\x20is\x20not\x20
SF:allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(NessusT
SF:Pv12,4D,"I\0\0\x01\xffj\x04Host\x20'192\.168\.45\.234'\x20is\x20not\x20
SF:allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server");
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows XP|2008 (87%)
OS CPE: cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_server_2008
OS fingerprint not ideal because: maxTimingRatio (2.396000e+00) is greater than 1.4
Aggressive OS guesses: Microsoft Windows XP SP3 (87%), Microsoft Windows Server 2008 (85%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=22%CT=1%CU=42895%PV=Y%DS=4%DC=T%G=N%TM=66C625F0%P=aarch64-unknown-linux-gnu)
SEQ(SP=100%GCD=1%ISR=10D%TI=I%TS=U)
SEQ(SP=106%GCD=1%ISR=10C%TS=U)
OPS(O1=M551NW8NNS%O2=M551NW8NNS%O3=M551NW8%O4=M551NW8NNS%O5=M551NW8NNS%O6=M551NNS)
WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)
ECN(R=Y%DF=Y%T=80%W=FFFF%O=M551NW8NNS%CC=N%Q=)
T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=N)
T7(R=N)
U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=C3A9%RUD=G)
IE(R=N)

Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-08-21T17:36:57
|_  start_date: N/A
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 11955/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 57309/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 58774/udp): CLEAN (Failed to receive data)
|   Check 4 (port 50044/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_clock-skew: -1s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

TRACEROUTE (using port 111/tcp)
HOP RTT       ADDRESS
1   424.70 ms 192.168.45.1
2   424.63 ms 192.168.45.254
3   424.84 ms 192.168.251.1
4   424.88 ms 192.168.196.141

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:37:52 2024 -- 1 IP address (1 host up) scanned in 2272.18 seconds

```