```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.145.144/scans/udp53/udp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.144/scans/udp53/xml/udp_53_dns_nmap.xml" 192.168.145.144
```

[/home/kali/Notes/Labs/A/192.168.145.144/scans/udp53/udp_53_dns_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.145.144/scans/udp53/udp_53_dns_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:30:11 2024 as: nmap -vv --reason -Pn -T4 -sU -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/A/192.168.145.144/scans/udp53/udp_53_dns_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.145.144/scans/udp53/xml/udp_53_dns_nmap.xml 192.168.145.144
Nmap scan report for 192.168.145.144
Host is up, received user-set (0.025s latency).
Scanned at 2024-08-05 22:30:11 EDT for 3s

PORT   STATE SERVICE REASON              VERSION
53/udp open  domain  udp-response ttl 58 Unbound
|_dns-nsec3-enum: Can't determine domain for host 192.168.145.144; use dns-nsec3-enum.domains script arg.
|_dns-nsec-enum: Can't determine domain for host 192.168.145.144; use dns-nsec-enum.domains script arg.
| dns-cache-snoop: 30 of 100 tested domains are cached.
| www.google.com
| yahoo.com
| www.yahoo.com
| baidu.com
| amazon.com
| qq.com
| live.com
| www.live.com
| www.linkedin.com
| twitter.com
| www.twitter.com
| bing.com
| www.yahoo.co.jp
| yandex.ru
| wordpress.com
| www.wordpress.com
| vk.com
| ebay.com
| msn.com
| www.msn.com
| www.ask.com
| mail.ru
| pinterest.com
| microsoft.com
| xvideos.com
| www.xvideos.com
| www.craigslist.org
| paypal.com
| www.paypal.com
|_apple.com
|_dns-recursion: Recursion appears to be enabled

Host script results:
|_dns-brute: Can't guess domain of "192.168.145.144"; use dns-brute.domain script argument.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:30:14 2024 -- 1 IP address (1 host up) scanned in 3.61 seconds

```
