```bash
nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dns_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dns_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:21:29 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dns_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp53/xml/tcp_53_dns_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.052s latency).
Scanned at 2025-02-11 10:21:29 EST for 41s

PORT   STATE SERVICE REASON          VERSION
53/tcp open  domain  syn-ack ttl 127 (generic dns response: SERVFAIL)
| fingerprint-strings: 
|   DNS-SD-TCP: 
|     _services
|     _dns-sd
|     _udp
|_    local
|_dns-nsec-enum: Can't determine domain for host 10.10.10.103; use dns-nsec-enum.domains script arg.
|_dns-nsec3-enum: Can't determine domain for host 10.10.10.103; use dns-nsec3-enum.domains script arg.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.95%I=7%D=2/11%Time=67AB6B0E%P=x86_64-pc-linux-gnu%r(DNS-
SF:SD-TCP,30,"\0\.\0\0\x80\x82\0\x01\0\0\0\0\0\0\t_services\x07_dns-sd\x04
SF:_udp\x05local\0\0\x0c\0\x01");

Host script results:
|_dns-brute: Can't guess domain of "10.10.10.103"; use dns-brute.domain script argument.

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:22:10 2025 -- 1 IP address (1 host up) scanned in 41.74 seconds

```
