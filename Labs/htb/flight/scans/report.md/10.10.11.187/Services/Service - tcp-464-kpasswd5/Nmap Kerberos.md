```bash
nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/flight/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/flight/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 10.10.11.187
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp464/tcp_464_kerberos_nmap.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp464/tcp_464_kerberos_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 18:21:21 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 464 --script=banner,krb5-enum-users -oN /home/kali/Notes/Labs/htb/flight/scans/tcp464/tcp_464_kerberos_nmap.txt -oX /home/kali/Notes/Labs/htb/flight/scans/tcp464/xml/tcp_464_kerberos_nmap.xml 10.10.11.187
Nmap scan report for 10.10.11.187
Host is up, received user-set (0.058s latency).
Scanned at 2025-01-13 18:21:22 EST for 20s

PORT    STATE SERVICE   REASON          VERSION
464/tcp open  kpasswd5? syn-ack ttl 127

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 18:21:42 2025 -- 1 IP address (1 host up) scanned in 21.29 seconds

```
