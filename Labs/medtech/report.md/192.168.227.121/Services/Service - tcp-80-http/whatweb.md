```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.227.121:80 2>&1
```

[/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://192.168.227.121:80
Status    : 200 OK
Title     : ,MedTech
IP        : 192.168.227.121
Country   : RESERVED, ZZ

Summary   : ASP_NET[4.0.30319], Bootstrap[4.3.1], HTML5, HTTPServer[Microsoft-IIS/10.0], JQuery[1.12.4], Meta-Author[Offensive Security], Microsoft-IIS[10.0], Modernizr[3.5.0.min], Script, X-Powered-By[ASP.NET], X-UA-Compatible[ie=edge]

Detected Plugins:
[ ASP_NET ]
	ASP.NET is a free web framework that enables great Web
	applications. Used by millions of developers, it runs some
	of the biggest sites in the world.

	Version      : 4.0.30319 (from X-AspNet-Version HTTP header)
	Google Dorks: (2)
	Website     : https://www.asp.net/

[ Bootstrap ]
	Bootstrap is an open source toolkit for developing with
	HTML, CSS, and JS.

	Version      : 4.3.1
	Website     : https://getbootstrap.com/

[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : Microsoft-IIS/10.0 (from server string)

[ JQuery ]
	A fast, concise, JavaScript that simplifies how to traverse
	HTML documents, handle events, perform animations, and add
	AJAX.

	Version      : 1.12.4
	Website     : http://jquery.com/

[ Meta-Author ]
	This plugin retrieves the author name from the meta name
	tag - info:
	http://www.webmarketingnow.com/tips/meta-tags-uncovered.html
	#author

	String       : Offensive Security

[ Microsoft-IIS ]
	Microsoft Internet Information Services (IIS) for Windows
	Server is a flexible, secure and easy-to-manage Web server
	for hosting anything on the Web. From media streaming to
	web application hosting, IIS's scalable and open
	architecture is ready to handle the most demanding tasks.

	Version      : 10.0
	Website     : http://www.iis.net/

[ Modernizr ]
	Modernizr adds classes to the <html> element which allow
	you to target specific browser functionality in your
	stylesheet. You don't actually need to write any Javascript
	to use it. [JavaScript]

	Version      : 3.5.0.min
	Website     : http://www.modernizr.com/

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.


[ X-Powered-By ]
	X-Powered-By HTTP header

	String       : ASP.NET (from x-powered-by string)

[ X-UA-Compatible ]
	This plugin retrieves the X-UA-Compatible value from the
	HTTP header and meta http-equiv tag. - More Info:
	http://msdn.microsoft.com/en-us/library/cc817574.aspx

	String       : ie=edge

HTTP Headers:
	HTTP/1.1 200 OK
	Cache-Control: private
	Content-Type: text/html; charset=utf-8
	Server: Microsoft-IIS/10.0
	X-AspNet-Version: 4.0.30319
	X-Powered-By: ASP.NET
	Date: Mon, 29 Jul 2024 11:57:04 GMT
	Connection: close
	Content-Length: 25997



```
