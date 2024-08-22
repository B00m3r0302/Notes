```bash
nmap -vv --reason -Pn -T4 -sV -p 81 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/xml/tcp_81_http_nmap.xml" 192.168.196.143
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:09:29 2024 as: nmap -vv --reason -Pn -T4 -sV -p 81 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/xml/tcp_81_http_nmap.xml 192.168.196.143
Nmap scan report for 192.168.196.143
Host is up, received user-set (0.15s latency).
Scanned at 2024-08-21 13:09:30 EDT for 188s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON         VERSION
81/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.41 ((Ubuntu))
|_http-chrono: Request times for /; avg: 2235.36ms; min: 888.48ms; max: 4708.72ms
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-mobileversion-checker: No mobile version detected.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-date: Wed, 21 Aug 2024 17:10:14 GMT; -1s from local time.
| http-headers: 
|   Date: Wed, 21 Aug 2024 17:09:54 GMT
|   Server: Apache/2.4.41 (Ubuntu)
|   Last-Modified: Mon, 10 May 2021 22:21:48 GMT
|   ETag: "e74-5c201341a9efc"
|   Accept-Ranges: bytes
|   Content-Length: 3700
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-malware-host: Host appears to be clean
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-title: Test Page for the Nginx HTTP Server on Fedora
|_http-errors: Couldn't find any error pages.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-php-version: Logo query returned unknown hash 9a3e19f24fe322a35f4978dd3d55fe91
|_Credits query returned unknown hash 9a3e19f24fe322a35f4978dd3d55fe91
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.196.143
|     
|     Path: http://192.168.196.143:81/
|     Line number: 72
|     Comment: 
|         /*]]>*/
|     
|     Path: http://192.168.196.143:81/
|     Line number: 8
|     Comment: 
|_        /*<![CDATA[*/
| http-vhosts: 
| 107 names had status 200
|_21 names had status ERROR
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1
|_http-traceroute: ERROR: Script execution failed (use -d to debug)
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-feed: Couldn't find any feeds.
|_http-server-header: Apache/2.4.41 (Ubuntu)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:12:38 2024 -- 1 IP address (1 host up) scanned in 189.51 seconds

```
