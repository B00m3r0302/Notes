```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.10.161:47001 2>&1 | tee "/home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_nikto.txt"
```

[/home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_nikto.txt](file:///home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.10.161
+ Target Hostname:    10.10.10.161
+ Target Port:        47001
+ Start Time:         2025-01-20 12:52:45 (GMT-5)
---------------------------------------------------------------------------
+ Server: Microsoft-HTTPAPI/2.0
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 7672 requests: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2025-01-20 13:06:34 (GMT-5) (829 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
