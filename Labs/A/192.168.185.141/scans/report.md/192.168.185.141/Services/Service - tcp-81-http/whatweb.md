```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.185.141:81 2>&1
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_whatweb.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_whatweb.txt):

```
WhatWeb report for http://192.168.185.141:81
Status    : 200 OK
Title     : Attendance and Payroll System
IP        : 192.168.185.141
Country   : RESERVED, ZZ

Summary   : Apache[2.4.51], Bootstrap, Cookies[PHPSESSID], HTML5, HTTPServer[Apache/2.4.51 (Win64) PHP/7.4.26], JQuery, PHP[7.4.26], Script[text/javascript], X-Powered-By[PHP/7.4.26], X-UA-Compatible[IE=edge]

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

[ Bootstrap ]
	Bootstrap is an open source toolkit for developing with
	HTML, CSS, and JS.

	Website     : https://getbootstrap.com/

[ Cookies ]
	Display the names of cookies in the HTTP headers. The
	values are not returned to save on space.

	String       : PHPSESSID

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

[ PHP ]
	PHP is a widely-used general-purpose scripting language
	that is especially suited for Web development and can be
	embedded into HTML. This plugin identifies PHP errors,
	modules and versions and extracts the local file path and
	username if present.

	Version      : 7.4.26
	Version      : 7.4.26
	Google Dorks: (2)
	Website     : http://www.php.net/

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.

	String       : text/javascript

[ X-Powered-By ]
	X-Powered-By HTTP header

	String       : PHP/7.4.26 (from x-powered-by string)

[ X-UA-Compatible ]
	This plugin retrieves the X-UA-Compatible value from the
	HTTP header and meta http-equiv tag. - More Info:
	http://msdn.microsoft.com/en-us/library/cc817574.aspx

	String       : IE=edge

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Tue, 06 Aug 2024 02:09:49 GMT
	Server: Apache/2.4.51 (Win64) PHP/7.4.26
	X-Powered-By: PHP/7.4.26
	Set-Cookie: PHPSESSID=1nr682pu1mtq1jv06gem21g3q2; path=/
	Expires: Thu, 19 Nov 1981 08:52:00 GMT
	Cache-Control: no-store, no-cache, must-revalidate
	Pragma: no-cache
	Content-Length: 4280
	Connection: close
	Content-Type: text/html; charset=UTF-8



```