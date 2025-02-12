```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:21:29 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.056s latency).
Scanned at 2025-02-11 10:21:29 EST for 176s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 127 Microsoft IIS httpd 10.0
|_http-malware-host: Host appears to be clean
| http-headers: 
|   Content-Length: 60
|   Content-Type: text/html
|   Last-Modified: Thu, 12 Jul 2018 17:39:25 GMT
|   Accept-Ranges: bytes
|   ETag: "56f2784671ad41:0"
|   Server: Microsoft-IIS/10.0
|   X-Powered-By: ASP.NET
|   Date: Tue, 11 Feb 2025 15:21:39 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-server-header: Microsoft-IIS/10.0
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-chrono: Request times for /; avg: 199.99ms; min: 159.46ms; max: 211.66ms
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-comments-displayer: Couldn't find any comments.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-feed: Couldn't find any feeds.
|_http-mobileversion-checker: No mobile version detected.
| http-vhosts: 
|_128 names had status 200
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|     /images/
|       gif: 1
|   Longest directory structure:
|     Depth: 1
|     Dir: /images/
|   Total files found (by extension):
|_    Other: 1; gif: 1
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
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
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-errors: Couldn't find any error pages.
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-date: Tue, 11 Feb 2025 15:21:39 GMT; -1s from local time.
| http-php-version: Logo query returned unknown hash 4dbbfe6aa4e77727db30e3fd5d6ed2f0
|_Credits query returned unknown hash 4dbbfe6aa4e77727db30e3fd5d6ed2f0
|_http-title: Site doesn't have a title (text/html).
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:24:25 2025 -- 1 IP address (1 host up) scanned in 176.33 seconds

```
