```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.196.141:80 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/tcp_80_http_nikto.txt"
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/tcp_80_http_nikto.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/tcp_80_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.196.141
+ Target Hostname:    192.168.196.141
+ Target Port:        80
+ Start Time:         2024-08-21 13:02:16 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.51 (Win64) PHP/7.4.26
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Apache/2.4.51 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ PHP/7.4.26 appears to be outdated (current is at least 8.1.5), PHP 7.4.28 for the 7.4 branch.
+ /index: Uncommon header 'tcn' found, with contents: list.
+ /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.html. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD, TRACE .
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
+ /icons/: Directory indexing found.
+ /images/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ ERROR: Error limit (20) reached for host, giving up. Last error: 
+ Scan terminated: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2024-08-21 14:02:06 (GMT-4) (3590 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
