```bash
nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.161
```

[/home/kali/Notes/Labs/htb/forest/scans/tcp88/tcp_88_kerberos_nmap.txt](file:///home/kali/Notes/Labs/htb/forest/scans/tcp88/tcp_88_kerberos_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 20 12:44:00 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 88 --script=banner,krb5-enum-users -oN /home/kali/Notes/Labs/htb/forest/scans/tcp88/tcp_88_kerberos_nmap.txt -oX /home/kali/Notes/Labs/htb/forest/scans/tcp88/xml/tcp_88_kerberos_nmap.xml 10.10.10.161
Nmap scan report for forest.htb.local (10.10.10.161)
Host is up, received user-set (0.084s latency).
Scanned at 2025-01-20 12:44:00 EST for 17s

PORT   STATE SERVICE      REASON          VERSION
88/tcp open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-01-20 17:50:59Z)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 20 12:44:17 2025 -- 1 IP address (1 host up) scanned in 17.09 seconds

```
