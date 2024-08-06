```bash
nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.145.144/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.144/scans/tcp53/xml/tcp_53_dns_nmap.xml" 192.168.145.144
```

[/home/kali/Notes/Labs/A/192.168.145.144/scans/tcp53/tcp_53_dns_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.145.144/scans/tcp53/tcp_53_dns_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:14:18 2024 as: nmap -vv --reason -Pn -T4 -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/A/192.168.145.144/scans/tcp53/tcp_53_dns_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.145.144/scans/tcp53/xml/tcp_53_dns_nmap.xml 192.168.145.144
Nmap scan report for 192.168.145.144
Host is up, received user-set (0.0014s latency).
Scanned at 2024-08-05 22:14:18 EDT for 21s

PORT   STATE SERVICE REASON         VERSION
53/tcp open  domain  syn-ack ttl 64 Unbound
|_dns-nsec3-enum: Can't determine domain for host 192.168.145.144; use dns-nsec3-enum.domains script arg.
|_dns-nsec-enum: Can't determine domain for host 192.168.145.144; use dns-nsec-enum.domains script arg.

Host script results:
|_dns-brute: Can't guess domain of "192.168.145.144"; use dns-brute.domain script argument.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:14:39 2024 -- 1 IP address (1 host up) scanned in 21.51 seconds

```
