```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 123 --script="banner,(ntp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/udp_123_ntp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/xml/udp_123_ntp_nmap.xml" 172.16.185.10
```

[/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/udp_123_ntp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/udp_123_ntp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Thu Aug  1 10:55:48 2024 as: nmap -vv --reason -Pn -T4 -sU -sV -p 123 "--script=banner,(ntp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/udp_123_ntp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/xml/udp_123_ntp_nmap.xml 172.16.185.10
Nmap scan report for 172.16.185.10
Host is up, received user-set (0.16s latency).
Scanned at 2024-08-01 10:55:48 EDT for 11s

PORT    STATE SERVICE REASON              VERSION
123/udp open  ntp     udp-response ttl 64 NTP v3
| ntp-info: 
|_  receive time stamp: 2024-08-01T14:56:03

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  1 10:55:59 2024 -- 1 IP address (1 host up) scanned in 10.97 seconds

```
