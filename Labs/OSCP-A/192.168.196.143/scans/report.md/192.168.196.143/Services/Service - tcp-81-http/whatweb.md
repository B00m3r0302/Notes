```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.196.143:81 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_whatweb.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_whatweb.txt):

```
WhatWeb report for http://192.168.196.143:81
Status    : 200 OK
Title     : Test Page for the Nginx HTTP Server on Fedora
IP        : 192.168.196.143
Country   : RESERVED, ZZ

Summary   : Apache[2.4.41], HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], PoweredBy[Fedora,nginx]

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

[ PoweredBy ]
	This plugin identifies instances of 'Powered by x' text and
	attempts to extract the value for x.

	String       : Fedora,nginx

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Wed, 21 Aug 2024 17:09:33 GMT
	Server: Apache/2.4.41 (Ubuntu)
	Last-Modified: Mon, 10 May 2021 22:21:48 GMT
	ETag: "e74-5c201341a9efc-gzip"
	Accept-Ranges: bytes
	Vary: Accept-Encoding
	Content-Encoding: gzip
	Content-Length: 1161
	Connection: close
	Content-Type: text/html



```