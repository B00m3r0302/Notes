```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:08 2024 as: nmap -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp22/xml/tcp_22_ssh_nmap.xml 192.168.196.141
Nmap scan report for 192.168.196.141
Host is up, received user-set.
Scanned at 2024-08-21 13:02:12 EDT for 1s

PORT   STATE    SERVICE REASON      VERSION
22/tcp filtered ssh     no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:02:13 2024 -- 1 IP address (1 host up) scanned in 5.21 seconds

```