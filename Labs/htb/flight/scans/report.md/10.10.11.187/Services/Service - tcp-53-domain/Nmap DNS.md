```bash
nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/flight/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/flight/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.11.187
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp53/tcp_53_dns_nmap.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp53/tcp_53_dns_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 18:21:20 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/flight/scans/tcp53/tcp_53_dns_nmap.txt -oX /home/kali/Notes/Labs/htb/flight/scans/tcp53/xml/tcp_53_dns_nmap.xml 10.10.11.187
Nmap scan report for 10.10.11.187
Host is up, received user-set (0.061s latency).
Scanned at 2025-01-13 18:21:21 EST for 42s

PORT   STATE SERVICE REASON          VERSION
53/tcp open  domain  syn-ack ttl 127 (generic dns response: SERVFAIL)
|_dns-nsec-enum: Can't determine domain for host 10.10.11.187; use dns-nsec-enum.domains script arg.
|_dns-nsec3-enum: Can't determine domain for host 10.10.11.187; use dns-nsec3-enum.domains script arg.
| fingerprint-strings: 
|   DNS-SD-TCP: 
|     _services
|     _dns-sd
|     _udp
|_    local
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.95%I=7%D=1/13%Time=6785A007%P=x86_64-pc-linux-gnu%r(DNS-
SF:SD-TCP,30,"\0\.\0\0\x80\x82\0\x01\0\0\0\0\0\0\t_services\x07_dns-sd\x04
SF:_udp\x05local\0\0\x0c\0\x01");

Host script results:
|_dns-brute: Can't guess domain of "10.10.11.187"; use dns-brute.domain script argument.

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 18:22:03 2025 -- 1 IP address (1 host up) scanned in 43.28 seconds

```
