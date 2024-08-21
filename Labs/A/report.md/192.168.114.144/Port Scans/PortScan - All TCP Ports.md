```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.114.144/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.114.144/scans/xml/_full_tcp_nmap.xml" 192.168.114.144
```

[/home/kali/Notes/Labs/A/192.168.114.144/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.114.144/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug 19 15:06:32 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/A/192.168.114.144/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.114.144/scans/xml/_full_tcp_nmap.xml 192.168.114.144
Nmap scan report for 192.168.114.144
Host is up, received user-set.
Scanned at 2024-08-19 15:06:33 UTC for 6581s
All 65535 scanned ports on 192.168.114.144 are in ignored states.
Not shown: 65535 filtered tcp ports (no-response)
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/19%OT=%CT=%CU=%PV=Y%G=N%TM=66C3792E%P=aarch64-unknown-linux-gnu)
SEQ()
U1(R=N)
IE(R=N)


TRACEROUTE (using proto 1/icmp)
HOP RTT     ADDRESS
1   2.29 ms 192.168.1.1
2   ... 30

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug 19 16:56:15 2024 -- 1 IP address (1 host up) scanned in 6582.61 seconds

```
