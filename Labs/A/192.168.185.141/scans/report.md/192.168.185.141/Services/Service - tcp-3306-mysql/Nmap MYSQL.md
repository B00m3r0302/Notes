```bash
nmap -vv --reason -Pn -T4 -sV -p 3306 --script="banner,(mysql* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/tcp_3306_mysql_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/xml/tcp_3306_mysql_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/tcp_3306_mysql_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/tcp_3306_mysql_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:09:33 2024 as: nmap -vv --reason -Pn -T4 -sV -p 3306 "--script=banner,(mysql* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/tcp_3306_mysql_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/xml/tcp_3306_mysql_nmap.xml 192.168.185.141
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.067s latency).
Scanned at 2024-08-05 22:09:34 EDT for 10s

PORT     STATE SERVICE REASON          VERSION
3306/tcp open  mysql   syn-ack ttl 125 MySQL (unauthorized)
|_mysql-empty-password: Host '192.168.45.166' is not allowed to connect to this MySQL server
| banner: G\x00\x00\x00\xFFj\x04Host '192.168.45.166' is not allowed to c
|_onnect to this MySQL server

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:09:44 2024 -- 1 IP address (1 host up) scanned in 11.72 seconds

```
