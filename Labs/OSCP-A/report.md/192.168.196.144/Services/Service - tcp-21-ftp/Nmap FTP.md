```bash
nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 192.168.196.144
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/tcp_21_ftp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/tcp_21_ftp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:44 2024 as: nmap -vv --reason -Pn -T4 -sV -p 21 "--script=banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/tcp_21_ftp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/xml/tcp_21_ftp_nmap.xml 192.168.196.144
Nmap scan report for 192.168.196.144
Host is up, received user-set (0.095s latency).
Scanned at 2024-08-21 13:00:45 EDT for 12s

PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 61 vsftpd 3.0.5
|_banner: 220 (vsFTPd 3.0.5)
Service Info: OS: Unix

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:00:57 2024 -- 1 IP address (1 host up) scanned in 13.29 seconds

```