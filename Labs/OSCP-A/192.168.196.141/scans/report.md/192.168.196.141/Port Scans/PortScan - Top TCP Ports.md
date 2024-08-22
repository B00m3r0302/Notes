```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/xml/_quick_tcp_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/xml/_quick_tcp_nmap.xml 192.168.196.141
Increasing send delay for 192.168.196.141 from 0 to 5 due to 299 out of 746 dropped probes since last increase.
Increasing send delay for 192.168.196.141 from 5 to 10 due to 11 out of 21 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -113143 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -113143 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -772218 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -772218 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -330427 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -330427 microseconds.  Ignoring time.
Nmap scan report for 192.168.196.141
Host is up, received user-set (0.12s latency).
Scanned at 2024-08-21 13:00:02 EDT for 125s
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE       REASON          VERSION
22/tcp   open  ssh           syn-ack ttl 125 OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 e0:3a:63:4a:07:83:4d:0b:6f:4e:8a:4d:79:3d:6e:4c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHi6qqQGQteAgLLakGf2MPORvtZSeF1gAL03sfUo/E/jsObuAOjzHPfw1OIfAyctU/gv17d0sz17kGDXbg4In4vxlnavXxnB/L2ipQLhAkFLo1YZLLwyUs0j1jiSW65Ax12A20nH0F3hbuqKsuWIPywR9XXc0cwhyY3ET06ZCbVVvP8ChGMd97uZTDeZtrnskYMXmqnfQpOGPL6e022+K5ud3MboyYXTlD0rGyVHyLCCXeg9QdxsVR5mZ8hSVCrwdX8Q4tb4kLYi+wpPx1KCirHEk/8O8I7YuA5KR4AeaMVSlqUhlm9MXaNw+5WZD2xOue0ZPCx2gxgKgndoUDfAagZrHr3dzgMUDgUnKTbtL/EIZdyzKh5C1TrN+yplSpqYjK975Q1qas7SUmzanN9S/PnhFFer/0j6hTtGlRalbxX12i2ifC0314ifnHY3Zz+2VD49RARArwvZR+7KcGKP+5tpCl9IyVf1xSKFFnJ0cQdhuAgJnkCfQXaQLHTzqSbys=
|   256 3f:16:ca:33:25:fd:a2:e6:bb:f6:b0:04:32:21:21:0b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOpOTM37eUD8SUKAqFVSNV8ECDl5yUqV7a41c39cXyPE6EMeNbKxWvQDoTw+WEYArHFAEj3SZbFupIZoZmvjFuA=
|   256 fe:b0:7a:14:bf:77:84:9a:b3:26:59:8d:ff:7e:92:84 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICyZUVdHOqTpEFyvELlmc7sCN1XFXQo7RdZdTRTPO2uJ
80/tcp   open  http          syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-title: Home
|_http-generator: Nicepage 4.8.2, nicepage.com
81/tcp   open  http          syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Attendance and Payroll System
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
135/tcp  open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack ttl 125
3306/tcp open  mysql         syn-ack ttl 125 MySQL (unauthorized)
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows XP (90%)
OS CPE: cpe:/o:microsoft:windows_xp::sp3
Aggressive OS guesses: Microsoft Windows XP SP3 (90%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=8/21%OT=22%CT=1%CU=35013%PV=Y%DS=4%DC=T%G=Y%TM=66C6
OS:1D8F%P=aarch64-unknown-linux-gnu)SEQ(SP=103%GCD=1%ISR=10D%TS=U)OPS(O1=M5
OS:51NW8NNS%O2=M551NW8NNS%O3=M551NW8%O4=M551NW8NNS%O5=M551NW8NNS%O6=M551NNS
OS:)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)ECN(R=Y%DF=Y%TG=80%
OS:W=FFFF%O=M551NW8NNS%CC=N%Q=)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M551NW8NNS%CC=N%Q
OS:=)T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS
OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%TG=80%W=0%S=Z%A=S+%F=AR%O=%RD=
OS:0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=N)
OS:U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=C21F%RUD=G)IE(R=
OS:N)

Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-08-21T17:01:53
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: 0s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 11955/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 57309/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 58774/udp): CLEAN (Timeout)
|   Check 4 (port 50044/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE (using port 3389/tcp)
HOP RTT       ADDRESS
1   134.01 ms 192.168.45.1
2   133.97 ms 192.168.45.254
3   134.07 ms 192.168.251.1
4   134.13 ms 192.168.196.141

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:02:07 2024 -- 1 IP address (1 host up) scanned in 127.12 seconds

```
