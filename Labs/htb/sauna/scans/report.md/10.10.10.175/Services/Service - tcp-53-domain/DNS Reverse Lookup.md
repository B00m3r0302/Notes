```bash
dig -p 53 -x 10.10.10.175 @10.10.10.175
```

[/home/kali/Notes/Labs/htb/sauna/scans/tcp53/tcp_53_dns_reverse-lookup.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/tcp53/tcp_53_dns_reverse-lookup.txt):

```
;; communications error to 10.10.10.175#53: timed out

; <<>> DiG 9.20.4-3-Debian <<>> -p 53 -x 10.10.10.175 @10.10.10.175
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 28442
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;175.10.10.10.in-addr.arpa.	IN	PTR

;; Query time: 4927 msec
;; SERVER: 10.10.10.175#53(10.10.10.175) (UDP)
;; WHEN: Wed Jan 22 09:52:10 EST 2025
;; MSG SIZE  rcvd: 54



```
