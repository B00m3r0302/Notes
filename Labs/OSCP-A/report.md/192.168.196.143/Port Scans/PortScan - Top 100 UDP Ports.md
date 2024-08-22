```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/xml/_top_100_udp_nmap.xml" 192.168.196.143
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/xml/_top_100_udp_nmap.xml 192.168.196.143
Nmap scan report for 192.168.196.143
Host is up, received user-set (0.16s latency).
Scanned at 2024-08-21 13:00:02 EDT for 1843s
All 100 scanned ports on 192.168.196.143 are in ignored states.
Not shown: 100 open|filtered udp ports (no-response)
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=%CT=%CU=%PV=Y%DS=4%DC=T%G=N%TM=66C62445%P=aarch64-unknown-linux-gnu)
SEQ(II=I)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Network Distance: 4 hops

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   113.66 ms 192.168.45.1
2   111.25 ms 192.168.45.254
3   113.10 ms 192.168.251.1
4   113.44 ms 192.168.196.143

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:30:45 2024 -- 1 IP address (1 host up) scanned in 1844.57 seconds

```
