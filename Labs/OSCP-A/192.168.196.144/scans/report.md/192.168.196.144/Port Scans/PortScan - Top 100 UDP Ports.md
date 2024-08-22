```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_top_100_udp_nmap.xml" 192.168.196.144
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_top_100_udp_nmap.xml 192.168.196.144
Increasing send delay for 192.168.196.144 from 0 to 50 due to 11 out of 17 dropped probes since last increase.
Warning: 192.168.196.144 giving up on port because retransmission cap hit (6).
Increasing send delay for 192.168.196.144 from 200 to 400 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 192.168.196.144 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 192.168.196.144
Host is up, received user-set (0.21s latency).
Scanned at 2024-08-21 13:00:02 EDT for 210s
Not shown: 91 closed udp ports (port-unreach)
PORT      STATE         SERVICE         REASON      VERSION
7/udp     open|filtered echo            no-response
49/udp    open|filtered tacacs          no-response
137/udp   open|filtered netbios-ns      no-response
515/udp   open|filtered printer         no-response
1813/udp  open|filtered radacct         no-response
2049/udp  open|filtered nfs             no-response
2223/udp  open|filtered rockwell-csp2   no-response
20031/udp open|filtered bakbonenetvault no-response
31337/udp open|filtered BackOrifice     no-response
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing an open TCP port so results incomplete
Aggressive OS guesses: Linksys WRT54G2 WAP (94%), Linux 2.6.32 (94%), Endian Firewall 2.3 (Linux 2.6) (94%), Linux 2.6.18 (94%), Linux 2.6.23 (94%), Linux 2.6.24 (94%), Cyberoam UTM firewall (94%), Linux 2.6.8 (Debian, x86) (90%), Microsoft Windows Server 2008 R2 SP1 (90%), Novell NetWare 6.5 (90%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=%CT=%CU=9%PV=Y%DS=10%DC=T%G=N%TM=66C61DE4%P=aarch64-unknown-linux-gnu)
SEQ()
T5(R=Y%DF=Y%TG=40%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=N)

Network Distance: 10 hops

TRACEROUTE (using port 67/udp)
HOP RTT       ADDRESS
1   656.79 ms 192.168.45.1
2   656.74 ms 192.168.45.254
3   657.07 ms 192.168.251.1
4   ... 9
10  559.03 ms 192.168.196.144

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:03:32 2024 -- 1 IP address (1 host up) scanned in 212.10 seconds

```
