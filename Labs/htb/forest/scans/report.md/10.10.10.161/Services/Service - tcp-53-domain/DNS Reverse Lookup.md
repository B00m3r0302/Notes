```bash
dig -p 53 -x 10.10.10.161 @10.10.10.161
```

[/home/kali/Notes/Labs/htb/forest/scans/tcp53/tcp_53_dns_reverse-lookup.txt](file:///home/kali/Notes/Labs/htb/forest/scans/tcp53/tcp_53_dns_reverse-lookup.txt):

```
;; communications error to 10.10.10.161#53: timed out
;; communications error to 10.10.10.161#53: timed out
;; communications error to 10.10.10.161#53: timed out

; <<>> DiG 9.20.4-3-Debian <<>> -p 53 -x 10.10.10.161 @10.10.10.161
;; global options: +cmd
;; no servers could be reached


```
