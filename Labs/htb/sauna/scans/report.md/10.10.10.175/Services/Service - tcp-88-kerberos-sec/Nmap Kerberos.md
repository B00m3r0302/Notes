```bash
nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.175
```

[/home/kali/Notes/Labs/htb/sauna/scans/tcp88/tcp_88_kerberos_nmap.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/tcp88/tcp_88_kerberos_nmap.txt):

```
# Nmap 7.95 scan initiated Wed Jan 22 09:52:00 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 88 --script=banner,krb5-enum-users -oN /home/kali/Notes/Labs/htb/sauna/scans/tcp88/tcp_88_kerberos_nmap.txt -oX /home/kali/Notes/Labs/htb/sauna/scans/tcp88/xml/tcp_88_kerberos_nmap.xml 10.10.10.175
Nmap scan report for 10.10.10.175
Host is up, received user-set (0.055s latency).
Scanned at 2025-01-22 09:52:11 EST for 16s

PORT   STATE SERVICE      REASON          VERSION
88/tcp open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-01-22 22:52:19Z)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan 22 09:52:27 2025 -- 1 IP address (1 host up) scanned in 27.70 seconds

```
