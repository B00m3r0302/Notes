```bash
nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 192.168.227.121
```

[/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp47001/tcp_47001_http_nmap.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp47001/tcp_47001_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Jul 29 08:11:41 2024 as: nmap -vv --reason -Pn -T4 -sV -p 47001 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp47001/tcp_47001_http_nmap.txt -oX /home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp47001/xml/tcp_47001_http_nmap.xml 192.168.227.121
Nmap scan report for 192.168.227.121
Host is up, received user-set (0.072s latency).
Scanned at 2024-07-29 08:11:42 EDT for 447s

Bug in http-security-headers: no string output.
PORT      STATE SERVICE REASON          VERSION
47001/tcp open  http    syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-malware-host: Host appears to be clean
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-mobileversion-checker: No mobile version detected.
|_http-comments-displayer: Couldn't find any comments.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-vhosts: 
|_128 names had status 404
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-chrono: Request times for /; avg: 212.16ms; min: 209.02ms; max: 215.68ms
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-headers: 
|   Content-Type: text/html; charset=us-ascii
|   Server: Microsoft-HTTPAPI/2.0
|   Date: Mon, 29 Jul 2024 12:11:59 GMT
|   Connection: close
|   Content-Length: 315
|   
|_  (Request type: GET)
|_http-title: Not Found
|_http-feed: Couldn't find any feeds.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=192.168.227.121
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://192.168.227.121:47001/
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
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
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-date: Mon, 29 Jul 2024 12:11:53 GMT; -1s from local time.
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 29 08:19:09 2024 -- 1 IP address (1 host up) scanned in 447.85 seconds

```
