```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:09:32 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.185.141
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.067s latency).
Scanned at 2024-08-05 22:09:35 EDT for 58s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 125 Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
| http-headers: 
|   Date: Tue, 06 Aug 2024 02:09:48 GMT
|   Server: Apache/2.4.51 (Win64) PHP/7.4.26
|   Last-Modified: Fri, 01 Apr 2022 12:37:15 GMT
|   ETag: "901a-5db9709d9433b"
|   Accept-Ranges: bytes
|   Content-Length: 36890
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-apache-negotiation: mod_negotiation enabled.
|_http-date: Tue, 06 Aug 2024 02:09:48 GMT; -2s from local time.
|_http-generator: Nicepage 4.8.2, nicepage.com
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-php-version: Logo query returned unknown hash 37e6bb29ab0ac359102ab80e86c0bdb8
|_Credits query returned unknown hash 37e6bb29ab0ac359102ab80e86c0bdb8
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; css: 2; js: 2
|     /images/
|       jpeg: 1; jpg: 3; png: 8
|   Longest directory structure:
|     Depth: 1
|     Dir: /images/
|   Total files found (by extension):
|_    Other: 1; css: 2; jpeg: 1; jpg: 3; js: 2; png: 8
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-trace: TRACE is enabled
| Headers:
| Date: Tue, 06 Aug 2024 02:09:46 GMT
| Server: Apache/2.4.51 (Win64) PHP/7.4.26
| Connection: close
| Transfer-Encoding: chunked
|_Content-Type: message/http
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-malware-host: Host appears to be clean
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.185.141
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16167
|     Comment: 
|         /*
|         	Background is added as a separate element.
|         	As animating opacity is much faster than animating rgba() background-color.
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 18224
|     Comment: 
|         /*begin-commonstyles animation*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 552
|     Comment: 
|         /* Slide effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 559
|     Comment: 
|         /* Wobble Right effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16776
|     Comment: 
|         /* pswp__ui--one-slide class is added when there is just one item in gallery */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16116
|     Comment: 
|         /* pswp = photoswipe */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 21376
|     Comment: 
|         /*end-variables font*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16765
|     Comment: 
|         /*
|         	pswp__ui--hidden class is added when controls are hidden
|         	e.g. when user taps to toggle visibility of controls
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 301
|     Comment: 
|         /**
|          * Link style.
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16641
|     Comment: 
|         /* We use .gif in browsers that don't support CSS animation */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 560
|     Comment: 
|         /* Wobble top effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 551
|     Comment: 
|         /* Over effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16419
|     Comment: 
|         /* no arrows on touch screens */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16321
|     Comment: 
|         /*begin-commonstyles photoswipe-default*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 563
|     Comment: 
|         /* Utility */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 561
|     Comment: 
|         /* Wobble bottom effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16112
|     Comment: 
|         /*! PhotoSwipe main CSS by Dmitry Semenov | photoswipe.com | MIT license */
|     
|     Path: http://192.168.185.141:80/jquery.js
|     Line number: 1
|     Comment: 
|         /*! jQuery v3.5.1 | (c) JS Foundation and other contributors | jquery.org/license */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 1870
|     Comment: 
|         /* ********  end of spacing ******** */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 562
|     Comment: 
|         /* Zoom and Rotate Effects */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16370
|     Comment: 
|         /* pswp__ui--over-close class it added when mouse is over element that should close gallery */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 1
|     Comment: 
|         /*begin-commonstyles library*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 772
|     Comment: 
|         /* Flip */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36077
|     Comment: 
|         /** common-rules **/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 364
|     Comment: 
|         /*! normalize.css v4.1.1 | MIT License | github.com/necolas/normalize.css */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16793
|     Comment: 
|         /*!
|          * animate.css -http://daneden.me/animate
|          * Version - 3.7.0
|          * Licensed under the MIT license - http://opensource.org/licenses/MIT
|          *
|          * Copyright (c) 2018 Daniel Eden
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16743
|     Comment: 
|         /* pswp--has_mouse class is added only when two subsequent mousemove events occur */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16111
|     Comment: 
|         /*begin-commonstyles photoswipe*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 21368
|     Comment: 
|         /*end-variables color*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 553
|     Comment: 
|         /* Over and Slide effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36266
|     Comment: 
|         /** color-rules **/
|     
|     Path: http://192.168.185.141:80/nicepage.js
|     Line number: 21
|     Comment: 
|         /*!
|         Waypoints - 4.0.1
|         Copyright \xC2\xA9 2011-2016 Caleb Troughton
|         Licensed under the MIT license.
|         https://github.com/imakewebthings/waypoints/blob/master/licenses.txt
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.js
|     Line number: 35
|     Comment: 
|         /*!
|          * gumshoejs v5.1.2
|          * A simple, framework-agnostic scrollspy script.
|          * (c) 2019 Chris Ferdinandi
|          * MIT License
|          * http://github.com/cferdinandi/gumshoe
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 906
|     Comment: 
|         /* Zoom */
|     
|     Path: http://192.168.185.141:80/nicepage.js
|     Line number: 28
|     Comment: 
|         /*!
|          * JavaScript Cookie v2.2.1
|          * https://github.com/js-cookie/js-cookie
|          *
|          * Copyright 2006, 2015 Klaus Hartl & Fagner Brack
|          * Released under the MIT license
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 556
|     Comment: 
|         /* Flip Top effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16792
|     Comment: 
|         /*end-commonstyles photoswipe-default*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16565
|     Comment: 
|         /*
|         
|         	3. Index indicator ("1 of X" counter)
|         
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.js
|     Line number: 13
|     Comment: 
|         /*!
|          * skrollr core
|          *
|          * Alexander Prinzhorn - https://github.com/Prinzhorn/skrollr
|          *
|          * Free to use under terms of MIT license
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 18261
|     Comment: 
|         /* Fix zoomIn animation for Internet Explorer */
|     
|     Path: http://192.168.185.141:80/nicepage.js
|     Line number: 10
|     Comment: 
|         /*! PhotoSwipe Default UI - 4.1.3 - 2019-01-08
|         * http://photoswipe.com
|         * Copyright (c) 2019 Dmitry Semenov; */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 554
|     Comment: 
|         /* Flip Left effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16773
|     Comment: 
|         /* Force paint & create composition layer for controls. */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16609
|     Comment: 
|         /* Fake caption element, used to calculate height of next/prev image */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16322
|     Comment: 
|         /*! PhotoSwipe Default UI CSS by Dmitry Semenov | photoswipe.com | MIT license */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16529
|     Comment: 
|         /* increase size of share links on touch devices */
|     
|     Path: http://192.168.185.141:80/nicepage.js
|     Line number: 2
|     Comment: 
|         /*!
|          * https://github.com/gilmoreorless/css-background-parser
|          * Copyright \xC2\xA9 2015 Gilmore Davidson under the MIT license: http://gilmoreorless.mit-license.org/
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 21353
|     Comment: 
|         /*begin-variables color*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 550
|     Comment: 
|         /* Fade effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 557
|     Comment: 
|         /* Flip Bottom effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16138
|     Comment: 
|         /* style is added when JS option showHideOpacity is set to true */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36435
|     Comment: 
|         /*end-variables base-font-size*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36232
|     Comment: 
|         /*end-media rules*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36350
|     Comment: 
|         /*end-variables sitestylecss*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36322
|     Comment: 
|         /** alt-color-rules **/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16251
|     Comment: 
|         /*
|         	div element that matches size of large image
|         	large image loads on top of it
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16517
|     Comment: 
|         /* round corners on the first/last list item */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16727
|     Comment: 
|         /* top black bar with buttons and "1 of X" indicator */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36238
|     Comment: 
|         /*begin-responsive rules*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 15389
|     Comment: 
|         /* override horizontal spacing */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36237
|     Comment: 
|         /** cms-rules **/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 293
|     Comment: 
|         /**
|          * Image style.
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 363
|     Comment: 
|         /*end-commonstyles library*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16460
|     Comment: 
|         /*
|         
|         	2. Share modal/popup and links
|         
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36433
|     Comment: 
|         /*begin-variables base-font-size*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 18372
|     Comment: 
|         /*end-commonstyles animation*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 837
|     Comment: 
|         /* Wooble */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36194
|     Comment: 
|         /** publish-rules **/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 35974
|     Comment: 
|         /*begin-variables sitestylecss*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 1018
|     Comment: 
|         /*TODO maye need another solution for negative marin*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 35972
|     Comment: 
|         /*end-variables colors*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16664
|     Comment: 
|         /*
|         			The idea of animating inner circle is based on Polymer ("material") loading indicator
|         			 by Keanu Lee https://blog.keanulee.com/2014/10/20/the-tale-of-three-spinners.html
|         		*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16323
|     Comment: 
|         /*
|         
|         	Contents:
|         
|         	1. Buttons
|         	2. Share modal and links
|         	3. Index indicator ("1 of X" counter)
|         	4. Caption
|         	5. Loading indicator
|         	6. Additional styles (root element, top bar, idle state, hidden state, etc.)
|         
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 21377
|     Comment: 
|         /*begin-variables colors*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 1016
|     Comment: 
|         /*display: inline-block;*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16613
|     Comment: 
|         /*
|         
|         	5. Loading indicator (preloader)
|         
|         	You can play with it here - http://codepen.io/dimsemenov/pen/yyBWoR
|         
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16150
|     Comment: 
|         /* autoprefixer: off */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 21369
|     Comment: 
|         /*begin-variables font*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16424
|     Comment: 
|         /*
|         	Arrow buttons hit area
|         	(icon is added to :before pseudo-element)
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 21340
|     Comment: 
|         /*begin-variables font-family*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36195
|     Comment: 
|         /*begin-media rules*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16200
|     Comment: 
|         /* Prevent selection and tap highlights */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16905
|     Comment: 
|         /* originally authored by Nick Pettit - https://github.com/nickpettit/glide */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16757
|     Comment: 
|         /* pswp__ui--idle class is added when mouse isn't moving for several seconds (JS option timeToIdle) */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 555
|     Comment: 
|         /* Flip Right effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16340
|     Comment: 
|         /* <button> css reset */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16752
|     Comment: 
|         /* pswp__ui--fit class is added when main image "fits" between top bar and bottom bar (caption) */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 36263
|     Comment: 
|         /*end-responsive rules*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16720
|     Comment: 
|         /* root element of UI */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16715
|     Comment: 
|         /*
|         
|         	6. Additional styles
|         
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 1
|     Comment: 
|         /*!
|          * froala_editor v4.0.6 (https://www.froala.com/wysiwyg-editor)
|          * License https://froala.com/wysiwyg-editor/terms/
|          * Copyright 2014-2021 Froala Labs
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 558
|     Comment: 
|         /* Wobble Left effect */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 98
|     Comment: 
|         /*  .fr-view[dir="rtl"] blockquote {
|             border-left: none;
|             border-right: solid 2px #5E35B1;
|             margin-right: 0;
|             padding-right: 5px;
|             padding-left: 0; }
|             .fr-view[dir="rtl"] blockquote blockquote {
|               border-color: #00BCD4; }
|               .fr-view[dir="rtl"] blockquote blockquote blockquote {
|                 border-color: #43A047; }
|           .fr-view blockquote {
|             border-left: solid 2px #5E35B1;
|             margin-left: 0;
|             padding-left: 5px;
|             color: #5E35B1; }
|             .fr-view blockquote blockquote {
|               border-color: #00BCD4;
|               color: #00BCD4; }
|               .fr-view blockquote blockquote blockquote {
|                 border-color: #43A047;
|                 color: #43A047; } */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16113
|     Comment: 
|         /*
|         	Styles for basic PhotoSwipe functionality (sliding area, open/close transitions)
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16383
|     Comment: 
|         /* Serve SVG sprite if browser supports SVG and resolution is more than 105dpi */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16140
|     Comment: 
|         /* 0.001, because opacity:0 doesn't trigger Paint action, which causes lag at start of transition */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16143
|     Comment: 
|         /* for open/close transition */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16335
|     Comment: 
|         /*
|         
|         	1. Buttons
|         
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16244
|     Comment: 
|         /*
|         	stretched thumbnail or div placeholder element (see below)
|         	style is added to avoid flickering in webkit/blink when layers overlap
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16581
|     Comment: 
|         /*
|         
|         	4. Caption
|         
|          */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16264
|     Comment: 
|         /*
|         	Error message appears when image is not loaded
|         	(JS option errorMsg controls markup)
|         */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16283
|     Comment: 
|         /* previews */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16319
|     Comment: 
|         /* end previews  */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16128
|     Comment: 
|         /* create separate layer, to avoid paint on window.onscroll in webkit/blink */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 16320
|     Comment: 
|         /*end-commonstyles photoswipe*/
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 1716
|     Comment: 
|         /* ********  spacing ******** */
|     
|     Path: http://192.168.185.141:80/nicepage.js
|     Line number: 7
|     Comment: 
|         /*! PhotoSwipe - v4.1.3 - 2019-01-08
|         * http://photoswipe.com
|         * Copyright (c) 2019 Dmitry Semenov; */
|     
|     Path: http://192.168.185.141:80/nicepage.css
|     Line number: 21352
|     Comment: 
|_        /*end-variables font-family*/
| http-vhosts: 
|_128 names had status 200
|_http-mobileversion-checker: No mobile version detected.
|_http-title: Home
|_http-errors: Couldn't find any error pages.
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
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
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-feed: Couldn't find any feeds.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-exif-spider: ERROR: Script execution failed (use -d to debug)
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.185.141
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://192.168.185.141:80/
|     Form id: name-2e40
|     Form action: #
|     
|     Path: http://192.168.185.141:80/
|     Form id: name-61fc
|_    Form action: #
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-fileupload-exploiter: 
|   
|     Couldn't find a file-type field.
|   
|_    Couldn't find a file-type field.
| http-enum: 
|   /blog/: Blog
|   /home.html: Possible admin folder
|   /icons/: Potentially interesting folder w/ directory listing
|   /images/: Potentially interesting directory w/ listing on 'apache/2.4.51 (win64) php/7.4.26'
|_  /script/: Potentially interesting directory w/ listing on 'apache/2.4.51 (win64) php/7.4.26'
| http-dombased-xss: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.185.141
|   Found the following indications of potential DOM based XSS: 
|     
|     Source: window.open(i.href,"pswp_share","scrollbars=yes,resizable=yes,toolbar=no,"+"location=yes,width=550,height=420,top=100,left="+(window.screen?Math.round(screen.width/2-275)
|_    Pages: http://192.168.185.141:80/nicepage.js
|_http-chrono: Request times for /; avg: 1877.68ms; min: 566.69ms; max: 4075.87ms
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:10:33 2024 -- 1 IP address (1 host up) scanned in 60.96 seconds

```
