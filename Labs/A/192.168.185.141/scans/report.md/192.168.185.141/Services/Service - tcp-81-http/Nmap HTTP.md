```bash
nmap -vv --reason -Pn -T4 -sV -p 81 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/xml/tcp_81_http_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:09:33 2024 as: nmap -vv --reason -Pn -T4 -sV -p 81 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/xml/tcp_81_http_nmap.xml 192.168.185.141
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.069s latency).
Scanned at 2024-08-05 22:09:35 EDT for 72s

PORT   STATE SERVICE REASON          VERSION
81/tcp open  http    syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
| http-php-version: Logo query returned unknown hash d32216776ce290a041979aedde4ac28f
| Credits query returned unknown hash d32216776ce290a041979aedde4ac28f
|_Version from header x-powered-by: PHP/7.4.26
|_http-date: Tue, 06 Aug 2024 02:09:40 GMT; -2s from local time.
| http-security-headers: 
|   Cache_Control: 
|     Header: Cache-Control: no-store, no-cache, must-revalidate
|   Pragma: 
|     Header: Pragma: no-cache
|   Expires: 
|_    Header: Expires: Thu, 19 Nov 1981 08:52:00 GMT
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
| http-trace: TRACE is enabled
| Headers:
| Date: Tue, 06 Aug 2024 02:09:44 GMT
| Server: Apache/2.4.51 (Win64) PHP/7.4.26
| Connection: close
| Transfer-Encoding: chunked
|_Content-Type: message/http
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-title: Attendance and Payroll System
|_http-apache-negotiation: mod_negotiation enabled.
|_http-chrono: Request times for /; avg: 1342.25ms; min: 424.88ms; max: 2974.38ms
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-headers: 
|   Date: Tue, 06 Aug 2024 02:09:48 GMT
|   Server: Apache/2.4.51 (Win64) PHP/7.4.26
|   X-Powered-By: PHP/7.4.26
|   Set-Cookie: PHPSESSID=urk5jqp8vso6amn3bjl0rkgpvj; path=/
|   Expires: Thu, 19 Nov 1981 08:52:00 GMT
|   Cache-Control: no-store, no-cache, must-revalidate
|   Pragma: no-cache
|   Connection: close
|   Content-Type: text/html; charset=UTF-8
|   
|_  (Request type: HEAD)
|_http-malware-host: Host appears to be clean
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|       httponly flag not set
|   /admin/: 
|     PHPSESSID: 
|       httponly flag not set
|   /admin/index.php: 
|     PHPSESSID: 
|       httponly flag not set
|   /Admin/: 
|     PHPSESSID: 
|       httponly flag not set
|   /index/: 
|     PHPSESSID: 
|_      httponly flag not set
| http-vhosts: 
|_128 names had status 200
|_http-feed: Couldn't find any feeds.
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.185.141
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1515
|     Comment: 
|          // behaves the same as moment#day except
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3252
|     Comment: 
|         /*
|          * Create a callback list using the following parameters:
|          *
|          *	options: an optional list of space-separated options that will change how
|          *			the callback list behaves or a more traditional option object
|          *
|          * By default a callback list will act like an event callback list and can be
|          * "fired" multiple times.
|          *
|          * Possible options:
|          *
|          *	once:			will ensure the callback list can only be fired once (like a Deferred)
|          *
|          *	memory:			will keep track of previous values and will call any callback added
|          *					after the list has been fired right away with the latest "memorized"
|          *					values (like a Deferred)
|          *
|          *	unique:			will ensure a callback can only be added once (no duplicate in the list)
|          *
|          *	stopOnFalse:	interrupt callings when a callback returns false
|          *
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2405
|     Comment: 
|          // handle meridiem
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2703
|     Comment: 
|          // 1000 * 60
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2334
|     Comment: 
|         
|         // constant that refers to the ISO standard
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3059
|     Comment: 
|         
|         // Give the init function the jQuery prototype for later instantiation
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3285
|     Comment: 
|         /* ' + this._i + ' */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6787
|     Comment: 
|         
|         // Animations created synchronously will run synchronously
|     
|     Path: http://192.168.185.141:81/
|     Line number: 13
|     Comment: 
|         <!-- Theme style -->
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 242
|     Comment: 
|          // Prevent infinite loop in case updateOffset creates new moment
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4108
|     Comment: 
|          // The following code bubbles up values, see the tests for
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1148
|     Comment: 
|          // the Date.UTC function remaps years 0-99 to 1900-1999
|     
|     Path: http://192.168.185.141:81/
|     Line number: 75
|     Comment: 
|         <!-- jQuery 3 -->
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 850
|     Comment: 
|         
|         // LOCALES
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4285
|     Comment: 
|         
|         // This function allows you to set a threshold for relative time strings
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3971
|     Comment: 
|         
|         // (true, fmt, 5)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2340
|     Comment: 
|         
|         // date from string and format string
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2106
|     Comment: 
|          // Replace multiple-spaces with a single space
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3933
|     Comment: 
|         
|         // Catch cases where $(document).ready() is called
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6598
|     Comment: 
|         
|         // These hooks are used by animate to expand properties
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 958
|     Comment: 
|          // No op
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 693
|     Comment: 
|          //       0 - 99
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2700
|     Comment: 
|          // representation for dateAddRemove
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3841
|     Comment: 
|         
|         // Week
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4185
|     Comment: 
|         
|         //	Implementation Summary
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1839
|     Comment: 
|         
|         // This function will load locale and then set the global locale.  If
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 729
|     Comment: 
|         
|         // Code from http://stackoverflow.com/questions/3561493/is-there-a-regexp-escape-function-in-javascript
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1741
|     Comment: 
|          // Using charAt should be more compatible.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3271
|     Comment: 
|          // native implementation is ~50x faster, use it when we can
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3226
|     Comment: 
|          // 1000 * 60 * 60
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2303
|     Comment: 
|          // Default to current week.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8671
|     Comment: 
|         /* Chain conversions given the request and the original response
|          * Also sets the responseXXX fields on the jqXHR instance
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2157
|     Comment: 
|         
|         // Add button/input type pseudos
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 842
|     Comment: 
|          // if we didn't find a month name, mark the date as invalid.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4100
|     Comment: 
|          // check: https://github.com/moment/moment/issues/2166
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3339
|     Comment: 
|         
|         // variables for this instance.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5633
|     Comment: 
|         
|         // Prefer a tbody over its parent table for containing new rows
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3837
|     Comment: 
|         
|         // Month
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3860
|     Comment: 
|         
|         // Second
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4140
|     Comment: 
|          // 400 years have 146097 days (taking into account leap year rules)
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8308
|     Comment: 
|         
|         // Related ticket - https://bugzilla.mozilla.org/show_bug.cgi?id=687787
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9754
|     Comment: 
|         
|         // Support: Safari 8 only
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1135
|     Comment: 
|          // https://stackoverflow.com/q/181348
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1825
|     Comment: 
|          // TODO: Find a better way to register and load all the locales in Node
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2819
|     Comment: 
|         
|         // from the actual represented time. That is why we call updateOffset
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 275
|     Comment: 
|         
|         // compare two arrays, return the number of differences
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 688
|     Comment: 
|          //       0 - 9
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 235
|     Comment: 
|         
|         // Moment prototype object
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1896
|     Comment: 
|          // created, so we won't end up with the child locale set.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8306
|     Comment: 
|         
|         // Support: Firefox <=44
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 516
|     Comment: 
|         
|         // Populate the class2type map
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 708
|     Comment: 
|         
|         // any word (or two) characters or numbers including two/three word month in arabic.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1252
|     Comment: 
|          // Sunday is the first day of the week.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1091
|     Comment: 
|         /**
|          * Detects XML nodes
|          * @param {Element|Object} elem An element or a document
|          * @returns {Boolean} True iff elem is a non-HTML XML node
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2617
|     Comment: 
|         
|         //
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7709
|     Comment: 
|         /* eslint no-unused-expressions: "off" */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3935
|     Comment: 
|         
|         // Hours
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2115
|     Comment: 
|          // TODO: Replace the vanilla JS Date object with an indepentent day-of-week check.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2203
|     Comment: 
|          // hooks is actually the exported moment object
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4191
|     Comment: 
|         
|         //	4. _Never_ expose "private" data to user code (TODO: Drop _data, _removeData)
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8106
|     Comment: 
|         
|         // Return jQuery for attributes-only inclusion
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2243
|     Comment: 
|          // * if no year, month, day of month are given, default to today
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 38
|     Comment: 
|          // even if its not own property I'd still call it non-empty
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2790
|     Comment: 
|          // Use low-level api, because this fn is low-level api.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 967
|     Comment: 
|          // TODO: Another silent failure?
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 929
|     Comment: 
|          // see sorting in computeMonthsParse
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2191
|     Comment: 
|         
|         // Pick the first defined of two or three arguments.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10242
|     Comment: 
|         
|         // Expose jQuery and $ identifiers, even in AMD
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 701
|     Comment: 
|          //    -inf - inf
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4324
|     Comment: 
|          // and also not between days and months (28-31 days per month)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3029
|     Comment: 
|          // converts floats to ints.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3235
|     Comment: 
|          // difference in months
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4356
|     Comment: 
|          // but not other JS (goog.date)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3126
|     Comment: 
|          // We want to compare the start of today, vs this.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2466
|     Comment: 
|          // if there is any input that was not parsed add a penalty for that format
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3030
|     Comment: 
|          // inp may be undefined, so careful calling replace on it.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2030
|     Comment: 
|         
|         // date from iso format
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1057
|     Comment: 
|         /**
|          * Returns a function to use in pseudos for positionals
|          * @param {Function} fn
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2337
|     Comment: 
|         
|         // constant that refers to the RFC 2822 form
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.slim.js
|     Line number: 1
|     Comment: 
|         /*!
|          * jQuery JavaScript Library v3.2.1 -ajax,-ajax/jsonp,-ajax/load,-ajax/parseXML,-ajax/script,-ajax/var/location,-ajax/var/nonce,-ajax/var/rquery,-ajax/xhr,-manipulation/_evalUrl,-event/ajax,-effects,-effects/Tween,-effects/animatedSelector
|          * https://jquery.com/
|          *
|          * Includes Sizzle.js
|          * https://sizzlejs.com/
|          *
|          * Copyright JS Foundation and other contributors
|          * Released under the MIT license
|          * https://jquery.org/license
|          *
|          * Date: 2017-03-20T19:00Z
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2747
|     Comment: 
|         
|         // https://msdn.microsoft.com/en-us/library/ms536429%28VS.85%29.aspx
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1048
|     Comment: 
|          // Sorting makes sure if one month (or abbr) is a prefix of another it
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 825
|     Comment: 
|         
|         // PARSING
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1155
|     Comment: 
|         
|         // start-of-first-week - start-of-year
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3854
|     Comment: 
|         
|         // Hour
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3371
|     Comment: 
|          // the following switch intentionally omits break keywords
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 700
|     Comment: 
|          //       0 - inf
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4189
|     Comment: 
|         
|         //		paths to a single mechanism.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4323
|     Comment: 
|          // (think of clock changes)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2266
|     Comment: 
|          // Apply timezone offset from input. The actual utcOffset can be changed
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1993
|     Comment: 
|         
|         // iso 8601 regex
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1796
|     Comment: 
|         
|         // pick the locale from the array
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2342
|     Comment: 
|          // TODO: Move this to another part of the creation flow to prevent circular deps
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2211
|     Comment: 
|         
|         // convert an array to a date.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1894
|     Comment: 
|          // backwards compat for now: also set the locale
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3282
|     Comment: 
|          // Flag to know if list is currently firing
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1765
|     Comment: 
|         
|         // weekdays
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4041
|     Comment: 
|         
|         // Side effect imports
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 182
|     Comment: 
|         
|         // Plugins that add properties should also add the key here (null value),
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1608
|     Comment: 
|          // Sorting makes sure if one weekday (or abbr) is a prefix of another it
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1138
|     Comment: 
|          // the date constructor remaps years 0-99 to 1900-1999
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 30
|     Comment: 
|          // IE8 will treat undefined and null as object if it wasn't for
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3876
|     Comment: 
|         
|         // The deferred used on DOM ready
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2224
|     Comment: 
|          //compute day of the year from weeks and weekdays
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2009
|     Comment: 
|          // YYYYMM is NOT allowed by the standard
|     
|     Path: http://192.168.185.141:81/
|     Line number: 17
|     Comment: 
|         
|         
|         
|           	<![endif]-->
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2256
|     Comment: 
|          // Check for 24:00:00.000
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3127
|     Comment: 
|          // Getting start-of-today depends on whether we're local/utc/offset or not.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1381
|     Comment: 
|         /* Contains
|         	---------------------------------------------------------------------- */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2960
|     Comment: 
|         
|         // and further modified to allow for strings containing both week and day
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4109
|     Comment: 
|          // examples of what that means.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 91
|     Comment: 
|          // We need to deep clone this object.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8312
|     Comment: 
|         
|         // which is spec violation - http://www.w3.org/TR/DOM-Level-3-Events/#events-focusevent-event-order
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9672
|     Comment: 
|         
|         // Detect, normalize options and install callbacks for jsonp requests
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2288
|     Comment: 
|          // create now).
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8788
|     Comment: 
|         /*
|         		timeout: 0,
|         		data: null,
|         		dataType: null,
|         		username: null,
|         		password: null,
|         		cache: null,
|         		throws: false,
|         		traditional: false,
|         		headers: {},
|         		*/
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2704
|     Comment: 
|          //using 1000 * 60 * 60 instead of 36e5 to avoid floating point rounding errors https://github.com/moment/moment/issues/2978
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3614
|     Comment: 
|         
|         // PRIOROITY
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5535
|     Comment: 
|         
|         // Support: Safari 7 only
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9612
|     Comment: 
|         
|         // Handle cache's special case and crossDomain
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9595
|     Comment: 
|         
|         // Install script dataType
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2105
|     Comment: 
|          // Remove comments and folding whitespace
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 44
|     Comment: 
|         
|         // arguments.callee.caller (trac-13335). But as of jQuery 3.0 (2016), strict mode should be common
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2438
|     Comment: 
|         
|         // date from string and array of format strings
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2365
|     Comment: 
|          // console.log('token', token, 'parsedInput', parsedInput,
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8595
|     Comment: 
|         
|         // Fixes #9887
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1263
|     Comment: 
|         /* QSA/matchesSelector
|         	---------------------------------------------------------------------- */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8566
|     Comment: 
|         
|         // Base inspection function for prefilters and transports
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8532
|     Comment: 
|         
|         // Base "constructor" for jQuery.ajaxPrefilter and jQuery.ajaxTransport
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8355
|     Comment: 
|         
|         // Cross-browser xml parsing
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2709
|     Comment: 
|          // It is impossible translate months into days without knowing
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3969
|     Comment: 
|         
|         // (true)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 608
|     Comment: 
|         
|         // ordinal:  'Mo'
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3955
|     Comment: 
|         
|         // Multifunctional method to get and set values of a collection
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4079
|     Comment: 
|         
|         // supports only 2.0-style subtract(1, 's') or subtract(duration)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 876
|     Comment: 
|          // this is not used
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1853
|     Comment: 
|          // moment.duration._locale = moment._locale = data;
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7379
|     Comment: 
|         
|         // Generate shortcuts for custom animations
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6795
|     Comment: 
|         
|         // Generate parameters to create a standard animation
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6764
|     Comment: 
|         
|         // Back compat <1.8 extension point
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9817
|     Comment: 
|         /**
|          * Load a url into a page
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3851
|     Comment: 
|         
|         // These usually indicate a programmer mistake during development,
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9662
|     Comment: 
|         
|         // Default jsonp settings
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1948
|     Comment: 
|          //short-circuit everything else
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4718
|     Comment: 
|         
|         // Support: IE <=9 only
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5616
|     Comment: 
|         /* eslint-disable max-len */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8518
|     Comment: 
|         /* Transports bindings
|         	 * 1) key is the dataType
|         	 * 2) the catchall symbol "*" can be used
|         	 * 3) selection will start with transport dataType and THEN go to "*" if needed
|         	 */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8507
|     Comment: 
|         /* Prefilters
|         	 * 1) They are useful to introduce custom dataTypes (see ajax/jsonp.js for an example)
|         	 * 2) These are called:
|         	 *    - BEFORE asking for a transport
|         	 *    - AFTER param serialization (s.data is a string if s.processData is true)
|         	 * 3) key is the dataType
|         	 * 4) the catchall symbol "*" can be used
|         	 * 5) execution will start with transport dataType and THEN continue down to "*" if needed
|         	 */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4236
|     Comment: 
|          // hours to day
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1323
|     Comment: 
|          // if we didn't get a weekday name, mark the date as invalid
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 703
|     Comment: 
|          // +00:00 -00:00 +0000 -0000 or Z
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 359
|     Comment: 
|          // TODO: Remove "ordinalParse" fallback in next major release.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 786
|     Comment: 
|          // I know
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6976
|     Comment: 
|         /* eslint-enable no-loop-func */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4345
|     Comment: 
|          // inspired by https://github.com/dordille/moment-isoduration/blob/master/moment.isoduration.js
|     
|     Path: http://192.168.185.141:81/
|     Line number: 16
|     Comment: 
|         <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 696
|     Comment: 
|          //       0 - 999
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10208
|     Comment: 
|         
|         // Note that for maximum portability, libraries that are not jQuery should
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4193
|     Comment: 
|         
|         //	6. Provide a clear path for implementation upgrade to WeakMap in 2014
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 907
|     Comment: 
|         /**
|          * Mark a function for special use by Sizzle
|          * @param {Function} fn The function to mark
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1
|     Comment: 
|         /*!
|          * jQuery JavaScript Library v3.2.1
|          * https://jquery.com/
|          *
|          * Includes Sizzle.js
|          * https://sizzlejs.com/
|          *
|          * Copyright JS Foundation and other contributors
|          * Released under the MIT license
|          * https://jquery.org/license
|          *
|          * Date: 2017-03-20T18:59Z
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10244
|     Comment: 
|         
|         // and CommonJS for browser emulators (#13566)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2
|     Comment: 
|         
|         //! version : 2.18.1
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10210
|     Comment: 
|         
|         // AMD loader is present. jQuery is a special case. For more information, see
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 314
|     Comment: 
|          // Remove trailing comma and space
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10206
|     Comment: 
|         
|         // to call noConflict to hide this version of jQuery, it will work.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 692
|     Comment: 
|          // -999999 - 999999
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10204
|     Comment: 
|         
|         // derived from file names, and jQuery is normally delivered in a lowercase
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10200
|     Comment: 
|         
|         // Register as a named AMD module, since jQuery can be concatenated with other
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10202
|     Comment: 
|         
|         // understands anonymous AMD modules. A named AMD is safest and most robust
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10100
|     Comment: 
|         
|         // getComputedStyle returns percent when specified for top/left/bottom/right;
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2313
|     Comment: 
|          // local weekday -- counting starts from begining of week
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1895
|     Comment: 
|          // make sure we set the locale AFTER all child locales have been
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 323
|     Comment: 
|         /* eslint-disable no-unused-vars */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10118
|     Comment: 
|         
|         // Create innerHeight, innerWidth, height, width, outerHeight and outerWidth methods
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3032
|     Comment: 
|          // apply sign while we're at it
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7699
|     Comment: 
|         
|         // forces the browser to respect setting selected
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10064
|     Comment: 
|         
|         // Create scrollLeft and scrollTop methods
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2054
|     Comment: 
|          // match[2] should be 'T' or space
|     
|     Path: http://192.168.185.141:81/
|     Line number: 15
|     Comment: 
|         <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9768
|     Comment: 
|         
|         // defaults to document
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3372
|     Comment: 
|          // to utilize falling through the cases.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2128
|     Comment: 
|          // military
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3878
|     Comment: 
|         
|         // Timezone
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 84
|     Comment: 
|         /* global Symbol */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9758
|     Comment: 
|         
|         // https://bugs.webkit.org/show_bug.cgi?id=137337
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9756
|     Comment: 
|         
|         // collapse sibling forms: the second one becomes a child of the first one.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8421
|     Comment: 
|         
|         // Serialize an array of form elements or a set of
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9883
|     Comment: 
|         
|         // Attach a bunch of functions for handling common AJAX events
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 887
|     Comment: 
|         /**
|          * Create key-value caches of limited size
|          * @returns {function(string, object)} Returns the Object data after storing it on itself with
|          *	property name the (space-suffixed) string and (if the cache is larger than Expr.cacheLength)
|          *	deleting the oldest entry
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8310
|     Comment: 
|         
|         // Support: Chrome <=48 - 49, Safari <=9.0 - 9.1
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 19
|     Comment: 
|         
|         // This is done to register the method called with moment()
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2423
|     Comment: 
|          // Fallback
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8087
|     Comment: 
|         
|         // Radios and checkboxes getter/setter
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7703
|     Comment: 
|         
|         // eslint rule "no-unused-expressions" is disabled for this code
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 817
|     Comment: 
|         
|         // ALIASES
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2140
|     Comment: 
|          // UT or +/-9999
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4123
|     Comment: 
|          // convert days to months
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4180
|     Comment: 
|         
|         // TODO: Use this.as('ms')?
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10096
|     Comment: 
|         
|         // Support: Safari <=7 - 9.1, Chrome <=37 - 49
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4128
|     Comment: 
|          // 12 months -> 1 year
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 691
|     Comment: 
|          //    0000 - 9999
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7577
|     Comment: 
|         
|         // Hooks for boolean attributes
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7444
|     Comment: 
|         
|         // Based off of the plugin by Clint Helfers, with permission.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6275
|     Comment: 
|         
|         // Return a property mapped along what jQuery.cssProps suggests or to
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2667
|     Comment: 
|          // only allow non-integers for smallest unit
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3863
|     Comment: 
|         
|         // Millisecond
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6255
|     Comment: 
|         
|         // Return a css property mapped to a potentially vendor prefixed property
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2083
|     Comment: 
|         
|         // RFC 2822 regex: For details see https://tools.ietf.org/html/rfc2822#section-3.3
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5695
|     Comment: 
|         
|         // Fix IE bugs, see support tests
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2617
|     Comment: 
|         /* Internal Use Only */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2375
|     Comment: 
|          // don't parse if it's not a known token
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3337
|     Comment: 
|         
|         // If passed a locale key, it will set the locale for this
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2705
|     Comment: 
|          // Because of dateAddRemove treats 24 hours as different from a
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1911
|     Comment: 
|          // MERGE
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5537
|     Comment: 
|         
|         // https://bugs.chromium.org/p/chromium/issues/detail?id=470258
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 563
|     Comment: 
|         
|         // MOMENTS
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9622
|     Comment: 
|         
|         // Bind script tag hack transport
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1159
|     Comment: 
|          // first-week day local weekday -- which local weekday is fwd
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.slim.min.js
|     Line number: 1
|     Comment: 
|         /*! jQuery v3.2.1 -ajax,-ajax/jsonp,-ajax/load,-ajax/parseXML,-ajax/script,-ajax/var/location,-ajax/var/nonce,-ajax/var/rquery,-ajax/xhr,-manipulation/_evalUrl,-event/ajax,-effects,-effects/Tween,-effects/animatedSelector | (c) JS Foundation and other contributors | jquery.org/license */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1517
|     Comment: 
|          // as a setter, sunday should belong to the previous week.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 357
|     Comment: 
|          // Lenient ordinal parsing accepts just a number in addition to
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2086
|     Comment: 
|         
|         // date and time from ref 2822 format
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 659
|     Comment: 
|         
|         // format date using native date object
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 606
|     Comment: 
|         
|         // token:    'M'
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3028
|     Comment: 
|          // We'd normally use ~~inp for this, but unfortunately it also
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2390
|     Comment: 
|          // add remaining unparsed input length to the string
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4322
|     Comment: 
|          // This is because there is no context-free conversion between hours and days
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 821
|     Comment: 
|         
|         // PRIORITY
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5531
|     Comment: 
|         
|         // Create mouseenter/leave events using mouseover/out and event-time checks
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 39
|     Comment: 
|         
|         // Pass this if window is not defined yet
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 951
|     Comment: 
|         /**
|          * Checks document order of two siblings
|          * @param {Element} a
|          * @param {Element} b
|          * @returns {Number} Returns less than 0 if a precedes b, greater than 0 if a follows b
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3866
|     Comment: 
|         
|         // Offset
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2765
|     Comment: 
|         
|         // '-1530'  > ['-15', '30']
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3967
|     Comment: 
|         
|         // (fmt, 5)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1902
|     Comment: 
|          // useful for testing
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3857
|     Comment: 
|         
|         // Minute
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5470
|     Comment: 
|         
|         // Includes all common event props including KeyEvent and MouseEvent specific props
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5430
|     Comment: 
|         
|         // jQuery.Event is based on DOM3 Events as specified by the ECMAScript Language Binding
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1134
|     Comment: 
|          // can't just apply() to create a date:
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2575
|     Comment: 
|          // object construction must be done this way.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4749
|     Comment: 
|         
|         // Mark scripts as having already been evaluated
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4701
|     Comment: 
|         
|         // We have to close these tags to support XHTML (#13200)
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4187
|     Comment: 
|         
|         //	1. Enforce API surface and semantic compatibility with 1.9.x branch
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2285
|     Comment: 
|          // TODO: We need to take the current isoWeekYear, but that depends on
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5621
|     Comment: 
|         /* eslint-enable */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3935
|     Comment: 
|         
|         // Support: IE <=9 - 10 only
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3926
|     Comment: 
|         
|         // The ready event handler and self cleanup method
|     
|     Path: http://192.168.185.141:81/
|     Line number: 11
|     Comment: 
|         <!-- Font Awesome -->
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1763
|     Comment: 
|         
|         // months
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3925
|     Comment: 
|         
|         // Day of Week
|     
|     Path: http://192.168.185.141:81/bower_components/font-awesome/css/font-awesome.min.css
|     Line number: 1
|     Comment: 
|         /*!
|          *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
|          *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3204
|     Comment: 
|          // don't support it.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3277
|     Comment: 
|         /**
|          * Return a human readable representation of a moment that can
|          * also be evaluated to get a new moment which is the same
|          *
|          * @link https://nodejs.org/dist/latest/docs/api/util.html#util_custom_inspect_function_on_objects
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3068
|     Comment: 
|         
|         // TODO: remove 'name' arg after deprecation is removed
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2706
|     Comment: 
|          // day when working around DST, we need to store them separately
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2745
|     Comment: 
|         
|         // Support: IE<8
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3203
|     Comment: 
|          // Treat the template element as a regular one in browsers that
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3202
|     Comment: 
|          // Support: IE 9 - 11 only, iOS 7 only, Android Browser <=4.3 only
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3062
|     Comment: 
|         
|         // Initialize central reference
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2711
|     Comment: 
|          // it separately.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2801
|     Comment: 
|          // https://github.com/moment/moment/pull/1871
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4074
|     Comment: 
|         
|         // supports only 2.0-style add(1, 's') or add(duration)
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2948
|     Comment: 
|         
|         // Initialize a jQuery object
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2853
|     Comment: 
|         
|         // Implement the identical functionality for filter and not
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4273
|     Comment: 
|         
|         // This function allows you to set the rounding function for relative time strings
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2710
|     Comment: 
|          // which months you are are talking about, so we have to store
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2738
|     Comment: 
|         
|         // Support: Webkit<537.32 - Safari 6.0.3/Chrome 25 (fixed in Chrome 27)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2319
|     Comment: 
|          // default to begining of week
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2637
|     Comment: 
|         
|         // TODO: Use [].sort instead?
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2731
|     Comment: 
|         
|         // Support: Chrome 14-35+
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 927
|     Comment: 
|          // TODO: add sorting
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3965
|     Comment: 
|         
|         // ()
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2245
|     Comment: 
|          // * if month is given, default only year
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 4966
|     Comment: 
|         /*
|          * Helper functions for managing events -- not part of the public interface.
|          * Props to Dean Edwards' addEvent library for many of the ideas.
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1831
|     Comment: 
|          // because defineLocale currently also sets the global locale, we
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3397
|     Comment: 
|          // weeks are a special case
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2735
|     Comment: 
|         
|         // Initialize against the default document
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2165
|     Comment: 
|         
|         // Easy API for creating new setFilters
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1088
|     Comment: 
|         
|         // Expose support vars for convenience
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 725
|     Comment: 
|         
|         // Optimize for push.apply( _, NodeList )
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2287
|     Comment: 
|          // a now version of current config (take local/utc/offset flags, and
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 690
|     Comment: 
|          //     000 - 999
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3847
|     Comment: 
|         
|         // Day
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1841
|     Comment: 
|         
|         // locale key.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8074
|     Comment: 
|         /* eslint-enable no-cond-assign */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8066
|     Comment: 
|         /* eslint-disable no-cond-assign */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 931
|     Comment: 
|          // make the regex if we don't have it already
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2813
|     Comment: 
|         
|         // keepLocalTime = true means only change the timezone, without
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2246
|     Comment: 
|          // * if year is given, don't default anything
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2728
|     Comment: 
|         
|         // Sort stability
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3537
|     Comment: 
|         /* fnDone, fnFail, fnProgress */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2647
|     Comment: 
|         /**
|          * A low-level selection function that works with Sizzle's compiled
|          *  selector functions
|          * @param {String|Function} selector A selector or a pre-compiled
|          *  selector function built with Sizzle.compile
|          * @param {Element} context
|          * @param {Array} [results]
|          * @param {Array} [seed] A set of elements to match against
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5644
|     Comment: 
|         
|         // Replace/restore the type attribute of script elements for safe DOM manipulation
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1686
|     Comment: 
|         /* matches from matchExpr["CHILD"]
|         				1 type (only|nth|...)
|         				2 what (child|of-type)
|         				3 argument (even|odd|\d*|\d*n([+-]\d+)?|...)
|         				4 xn-component of xn+y argument ([+-]?\d*n|)
|         				5 sign of xn-component
|         				6 x of xn-component
|         				7 sign of y-component
|         				8 y of y-component
|         			*/
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 694
|     Comment: 
|          //     999 - 9999
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1616
|     Comment: 
|         /**
|          * Utility function for retrieving the text value of an array of DOM nodes
|          * @param {Array|Element} elem
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2958
|     Comment: 
|         
|         // from http://docs.closure-library.googlecode.com/git/closure_goog_date_date.js.source.html
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 979
|     Comment: 
|         /**
|          * Returns a function to use in pseudos for input types
|          * @param {String} type
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2107
|     Comment: 
|          // Remove leading and trailing spaces
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3882
|     Comment: 
|         
|         // Deprecations
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1583
|     Comment: 
|         /**
|          * Document sorting and removing duplicates
|          * @param {ArrayLike} results
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3251
|     Comment: 
|          //check for negative zero, return zero if negative zero
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4318
|     Comment: 
|          // for ISO strings we do not use the normal bubbling rules:
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1409
|     Comment: 
|         /* Sorting
|         	---------------------------------------------------------------------- */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 706
|     Comment: 
|          // 123456789 123456789.123
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8593
|     Comment: 
|         
|         // A special extend for ajax options
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.min.js
|     Line number: 1
|     Comment: 
|         /*! jQuery v3.2.1 | (c) JS Foundation and other contributors | jquery.org/license */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2726
|     Comment: 
|         
|         // One-time assignments
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2251
|     Comment: 
|          // Zero out whatever was not defaulted, including time
|     
|     Path: http://192.168.185.141:81/dist/css/AdminLTE.min.css
|     Line number: 1
|     Comment: 
|         /*!
|          *   AdminLTE v2.4.0
|          *   Author: Almsaeed Studio
|          *	 Website: Almsaeed Studio <https://adminlte.io>
|          *   License: Open source - MIT
|          *           Please visit http://opensource.org/licenses/MIT for more information
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4141
|     Comment: 
|          // 400 years have 12 months === 4800
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1038
|     Comment: 
|         /* jshint -W018 */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7697
|     Comment: 
|         
|         // Support: IE <=11 only
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 85
|     Comment: 
|         
|         // Defining this global in .eslintrc.json would create a danger of using the global
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1798
|     Comment: 
|         
|         // substring from most specific to least, but move to the next array item if it's a more specific variant than the current root
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 937
|     Comment: 
|         /**
|          * Adds the same handler for all of the specified attrs
|          * @param {String} attrs Pipe-separated list of attributes
|          * @param {Function} handler The method that will be applied
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9588
|     Comment: 
|         
|         // Prevent auto-execution of scripts when no explicit dataType was provided (See gh-2432)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1253
|     Comment: 
|          // The week that contains Jan 1st is the first week of the year.
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 539
|     Comment: 
|         /*!
|          * Sizzle CSS Selector Engine v2.3.3
|          * https://sizzlejs.com/
|          *
|          * Copyright jQuery Foundation and other contributors
|          * Released under the MIT license
|          * http://jquery.org/license
|          *
|          * Date: 2016-08-08
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 990
|     Comment: 
|         /**
|          * Returns a function to use in pseudos for buttons
|          * @param {String} type
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 9766
|     Comment: 
|         
|         // Argument "data" should be string of html
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2154
|     Comment: 
|         
|         // date from iso format or fallback
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1103
|     Comment: 
|         /**
|          * Sets document-related variables once based on the current document
|          * @param {Element|Object} [doc] An element or document object to use to set the document
|          * @returns {Object} Returns the current document
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4355
|     Comment: 
|          // this is the same as C#'s (Noda) and python (isodate)...
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 6972
|     Comment: 
|         /* eslint-disable no-loop-func */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4334
|     Comment: 
|          // 3600 seconds -> 60 minutes -> 1 hour
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1049
|     Comment: 
|          // will match the longer piece.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4321
|     Comment: 
|          //  * months bubble up until they become years
|     
|     Path: http://192.168.185.141:81/
|     Line number: 22
|     Comment: 
|         <!-- Google Font -->
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2759
|     Comment: 
|         
|         // Support: IE<9
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2763
|     Comment: 
|         
|         // timezone chunker
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2213
|     Comment: 
|         
|         // note: all values past the year are optional and will default to the lowest possible value.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3376
|     Comment: 
|         /* falls through */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1165
|     Comment: 
|         
|         // https://en.wikipedia.org/wiki/ISO_week_date#Calculating_a_date_given_the_year.2C_week_number_and_weekday
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2576
|     Comment: 
|          // https://github.com/moment/moment/issues/1423
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2615
|     Comment: 
|         
|         // Pick a moment m from moments so that m[fn](other) is true for all
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4099
|     Comment: 
|          // if we have a mix of positive and negative values, bubble down first
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2798
|     Comment: 
|         
|         // Deprecated
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1516
|     Comment: 
|          // as a getter, returns 7 instead of 0 (1-7 range instead of 0-6)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 689
|     Comment: 
|          //      00 - 99
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4238
|     Comment: 
|          // months to year
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4237
|     Comment: 
|          // days to month
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3419
|     Comment: 
|          // 'date' is an alias for 'day', so it should be considered as such.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 243
|     Comment: 
|          // objects.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4234
|     Comment: 
|          // seconds to minute
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4233
|     Comment: 
|          // a few seconds to seconds
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 7701
|     Comment: 
|         
|         // The getter ensures a default option is selected
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4173
|     Comment: 
|          // Math.floor prevents floating point math errors here
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 384
|     Comment: 
|          // make sure changes to properties don't modify parent config
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4165
|     Comment: 
|          // handle milliseconds separately because of floating point math errors (issue #1867)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4146
|     Comment: 
|          // the reverse of daysToMonths
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1079
|     Comment: 
|         /**
|          * Checks a node for validity as a Sizzle context
|          * @param {Element|Object=} context
|          * @returns {Element|Object|Boolean} The input node if acceptable, otherwise a falsy value
|          */
|     
|     Path: http://192.168.185.141:81/
|     Line number: 79
|     Comment: 
|         <!-- Moment JS -->
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 916
|     Comment: 
|         /**
|          * Support testing using an element
|          * @param {Function} fn Passed the created element and returns a boolean result
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 257
|     Comment: 
|          // -0 -> 0
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2116
|     Comment: 
|          // day of week given
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 8612
|     Comment: 
|         /* Handles responses to an ajax request:
|          * - finds the right dataType (mediates between content-type and expected dataType)
|          * - returns the corresponding response
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3228
|     Comment: 
|          // 1000 * 60 * 60 * 24 * 7, negate dst
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1832
|     Comment: 
|          // want to undo that for lazy loaded locales
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3830
|     Comment: 
|         
|         // Week Year
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1086
|     Comment: 
|         
|         // PRIORITIES
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 358
|     Comment: 
|          // number + (possibly) stuff coming from _dayOfMonthOrdinalParse.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1813
|     Comment: 
|          //the next array item is better than a shallower substring of this one
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 704
|     Comment: 
|          // +00 -00 +00:00 -00:00 +0000 -0000 or Z
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2702
|     Comment: 
|          // 1000
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2286
|     Comment: 
|          // how we interpret now (local, utc, fixed offset). So create
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4241
|     Comment: 
|         
|         // helper function for moment.fn.from, moment.fn.fromNow, and moment.duration.fn.humanize
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3237
|     Comment: 
|          // b is in (anchor - 1 month, anchor + 1 month)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4319
|     Comment: 
|          //  * milliseconds bubble up until they become hours
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1787
|     Comment: 
|         
|         // internal storage for locale config files
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2015
|     Comment: 
|         
|         // iso time formats and regexes
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 928
|     Comment: 
|          // Sorting makes sure if one month (or abbr) is a prefix of another
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 5533
|     Comment: 
|         
|         // Do the same for pointerenter/pointerleave and pointerover/pointerout
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 695
|     Comment: 
|          //   99999 - 999999
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1740
|     Comment: 
|          // IE8 Quirks Mode & IE7 Standards Mode do not allow accessing strings like arrays
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1757
|     Comment: 
|         
|         // Setting the hour should keep the time, because the user explicitly
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1759
|     Comment: 
|         
|         // a new timezone) makes sense. Adding/subtracting hours does not follow
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3227
|     Comment: 
|          // 1000 * 60 * 60 * 24, negate dst
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4
|     Comment: 
|         
|         //! license : MIT
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3826
|     Comment: 
|         
|         // Year
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1001
|     Comment: 
|         /**
|          * Returns a function to use in pseudos for :enabled/:disabled
|          * @param {Boolean} disabled true for :disabled; false for :enabled
|          */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1109
|     Comment: 
|         
|         // HELPERS
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2229
|     Comment: 
|          //if the day of the year is set, figure out what it is
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1119
|     Comment: 
|         
|         // HOOKS
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2784
|     Comment: 
|         
|         // Return a moment from input, that is local/utc/zone equivalent to model.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2242
|     Comment: 
|          // Default to current date.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2244
|     Comment: 
|          // * if day of month is given, default month and year
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2807
|     Comment: 
|         
|         // This function will be called whenever a moment is mutated.
|     
|     Path: http://192.168.185.141:81/
|     Line number: 9
|     Comment: 
|         <!-- Bootstrap 3.3.7 -->
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2366
|     Comment: 
|          //         'regex', getParseRegexForToken(token, config));
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1137
|     Comment: 
|         /* Attributes
|         	---------------------------------------------------------------------- */
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 42
|     Comment: 
|         
|         // Edge <= 12 - 13+, Firefox <=18 - 45+, IE 10 - 11, Safari 5.1 - 9+, iOS 6 - 9.1
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4320
|     Comment: 
|          //  * days do not bubble at all
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2267
|     Comment: 
|          // with parseZone.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 31
|     Comment: 
|          // input != null
|     
|     Path: http://192.168.185.141:81/
|     Line number: 7
|     Comment: 
|         <!-- Tell the browser to be responsive to screen width -->
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2354
|     Comment: 
|          // This array is used to make a Date, either with `new Date` or `Date.UTC`
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1923
|     Comment: 
|          // pass null for config to unupdate, useful for tests
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 803
|     Comment: 
|         
|         // FORMATTING
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3405
|     Comment: 
|          // quarters are also special
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 1148
|     Comment: 
|         /* getElement(s)By*
|         	---------------------------------------------------------------------- */
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2433
|     Comment: 
|          // this is not supposed to happen
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2469
|     Comment: 
|          //or tokens
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2499
|     Comment: 
|          // Adding is smart enough around DST
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3834
|     Comment: 
|         
|         // Quarter
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2619
|     Comment: 
|         
|         // first element is an array of moment objects.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2417
|     Comment: 
|          // nothing to do
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 941
|     Comment: 
|          // test the regex
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 2951
|     Comment: 
|         
|         // A central reference to the root jQuery(document)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2821
|     Comment: 
|         
|         // _changeInProgress == true case, then we have to adjust, because
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3458
|     Comment: 
|          // new Date(NaN).toJSON() === null
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2955
|     Comment: 
|         
|         // ASP.NET json date format regex
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2992
|     Comment: 
|          // the millisecond decimal point is included in the match
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2800
|     Comment: 
|          // On Firefox.24 Date#getTimezoneOffset returns a floating point.
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2137
|     Comment: 
|          // Zone
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2556
|     Comment: 
|          // from milliseconds
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2307
|     Comment: 
|          // weekday -- low day numbers are considered next week
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1157
|     Comment: 
|          // first-week day -- which january is always in the first week (4 for iso, 1 for other)
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3243
|     Comment: 
|          // linear across the month
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 3072
|     Comment: 
|          //invert the arguments, but complain about it
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 10098
|     Comment: 
|         
|         // Webkit bug: https://bugs.webkit.org/show_bug.cgi?id=29084
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 4235
|     Comment: 
|          // minutes to hour
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2815
|     Comment: 
|         
|         // 5:31:26 +0200 It is possible that 5:31:26 doesn't exist with offset
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2396
|     Comment: 
|          // clear _12h flag if hour is <= 12
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2965
|     Comment: 
|          // matching against regexp is expensive, do it on demand
|     
|     Path: http://192.168.185.141:81/bower_components/jquery/dist/jquery.js
|     Line number: 3243
|     Comment: 
|         
|         // Convert String-formatted options into Object-formatted ones
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 697
|     Comment: 
|          //       0 - 9999
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 1935
|     Comment: 
|         
|         // returns locale data
|     
|     Path: http://192.168.185.141:81/bower_components/moment/moment.js
|     Line number: 2177
|     Comment: 
|_         // Final attempt, use Input Fallback
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-sql-injection: 
|   Possible sqli for queries:
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=N%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=D%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/?C=N%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=M%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=S%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=N%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.185.141:81/bower_components/jquery/dist/?C=D%3BO%3DA%27%20OR%20sqlspider
|_    http://192.168.185.141:81/bower_components/jquery/dist/?C=N%3BO%3DA%27%20OR%20sqlspider
|_http-errors: Couldn't find any error pages.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-grep: 
|   (1) http://192.168.185.141:81/bower_components/jquery/dist/: 
|     (1) ip: 
|_      + 192.168.185.141
| http-referer-checker: 
| Spidering limited to: maxpagecount=30
|   https://oss.maxcdn.com:443/respond/1.4.2/respond.min.js
|_  https://oss.maxcdn.com:443/html5shiv/3.7.3/html5shiv.min.js
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|     /bower_components/font-awesome/css/
|       css: 1
|     /bower_components/jquery/
|       Other: 1
|     /bower_components/jquery/dist/
|       Other: 1; js: 5; map: 2
|     /bower_components/moment/
|       js: 1
|     /dist/css/
|       css: 1
|     /icons/
|       gif: 3
|   Longest directory structure:
|     Depth: 3
|     Dir: /bower_components/font-awesome/css/
|   Total files found (by extension):
|_    Other: 3; css: 2; gif: 3; js: 6; map: 2
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.php: Possible admin folder
|   /Admin/: Possible admin folder
|   /scripts/fckeditor/editor/filemanager/connectors/test.html: Digitalus CMS/FCKEditor File upload
|   /scripts/fckeditor/editor/filemanager/connectors/uploadtest.html: Digitalus CMS/FCKEditor File upload
|   /db/: BlogWorx Database
|   /db/: Potentially interesting directory w/ listing on 'apache/2.4.51 (win64) php/7.4.26'
|   /icons/: Potentially interesting folder w/ directory listing
|   /images/: Potentially interesting directory w/ listing on 'apache/2.4.51 (win64) php/7.4.26'
|   /index/: Potentially interesting folder
|_  /scripts/: Potentially interesting folder
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-fileupload-exploiter: 
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|_    Couldn't find a file-type field.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-mobileversion-checker: No mobile version detected.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:10:47 2024 -- 1 IP address (1 host up) scanned in 74.71 seconds

```
