```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.196.143
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:09:28 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.196.143
Nmap scan report for 192.168.196.143
Host is up, received user-set (0.13s latency).
Scanned at 2024-08-21 13:09:29 EDT for 207s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.41 ((Ubuntu))
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-grep: 
|   (1) http://192.168.196.143:80/manual: 
|     (1) ip: 
|_      + 192.168.196.143
|_http-feed: Couldn't find any feeds.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 2
|     /icons/
|       png: 1
|     /themes/default/css/
|       css: 3
|     /themes/default/img/
|       svg: 1
|     /themes/default/js/
|       js: 3
|   Longest directory structure:
|     Depth: 3
|     Dir: /themes/default/js/
|   Total files found (by extension):
|_    Other: 2; css: 3; js: 3; png: 1; svg: 1
| http-headers: 
|   Date: Wed, 21 Aug 2024 17:10:40 GMT
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
|_http-malware-host: Host appears to be clean
|_http-date: Wed, 21 Aug 2024 17:09:37 GMT; -11s from local time.
|_http-chrono: Request times for /; avg: 2962.50ms; min: 342.96ms; max: 6036.21ms
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=192.168.196.143
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://192.168.196.143:80/manual
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-mobileversion-checker: No mobile version detected.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
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
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.196.143
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 227
|     Comment: 
|         /*** UTILITIES ***/
|     
|     Path: http://192.168.196.143:80/themes/default/js/utils.js
|     Line number: 71
|     Comment: 
|         /**
|          * Slides a element down (i.e. show a hidden element)
|          *
|          * @param {HTMLElement} element        the element to slide down
|          * @param {function}    finishCallback function to call when the animation has
|          *     been finished (i.e. the element is visible)
|          * @param {function}    startCallback  function to call when the animation starts
|          */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 1
|     Comment: 
|         /**
|          * Pico's Default Theme
|          *
|          * Pico's default theme is a bit bare - but that's intentional! The default
|          * theme isn't meant for production use, it's actually a template for you to
|          * design your own theme around.
|          *
|          * Pico is a stupidly simple, blazing fast, flat file CMS.
|          *
|          * @author  Gilbert Pellegrom
|          * @author  Daniel Rudolf
|          * @link    http://picocms.org
|          * @license http://opensource.org/licenses/MIT The MIT License
|          * @version 3.0
|          */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 64
|     Comment: 
|         /*** BASIC LAYOUT: HEADER ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 58
|     Comment: 
|         /* '\xEE\xA0\x80' */
|     
|     Path: http://192.168.196.143:80/themes/default/js/utils.js
|     Line number: 14
|     Comment: 
|         /**
|          * Checks whether the client's browser is able to slide elements or not
|          *
|          * @return {bool} TRUE when the browser supports sliding, FALSE otherwise
|          */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 40
|     Comment: 
|         /* fix buttons height, for twitter bootstrap */
|     
|     Path: http://192.168.196.143:80/
|     Line number: 4
|     Comment: 
|         <!--
|             Modified from the Debian original for Ubuntu
|             Last updated: 2016-11-16
|             See: https://launchpad.net/bugs/1288690
|           -->
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 104
|     Comment: 
|         /* IE8 + IE9 clearfix */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 279
|     Comment: 
|         /*** LISTS ***/
|     
|     Path: http://192.168.196.143:80/
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
|         -->
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 12
|     Comment: 
|         /* Chrome hack: SVG is rendered more smooth in Windozze. 100% magic, uncomment if you need it. */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 36
|     Comment: 
|         /* For safety - reset parent styles, that can break glyph codes*/
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 61
|     Comment: 
|         /* '\xEF\x85\x95' */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 43
|     Comment: 
|         /* Animation center compensation - margins should be symmetric */
|     
|     Path: http://192.168.196.143:80/themes/default/js/utils.js
|     Line number: 1
|     Comment: 
|         /**
|          * Pico's Default Theme - JavaScript helper
|          *
|          * Pico is a stupidly simple, blazing fast, flat file CMS.
|          *
|          * @author  Daniel Rudolf
|          * @link    http://picocms.org
|          * @license http://opensource.org/licenses/MIT The MIT License
|          * @version 3.0
|          */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 59
|     Comment: 
|         /* '\xEF\x82\x9B' */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 14
|     Comment: 
|         /*
|         @media screen and (-webkit-min-device-pixel-ratio:0) {
|             @font-face {
|                 font-family: 'fontello';
|                 src: url('../icon/fontello.svg?13793670#fontello') format('svg');
|             }
|         }
|         */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 13
|     Comment: 
|         /* Note, that will break hinting! In other OS-es font will be not as sharp as it could be */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 111
|     Comment: 
|         /*** BASIC LAYOUT: FOOTER ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 320
|     Comment: 
|         /*** BLOCKQUOTE ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 60
|     Comment: 
|         /* '\xEF\x83\x89' */
|     
|     Path: http://192.168.196.143:80/themes/default/js/pico.js
|     Line number: 17
|     Comment: 
|          // wrap tables
|     
|     Path: http://192.168.196.143:80/themes/default/js/pico.js
|     Line number: 29
|     Comment: 
|          // responsive menu
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 55
|     Comment: 
|         /* text-shadow: 1px 1px 1px rgba(127, 127, 127, 0.3); */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 54
|     Comment: 
|         /* Uncomment for 3D effect */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 50
|     Comment: 
|         /* Font smoothing. That was taken from TWBS */
|     
|     Path: http://192.168.196.143:80/themes/default/js/pico.js
|     Line number: 14
|     Comment: 
|          // capability CSS classes
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 132
|     Comment: 
|         /*** BASIC LAYOUT: EXTRA SMALL DEVICES ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 44
|     Comment: 
|         /* remove if not needed */
|     
|     Path: http://192.168.196.143:80/themes/default/js/utils.js
|     Line number: 24
|     Comment: 
|         /**
|          * Slides a element up (i.e. hide a element by changing its height to 0px)
|          *
|          * @param {HTMLElement} element        the element to slide up
|          * @param {function}    finishCallback function to call when the animation has
|          *     been finished (i.e. the element is hidden)
|          * @param {function}    startCallback  function to call when the animation starts
|          */
|     
|     Path: http://192.168.196.143:80/themes/default/js/modernizr-3.3.1-custom.min.js
|     Line number: 1
|     Comment: 
|         /*! modernizr 3.3.1 (Custom Build) | MIT *
|          * https://modernizr.com/download/?-classlist-csstransitions-requestanimationframe !*/
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 34
|     Comment: 
|         /* opacity: .8; */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 250
|     Comment: 
|         /*** TABLES ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 291
|     Comment: 
|         /*** CODE ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 329
|     Comment: 
|         /*** FORMS ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 47
|     Comment: 
|         /* you can be more comfortable with increased icons size */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 173
|     Comment: 
|         /*** TYPOGRAPHY ***/
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 382
|     Comment: 
|         /* Firefox input size fix */
|     
|     Path: http://192.168.196.143:80/themes/default/css/fontello.css
|     Line number: 48
|     Comment: 
|         /* font-size: 120%; */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 42
|     Comment: 
|         /*** BASIC LAYOUT ***/
|     
|     Path: http://192.168.196.143:80/themes/default/js/utils.js
|     Line number: 124
|     Comment: 
|         /**
|          * Checks whether a element is visible or not
|          *
|          * @param {HTMLElement} element the element to check
|          *
|          * @return {bool} TRUE when the element is visible, FALSE otherwise
|          */
|     
|     Path: http://192.168.196.143:80/themes/default/css/style.css
|     Line number: 61
|     Comment: 
|_        /* very ugly overflow fix, avoid this whenever possible! */
|_http-traceroute: ERROR: Script execution failed (use -d to debug)
| http-vhosts: 
| 85 names had status ERROR
|_43 names had status 200
|_http-title: Apache2 Ubuntu Default Page: It works

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:12:56 2024 -- 1 IP address (1 host up) scanned in 208.35 seconds

```
