```bash
nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/blackfield/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/blackfield/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.192
```

[/home/kali/Notes/Labs/htb/blackfield/scans/tcp88/tcp_88_kerberos_nmap.txt](file:///home/kali/Notes/Labs/htb/blackfield/scans/tcp88/tcp_88_kerberos_nmap.txt):

```
# Nmap 7.95 scan initiated Sat Jan 25 10:54:06 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 88 --script=banner,krb5-enum-users -oN /home/kali/Notes/Labs/htb/blackfield/scans/tcp88/tcp_88_kerberos_nmap.txt -oX /home/kali/Notes/Labs/htb/blackfield/scans/tcp88/xml/tcp_88_kerberos_nmap.xml 10.10.10.192
Nmap scan report for 10.10.10.192
Host is up, received user-set (0.065s latency).
Scanned at 2025-01-25 10:54:07 EST for 17s

PORT   STATE SERVICE      REASON          VERSION
88/tcp open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-01-25 22:54:13Z)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jan 25 10:54:24 2025 -- 1 IP address (1 host up) scanned in 17.63 seconds

```
