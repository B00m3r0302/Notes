```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.196.143:443 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_whatweb.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_whatweb.txt):

```
WhatWeb report for http://192.168.196.143:443
Status    : 200 OK
Title     : Apache2 Ubuntu Default Page: It works
IP        : 192.168.196.143
Country   : RESERVED, ZZ

Summary   : Apache[2.4.41], HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.41 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : Ubuntu Linux
	String       : Apache/2.4.41 (Ubuntu) (from server string)

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Wed, 21 Aug 2024 17:09:34 GMT
	Server: Apache/2.4.41 (Ubuntu)
	Last-Modified: Mon, 10 May 2021 22:21:34 GMT
	ETag: "2aa6-5c20133410907-gzip"
	Accept-Ranges: bytes
	Vary: Accept-Encoding
	Content-Encoding: gzip
	Content-Length: 3138
	Connection: close
	Content-Type: text/html



```
