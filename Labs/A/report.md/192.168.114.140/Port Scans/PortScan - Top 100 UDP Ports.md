```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/A/192.168.114.140/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.114.140/scans/xml/_top_100_udp_nmap.xml" 192.168.114.140
```

[/home/kali/Notes/Labs/A/192.168.114.140/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.114.140/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug 19 15:04:29 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/A/192.168.114.140/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.114.140/scans/xml/_top_100_udp_nmap.xml 192.168.114.140
Nmap scan report for 192.168.114.140
Host is up, received user-set.
Scanned at 2024-08-19 15:04:30 UTC for 1837s
All 100 scanned ports on 192.168.114.140 are in ignored states.
Not shown: 100 open|filtered udp ports (no-response)
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/19%OT=%CT=%CU=%PV=Y%G=N%TM=66C3662B%P=aarch64-unknown-linux-gnu)
SEQ()
U1(R=N)
IE(R=N)


TRACEROUTE (using proto 1/icmp)
HOP RTT     ADDRESS
1   3.38 ms 192.168.1.1
2   ... 30

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug 19 15:35:07 2024 -- 1 IP address (1 host up) scanned in 1838.14 seconds

```