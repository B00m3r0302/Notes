```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_quick_tcp_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:07:56 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_quick_tcp_nmap.xml 192.168.185.141
Warning: Hit PCRE_ERROR_MATCHLIMIT when probing for service http with the regex '^HTTP/1\.1 \d\d\d (?:[^\r\n]*\r\n(?!\r\n))*?.*\r\nServer: Virata-EmWeb/R([\d_]+)\r\nContent-Type: text/html; ?charset=UTF-8\r\nExpires: .*<title>HP (Color |)LaserJet ([\w._ -]+)&nbsp;&nbsp;&nbsp;'
adjust_timeouts2: packet supposedly had rtt of -429544 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -429544 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -189189 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -189189 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -214125 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -214125 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -212532 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -212532 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -504386 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -504386 microseconds.  Ignoring time.
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.069s latency).
Scanned at 2024-08-05 22:07:57 EDT for 95s
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
|_http-generator: Nicepage 4.8.2, nicepage.com
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-title: Home
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
81/tcp   open  http          syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Attendance and Payroll System
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
135/tcp  open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack ttl 125
3306/tcp open  mysql         syn-ack ttl 125 MySQL (unauthorized)
Device type: general purpose|specialized|WAP
Running (JUST GUESSING): OpenBSD 4.X (90%), Microsoft Windows XP|2008|98 (89%), FreeBSD 6.X (88%), VMware ESXi 5.X (86%), Apple embedded (85%)
OS CPE: cpe:/o:openbsd:openbsd:4.0 cpe:/o:microsoft:windows_xp::sp1 cpe:/o:freebsd:freebsd:6.2 cpe:/o:vmware:esxi:5.0 cpe:/o:microsoft:windows_server_2008 cpe:/o:microsoft:windows_98 cpe:/h:apple:airport_extreme
Aggressive OS guesses: OpenBSD 4.0 (90%), Microsoft Windows XP Home SP1 (French) (89%), Microsoft Windows XP SP3 (88%), FreeBSD 6.2-RELEASE (88%), OpenBSD 4.3 (87%), VMware ESXi 5.0 (86%), Microsoft Windows Server 2008 (85%), Microsoft Windows 98 SE (85%), Apple AirPort Extreme WAP (85%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=8/5%OT=22%CT=1%CU=42697%PV=Y%DS=4%DC=T%G=Y%TM=66B18
OS:5DC%P=x86_64-pc-linux-gnu)SEQ()SEQ(SP=FD%GCD=1%ISR=FD%TS=U)SEQ(SP=FD%GCD
OS:=1%ISR=FD%TI=I%TS=U)OPS(O1=M551NW8NNS%O2=M551NW8NNS%O3=M551NW8%O4=M551NW
OS:8NNS%O5=M551NW8NNS%O6=M551NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFF
OS:F%W6=FF70)ECN(R=Y%DF=Y%TG=80%W=FFFF%O=M551NW8NNS%CC=N%Q=)ECN(R=Y%DF=Y%T=
OS:80%W=FFFF%O=M551NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)T
OS:1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T
OS:G=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%
OS:RD=0%Q=)T6(R=N)T7(R=N)U1(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%
OS:RIPCK=G%RUCK=880D%RUD=G)IE(R=N)

Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=253 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: -1s
| smb2-time: 
|   date: 2024-08-06T02:09:15
|_  start_date: N/A
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 60269/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 59619/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 62215/udp): CLEAN (Timeout)
|   Check 4 (port 46131/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE (using port 8080/tcp)
HOP RTT      ADDRESS
1   67.42 ms 192.168.45.1
2   67.20 ms 192.168.45.254
3   67.63 ms 192.168.251.1
4   67.82 ms 192.168.185.141

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:09:32 2024 -- 1 IP address (1 host up) scanned in 96.85 seconds

```
