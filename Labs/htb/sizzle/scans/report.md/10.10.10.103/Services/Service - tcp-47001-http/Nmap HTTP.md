```bash
nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:23:35 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 47001 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/xml/tcp_47001_http_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.066s latency).
Scanned at 2025-02-11 10:23:35 EST for 350s

Bug in http-security-headers: no string output.
PORT      STATE SERVICE REASON          VERSION
47001/tcp open  http    syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-comments-displayer: Couldn't find any comments.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-feed: Couldn't find any feeds.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-chrono: Request times for /; avg: 206.09ms; min: 204.43ms; max: 207.74ms
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-title: Not Found
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=10.10.10.103
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://10.10.10.103:47001/
| http-vhosts: 
|_128 names had status 404
|_http-malware-host: Host appears to be clean
|_http-date: Tue, 11 Feb 2025 15:23:42 GMT; -1s from local time.
|_http-mobileversion-checker: No mobile version detected.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-referer-checker: Couldn't find any cross-domain scripts.
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
| http-headers: 
|   Content-Type: text/html; charset=us-ascii
|   Server: Microsoft-HTTPAPI/2.0
|   Date: Tue, 11 Feb 2025 15:23:47 GMT
|   Connection: close
|   Content-Length: 315
|   
|_  (Request type: GET)
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:29:25 2025 -- 1 IP address (1 host up) scanned in 349.64 seconds

```
