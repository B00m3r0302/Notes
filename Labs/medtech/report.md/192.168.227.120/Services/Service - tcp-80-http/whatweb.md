```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.227.120:80 2>&1
```

[/home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://192.168.227.120:80
Status    : 200 OK
Title     : PAW! (PWK Awesome Website)
IP        : 192.168.227.120
Country   : RESERVED, ZZ

Summary   : HTML5, HTTPServer[WEBrick/1.6.1 (Ruby/2.7.4/2021-07-07)], Open-Graph-Protocol[website], Ruby[2.7.4,WEBrick/1.6.1], Script[application/ld+json]

Detected Plugins:
[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : WEBrick/1.6.1 (Ruby/2.7.4/2021-07-07) (from server string)

[ Open-Graph-Protocol ]
	The Open Graph protocol enables you to integrate your Web
	pages into the social graph. It is currently designed for
	Web pages representing profiles of real-world things .
	things like movies, sports teams, celebrities, and
	restaurants. Including Open Graph tags on your Web page,
	makes your page equivalent to a Facebook Page.

	Version      : website

[ Ruby ]
	Ruby is a dynamic, open source programming language with a
	focus on simplicity and productivity. It has an elegant
	syntax that is natural to read and easy to write.

	Version      : 2.7.4
	Version      : WEBrick/1.6.1
	Version      : 2.7.4
	Website     : http://www.ruby-lang.org/

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.

	String       : application/ld+json

HTTP Headers:
	HTTP/1.1 200 OK
	Etag: 65796-1229-66058b2c
	Content-Type: text/html; charset=utf-8
	Content-Length: 4649
	Last-Modified: Thu, 28 Mar 2024 15:22:20 GMT
	Cache-Control: private, max-age=0, proxy-revalidate, no-store, no-cache, must-revalidate
	Server: WEBrick/1.6.1 (Ruby/2.7.4/2021-07-07)
	Date: Mon, 29 Jul 2024 11:55:53 GMT
	Connection: close



```
