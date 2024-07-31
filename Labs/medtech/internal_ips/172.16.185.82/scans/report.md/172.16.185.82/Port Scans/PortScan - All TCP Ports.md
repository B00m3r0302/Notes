```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/xml/_full_tcp_nmap.xml" 172.16.185.82
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:31:13 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/xml/_full_tcp_nmap.xml 172.16.185.82
Nmap scan report for 172.16.185.82
Host is up, received user-set (0.043s latency).
Scanned at 2024-07-31 12:31:13 EDT for 1378s
Not shown: 65522 filtered tcp ports (no-response)
PORT      STATE SERVICE       REASON         VERSION
135/tcp   open  msrpc         syn-ack ttl 64 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 64 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds? syn-ack ttl 64
3389/tcp  open  ms-wbt-server syn-ack ttl 64 Microsoft Terminal Services
5040/tcp  open  unknown       syn-ack ttl 64
49664/tcp open  unknown       syn-ack ttl 64
49665/tcp open  unknown       syn-ack ttl 64
49666/tcp open  unknown       syn-ack ttl 64
49667/tcp open  unknown       syn-ack ttl 64
49668/tcp open  unknown       syn-ack ttl 64
49669/tcp open  unknown       syn-ack ttl 64
49670/tcp open  unknown       syn-ack ttl 64
49671/tcp open  unknown       syn-ack ttl 64
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: switch|game console|phone|storage-misc
Running (JUST GUESSING): Cisco embedded (94%), Sony embedded (90%), Nokia Symbian OS (87%), Apple embedded (87%), Sony Ericsson embedded (86%)
OS CPE: cpe:/h:cisco:sf300 cpe:/h:cisco:sg300 cpe:/h:sony:playstation_3 cpe:/o:nokia:symbian_os cpe:/h:sonyericsson:w705 cpe:/h:sonyericsson:w715
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Cisco SF300 or SG300 switch (94%), Sony PlayStation 3 game console (90%), Cisco SG 500 switch (88%), Nokia 3600i mobile phone (87%), Apple Time Capsule NAS device (87%), Sony Ericsson W705 or W715 Walkman mobile phone (86%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=7/31%OT=135%CT=%CU=%PV=Y%G=N%TM=66AA6C33%P=x86_64-pc-linux-gnu)
SEQ(CI=I)
SEQ(CI=I%II=RI)
ECN(R=N)
ECN(R=Y%DF=N%TG=40%W=7200%O=M5B4NW7%CC=N%Q=)
T1(R=N)
T2(R=Y%DF=N%TG=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)
T3(R=N)
T4(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T6(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=N%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=S%TG=40%CD=S)

Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| nbstat: NetBIOS name: CLIENT01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:0c:26 (VMware)
| Names:
|   CLIENT01<20>         Flags: <unique><active>
|   CLIENT01<00>         Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:0c:26:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 46974/tcp): CLEAN (Timeout)
|   Check 2 (port 56816/tcp): CLEAN (Timeout)
|   Check 3 (port 20973/udp): CLEAN (Timeout)
|   Check 4 (port 46486/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_smb2-time: Protocol negotiation failed (SMB2)
|_smb2-security-mode: Couldn't establish a SMBv2 connection.

TRACEROUTE
HOP RTT      ADDRESS
1   43.02 ms 172.16.185.82

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 12:54:11 2024 -- 1 IP address (1 host up) scanned in 1377.52 seconds

```
