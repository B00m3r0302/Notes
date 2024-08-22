```bash
nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 192.168.196.145
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp21/tcp_21_ftp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp21/tcp_21_ftp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:38 2024 as: nmap -vv --reason -Pn -T4 -sV -p 21 "--script=banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp21/tcp_21_ftp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp21/xml/tcp_21_ftp_nmap.xml 192.168.196.145
Nmap scan report for 192.168.196.145
Host is up, received user-set (0.59s latency).
Scanned at 2024-08-21 13:02:44 EDT for 42s

PORT   STATE SERVICE REASON          VERSION
21/tcp open  ftp     syn-ack ttl 125 Microsoft ftpd
|_banner: 220 Microsoft FTP Service
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|_  SYST: Windows_NT
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:03:26 2024 -- 1 IP address (1 host up) scanned in 47.99 seconds

```
