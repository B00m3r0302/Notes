```bash
nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/tcp_47001_http_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/tcp_47001_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:38:05 2024 as: nmap -vv --reason -Pn -T4 -sV -p 47001 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/tcp_47001_http_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/xml/tcp_47001_http_nmap.xml 192.168.196.141
Nmap scan report for 192.168.196.141
Host is up, received user-set.
Scanned at 2024-08-21 13:38:09 EDT for 1s

PORT      STATE    SERVICE REASON      VERSION
47001/tcp filtered winrm   no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:38:11 2024 -- 1 IP address (1 host up) scanned in 6.33 seconds

```