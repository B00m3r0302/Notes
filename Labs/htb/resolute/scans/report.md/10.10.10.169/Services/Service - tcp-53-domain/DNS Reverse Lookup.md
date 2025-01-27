```bash
dig -p 53 -x 10.10.10.169 @10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp53/tcp_53_dns_reverse-lookup.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp53/tcp_53_dns_reverse-lookup.txt):

```
;; communications error to 10.10.10.169#53: timed out
;; communications error to 10.10.10.169#53: timed out
;; communications error to 10.10.10.169#53: timed out

; <<>> DiG 9.20.4-3-Debian <<>> -p 53 -x 10.10.10.169 @10.10.10.169
;; global options: +cmd
;; no servers could be reached


```
