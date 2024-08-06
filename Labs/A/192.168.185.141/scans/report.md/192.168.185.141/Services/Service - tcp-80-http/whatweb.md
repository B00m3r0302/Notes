```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.185.141:80 2>&1
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://192.168.185.141:80
Status    : 200 OK
Title     : Home
IP        : 192.168.185.141
Country   : RESERVED, ZZ

Summary   : Apache[2.4.51], HTML5, HTTPServer[Apache/2.4.51 (Win64) PHP/7.4.26], JQuery, MetaGenerator[Nicepage 4.8.2, nicepage.com], Open-Graph-Protocol[website], PHP[7.4.26], Script[application/ld+json,text/javascript]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.51 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : Apache/2.4.51 (Win64) PHP/7.4.26 (from server string)

[ JQuery ]
	A fast, concise, JavaScript that simplifies how to traverse
	HTML documents, handle events, perform animations, and add
	AJAX.

	Website     : http://jquery.com/

[ MetaGenerator ]
	This plugin identifies meta generator tags and extracts its
	value.

	String       : Nicepage 4.8.2, nicepage.com

[ Open-Graph-Protocol ]
	The Open Graph protocol enables you to integrate your Web
	pages into the social graph. It is currently designed for
	Web pages representing profiles of real-world things .
	things like movies, sports teams, celebrities, and
	restaurants. Including Open Graph tags on your Web page,
	makes your page equivalent to a Facebook Page.

	Version      : website

[ PHP ]
	PHP is a widely-used general-purpose scripting language
	that is especially suited for Web development and can be
	embedded into HTML. This plugin identifies PHP errors,
	modules and versions and extracts the local file path and
	username if present.

	Version      : 7.4.26
	Google Dorks: (2)
	Website     : http://www.php.net/

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.

	String       : application/ld+json,text/javascript

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Tue, 06 Aug 2024 02:09:48 GMT
	Server: Apache/2.4.51 (Win64) PHP/7.4.26
	Last-Modified: Fri, 01 Apr 2022 12:37:15 GMT
	ETag: "901a-5db9709d9433b"
	Accept-Ranges: bytes
	Content-Length: 36890
	Connection: close
	Content-Type: text/html



```
