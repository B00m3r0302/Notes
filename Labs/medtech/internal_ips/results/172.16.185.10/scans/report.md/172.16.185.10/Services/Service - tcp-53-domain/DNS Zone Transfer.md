```bash
dig AXFR -p 53 @172.16.185.10
```

[/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dns_zone-transfer.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dns_zone-transfer.txt):

```

; <<>> DiG 9.20.0-Debian <<>> AXFR -p 53 @172.16.185.10
; (1 server found)
;; global options: +cmd
.			86400	IN	NS	d.root-servers.net.
.			86400	IN	NS	f.root-servers.net.
.			86400	IN	NS	i.root-servers.net.
.			86400	IN	NS	g.root-servers.net.
.			86400	IN	NS	h.root-servers.net.
.			86400	IN	NS	c.root-servers.net.
.			86400	IN	NS	l.root-servers.net.
.			86400	IN	NS	b.root-servers.net.
.			86400	IN	NS	m.root-servers.net.
.			86400	IN	NS	j.root-servers.net.
.			86400	IN	NS	e.root-servers.net.
.			86400	IN	NS	a.root-servers.net.
.			86400	IN	NS	k.root-servers.net.
d.root-servers.net.	86400	IN	A	199.7.91.13
;; Query time: 324 msec
;; SERVER: 172.16.185.10#53(172.16.185.10) (UDP)
;; WHEN: Thu Aug 01 10:35:42 EDT 2024
;; MSG SIZE  rcvd: 268



```
