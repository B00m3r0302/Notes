```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/xml/_top_100_udp_nmap.xml" 172.16.185.83
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:35:29 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/xml/_top_100_udp_nmap.xml 172.16.185.83
Nmap scan report for 172.16.185.83
Host is up, received user-set (0.19s latency).
Scanned at 2024-07-31 12:35:29 EDT for 1935s
Not shown: 99 open|filtered udp ports (no-response)
PORT    STATE SERVICE    REASON              VERSION
137/udp open  netbios-ns udp-response ttl 64 Microsoft Windows or Samba netbios-ns (workgroup: MEDTECH)
| nbns-interfaces: 
|   hostname: CLIENT02
|   interfaces: 
|_    172.16.185.83
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing an open TCP port so results incomplete
Aggressive OS guesses: Rockwell Automation 1761-NET-ENI Ethernet-to-RS-232-C interface module (94%), XigmaNAS (FreeBSD 11.2-RELEASE) (94%), AVM FRITZ!Box FON WLAN 7170 WAP (Linux 2.6.13) (94%), XigmaNAS (FreeBSD 12.2-RELEASE) (94%), Cisco SG 300-10, Dell PowerConnect 2748, Linksys SLM2024, SLM2048, or SLM224P, or Netgear FS728TP or GS724TP switch (94%), Dell PowerConnect 5316M switch (94%), Linksys SRW2000-series or Allied Telesyn AT-8000S switch (94%), Linksys SRW2024 switch (94%), Netgear FS700TS Smart Switch (94%), Blue Coat SGOS 4.2.2.2 (94%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=7/31%OT=%CT=%CU=%PV=Y%G=N%TM=66AA6F60%P=x86_64-pc-linux-gnu)
SEQ(CI=I%II=RI)
T6(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=N%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=S%TG=40%CD=S)

Service Info: Host: CLIENT02

Host script results:
| nbstat: NetBIOS name: CLIENT02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:6d:f3 (VMware)
| Names:
|   CLIENT02<20>         Flags: <unique><active>
|   CLIENT02<00>         Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:6d:f3:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00

TRACEROUTE
HOP RTT       ADDRESS
1   187.74 ms 172.16.185.83

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 13:07:44 2024 -- 1 IP address (1 host up) scanned in 1935.46 seconds

```
