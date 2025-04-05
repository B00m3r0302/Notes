```bash
whatweb --color=never --no-errors -a 3 -v https://10.10.10.103:443 2>&1
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_whatweb.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_whatweb.txt):

```
WhatWeb report for https://10.10.10.103:443
Status    : 200 OK
Title     : <None>
IP        : 10.10.10.103
Country   : RESERVED, ZZ

Summary   : HTTPServer[Microsoft-IIS/10.0], Microsoft-IIS[10.0], X-Powered-By[ASP.NET]

Detected Plugins:
[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : Microsoft-IIS/10.0 (from server string)

[ Microsoft-IIS ]
	Microsoft Internet Information Services (IIS) for Windows
	Server is a flexible, secure and easy-to-manage Web server
	for hosting anything on the Web. From media streaming to
	web application hosting, IIS's scalable and open
	architecture is ready to handle the most demanding tasks.

	Version      : 10.0
	Website     : http://www.iis.net/

[ X-Powered-By ]
	X-Powered-By HTTP header

	String       : ASP.NET (from x-powered-by string)

HTTP Headers:
	HTTP/1.1 200 OK
	Content-Type: text/html
	Last-Modified: Thu, 12 Jul 2018 17:39:25 GMT
	Accept-Ranges: bytes
	ETag: "56f2784671ad41:0"
	Server: Microsoft-IIS/10.0
	X-Powered-By: ASP.NET
	Date: Tue, 11 Feb 2025 15:21:30 GMT
	Connection: close
	Content-Length: 60



```
