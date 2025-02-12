```bash
nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp21/tcp_21_ftp_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp21/tcp_21_ftp_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:21:29 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 21 "--script=banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp21/tcp_21_ftp_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp21/xml/tcp_21_ftp_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.055s latency).
Scanned at 2025-02-11 10:21:29 EST for 2s

PORT   STATE SERVICE REASON          VERSION
21/tcp open  ftp     syn-ack ttl 127 Microsoft ftpd
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|_  SYST: Windows_NT
|_banner: 220 Microsoft FTP Service
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:21:31 2025 -- 1 IP address (1 host up) scanned in 1.93 seconds

```
