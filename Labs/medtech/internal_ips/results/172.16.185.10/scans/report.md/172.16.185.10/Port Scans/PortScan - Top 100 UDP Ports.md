```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/xml/_top_100_udp_nmap.xml" 172.16.185.10
```

[/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Thu Aug  1 10:26:30 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/xml/_top_100_udp_nmap.xml 172.16.185.10
Nmap scan report for 172.16.185.10
Host is up, received user-set (0.10s latency).
Scanned at 2024-08-01 10:26:31 EDT for 1756s
Not shown: 96 open|filtered udp ports (no-response)
PORT    STATE SERVICE      REASON              VERSION
53/udp  open  domain       udp-response ttl 64 (generic dns response: NOTIMP)
|_dns-recursion: Recursion appears to be enabled
| fingerprint-strings: 
|   NBTStat: 
|_    CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
88/udp  open  kerberos-sec udp-response        Microsoft Windows Kerberos (server time: 2024-08-01 14:26:41Z)
123/udp open  ntp          udp-response ttl 64 NTP v3
| ntp-info: 
|_  receive time stamp: 2024-08-01T14:33:28
137/udp open  netbios-ns   udp-response ttl 64 Microsoft Windows or Samba netbios-ns (workgroup: MEDTECH)
| nbns-interfaces: 
|   hostname: DC01
|   interfaces: 
|_    172.16.185.10
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-UDP:V=7.94SVN%I=7%D=8/1%Time=66AB9B2B%P=x86_64-pc-linux-gnu%r(NB
SF:TStat,32,"\x80\xf0\x80\x82\0\x01\0\0\0\0\0\0\x20CKAAAAAAAAAAAAAAAAAAAAA
SF:AAAAAAAAA\0\0!\0\x01");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing an open TCP port so results incomplete
Aggressive OS guesses: Sanyo PLC-XU88 digital video projector (95%), Linux 2.6.18 (93%), Buffalo BS-GS switch (92%), Printronix T5304 label printer (92%), Asus WL-500gP wireless broadband router (92%), AXIS 70U Network Document Server (92%), Brother HL-2700CN printer (92%), Brother MFC-7820N printer (92%), IBM 6400 printer (software version 7.0.9.6) (92%), Intel Express 510T, 520T, or 550T switch (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/1%OT=%CT=%CU=%PV=Y%G=N%TM=66ABA1F4%P=x86_64-pc-linux-gnu)
SEQ(CI=I)
SEQ(CI=I%II=RI)
T6(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=N%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=N)
IE(R=Y%DFI=S%TG=40%CD=S)

Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:2d:3a (VMware)
| Names:
|   DC01<20>             Flags: <unique><active>
|   DC01<00>             Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
|   MEDTECH<1c>          Flags: <group><active>
|   MEDTECH<1b>          Flags: <unique><active>
| Statistics:
|   00:50:56:bf:2d:3a:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_clock-skew: 10s

TRACEROUTE
HOP RTT       ADDRESS
1   100.44 ms 172.16.185.10

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  1 10:55:48 2024 -- 1 IP address (1 host up) scanned in 1757.56 seconds

```
