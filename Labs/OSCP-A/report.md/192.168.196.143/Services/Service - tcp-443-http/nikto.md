```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.196.143:443 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_nikto.txt"
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_nikto.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.196.143
+ Target Hostname:    192.168.196.143
+ Target Port:        443
+ Start Time:         2024-08-21 13:09:32 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Multiple index files found: /index.php, /index.html.
+ Apache/2.4.41 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 2aa6, size: 5c20133410907, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ ERROR: Error limit (20) reached for host, giving up. Last error: 
+ Scan terminated: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2024-08-21 13:41:47 (GMT-4) (1935 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```