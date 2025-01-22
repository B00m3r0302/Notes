```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.10.175:80 2>&1
```

[/home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://10.10.10.175:80
Status    : 200 OK
Title     : Egotistical Bank :: Home
IP        : 10.10.10.175
Country   : RESERVED, ZZ

Summary   : Bootstrap[4.0.0], Email[example@email.com,info@example.com], HTML5, HTTPServer[Microsoft-IIS/10.0], Microsoft-IIS[10.0], Script

Detected Plugins:
[ Bootstrap ]
	Bootstrap is an open source toolkit for developing with
	HTML, CSS, and JS.

	Version      : 4.0.0
	Website     : https://getbootstrap.com/

[ Email ]
	Extract email addresses. Find valid email address and
	syntactically invalid email addresses from mailto: link
	tags. We match syntactically invalid links containing
	mailto: to catch anti-spam email addresses, eg. bob at
	gmail.com. This uses the simplified email regular
	expression from
	http://www.regular-expressions.info/email.html for valid
	email address matching.

	String       : example@email.com,info@example.com
	String       : example@email.com

[ HTML5 ]
	HTML version 5, detected by the doctype declaration


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

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.


HTTP Headers:
	HTTP/1.1 200 OK
	Content-Type: text/html
	Content-Encoding: gzip
	Last-Modified: Thu, 23 Jan 2020 17:14:44 GMT
	Accept-Ranges: bytes
	ETag: "01ae9b10d2d51:0"
	Vary: Accept-Encoding
	Server: Microsoft-IIS/10.0
	Date: Wed, 22 Jan 2025 22:52:02 GMT
	Connection: close
	Content-Length: 4868



```
