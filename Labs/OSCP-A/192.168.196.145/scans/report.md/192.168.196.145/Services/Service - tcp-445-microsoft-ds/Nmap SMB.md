```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp445/xml/tcp_445_smb_nmap.xml" 192.168.196.145
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:39 2024 as: nmap -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp445/xml/tcp_445_smb_nmap.xml 192.168.196.145
Nmap scan report for 192.168.196.145
Host is up, received user-set.
Scanned at 2024-08-21 13:02:41 EDT for 1s

PORT    STATE    SERVICE      REASON      VERSION
445/tcp filtered microsoft-ds no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:02:42 2024 -- 1 IP address (1 host up) scanned in 4.05 seconds

```
