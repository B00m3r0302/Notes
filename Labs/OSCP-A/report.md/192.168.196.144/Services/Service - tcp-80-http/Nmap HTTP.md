```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.196.144
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:44 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.196.144
Nmap scan report for 192.168.196.144
Host is up, received user-set.
Scanned at 2024-08-21 13:00:45 EDT for 1s

PORT   STATE    SERVICE REASON      VERSION
80/tcp filtered http    no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:00:46 2024 -- 1 IP address (1 host up) scanned in 2.23 seconds

```
