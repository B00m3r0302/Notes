```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/xml/_full_tcp_nmap.xml" 172.16.185.83
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:33:11 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/xml/_full_tcp_nmap.xml 172.16.185.83
Increasing send delay for 172.16.185.83 from 0 to 5 due to 402 out of 1004 dropped probes since last increase.
Increasing send delay for 172.16.185.83 from 5 to 10 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 172.16.185.83
Host is up, received user-set (0.059s latency).
Scanned at 2024-07-31 12:33:12 EDT for 4153s
Not shown: 65522 filtered tcp ports (no-response)
PORT      STATE SERVICE    REASON         VERSION
135/tcp   open  tcpwrapped syn-ack ttl 64
139/tcp   open  tcpwrapped syn-ack ttl 64
445/tcp   open  tcpwrapped syn-ack ttl 64
5040/tcp  open  tcpwrapped syn-ack ttl 64
5985/tcp  open  tcpwrapped syn-ack ttl 64
47001/tcp open  tcpwrapped syn-ack ttl 64
49664/tcp open  tcpwrapped syn-ack ttl 64
49665/tcp open  tcpwrapped syn-ack ttl 64
49666/tcp open  tcpwrapped syn-ack ttl 64
49667/tcp open  tcpwrapped syn-ack ttl 64
49668/tcp open  tcpwrapped syn-ack ttl 64
49669/tcp open  tcpwrapped syn-ack ttl 64
49670/tcp open  tcpwrapped syn-ack ttl 64
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Cisco SF300 or SG300 switch (93%), Nokia 3600i mobile phone (93%), Apple Time Capsule NAS device (92%), Sony Ericsson W705 or W715 Walkman mobile phone (91%), Aastra 6731i VoIP phone or Apple AirPort Express WAP (89%), Konica Minolta bizhub 250 printer (89%), Sony PlayStation 3 game console (89%), Cisco ATA 188 VoIP adapter (88%), Samsung CLP-310N or CLX-3175RW, or Xerox Phaser 6110 printer (88%), Samsung CLX-3160FN printer (88%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=7/31%OT=49670%CT=%CU=%PV=Y%G=N%TM=66AA7781%P=x86_64-pc-linux-gnu)
SEQ(CI=I)
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
|_smb2-time: Protocol negotiation failed (SMB2)
| nbstat: NetBIOS name: CLIENT02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:6d:f3 (VMware)
| Names:
|   CLIENT02<20>         Flags: <unique><active>
|   CLIENT02<00>         Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:6d:f3:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_smb2-security-mode: Couldn't establish a SMBv2 connection.
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 53052/tcp): CLEAN (Timeout)
|   Check 2 (port 43167/tcp): CLEAN (Timeout)
|   Check 3 (port 46505/udp): CLEAN (Timeout)
|   Check 4 (port 48446/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE
HOP RTT      ADDRESS
1   58.96 ms 172.16.185.83

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 13:42:25 2024 -- 1 IP address (1 host up) scanned in 4154.02 seconds

```
