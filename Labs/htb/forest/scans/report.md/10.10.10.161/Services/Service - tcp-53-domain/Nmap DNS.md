```bash
nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.10.161
```

[/home/kali/Notes/Labs/htb/forest/scans/tcp53/tcp_53_dns_nmap.txt](file:///home/kali/Notes/Labs/htb/forest/scans/tcp53/tcp_53_dns_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 20 12:44:00 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/forest/scans/tcp53/tcp_53_dns_nmap.txt -oX /home/kali/Notes/Labs/htb/forest/scans/tcp53/xml/tcp_53_dns_nmap.xml 10.10.10.161
Nmap scan report for forest.htb.local (10.10.10.161)
Host is up, received user-set (0.062s latency).
Scanned at 2025-01-20 12:44:00 EST for 42s

PORT   STATE SERVICE REASON          VERSION
53/tcp open  domain  syn-ack ttl 127 (generic dns response: SERVFAIL)
| dns-nsec-enum: 
|_  No NSEC records found
| dns-nsec3-enum: 
|_  DNSSEC NSEC3 not supported
| fingerprint-strings: 
|   DNS-SD-TCP: 
|     _services
|     _dns-sd
|     _udp
|_    local
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.95%I=7%D=1/20%Time=678E8B76%P=x86_64-pc-linux-gnu%r(DNS-
SF:SD-TCP,30,"\0\.\0\0\x80\x82\0\x01\0\0\0\0\0\0\t_services\x07_dns-sd\x04
SF:_udp\x05local\0\0\x0c\0\x01");

Host script results:
| dns-brute: 
|_  DNS Brute-force hostnames: No results.

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 20 12:44:42 2025 -- 1 IP address (1 host up) scanned in 42.36 seconds

```
