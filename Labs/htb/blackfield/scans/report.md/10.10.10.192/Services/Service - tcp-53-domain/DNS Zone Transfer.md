```bash
dig AXFR -p 53 @10.10.10.192
```

[/home/kali/Notes/Labs/htb/blackfield/scans/tcp53/tcp_53_dns_zone-transfer.txt](file:///home/kali/Notes/Labs/htb/blackfield/scans/tcp53/tcp_53_dns_zone-transfer.txt):

```
;; communications error to 10.10.10.192#53: timed out

; <<>> DiG 9.20.4-3-Debian <<>> AXFR -p 53 @10.10.10.192
; (1 server found)
;; global options: +cmd
;; Query time: 4238 msec
;; SERVER: 10.10.10.192#53(10.10.10.192) (UDP)
;; WHEN: Sat Jan 25 10:54:16 EST 2025
;; MSG SIZE  rcvd: 28



```
