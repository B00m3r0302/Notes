```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.196.141:47001 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/tcp_47001_http_nikto.txt"
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/tcp_47001_http_nikto.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp47001/tcp_47001_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.196.141
+ Target Hostname:    192.168.196.141
+ Target Port:        47001
+ Start Time:         2024-08-21 13:38:11 (GMT-4)
---------------------------------------------------------------------------
+ Server: Microsoft-HTTPAPI/2.0
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 7731 requests: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2024-08-21 15:21:15 (GMT-4) (6184 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```