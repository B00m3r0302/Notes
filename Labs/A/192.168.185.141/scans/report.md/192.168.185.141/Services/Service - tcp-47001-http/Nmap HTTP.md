```bash
nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:19:14 2024 as: nmap -vv --reason -Pn -T4 -sV -p 47001 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/xml/tcp_47001_http_nmap.xml 192.168.185.141
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.074s latency).
Scanned at 2024-08-05 22:19:15 EDT for 443s

Bug in http-security-headers: no string output.
PORT      STATE SERVICE REASON          VERSION
47001/tcp open  http    syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-comments-displayer: Couldn't find any comments.
| http-useragent-tester: 
|   Status for browser useragent: 404
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
|_http-mobileversion-checker: No mobile version detected.
|_http-date: Tue, 06 Aug 2024 02:19:29 GMT; -2s from local time.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-title: Not Found
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-malware-host: Host appears to be clean
| http-vhosts: 
|_128 names had status 404
| http-headers: 
|   Content-Type: text/html; charset=us-ascii
|   Server: Microsoft-HTTPAPI/2.0
|   Date: Tue, 06 Aug 2024 02:19:31 GMT
|   Connection: close
|   Content-Length: 315
|   
|_  (Request type: GET)
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=192.168.185.141
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://192.168.185.141:47001/
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-chrono: Request times for /; avg: 240.85ms; min: 212.33ms; max: 271.49ms
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-feed: Couldn't find any feeds.
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:26:39 2024 -- 1 IP address (1 host up) scanned in 444.49 seconds

```
