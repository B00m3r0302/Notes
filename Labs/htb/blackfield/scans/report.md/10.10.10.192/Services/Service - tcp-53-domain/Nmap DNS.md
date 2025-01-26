```bash
nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/blackfield/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/blackfield/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.10.192
```

[/home/kali/Notes/Labs/htb/blackfield/scans/tcp53/tcp_53_dns_nmap.txt](file:///home/kali/Notes/Labs/htb/blackfield/scans/tcp53/tcp_53_dns_nmap.txt):

```
# Nmap 7.95 scan initiated Sat Jan 25 10:54:06 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/blackfield/scans/tcp53/tcp_53_dns_nmap.txt -oX /home/kali/Notes/Labs/htb/blackfield/scans/tcp53/xml/tcp_53_dns_nmap.xml 10.10.10.192
Nmap scan report for 10.10.10.192
Host is up, received user-set (0.058s latency).
Scanned at 2025-01-25 10:54:07 EST for 21s

PORT   STATE SERVICE REASON          VERSION
53/tcp open  domain  syn-ack ttl 127 Simple DNS Plus
|_dns-nsec-enum: Can't determine domain for host 10.10.10.192; use dns-nsec-enum.domains script arg.
|_dns-nsec3-enum: Can't determine domain for host 10.10.10.192; use dns-nsec3-enum.domains script arg.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_dns-brute: Can't guess domain of "10.10.10.192"; use dns-brute.domain script argument.

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jan 25 10:54:28 2025 -- 1 IP address (1 host up) scanned in 22.37 seconds

```
