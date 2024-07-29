```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.227.121:80 2>&1 | tee "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_nikto.txt"
```

[/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_nikto.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.227.121
+ Target Hostname:    192.168.227.121
+ Target Port:        80
+ Start Time:         2024-07-29 07:57:04 (GMT-4)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ /: Retrieved x-aspnet-version header: 4.0.30319.
+ /: Retrieved x-powered-by header: ASP.NET.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OPTIONS: Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ OPTIONS: Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ 7732 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2024-07-29 08:11:52 (GMT-4) (888 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
