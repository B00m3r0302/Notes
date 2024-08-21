```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.114.145/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.114.145/scans/xml/_full_tcp_nmap.xml" 192.168.114.145
```

[/home/kali/Notes/Labs/A/192.168.114.145/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.114.145/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug 19 15:35:08 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/A/192.168.114.145/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.114.145/scans/xml/_full_tcp_nmap.xml 192.168.114.145
Nmap scan report for 192.168.114.145
Host is up, received user-set.
Scanned at 2024-08-19 15:35:08 UTC for 6582s
All 65535 scanned ports on 192.168.114.145 are in ignored states.
Not shown: 65535 filtered tcp ports (no-response)
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/19%OT=%CT=%CU=%PV=Y%G=N%TM=66C37FE2%P=aarch64-unknown-linux-gnu)
SEQ()
U1(R=N)
IE(R=N)


TRACEROUTE (using proto 1/icmp)
HOP RTT     ADDRESS
1   1.83 ms 192.168.1.1
2   ... 30

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug 19 17:24:50 2024 -- 1 IP address (1 host up) scanned in 6582.44 seconds

```
