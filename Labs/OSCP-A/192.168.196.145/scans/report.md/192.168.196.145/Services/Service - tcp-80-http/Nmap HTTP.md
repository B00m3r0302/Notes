```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.196.145
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:38 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.196.145
Nmap scan report for 192.168.196.145
Host is up, received user-set (0.60s latency).
Scanned at 2024-08-21 13:02:44 EDT for 810s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 125 Microsoft IIS httpd 10.0
|_http-malware-host: Host appears to be clean
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-headers: 
|   Content-Length: 30823
|   Content-Type: text/html
|   Last-Modified: Fri, 30 Jul 2021 21:15:24 GMT
|   Accept-Ranges: bytes
|   ETag: "934b038885d71:0"
|   Server: Microsoft-IIS/10.0
|   Date: Wed, 21 Aug 2024 17:03:04 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-feed: Couldn't find any feeds.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|     /assets/
|       ico: 1
|     /assets/img/
|       svg: 1
|     /assets/img/portfolio/
|       png: 6
|     /css/
|       css: 1
|     /js/
|       js: 1
|   Longest directory structure:
|     Depth: 3
|     Dir: /assets/img/portfolio/
|   Total files found (by extension):
|_    Other: 1; css: 1; ico: 1; js: 1; png: 6; svg: 1
| http-grep: 
|   (1) http://192.168.196.145:80/: 
|     (1) email: 
|_      + name@example.com
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
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-server-header: Microsoft-IIS/10.0
|_http-date: Wed, 21 Aug 2024 17:03:09 GMT; -2s from local time.
| http-vhosts: 
| 123 names had status 200
| wiki
| syslog
| citrix
| ipv6
|_mta
| http-referer-checker: 
| Spidering limited to: maxpagecount=30
|   https://cdn.startbootstrap.com:443/sb-forms-0.4.1.js
|   https://cdn.jsdelivr.net:443/npm/bootstrap15.0.2/dist/js/bootstrap.bundle.min.js
|_  https://use.fontawesome.com:443/releases/v5.15.3/js/all.js
|_http-errors: Couldn't find any error pages.
|_http-internal-ip-disclosure: ERROR: Script execution failed (use -d to debug)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.196.145
|     
|     Path: http://192.168.196.145:80/
|     Line number: 9
|     Comment: 
|         <!-- Favicon-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 7352
|     Comment: 
|         /* rtl:end:remove */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 220
|     Comment: 
|         <!-- Footer-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 208
|     Comment: 
|         <!-- Submit error message-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 190
|     Comment: 
|         <!-- Message input-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 5795
|     Comment: 
|         /* rtl:begin:ignore */
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 229
|     Comment: 
|         /* rtl:ignore */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 135
|     Comment: 
|         <!-- About Section Content-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 290
|     Comment: 
|         <!-- Portfolio Modal 2-->
|     
|     Path: http://192.168.196.145:80/js/scripts.js
|     Line number: 26
|     Comment: 
|          // Shrink the navbar 
|     
|     Path: http://192.168.196.145:80/
|     Line number: 418
|     Comment: 
|         <!-- Portfolio Modal 6-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 166
|     Comment: 
|         <!-- This form is pre-integrated with SB Forms.-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 253
|     Comment: 
|         <!-- Copyright Section-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 267
|     Comment: 
|         <!-- Portfolio Modal - Title-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 13
|     Comment: 
|         <!-- Google fonts-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 452
|     Comment: 
|         <!-- Core theme JS-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 7
|     Comment: 
|         /*!
|          * Bootstrap v5.0.2 (https://getbootstrap.com/)
|          * Copyright 2011-2021 The Bootstrap Authors
|          * Copyright 2011-2021 Twitter, Inc.
|          * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
|          */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 85
|     Comment: 
|         <!-- Portfolio Item 3-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 20
|     Comment: 
|         <!-- Navigation-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 171
|     Comment: 
|         <!-- Name input-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 160
|     Comment: 
|         <!-- Contact Section Form-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 168
|     Comment: 
|         <!-- https://startbootstrap.com/solution/contact-forms-->
|     
|     Path: http://192.168.196.145:80/js/scripts.js
|     Line number: 12
|     Comment: 
|          // Navbar shrink function
|     
|     Path: http://192.168.196.145:80/
|     Line number: 163
|     Comment: 
|         <!-- * * * * * * * * * * * * * * *-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 450
|     Comment: 
|         <!-- Bootstrap core JS-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 2
|     Comment: 
|         /*!
|         * Start Bootstrap - Freelancer v7.0.3 (https://startbootstrap.com/theme/freelancer)
|         * Copyright 2013-2021 Start Bootstrap
|         * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
|         */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 167
|     Comment: 
|         <!-- To make this form functional, sign up at-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 5806
|     Comment: 
|         /* rtl:end:ignore */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 169
|     Comment: 
|         <!-- to get an API token!-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 454
|     Comment: 
|         <!-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 184
|     Comment: 
|         <!-- Phone number input-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 54
|     Comment: 
|         <!-- Portfolio Section-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 67
|     Comment: 
|         <!-- Portfolio Item 1-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 140
|     Comment: 
|         <!-- About Section Button-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 94
|     Comment: 
|         <!-- Portfolio Item 4-->
|     
|     Path: http://192.168.196.145:80/js/scripts.js
|     Line number: 41
|     Comment: 
|          // Collapse responsive navbar when toggler is visible
|     
|     Path: http://192.168.196.145:80/
|     Line number: 199
|     Comment: 
|         <!-- has successfully submitted-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 455
|     Comment: 
|         <!-- * *                               SB Forms JS                               * *-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 241
|     Comment: 
|         <!-- Footer About Text-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 196
|     Comment: 
|         <!-- Submit success message-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 76
|     Comment: 
|         <!-- Portfolio Item 2-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 40
|     Comment: 
|         <!-- Masthead Avatar Image-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 112
|     Comment: 
|         <!-- Portfolio Item 6-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 258
|     Comment: 
|         <!-- Portfolio Modal 1-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 211
|     Comment: 
|         <!-- an error submitting the form-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 456
|     Comment: 
|         <!-- * * Activate your form at https://startbootstrap.com/solution/contact-forms * *-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 7346
|     Comment: 
|         /* rtl:begin:remove */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 127
|     Comment: 
|         <!-- About Section Heading-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 322
|     Comment: 
|         <!-- Portfolio Modal 3-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 177
|     Comment: 
|         <!-- Email address input-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 4556
|     Comment: 
|         /* rtl: var(--bs-breadcrumb-divider, "/") */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 354
|     Comment: 
|         <!-- Portfolio Modal 4-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 42
|     Comment: 
|         <!-- Masthead Heading-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 413
|     Comment: 
|         /* rtl:raw:
|         [type="tel"],
|         [type="url"],
|         [type="email"],
|         [type="number"] {
|           direction: ltr;
|         }
|         */
|     
|     Path: http://192.168.196.145:80/js/scripts.js
|     Line number: 32
|     Comment: 
|          // Activate Bootstrap scrollspy on the main nav element
|     
|     Path: http://192.168.196.145:80/js/scripts.js
|     Line number: 29
|     Comment: 
|          // Shrink the navbar when page is scrolled
|     
|     Path: http://192.168.196.145:80/js/scripts.js
|     Line number: 8
|     Comment: 
|         
|         // 
|     
|     Path: http://192.168.196.145:80/js/scripts.js
|     Line number: 6
|     Comment: 
|         
|         //
|     
|     Path: http://192.168.196.145:80/
|     Line number: 11
|     Comment: 
|         <!-- Font Awesome icons (free version)-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 210
|     Comment: 
|         <!-- This is what your users will see when there is-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 275
|     Comment: 
|         <!-- Portfolio Modal - Image-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 57
|     Comment: 
|         <!-- Portfolio Section Heading-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 103
|     Comment: 
|         <!-- Portfolio Item 5-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 213
|     Comment: 
|         <!-- Submit Button-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 233
|     Comment: 
|         <!-- Footer Social Icons-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 197
|     Comment: 
|         <!---->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 386
|     Comment: 
|         <!-- Portfolio Modal 5-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 164
|     Comment: 
|         <!-- * * SB Forms Contact Form * *-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 277
|     Comment: 
|         <!-- Portfolio Modal - Text-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 124
|     Comment: 
|         <!-- About Section-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 37
|     Comment: 
|         <!-- Masthead-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 16
|     Comment: 
|         <!-- Core theme CSS (includes Bootstrap)-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 257
|     Comment: 
|         <!-- Portfolio Modals-->
|     
|     Path: http://192.168.196.145:80/css/styles.css
|     Line number: 5882
|     Comment: 
|         /* rtl:options: {
|           "autoRename": true,
|           "stringMap":[ {
|             "name"    : "prev-next",
|             "search"  : "prev",
|             "replace" : "next"
|           } ]
|         } */
|     
|     Path: http://192.168.196.145:80/
|     Line number: 65
|     Comment: 
|         <!-- Portfolio Grid Items-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 50
|     Comment: 
|         <!-- Masthead Subheading-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 224
|     Comment: 
|         <!-- Footer Location-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 44
|     Comment: 
|         <!-- Icon Divider-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 149
|     Comment: 
|         <!-- Contact Section-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 198
|     Comment: 
|         <!-- This is what your users will see when the form-->
|     
|     Path: http://192.168.196.145:80/
|     Line number: 152
|     Comment: 
|_        <!-- Contact Section Heading-->
|_http-mobileversion-checker: No mobile version detected.
|_http-chrono: Request times for /; avg: 2054.81ms; min: 1191.13ms; max: 3765.13ms
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-favicon: Unknown favicon MD5: 556F31ACD686989B1AFCF382C05846AA
| http-fileupload-exploiter: 
|   
|_    Couldn't find a file-type field.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-title: Samuel's Personal Site
| http-php-version: Logo query returned unknown hash 9f850357265c324b78b89e82e4e8ec7c
|_Credits query returned unknown hash 9f850357265c324b78b89e82e4e8ec7c
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:16:14 2024 -- 1 IP address (1 host up) scanned in 816.14 seconds

```
