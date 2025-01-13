```bash
nmap -vv --reason -Pn -T4 -sV -p 636 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/timelapse/scans/tcp636/tcp_636_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/timelapse/scans/tcp636/xml/tcp_636_ldap_nmap.xml" 10.10.11.152
```

[/home/kali/Notes/Labs/htb/timelapse/scans/tcp636/tcp_636_ldap_nmap.txt](file:///home/kali/Notes/Labs/htb/timelapse/scans/tcp636/tcp_636_ldap_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 12:38:11 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 636 "--script=banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/timelapse/scans/tcp636/tcp_636_ldap_nmap.txt -oX /home/kali/Notes/Labs/htb/timelapse/scans/tcp636/xml/tcp_636_ldap_nmap.xml 10.10.11.152
Nmap scan report for 10.10.11.152
Host is up, received user-set (0.084s latency).
Scanned at 2025-01-13 12:38:11 EST for 4s

PORT    STATE SERVICE    REASON          VERSION
636/tcp open  tcpwrapped syn-ack ttl 127
|_ssl-ccs-injection: No reply from server (TIMEOUT)

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 12:38:15 2025 -- 1 IP address (1 host up) scanned in 3.90 seconds

```
