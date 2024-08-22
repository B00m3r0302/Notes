```bash
nmap -vv --reason -Pn -T4 -sV -p 443 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/xml/tcp_443_http_nmap.xml" 192.168.196.143
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:09:29 2024 as: nmap -vv --reason -Pn -T4 -sV -p 443 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/xml/tcp_443_http_nmap.xml 192.168.196.143
Nmap scan report for 192.168.196.143
Host is up, received user-set (0.15s latency).
Scanned at 2024-08-21 13:09:33 EDT for 371s

PORT    STATE SERVICE REASON         VERSION
443/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.41
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.196.143
|     
|     Path: http://192.168.196.143:443/
|     Line number: 4
|     Comment: 
|         <!--
|             Modified from the Debian original for Ubuntu
|             Last updated: 2016-11-16
|             See: https://launchpad.net/bugs/1288690
|           -->
|     
|     Path: http://192.168.196.143:443/
|     Line number: 201
|     Comment: 
|         <!--      <div class="table_of_contents floating_element">
|                 <div class="section_header section_header_grey">
|                   TABLE OF CONTENTS
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#about">About</a>
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#changes">Changes</a>
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#scope">Scope</a>
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#files">Config files</a>
|                 </div>
|               </div>
|_        -->
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|     /icons/
|       png: 1
|   Longest directory structure:
|     Depth: 1
|     Dir: /icons/
|   Total files found (by extension):
|_    Other: 1; png: 1
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-security-headers: 
|   Strict_Transport_Security: 
|_    HSTS not configured in HTTPS Server
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-date: Wed, 21 Aug 2024 17:09:47 GMT; -2s from local time.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-mobileversion-checker: No mobile version detected.
|_http-chrono: Request times for /; avg: 2163.64ms; min: 893.95ms; max: 5646.05ms
|_http-malware-host: Host appears to be clean
|_http-title: Apache2 Ubuntu Default Page: It works
| http-vhosts: 
| 101 names had status 200
|_27 names had status ERROR
| http-grep: 
|   (1) http://192.168.196.143:443/manual: 
|     (1) ip: 
|_      + 192.168.196.143
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=192.168.196.143
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://192.168.196.143:443/manual
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
| http-headers: 
|   Date: Wed, 21 Aug 2024 17:10:16 GMT
|   Server: Apache/2.4.41 (Ubuntu)
|   Last-Modified: Mon, 10 May 2021 22:21:34 GMT
|   ETag: "2aa6-5c20133410907"
|   Accept-Ranges: bytes
|   Content-Length: 10918
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-feed: Couldn't find any feeds.
| http-referer-checker: 
| Spidering limited to: maxpagecount=30
|   https://192.168.196.143:443/themes/default/js/utils.js
|   https://192.168.196.143:443/themes/default/js/pico.js
|_  https://192.168.196.143:443/themes/default/js/modernizr-3.3.1-custom.min.js
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
| http-useragent-tester: 
|   Allowed User Agents: 
|     GT::WWW
|   Change in Status Code: 
|     WWW-Mechanize/1.34: 200
|     Snoopy: 200
|     Wget/1.13.4 (linux-gnu): 200
|     PECL::HTTP: 200
|     PHPCrawl: 200
|     http client: 200
|     lwp-trivial: 200
|     libwww: 200
|     Zend_Http_Client: 200
|     Python-urllib/2.5: 200
|     libcurl-agent/1.0: 200
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html): 200
|     HTTP::Lite: 200
|     URI::Fetch: 200
|     PHP/: 200
|_    MFC_Tear_Sample: 200
|_ssl-ccs-injection: No reply from server (TIMEOUT)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
| http-enum: 
|   /0/: Potentially interesting folder
|_  /index/: Potentially interesting folder
Service Info: Host: 127.0.0.2

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:15:44 2024 -- 1 IP address (1 host up) scanned in 375.74 seconds

```
