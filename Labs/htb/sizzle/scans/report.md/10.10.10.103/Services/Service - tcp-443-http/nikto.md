```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host https://10.10.10.103:443 2>&1 | tee "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nikto.txt"
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nikto.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.10.103
+ Target Hostname:    10.10.10.103
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /CN=sizzle.htb.local
                   Ciphers:  ECDHE-RSA-AES256-GCM-SHA384
                   Issuer:   /DC=LOCAL/DC=HTB/CN=HTB-SIZZLE-CA
+ Start Time:         2025-02-11 10:21:30 (GMT-5)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ /: Retrieved x-powered-by header: ASP.NET.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /TSyDmZLv.ashx: Retrieved x-aspnet-version header: 4.0.30319.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Hostname '10.10.10.103' does not match certificate's names: sizzle.htb.local. See: https://cwe.mitre.org/data/definitions/297.html
+ OPTIONS: Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ OPTIONS: Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ 7825 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2025-02-11 11:02:25 (GMT-5) (2455 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
