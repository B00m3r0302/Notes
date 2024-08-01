```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/xml/_full_tcp_nmap.xml" 172.16.185.12
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:30:46 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/xml/_full_tcp_nmap.xml 172.16.185.12
Increasing send delay for 172.16.185.12 from 0 to 5 due to 477 out of 1191 dropped probes since last increase.
Increasing send delay for 172.16.185.12 from 5 to 10 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 172.16.185.12
Host is up, received user-set (0.055s latency).
Scanned at 2024-07-31 12:30:46 EDT for 11653s
Not shown: 65523 filtered tcp ports (no-response)
PORT      STATE SERVICE    REASON         VERSION
135/tcp   open  tcpwrapped syn-ack ttl 64
139/tcp   open  tcpwrapped syn-ack ttl 64
445/tcp   open  tcpwrapped syn-ack ttl 64
3389/tcp  open  tcpwrapped syn-ack ttl 64
5985/tcp  open  tcpwrapped syn-ack ttl 64
49664/tcp open  tcpwrapped syn-ack ttl 64
49665/tcp open  tcpwrapped syn-ack ttl 64
49666/tcp open  tcpwrapped syn-ack ttl 64
49667/tcp open  tcpwrapped syn-ack ttl 64
49668/tcp open  tcpwrapped syn-ack ttl 64
49669/tcp open  tcpwrapped syn-ack ttl 64
49671/tcp open  tcpwrapped syn-ack ttl 64
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: switch|game console|phone|storage-misc
Running (JUST GUESSING): Cisco embedded (94%), Sony embedded (90%), Nokia Symbian OS (87%), Apple embedded (87%), Sony Ericsson embedded (86%)
OS CPE: cpe:/h:cisco:sf300 cpe:/h:cisco:sg300 cpe:/h:sony:playstation_3 cpe:/o:nokia:symbian_os cpe:/h:sonyericsson:w705 cpe:/h:sonyericsson:w715
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Cisco SF300 or SG300 switch (94%), Sony PlayStation 3 game console (90%), Cisco SG 500 switch (88%), Nokia 3600i mobile phone (87%), Apple Time Capsule NAS device (87%), Sony Ericsson W705 or W715 Walkman mobile phone (86%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=7/31%OT=49671%CT=%CU=%PV=Y%G=N%TM=66AA943B%P=x86_64-pc-linux-gnu)
SEQ(CI=I%II=RI)
ECN(R=N)
T1(R=N)
T2(R=Y%DF=N%TG=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)
T3(R=N)
T4(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T6(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=N%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=S%TG=40%CD=S)


Host script results:
| nbstat: NetBIOS name: DEV04, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:7b:40 (VMware)
| Names:
|   DEV04<00>            Flags: <unique><active>
|   DEV04<20>            Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:7b:40:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_smb2-security-mode: Couldn't establish a SMBv2 connection.
|_smb2-time: Protocol negotiation failed (SMB2)
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 53547/tcp): CLEAN (Timeout)
|   Check 2 (port 58868/tcp): CLEAN (Timeout)
|   Check 3 (port 42793/udp): CLEAN (Timeout)
|   Check 4 (port 15125/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE
HOP RTT      ADDRESS
1   54.54 ms 172.16.185.12

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 15:44:59 2024 -- 1 IP address (1 host up) scanned in 11653.64 seconds

```
