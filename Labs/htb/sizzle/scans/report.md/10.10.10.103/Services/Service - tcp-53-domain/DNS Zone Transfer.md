```bash
dig AXFR -p 53 @10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dns_zone-transfer.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dns_zone-transfer.txt):

```
;; communications error to 10.10.10.103#53: timed out
;; communications error to 10.10.10.103#53: timed out
;; communications error to 10.10.10.103#53: timed out

; <<>> DiG 9.20.4-4-Debian <<>> AXFR -p 53 @10.10.10.103
; (1 server found)
;; global options: +cmd
;; no servers could be reached


```
