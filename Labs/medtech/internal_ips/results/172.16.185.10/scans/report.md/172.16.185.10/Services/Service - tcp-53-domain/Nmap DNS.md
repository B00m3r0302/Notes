```bash
nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/xml/tcp_53_dns_nmap.xml" 172.16.185.10
```

[/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dns_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dns_nmap.txt):

```
# Nmap 7.94SVN scan initiated Thu Aug  1 10:35:42 2024 as: nmap -vv --reason -Pn -T4 -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dns_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/xml/tcp_53_dns_nmap.xml 172.16.185.10
Nmap scan report for 172.16.185.10
Host is up, received user-set (0.12s latency).
Scanned at 2024-08-01 10:35:42 EDT for 163s

PORT   STATE SERVICE REASON         VERSION
53/tcp open  domain? syn-ack ttl 64
|_dns-nsec3-enum: Can't determine domain for host 172.16.185.10; use dns-nsec3-enum.domains script arg.
|_dns-nsec-enum: Can't determine domain for host 172.16.185.10; use dns-nsec-enum.domains script arg.

Host script results:
|_dns-brute: Can't guess domain of "172.16.185.10"; use dns-brute.domain script argument.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  1 10:38:25 2024 -- 1 IP address (1 host up) scanned in 163.42 seconds

```
