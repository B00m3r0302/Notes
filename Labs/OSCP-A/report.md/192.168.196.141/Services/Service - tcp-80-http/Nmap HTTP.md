```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:08 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.196.141
Nmap scan report for 192.168.196.141
Host is up, received user-set (0.45s latency).
Scanned at 2024-08-21 13:02:15 EDT for 209s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-title: Home
|_http-malware-host: Host appears to be clean
| http-headers: 
|   Date: Wed, 21 Aug 2024 17:02:33 GMT
|   Server: Apache/2.4.51 (Win64) PHP/7.4.26
|   Last-Modified: Fri, 01 Apr 2022 12:37:15 GMT
|   ETag: "901a-5db9709d9433b"
|   Accept-Ranges: bytes
|   Content-Length: 36890
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.196.141
|     
|     Path: http://192.168.196.141:80/nicepage.js
|     Line number: 21
|     Comment: 
|         /*!
|         Waypoints - 4.0.1
|         Copyright \xC2\xA9 2011-2016 Caleb Troughton
|         Licensed under the MIT license.
|         https://github.com/imakewebthings/waypoints/blob/master/licenses.txt
|         */
|     
|     Path: http://192.168.196.141:80/nicepage.js
|     Line number: 7
|     Comment: 
|         /*! PhotoSwipe - v4.1.3 - 2019-01-08
|         * http://photoswipe.com
|         * Copyright (c) 2019 Dmitry Semenov; */
|     
|     Path: http://192.168.196.141:80/nicepage.js
|     Line number: 2
|     Comment: 
|         /*!
|          * https://github.com/gilmoreorless/css-background-parser
|          * Copyright \xC2\xA9 2015 Gilmore Davidson under the MIT license: http://gilmoreorless.mit-license.org/
|          */
|     
|     Path: http://192.168.196.141:80/nicepage.js
|     Line number: 35
|     Comment: 
|         /*!
|          * gumshoejs v5.1.2
|          * A simple, framework-agnostic scrollspy script.
|          * (c) 2019 Chris Ferdinandi
|          * MIT License
|          * http://github.com/cferdinandi/gumshoe
|          */
|     
|     Path: http://192.168.196.141:80/nicepage.js
|     Line number: 13
|     Comment: 
|         /*!
|          * skrollr core
|          *
|          * Alexander Prinzhorn - https://github.com/Prinzhorn/skrollr
|          *
|          * Free to use under terms of MIT license
|          */
|     
|     Path: http://192.168.196.141:80/nicepage.js
|     Line number: 28
|     Comment: 
|         /*!
|          * JavaScript Cookie v2.2.1
|          * https://github.com/js-cookie/js-cookie
|          *
|          * Copyright 2006, 2015 Klaus Hartl & Fagner Brack
|          * Released under the MIT license
|          */
|     
|     Path: http://192.168.196.141:80/nicepage.js
|     Line number: 10
|     Comment: 
|         /*! PhotoSwipe Default UI - 4.1.3 - 2019-01-08
|         * http://photoswipe.com
|_        * Copyright (c) 2019 Dmitry Semenov; */
|_http-feed: Couldn't find any feeds.
|_http-date: Wed, 21 Aug 2024 17:02:45 GMT; -3s from local time.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-vhosts: 
|_128 names had status 200
| http-dombased-xss: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.196.141
|   Found the following indications of potential DOM based XSS: 
|     
|     Source: window.open(i.href,"pswp_share","scrollbars=yes,resizable=yes,toolbar=no,"+"location=yes,width=550,height=420,top=100,left="+(window.screen?Math.round(screen.width/2-275)
|_    Pages: http://192.168.196.141:80/nicepage.js
|_http-chrono: Request times for /; avg: 4684.46ms; min: 3292.66ms; max: 6117.38ms
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
| http-php-version: Logo query returned unknown hash 37e6bb29ab0ac359102ab80e86c0bdb8
|_Credits query returned unknown hash 37e6bb29ab0ac359102ab80e86c0bdb8
|_http-apache-negotiation: mod_negotiation enabled.
|_http-generator: Nicepage 4.8.2, nicepage.com
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.196.141
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://192.168.196.141:80/
|     Form id: name-2e40
|     Form action: #
|     
|     Path: http://192.168.196.141:80/
|     Form id: name-61fc
|_    Form action: #
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
| http-trace: TRACE is enabled
| Headers:
| Date: Wed, 21 Aug 2024 17:02:25 GMT
| Server: Apache/2.4.51 (Win64) PHP/7.4.26
| Connection: close
| Transfer-Encoding: chunked
|_Content-Type: message/http
|_http-errors: Couldn't find any error pages.
|_http-exif-spider: ERROR: Script execution failed (use -d to debug)
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; css: 2; js: 2
|     /images/
|       jpeg: 1; jpg: 3; png: 8
|   Longest directory structure:
|     Depth: 1
|     Dir: /images/
|   Total files found (by extension):
|_    Other: 1; css: 2; jpeg: 1; jpg: 3; js: 2; png: 8
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-enum: 
|   /blog/: Blog
|   /home.html: Possible admin folder
|   /icons/: Potentially interesting folder w/ directory listing
|   /images/: Potentially interesting directory w/ listing on 'apache/2.4.51 (win64) php/7.4.26'
|_  /script/: Potentially interesting directory w/ listing on 'apache/2.4.51 (win64) php/7.4.26'
|_http-mobileversion-checker: No mobile version detected.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
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
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-grep: 
|   (1) http://192.168.196.141:80/%25url%25: 
|     (1) ip: 
|_      + 192.168.196.141

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:05:44 2024 -- 1 IP address (1 host up) scanned in 215.72 seconds

```
