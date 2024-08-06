```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_top_100_udp_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:07:56 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_top_100_udp_nmap.xml 192.168.185.141
Warning: 192.168.185.141 giving up on port because retransmission cap hit (6).
Increasing send delay for 192.168.185.141 from 100 to 200 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 192.168.185.141 from 200 to 400 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 192.168.185.141 from 400 to 800 due to 11 out of 13 dropped probes since last increase.
Increasing send delay for 192.168.185.141 from 800 to 1000 due to 11 out of 17 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -232522 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -532399 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -532399 microseconds.  Ignoring time.
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.10s latency).
Scanned at 2024-08-05 22:07:57 EDT for 394s
Not shown: 84 closed udp ports (port-unreach)
PORT      STATE         SERVICE     REASON      VERSION
68/udp    open|filtered dhcpc       no-response
111/udp   open|filtered rpcbind     no-response
123/udp   open|filtered ntp         no-response
137/udp   open|filtered netbios-ns  no-response
138/udp   open|filtered netbios-dgm no-response
500/udp   open|filtered isakmp      no-response
631/udp   open|filtered ipp         no-response
1025/udp  open|filtered blackjack   no-response
1900/udp  open|filtered upnp        no-response
2049/udp  open|filtered nfs         no-response
4500/udp  open|filtered nat-t-ike   no-response
5353/udp  open|filtered zeroconf    no-response
49156/udp open|filtered unknown     no-response
49185/udp open|filtered unknown     no-response
49194/udp open|filtered unknown     no-response
49200/udp open|filtered unknown     no-response
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing an open TCP port so results incomplete
Aggressive OS guesses: Linux 2.6.18 (92%), Linux 2.6.30 (92%), Microsoft Windows Server 2008 R2 (91%), Microsoft Windows Server 2008 R2 SP1 (91%), Microsoft Windows Server 2008 SP2 Datacenter Version (91%), Microsoft Windows Server 2012 Data Center (91%), Microsoft Windows Server 2012 R2 (91%), Microsoft Windows Server 2016 (91%), Microsoft Windows 7 (91%), Microsoft Windows 7 SP1 (91%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/5%OT=%CT=%CU=7%PV=Y%DS=4%DC=T%G=N%TM=66B18707%P=x86_64-pc-linux-gnu)
SEQ()
T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=AF2%RUD=G)
IE(R=N)

Network Distance: 4 hops

TRACEROUTE (using port 7/udp)
HOP RTT       ADDRESS
1   295.90 ms 192.168.45.1
2   295.76 ms 192.168.45.254
3   296.14 ms 192.168.251.1
4   296.38 ms 192.168.185.141

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:14:31 2024 -- 1 IP address (1 host up) scanned in 396.00 seconds

```
