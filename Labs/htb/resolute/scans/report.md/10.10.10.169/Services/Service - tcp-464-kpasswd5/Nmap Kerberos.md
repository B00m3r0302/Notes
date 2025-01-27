```bash
nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp464/tcp_464_kerberos_nmap.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp464/tcp_464_kerberos_nmap.txt):

```
# Nmap 7.95 scan initiated Sun Jan 26 20:15:40 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 464 --script=banner,krb5-enum-users -oN /home/kali/Notes/Labs/htb/resolute/scans/tcp464/tcp_464_kerberos_nmap.txt -oX /home/kali/Notes/Labs/htb/resolute/scans/tcp464/xml/tcp_464_kerberos_nmap.xml 10.10.10.169
Nmap scan report for 10.10.10.169
Host is up, received user-set (0.053s latency).
Scanned at 2025-01-26 20:15:40 EST for 20s

PORT    STATE SERVICE   REASON          VERSION
464/tcp open  kpasswd5? syn-ack ttl 127

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jan 26 20:16:00 2025 -- 1 IP address (1 host up) scanned in 19.77 seconds

```
