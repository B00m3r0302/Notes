```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.10.175:80 2>&1 | tee "/home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_nikto.txt"
```

[/home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_nikto.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.10.175
+ Target Hostname:    10.10.10.175
+ Target Port:        80
+ Start Time:         2025-01-22 09:52:01 (GMT-5)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OPTIONS: Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ OPTIONS: Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ ERROR: Error limit (20) reached for host, giving up. Last error: opening stream: can't connect (timeout): Operation now in progress
+ Scan terminated: 20 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-01-22 10:06:20 (GMT-5) (859 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
