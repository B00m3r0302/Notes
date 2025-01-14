```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.11.187:80 2>&1 | tee "/home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_nikto.txt"
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_nikto.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.11.187
+ Target Hostname:    10.10.11.187
+ Target Port:        80
+ Start Time:         2025-01-13 18:21:23 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ OpenSSL/1.1.1m appears to be outdated (current is at least 3.0.7). OpenSSL 1.1.1s is current for the 1.x branch and will be supported until Nov 11 2023.
+ Apache/2.4.52 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ PHP/8.1.1 appears to be outdated (current is at least 8.1.5), PHP 7.4.28 for the 7.4 branch.
+ OPTIONS: Allowed HTTP Methods: OPTIONS, HEAD, GET, POST, TRACE .
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
+ /css/: Directory indexing found.
+ /css/: This might be interesting.
+ /icons/: Directory indexing found.
+ /images/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8448 requests: 0 error(s) and 12 item(s) reported on remote host
+ End Time:           2025-01-13 18:29:48 (GMT-5) (505 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
