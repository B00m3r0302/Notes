```bash
dig AXFR -p 53 @10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp53/tcp_53_dns_zone-transfer.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp53/tcp_53_dns_zone-transfer.txt):

```
;; communications error to 10.10.10.169#53: timed out
;; communications error to 10.10.10.169#53: timed out
;; communications error to 10.10.10.169#53: timed out

; <<>> DiG 9.20.4-3-Debian <<>> AXFR -p 53 @10.10.10.169
; (1 server found)
;; global options: +cmd
;; no servers could be reached


```
