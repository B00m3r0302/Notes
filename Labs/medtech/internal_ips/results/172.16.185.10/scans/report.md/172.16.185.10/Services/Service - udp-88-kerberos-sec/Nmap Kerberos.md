```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/udp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/xml/udp_88_kerberos_nmap.xml" 172.16.185.10
```

[/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/udp_88_kerberos_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/udp_88_kerberos_nmap.txt):

```
# Nmap 7.94SVN scan initiated Thu Aug  1 10:55:48 2024 as: nmap -vv --reason -Pn -T4 -sU -sV -p 88 --script=banner,krb5-enum-users -oN /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/udp_88_kerberos_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/xml/udp_88_kerberos_nmap.xml 172.16.185.10
Nmap scan report for 172.16.185.10
Host is up, received user-set (0.17s latency).
Scanned at 2024-08-01 10:55:48 EDT for 1s

PORT   STATE SERVICE      REASON              VERSION
88/udp open  kerberos-sec udp-response ttl 64 Microsoft Windows Kerberos (server time: 2024-08-01 14:55:49Z)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  1 10:55:49 2024 -- 1 IP address (1 host up) scanned in 1.05 seconds

```
