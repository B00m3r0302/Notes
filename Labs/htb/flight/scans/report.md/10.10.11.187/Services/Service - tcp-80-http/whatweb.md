```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.11.187:80 2>&1
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://10.10.11.187:80
Status    : 200 OK
Title     : g0 Aviation
IP        : 10.10.11.187
Country   : RESERVED, ZZ

Summary   : Apache[2.4.52], HTML5, HTTPServer[Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1], JQuery[1.4.2], OpenSSL[1.1.1m], PHP[8.1.1], Script[text/javascript]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.52 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1 (from server string)

[ JQuery ]
	A fast, concise, JavaScript that simplifies how to traverse
	HTML documents, handle events, perform animations, and add
	AJAX.

	Version      : 1.4.2
	Website     : http://jquery.com/

[ OpenSSL ]
	The OpenSSL Project is a collaborative effort to develop a
	robust, commercial-grade, full-featured, and Open Source
	toolkit implementing the Secure Sockets Layer (SSL v2/v3)
	and Transport Layer Security (TLS v1) protocols as well as
	a full-strength general purpose cryptography library.

	Version      : 1.1.1m
	Website     : http://www.openssl.org/

[ PHP ]
	PHP is a widely-used general-purpose scripting language
	that is especially suited for Web development and can be
	embedded into HTML. This plugin identifies PHP errors,
	modules and versions and extracts the local file path and
	username if present.

	Version      : 8.1.1
	Google Dorks: (2)
	Website     : http://www.php.net/

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.

	String       : text/javascript

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Tue, 14 Jan 2025 06:21:25 GMT
	Server: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1
	Last-Modified: Thu, 24 Feb 2022 05:58:10 GMT
	ETag: "1b9d-5d8bd444f0080"
	Accept-Ranges: bytes
	Content-Length: 7069
	Connection: close
	Content-Type: text/html



```
