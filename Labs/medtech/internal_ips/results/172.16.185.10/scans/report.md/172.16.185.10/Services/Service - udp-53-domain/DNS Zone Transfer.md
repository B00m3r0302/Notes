```bash
dig AXFR -p 53 @172.16.185.10
```

[/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp53/udp_53_dns_zone-transfer.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp53/udp_53_dns_zone-transfer.txt):

```

; <<>> DiG 9.20.0-Debian <<>> AXFR -p 53 @172.16.185.10
; (1 server found)
;; global options: +cmd
.			85194	IN	NS	f.root-servers.net.
.			85194	IN	NS	i.root-servers.net.
.			85194	IN	NS	g.root-servers.net.
.			85194	IN	NS	h.root-servers.net.
.			85194	IN	NS	c.root-servers.net.
.			85194	IN	NS	l.root-servers.net.
.			85194	IN	NS	b.root-servers.net.
.			85194	IN	NS	m.root-servers.net.
.			85194	IN	NS	j.root-servers.net.
.			85194	IN	NS	e.root-servers.net.
.			85194	IN	NS	a.root-servers.net.
.			85194	IN	NS	k.root-servers.net.
.			85194	IN	NS	d.root-servers.net.
f.root-servers.net.	86399	IN	A	192.5.5.241
d.root-servers.net.	85194	IN	A	199.7.91.13
;; Query time: 184 msec
;; SERVER: 172.16.185.10#53(172.16.185.10) (UDP)
;; WHEN: Thu Aug 01 10:55:48 EDT 2024
;; MSG SIZE  rcvd: 284



```
