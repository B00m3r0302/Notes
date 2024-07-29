```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.227.120
```

[/home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Jul 29 07:55:51 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Notes/Labs/medtech/192.168.227.120/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.227.120
Nmap scan report for 192.168.227.120
Host is up, received user-set (0.075s latency).
Scanned at 2024-07-29 07:55:54 EDT for 483s

PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 61 WEBrick httpd 1.6.1 (Ruby 2.7.4 (2021-07-07))
|_http-title: PAW! (PWK Awesome Website)
| http-vuln-cve2011-3192: 
|   VULNERABLE:
|   Apache byterange filter DoS
|     State: VULNERABLE
|     IDs:  CVE:CVE-2011-3192  BID:49303
|       The Apache web server is vulnerable to a denial of service attack when numerous
|       overlapping byte ranges are requested.
|     Disclosure date: 2011-08-19
|     References:
|       https://www.tenable.com/plugins/nessus/55976
|       https://seclists.org/fulldisclosure/2011/Aug/175
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-3192
|_      https://www.securityfocus.com/bid/49303
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-mobileversion-checker: No mobile version detected.
| http-security-headers: 
|   Cache_Control: 
|_    Header: Cache-Control: private, max-age=0, proxy-revalidate, no-store, no-cache, must-revalidate
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
| http-vhosts: 
| 127 names had status 200
|_ssl
|_http-php-version: Logo query returned unknown hash 0768772ee8cf8a4b9d3f0086ee2d5df2
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-malware-host: Host appears to be clean
| http-grep: 
|   (1) http://192.168.227.120:80/assets/js/: 
|     (1) ip: 
|_      + 192.168.227.120
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-backup-finder: ERROR: Script execution failed (use -d to debug)
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-headers: 
|   Etag: 65796-1229-66058b2c
|   Content-Type: text/html; charset=utf-8
|   Content-Length: 4649
|   Last-Modified: Thu, 28 Mar 2024 15:22:20 GMT
|   Cache-Control: private, max-age=0, proxy-revalidate, no-store, no-cache, must-revalidate
|   Server: WEBrick/1.6.1 (Ruby/2.7.4/2021-07-07)
|   Date: Mon, 29 Jul 2024 11:56:07 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-errors: Couldn't find any error pages.
| http-feed: 
| Spidering limited to: maxpagecount=40; withinhost=192.168.227.120
|   Found the following feeds: 
|_    Atom (version 4.2.2): http://192.168.227.120:80/feed.xml
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-date: Mon, 29 Jul 2024 11:56:01 GMT; -1s from local time.
|_http-server-header: WEBrick/1.6.1 (Ruby/2.7.4/2021-07-07)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; xml: 1
|     /assets/
|       Other: 1
|     /assets/css/
|       Other: 1; css: 1; map: 1
|     /assets/js/
|       Other: 1; js: 2
|     /assets/js/lunr/
|       Other: 1
|     /assets/js/plugins/
|       Other: 1
|     /assets/js/vendor/
|       Other: 1
|   Longest directory structure:
|     Depth: 3
|     Dir: /assets/js/vendor/
|   Total files found (by extension):
|_    Other: 7; css: 1; js: 2; map: 1; xml: 1
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
| http-sql-injection: 
|   Possible sqli for queries:
|     http://192.168.227.120:80/assets/js/?S=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?M=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?N=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?M=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?N=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?S=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?S=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?N=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?M=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/vendor/?M=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/vendor/?N=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/vendor/?S=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?S=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?N=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?M=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/lunr/?M=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/lunr/?S=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/lunr/?N=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?S=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?N=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/?M=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/?N=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/?S=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/?M=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/plugins/?N=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/plugins/?M=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/js/plugins/?S=D%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?S=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?M=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?N=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?S=A%27%20OR%20sqlspider
|     http://192.168.227.120:80/assets/css/?M=A%27%20OR%20sqlspider
|_    http://192.168.227.120:80/assets/css/?N=A%27%20OR%20sqlspider
| http-fileupload-exploiter: 
|   
|     Couldn't find a file-type field.
|   
|_    Couldn't find a file-type field.
|_http-chrono: Request times for /; avg: 415.33ms; min: 304.18ms; max: 562.04ms
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.227.120
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 69
|     Comment: 
|          // applied to the content
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 50
|     Comment: 
|          // set focus on input
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Type\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 72
|     Comment: 
|          // Set Context\n  $context-setter: private-breakpoint-set-context($default, $feature);\n\n  @if (breakpoint-get('to ems') == true) and (type-of($feature) == 'number') {\n    @return '#{$default}: #{breakpoint-to-base-em($feature)}';\n  }\n  @else {\n    @return '#{$default}: #{$feature}';\n  }\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 56
|     Comment: 
|          // Smooth scrolling
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* remove vertical scrollbar in IE6-9*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Selected elements */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 97
|     Comment: 
|         <!--[if lt IE 9]>
|         <div class="notice--danger align-center" style="margin: 0;">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade your browser</a> to improve your experience.</div>
|         <![endif]-->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* remove space above paragraphs that appear directly after notice headline*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Keyword */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Attribute */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 159
|     Comment: 
|         /* Provides an easy way to include a clearfix for containing floats. link http://cssmojo.com/latest_new_clearfix_so_far/ example scss - Usage .element { @include clearfix; } example css - CSS Output .element::after { clear: both; content: ""; display: table; } */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* type scale */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* overlay the lines by setting both their top values to 0*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 97
|     Comment: 
|         /*\n   Bourbon clearfix\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1523
|     Comment: 
|         /* Features ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 226
|     Comment: 
|         /* ========================================================================== BASE ELEMENTS ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 17
|     Comment: 
|         /* Colors ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* fills width of parent container */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* system typefaces */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1682
|     Comment: 
|         /* Hide the following elements on print ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 157
|     Comment: 
|         /* em function ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1392
|     Comment: 
|         /* Comments ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* ==========================================================================\n   Syntax highlighting\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* line numbers*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Responsive Video Embed\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* social icons*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.Number.Oct */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /*\n   Breadcrumb navigation links\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 93
|     Comment: 
|          // Allow context-only shorthand, without span\n  @if ($context-only) and (not index($shorthand, 'of')) {\n    @if su-valid-columns($shorthand, 'fail-silent') {\n      $shorthand: 'of' $shorthand;\n    } @else {\n      $shorthand: join('of', $shorthand);\n    }\n  }\n\n  // loop through the shorthand list\n  @for $i from 1 through length($shorthand) {\n    $item: nth($shorthand, $i);\n    $type: type-of($item);\n    $error: false;\n    $details: '[#{$type}] `#{$item}`';\n\n    // if we know what's supposed to be coming next\xE2\x80\xA6\n    @if $next {\n\n      // Add to the return map\n      $return: map-merge($return, ($next: $item));\n\n      // Reset next to `false`\n      $next: false;\n\n    } @else { // If we don't know what's supposed to be coming\xE2\x80\xA6\n\n      // Keywords\xE2\x80\xA6\n      @if ($type == 'string') {\n        // Check the map for keywords\xE2\x80\xA6\n        @if map-has-key($options, $item) {\n          $setting: map-get($options, $item);\n\n          // Spread could be on the span or the container\xE2\x80\xA6\n          @if ($setting == 'spread') and ($of) {\n            $return: map-merge($return, ('container-spread': $item));\n          } @else {\n            $return: map-merge($return, ($setting: $item));\n          }\n\n        } @else if ($item == 'all') {\n          // `All` is a span shortcut\n          $span: 'all';\n        } @else if ($item == 'at') {\n          // Some keywords setup what's next\xE2\x80\xA6\n          $next: 'location';\n        } @else if ($item == 'set-gutters') {\n          $next: 'gutters';\n        } @else if ($item == 'of') {\n          $of: true;\n        } @else {\n          $error: true;\n        }\n\n      } @else if ($type == 'number') or ($type == 'list') { // Numbers & lists\xE2\x80\xA6\n\n        @if not ($span or $of) {\n          // We don't have a span, and we're not expecting context\xE2\x80\xA6\n          $span: $item;\n        } @else if ($of) and (not $columns) {\n          // We are expecting context\xE2\x80\xA6\n          $columns: $item;\n        } @else {\n          $error: true;\n        }\n\n      } @else {\n        $error: true;\n      }\n    }\n\n    @if $error {\n      @return _susy-error('#{$parse-error} #{$details}', 'susy-parse');\n    }\n  }\n\n  // If we have span, merge it in\n  @if $span {\n    $return: map-merge($return, ('span': $span));\n  }\n\n  // If we have columns, merge them in\n  @if $columns {\n    $return: map-merge($return, ('columns': $columns));\n  }\n\n  // Return the map of settings\xE2\x80\xA6\n  @return $return;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Required\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* image align left */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* clearfix */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Display block in IE6-9 and FF3 */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|         /* Utility classes */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 80
|     Comment: 
|          // if true, emit custom events
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Interpol */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /**\n *  Default Kramdown usage (no indents!):\n *  <div class=\"notice\" markdown=\"1\">\n *  #### Headline for the Notice\n *  Text for the notice\n *  </div>\n */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /*\n     .form--loading\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Prevents modern browsers from displaying 'audio' without controls */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /* extend grid elements to the right */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 412
|     Comment: 
|         /* .form-group ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Heredoc */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 94
|     Comment: 
|          //   }
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 1
|     Comment: 
|         /* ==========================================================================
|            jQuery plugin settings and other scripts
|            ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1074
|     Comment: 
|         /* Visibility ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 84
|     Comment: 
|         /* The shadow behind the image */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|         /* Mixins and functions */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 95
|     Comment: 
|          // the result is a bit under 50% to account for gutters\n///     width: susy-span(6 of 12);\n///   }\n///\n/// @example scss - span a specific segment of asymmetrical grid\n///   .foo {\n///     width: susy-span(3 at 3 of (1 2 3 5 8));\n///   }\n@function susy-span(\n  $span,\n  $config: ()\n) {\n  $output: susy-compile($span, $config);\n\n  @if map-get($output, 'span') {\n    @return su-call('su-span', $output);\n  }\n\n  $actual: '[#{type-of($span)}] `#{inspect($span)}`';\n  @return _susy-error(\n    'Unable to determine span value from #{$actual}.',\n    'susy-span');\n}\n\n\n\n// Susy Gutter\n// -----------\n/// The gutter function returns\n/// the width of a single gutter on your grid,\n/// to be applied where you see fit \xE2\x80\x93\n/// on `margins`, `padding`, `transform`, or element `width`.\n///\n/// - This is a thin syntax-sugar shell around\n///   the core-math `su-gutter()` function.\n/// - The un-prefixed alias `gutter()` is available by default.\n///\n/// @group b-api\n/// @see su-gutter\n/// @see $susy\n///\n/// @param {list | number} $context [null] -\n///   Optional context for nested gutters,\n///   including shorthand for\n///   `columns`, `gutters`, and `container-spread`\n///   (additional shorthand will be ignored)\n///\n/// @param {map} $config [()] -\n///   Optional map of Susy grid configuration settings.\n///   See `$susy` documentation for details.\n///\n/// @return {length} -\n///   Width of a gutter as `%` of current context,\n///   or in the units defined by `column-width` when available\n///\n/// @example scss - add gutters before or after an element\n///   .floats {\n///     float: left;\n///     width: span(3 of 6);\n///     margin-left: gutter(of 6);\n///   }\n///\n/// @example scss - add gutters to padding\n///   .flexbox {\n///     flex: 1 1 span(3 wide of 6 wide);\n///     padding: gutter(of 6) / 2;\n///   }\n///\n@function susy-gutter(\n  $context: susy-get('columns'),\n  $config: ()\n) {\n  $context: susy-compile($context, $config, 'context-only');\n\n  @return su-call('su-gutter', $context);\n}\n\n\n\n// Susy Slice\n// ----------\n/// Working with asymmetrical grids (un-equal column widths)\n/// can be challenging \xE2\x80\x93\xC2\xA0\n/// expecially when they involve fluid/fractional elements.\n/// Describing a context `of (15em 6em 6em 6em 15em)` is a lot\n/// to put inside the span or gutter function shorthand.\n/// This slice function returns a sub-slice of asymmetrical columns to use\n/// for a nested context.\n/// `slice(3 at 2)` will give you a subset of the global grid,\n/// spanning 3 columns, starting with the second.\n///\n/// - This is a thin syntax-sugar shell around\n///   the core-math `su-slice()` function.\n/// - The un-prefixed alias `slice()` is available by default.\n///\n/// @group b-api\n/// @see su-slice\n/// @see $susy\n///\n/// @param {list} $span -\n///   Shorthand expression to define the subset span, optionally containing:\n///   - `at $n`, `first`, or `last` location on asymmetrical grids;\n///   - `of $n <spread>` for available grid columns\n///     and spread of the container\n///     - Span-counts like `of 6` are only valid\n///       in the context of symmetrical grids\n///     - Valid spreads include `narrow`, `wide`, or `wider`\n///\n/// @param {map} $config [()] -\n///   Optional map of Susy grid configuration settings.\n///   See `$susy` documentation for details.\n///\n/// @return {list} -\n///   Subset list of columns for use for a nested context\n///\n/// @example scss - Return a nested segment of asymmetrical grid\n///   $context: susy-slice(3 at 3 of (1 2 3 5 8));\n///   /* $context: #{$context}; */\n@function susy-slice(\n  $span,\n  $config: ()\n) {\n  $span: susy-compile($span, $config);\n\n  @return su-call('su-slice', $span);\n}\n\n\n\n/// ## Building Grids\n/// The web has come a long way\n/// since the days of double-margin-hacks\n/// and inconsistent subpixel rounding.\n/// In addition to floats and tables,\n/// we can now use much more powerful tools,\n/// like flexbox and CSS grid,\n/// to build more interesting and responsive layouts.\n///\n/// With Susy3, we hope you'll start moving in that direction.\n/// You can still build classic 12-column Grid Systems,\n/// and we'll help you get there,\n/// but Susy3 is primarily designed for a grid-math-on-demand\n/// approach to layout:\n/// applying our functions only where you really need grid math.\n/// Read the [intro article by OddBird][welcome] for more details.\n///\n/// [welcome]: http://oddbird.net/2017/06/28/susy3/\n///\n/// @group b-api\n/// @link http://oddbird.net/2017/06/28/susy3/ Article: Welcome to Susy3\n///\n/// @example scss - floats\n///   .float {\n///     width: span(3);\n///     margin-right: gutter();\n///   }\n///\n/// @example scss - flexbox\n///   .flexbox {\n///     flex: 1 1 span(3);\n///     // half a gutter on either side\xE2\x80\xA6\n///     padding: 0 gutter() / 2;\n///   }\n///\n/// @example scss - pushing and pulling\n///   .push-3 {\n///     margin-left: span(3 wide);\n///   }\n///\n///   .pull-3 {\n///     margin-left: 0 - span(3 wide);\n///   }\n///\n/// @example scss - building an attribute system\n///   // markup example: <div data-span=\"last 3\"></div>\n///   [data-span] {\n///     float: left;\n///\n///     &:not([data-span*='last']) {\n///       margin-right: gutter();\n///     }\n///   }\n///\n///   @for $span from 1 through length(susy-get('columns')) {\n///     [data-span*='#{$span}'] {\n///       width: span($span);\n///     }\n///   }\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* sticky footer fix */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Remove outline from links */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 457
|     Comment: 
|         /* ========================================================================== ANIMATIONS ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* inner padding and border oddities in FF3/4*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /* remove border*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1449
|     Comment: 
|         /* ========================================================================== ARCHIVE ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Symbol */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /*\n   Grid\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Remove margin */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 91
|     Comment: 
|         /* #{$key}: #{$value} */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1582
|     Comment: 
|         /* Default ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1256
|     Comment: 
|         /* Responsive Video Embed ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Variable.Global */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* buttons */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Keyword.Namespace */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* abbreviations */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 925
|     Comment: 
|         /* ========================================================================== Syntax highlighting ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* Info notice */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1224
|     Comment: 
|         /* Modals ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1239
|     Comment: 
|         /* Footnotes ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Generic.Inserted */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* reduce orphans and widows when printing */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 124
|     Comment: 
|          // Add anchors for headings
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1253
|     Comment: 
|         /* Google Custom Search Engine ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 9
|     Comment: 
|          // Sticky sidebar
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1681
|     Comment: 
|         /* ========================================================================== PRINT STYLES ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 879
|     Comment: 
|         /* ========================================================================== SEARCH ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 16
|     Comment: 
|          // fix
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1440
|     Comment: 
|         /* Wide Pages ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Generic.Heading */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1350
|     Comment: 
|         /* Page meta ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /* selected*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* override*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Escape */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1491
|     Comment: 
|         /* List view ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /* next/previous buttons */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* Danger notice */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* disabled */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 545
|     Comment: 
|         /* ========================================================================== NOTICE TEXT BLOCKS ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Variable.Instance */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 76
|     Comment: 
|          // how far from the top of the page to activate a content area
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1193
|     Comment: 
|         /* Navicons ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /*\n   Default button\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* extra large button */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1122
|     Comment: 
|         /* Images ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 13
|     Comment: 
|          // width should match $large Sass variable
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Prevent sub and sup affecting line-height in all browsers */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 61
|     Comment: 
|          // skin\n@import \"minimal-mistakes\"; // main partials",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* screen readers */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /* Place inside an archive layout */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 158
|     Comment: 
|         /* Bourbon clearfix ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 546
|     Comment: 
|         /** Default Kramdown usage (no indents!): <div class="notice" markdown="1"> #### Headline for the Notice Text for the notice </div> */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* notices */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Generic.Strong */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 46
|     Comment: 
|          // Search toggle
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 62
|     Comment: 
|         /* ==========================================================================\n   Dark skin\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 84
|     Comment: 
|          // shadow on image or iframe\n$mfp-popup-padding-left:              8px !default; // Padding from left and from right side\n$mfp-popup-padding-left-mobile:       6px !default; // Same as above, but is applied when width of window is less than 800px\n\n$mfp-z-index-base:                    1040 !default; // Base z-index of popup\n$mfp-include-arrows:                  true !default; // include styles for nav arrows\n$mfp-controls-opacity:                0.65 !default;\n$mfp-controls-color:                  #FFF !default;\n$mfp-controls-border-color:           #3F3F3F !default;\n$mfp-inner-close-icon-color:          #333 !default;\n$mfp-controls-text-color:             #CCC !default; // Color of preloader and \"1 of X\" indicator\n$mfp-controls-text-color-hover:       #FFF !default;\n$mfp-IE7support:                      true !default; // Very basic IE7 support\n\n// Iframe-type options\n$mfp-include-iframe-type:             true !default;\n$mfp-iframe-padding-top:              40px !default;\n$mfp-iframe-background:               #000 !default;\n$mfp-iframe-max-width:                900px !default;\n$mfp-iframe-ratio:                    9/16 !default;\n\n// Image-type options\n$mfp-include-image-type:              true !default;\n$mfp-image-background:                #444 !default;\n$mfp-image-padding-top:               40px !default;\n$mfp-image-padding-bottom:            40px !default;\n$mfp-include-mobile-layout-for-image: true !default; // Removes paddings from top and bottom\n\n// Image caption options\n$mfp-caption-title-color:             #F3F3F3 !default;\n$mfp-caption-subtitle-color:          #BDBDBD !default;\n\n// A11y\n$mfp-use-visuallyhidden:              false !default; // Hide content from browsers, but make it available for screen readers\n\n\n\n////////////////////////\n// 2. General styles\n////////////////////////\n\n// Transluscent overlay\n.mfp-bg {\n  top: 0;\n  left: 0;\n  width: 100%;\n  height: 100%;\n  z-index: $mfp-z-index-base + 2;\n  overflow: hidden;\n  position: fixed;\n\n  background: $mfp-overlay-color;\n  opacity: $mfp-overlay-opacity;\n  @if $mfp-IE7support {\n    filter: unquote(\"alpha(opacity=#{$mfp-overlay-opacity*100})\");\n  }\n}\n\n// Wrapper for popup\n.mfp-wrap {\n  top: 0;\n  left: 0;\n  width: 100%;\n  height: 100%;\n  z-index: $mfp-z-index-base + 3;\n  position: fixed;\n  outline: none !important;\n  -webkit-backface-visibility: hidden; // fixes webkit bug that can cause \"false\" scrollbar\n}\n\n// Root container\n.mfp-container {\n  text-align: center;\n  position: absolute;\n  width: 100%;\n  height: 100%;\n  left: 0;\n  top: 0;\n  padding: 0 $mfp-popup-padding-left;\n  -webkit-box-sizing: border-box;\n  -moz-box-sizing: border-box;\n  box-sizing: border-box;\n}\n\n// Vertical centerer helper\n.mfp-container {\n  &:before {\n    content: '';\n    display: inline-block;\n    height: 100%;\n    vertical-align: middle;\n  }\n}\n\n// Remove vertical centering when popup has class `mfp-align-top`\n.mfp-align-top {\n  .mfp-container {\n    &:before {\n      display: none;\n    }\n  }\n}\n\n// Popup content holder\n.mfp-content {\n  position: relative;\n  display: inline-block;\n  vertical-align: middle;\n  margin: 0 auto;\n  text-align: left;\n  z-index: $mfp-z-index-base + 5;\n}\n.mfp-inline-holder,\n.mfp-ajax-holder {\n  .mfp-content {\n    width: 100%;\n    cursor: auto;\n  }\n}\n\n// Cursors\n.mfp-ajax-cur {\n  cursor: progress;\n}\n.mfp-zoom-out-cur {\n  &, .mfp-image-holder .mfp-close {\n    cursor: -moz-zoom-out;\n    cursor: -webkit-zoom-out;\n    cursor: zoom-out;\n  }\n}\n.mfp-zoom {\n  cursor: pointer;\n  cursor: -webkit-zoom-in;\n  cursor: -moz-zoom-in;\n  cursor: zoom-in;\n}\n.mfp-auto-cursor {\n  .mfp-content {\n    cursor: auto;\n  }\n}\n\n.mfp-close,\n.mfp-arrow,\n.mfp-preloader,\n.mfp-counter {\n  -webkit-user-select:none;\n  -moz-user-select: none;\n  user-select: none;\n}\n\n// Hide the image during the loading\n.mfp-loading {\n  &.mfp-figure {\n    display: none;\n  }\n}\n\n// Helper class that hides stuff\n@if $mfp-use-visuallyhidden {\n  // From HTML5 Boilerplate https://github.com/h5bp/html5-boilerplate/blob/v4.2.0/doc/css.md#visuallyhidden\n  .mfp-hide {\n    border: 0 !important;\n    clip: rect(0 0 0 0) !important;\n    height: 1px !important;\n    margin: -1px !important;\n    overflow: hidden !important;\n    padding: 0 !important;\n    position: absolute !important;\n    width: 1px !important;\n  }\n} @else {\n  .mfp-hide {\n    display: none !important;\n  }\n}\n\n\n////////////////////////\n// 3. Appearance\n////////////////////////\n\n// Preloader and text that displays error messages\n.mfp-preloader {\n  color: $mfp-controls-text-color;\n  position: absolute;\n  top: 50%;\n  width: auto;\n  text-align: center;\n  margin-top: -0.8em;\n  left: 8px;\n  right: 8px;\n  z-index: $mfp-z-index-base + 4;\n  a {\n    color: $mfp-controls-text-color;\n    &:hover {\n      color: $mfp-controls-text-color-hover;\n    }\n  }\n}\n\n// Hide preloader when content successfully loaded\n.mfp-s-ready {\n  .mfp-preloader {\n    display: none;\n  }\n}\n\n// Hide content when it was not loaded\n.mfp-s-error {\n  .mfp-content {\n    display: none;\n  }\n}\n\n// CSS-reset for buttons\nbutton {\n  &.mfp-close,\n  &.mfp-arrow {\n    overflow: visible;\n    cursor: pointer;\n    background: transparent;\n    border: 0;\n    -webkit-appearance: none;\n    display: block;\n    outline: none;\n    padding: 0;\n    z-index: $mfp-z-index-base + 6;\n    -webkit-box-shadow: none;\n    box-shadow: none;\n  }\n  &::-moz-focus-inner {\n      padding: 0;\n      border: 0\n  }\n}\n\n\n// Close icon\n.mfp-close {\n  width: 44px;\n  height: 44px;\n  line-height: 44px;\n\n  position: absolute;\n  right: 0;\n  top: 0;\n  text-decoration: none;\n  text-align: center;\n  opacity: $mfp-controls-opacity;\n  @if $mfp-IE7support {\n    filter: unquote(\"alpha(opacity=#{$mfp-controls-opacity*100})\");\n  }\n  padding: 0 0 18px 10px;\n  color: $mfp-controls-color;\n\n  font-style: normal;\n  font-size: 28px;\n  font-family: $serif;\n\n  &:hover,\n  &:focus {\n    opacity: 1;\n    @if $mfp-IE7support {\n      filter: unquote(\"alpha(opacity=#{1*100})\");\n    }\n  }\n\n  &:active {\n    top: 1px;\n  }\n}\n.mfp-close-btn-in {\n  .mfp-close {\n    color: $mfp-inner-close-icon-color;\n  }\n}\n.mfp-image-holder,\n.mfp-iframe-holder {\n  .mfp-close {\n    color: $mfp-controls-color;\n    right: -6px;\n    text-align: right;\n    padding-right: 6px;\n    width: 100%;\n  }\n}\n\n// \"1 of X\" counter\n.mfp-counter {\n  position: absolute;\n  top: 0;\n  right: 0;\n  color: $mfp-controls-text-color;\n  font-size: 12px;\n  line-height: 18px;\n}\n\n// Navigation arrows\n@if $mfp-include-arrows {\n  .mfp-arrow {\n    position: absolute;\n    opacity: $mfp-controls-opacity;\n    @if $mfp-IE7support {\n      filter: unquote(\"alpha(opacity=#{$mfp-controls-opacity*100})\");\n    }\n    margin: 0;\n    top: 50%;\n    margin-top: -55px;\n    padding: 0;\n    width: 90px;\n    height: 110px;\n    -webkit-tap-highlight-color: rgba(0,0,0,0);\n    &:active {\n      margin-top: -54px;\n    }\n    &:hover,\n    &:focus {\n      opacity: 1;\n      @if $mfp-IE7support {\n        filter: unquote(\"alpha(opacity=#{1*100})\");\n      }\n    }\n    &:before,\n    &:after,\n    .mfp-b,\n    .mfp-a {\n      content: '';\n      display: block;\n      width: 0;\n      height: 0;\n      position: absolute;\n      left: 0;\n      top: 0;\n      margin-top: 35px;\n      margin-left: 35px;\n      border: medium inset transparent;\n    }\n\n    &:after,\n    .mfp-a {\n\n      border-top-width: 13px;\n      border-bottom-width: 13px;\n      top:8px;\n    }\n\n    &:before,\n    .mfp-b {\n      border-top-width: 21px;\n      border-bottom-width: 21px;\n      opacity: 0.7;\n    }\n\n  }\n\n  .mfp-arrow-left {\n    left: 0;\n\n    &:after,\n    .mfp-a {\n      border-right: 17px solid $mfp-controls-color;\n      margin-left: 31px;\n    }\n    &:before,\n    .mfp-b {\n      margin-left: 25px;\n      border-right: 27px solid $mfp-controls-border-color;\n    }\n  }\n\n  .mfp-arrow-right {\n    right: 0;\n    &:after,\n    .mfp-a {\n      border-left: 17px solid $mfp-controls-color;\n      margin-left: 39px\n    }\n    &:before,\n    .mfp-b {\n      border-left: 27px solid $mfp-controls-border-color;\n    }\n  }\n}\n\n\n\n// Iframe content type\n@if $mfp-include-iframe-type {\n  .mfp-iframe-holder {\n    padding-top: $mfp-iframe-padding-top;\n    padding-bottom: $mfp-iframe-padding-top;\n    .mfp-content {\n      line-height: 0;\n      width: 100%;\n      max-width: $mfp-iframe-max-width;\n    }\n    .mfp-close {\n      top: -40px;\n    }\n  }\n  .mfp-iframe-scaler {\n    width: 100%;\n    height: 0;\n    overflow: hidden;\n    padding-top: $mfp-iframe-ratio * 100%;\n    iframe {\n      position: absolute;\n      display: block;\n      top: 0;\n      left: 0;\n      width: 100%;\n      height: 100%;\n      box-shadow: $mfp-shadow;\n      background: $mfp-iframe-background;\n    }\n  }\n}\n\n\n\n// Image content type\n@if $mfp-include-image-type {\n\n  /* Main image in popup */\n  img {\n    &.mfp-img {\n      width: auto;\n      max-width: 100%;\n      height: auto;\n      display: block;\n      line-height: 0;\n      -webkit-box-sizing: border-box;\n      -moz-box-sizing: border-box;\n      box-sizing: border-box;\n      padding: $mfp-image-padding-top 0 $mfp-image-padding-bottom;\n      margin: 0 auto;\n    }\n  }\n\n  /* The shadow behind the image */\n  .mfp-figure {\n    line-height: 0;\n    &:after {\n      content: '';\n      position: absolute;\n      left: 0;\n      top: $mfp-image-padding-top;\n      bottom: $mfp-image-padding-bottom;\n      display: block;\n      right: 0;\n      width: auto;\n      height: auto;\n      z-index: -1;\n      box-shadow: $mfp-shadow;\n      background: $mfp-image-background;\n    }\n    small {\n      color: $mfp-caption-subtitle-color;\n      display: block;\n      font-size: 12px;\n      line-height: 14px;\n    }\n    figure {\n      margin: 0;\n    }\n    figcaption {\n      margin-top: 0;\n      margin-bottom: 0; // reset for bottom spacing\n    }\n  }\n  .mfp-bottom-bar {\n    margin-top: -$mfp-image-padding-bottom + 4;\n    position: absolute;\n    top: 100%;\n    left: 0;\n    width: 100%;\n    cursor: auto;\n  }\n  .mfp-title {\n    text-align: left;\n    line-height: 18px;\n    color: $mfp-caption-title-color;\n    word-wrap: break-word;\n    padding-right: 36px; // leave some space for counter at right side\n  }\n\n  .mfp-image-holder {\n    .mfp-content {\n      max-width: 100%;\n    }\n  }\n\n  .mfp-gallery {\n    .mfp-image-holder {\n      .mfp-figure {\n        cursor: pointer;\n      }\n    }\n  }\n\n\n  @if $mfp-include-mobile-layout-for-image {\n    @media screen and (max-width: 800px) and (orientation:landscape), screen and (max-height: 300px) {\n      /**\n       * Remove all paddings around the image on small screen\n       */\n      .mfp-img-mobile {\n        .mfp-image-holder {\n          padding-left: 0;\n          padding-right: 0;\n        }\n        img {\n          &.mfp-img {\n            padding: 0;\n          }\n        }\n        .mfp-figure {\n          // The shadow behind the image\n          &:after {\n            top: 0;\n            bottom: 0;\n          }\n          small {\n            display: inline;\n            margin-left: 5px;\n          }\n        }\n        .mfp-bottom-bar {\n          background: rgba(0,0,0,0.6);\n          bottom: 0;\n          margin: 0;\n          top: auto;\n          padding: 3px 5px;\n          position: fixed;\n          -webkit-box-sizing: border-box;\n          -moz-box-sizing: border-box;\n          box-sizing: border-box;\n          &:empty {\n            padding: 0;\n          }\n        }\n        .mfp-counter {\n          right: 5px;\n          top: 3px;\n        }\n        .mfp-close {\n          top: 0;\n          right: 0;\n          width: 35px;\n          height: 35px;\n          line-height: 35px;\n          background: rgba(0, 0, 0, 0.6);\n          position: fixed;\n          text-align: center;\n          padding: 0;\n        }\n      }\n    }\n  }\n}\n\n\n\n// Scale navigation arrows and reduce padding from sides\n@media all and (max-width: 900px) {\n  .mfp-arrow {\n    -webkit-transform: scale(0.75);\n    transform: scale(0.75);\n  }\n  .mfp-arrow-left {\n    -webkit-transform-origin: 0;\n    transform-origin: 0;\n  }\n  .mfp-arrow-right {\n    -webkit-transform-origin: 100%;\n    transform-origin: 100%;\n  }\n  .mfp-container {\n    padding-left: $mfp-popup-padding-left-mobile;\n    padding-right: $mfp-popup-padding-left-mobile;\n  }\n}\n\n\n\n// IE7 support\n// Styles that make popup look nicier in old IE\n@if $mfp-IE7support {\n  .mfp-ie7 {\n    .mfp-img {\n      padding: 0;\n    }\n    .mfp-bottom-bar {\n      width: 600px;\n      left: 50%;\n      margin-left: -300px;\n      margin-top: 5px;\n      padding-bottom: 5px;\n    }\n    .mfp-container {\n      padding: 0;\n    }\n    .mfp-content {\n      padding-top: 44px;\n    }\n    .mfp-close {\n      top: 0;\n      right: 0;\n      padding-top: 0;\n    }\n  }\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Responsive images (ensure images don't scale beyond their parents) */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 722
|     Comment: 
|         /* Post pagination navigation links ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 73
|     Comment: 
|          // If we're forcing\n  @if not ($empty-media) or not ($first) {\n    $leader: 'and ';\n  }\n\n  $first: nth($feature, 1);\n  $second: nth($feature, 2);\n\n  // If we've got two numbers, we know we need to use the default pair because there are no media queries that has a media feature that is a number\n  @if type-of($first) == 'number' and type-of($second) == 'number' {\n    $parsed: breakpoint-parse-default-pair($first, $second);\n  }\n  // If they are both strings, we send it through the string parser\n  @else if type-of($first) == 'string' and type-of($second) == 'string' {\n    $parsed: breakpoint-parse-double-string($first, $second);\n  }\n  // If it's a string/number pair, we parse it as a normal double\n  @else {\n    $parsed: breakpoint-parse-double-default($first, $second);\n  }\n\n  @return $leader + $parsed;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* IE7-8 need help adjusting responsive images*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.Number.Integer */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 95
|     Comment: 
|          //   return true;
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|          // hide\n      }\n\n      &:hover:before {\n        -webkit-transform: scaleX(1);\n        -ms-transform: scaleX(1);\n        transform: scaleX(1); // reveal\n      }\n    }\n  }\n\n  .hidden-links {\n    position: absolute;\n    top: 100%;\n    right: 0;\n    margin-top: 15px;\n    padding: 5px;\n    border: 1px solid $border-color;\n    border-radius: $border-radius;\n    background: $background-color;\n    -webkit-box-shadow: 0 2px 4px 0 rgba(#000, 0.16),\n      0 2px 10px 0 rgba(#000, 0.12);\n    box-shadow: 0 2px 4px 0 rgba(#000, 0.16), 0 2px 10px 0 rgba(#000, 0.12);\n\n    &.hidden {\n      display: none;\n    }\n\n    a {\n      margin: 0;\n      padding: 10px 20px;\n      font-size: $type-size-5;\n\n      &:hover {\n        color: $masthead-link-color-hover;\n        background: $navicon-link-color-hover;\n      }\n    }\n\n    &:before {\n      content: \"\";\n      position: absolute;\n      top: -11px;\n      right: 10px;\n      width: 0;\n      border-style: solid;\n      border-width: 0 10px 10px;\n      border-color: $border-color transparent;\n      display: block;\n      z-index: 0;\n    }\n\n    &:after {\n      content: \"\";\n      position: absolute;\n      top: -10px;\n      right: 10px;\n      width: 0;\n      border-style: solid;\n      border-width: 0 10px 10px;\n      border-color: $background-color transparent;\n      display: block;\n      z-index: 1;\n    }\n\n    li {\n      display: block;\n      border-bottom: 1px solid $border-color;\n\n      &:last-child {\n        border-bottom: none;\n      }\n    }\n  }\n}\n\n.no-js {\n  .greedy-nav {\n    .visible-links {\n      -ms-flex-wrap: wrap;\n      flex-wrap: wrap;\n      overflow: visible;\n    }\n  }\n}\n\n/*\n     Navigation list\n     ========================================================================== */\n\n.nav__list {\n  margin-bottom: 1.5em;\n\n  input[type=\"checkbox\"],\n  label {\n    display: none;\n  }\n\n  @include breakpoint(max-width $large - 1px) {\n    label {\n      position: relative;\n      display: inline-block;\n      padding: 0.5em 2.5em 0.5em 1em;\n      color: $gray;\n      font-size: $type-size-6;\n      font-weight: bold;\n      border: 1px solid $light-gray;\n      border-radius: $border-radius;\n      z-index: 20;\n      -webkit-transition: 0.2s ease-out;\n      transition: 0.2s ease-out;\n      cursor: pointer;\n\n      &:before,\n      &:after {\n        content: \"\";\n        position: absolute;\n        right: 1em;\n        top: 1.25em;\n        width: 0.75em;\n        height: 0.125em;\n        line-height: 1;\n        background-color: $gray;\n        -webkit-transition: 0.2s ease-out;\n        transition: 0.2s ease-out;\n      }\n\n      &:after {\n        -webkit-transform: rotate(90deg);\n        -ms-transform: rotate(90deg);\n        transform: rotate(90deg);\n      }\n\n      &:hover {\n        color: #fff;\n        border-color: $gray;\n        background-color: mix(white, #000, 20%);\n\n        &:before,\n        &:after {\n          background-color: #fff;\n        }\n      }\n    }\n\n    /* selected*/\n    input:checked + label {\n      color: white;\n      background-color: mix(white, #000, 20%);\n\n      &:before,\n      &:after {\n        background-color: #fff;\n      }\n    }\n\n    /* on hover show expand*/\n    label:hover:after {\n      -webkit-transform: rotate(90deg);\n      -ms-transform: rotate(90deg);\n      transform: rotate(90deg);\n    }\n\n    input:checked + label:hover:after {\n      -webkit-transform: rotate(0);\n      -ms-transform: rotate(0);\n      transform: rotate(0);\n    }\n\n    ul {\n      margin-bottom: 1em;\n    }\n\n    a {\n      display: block;\n      padding: 0.25em 0;\n\n      @include breakpoint($large) {\n        padding-top: 0.125em;\n        padding-bottom: 0.125em;\n      }\n\n      &:hover {\n        text-decoration: underline;\n      }\n    }\n  }\n}\n\n.nav__list .nav__items {\n  margin: 0;\n  font-size: 1.25rem;\n\n  a {\n    color: inherit;\n  }\n\n  .active {\n    margin-left: -0.5em;\n    padding-left: 0.5em;\n    padding-right: 0.5em;\n    font-weight: bold;\n  }\n\n  @include breakpoint(max-width $large - 1px) {\n    position: relative;\n    max-height: 0;\n    opacity: 0%;\n    overflow: hidden;\n    z-index: 10;\n    -webkit-transition: 0.3s ease-in-out;\n    transition: 0.3s ease-in-out;\n    -webkit-transform: translate(0, 10%);\n    -ms-transform: translate(0, 10%);\n    transform: translate(0, 10%);\n  }\n}\n\n@include breakpoint(max-width $large - 1px) {\n  .nav__list input:checked ~ .nav__items {\n    -webkit-transition: 0.5s ease-in-out;\n    transition: 0.5s ease-in-out;\n    max-height: 9999px; /* exaggerate max-height to accommodate tall lists*/\n    overflow: visible;\n    opacity: 1;\n    margin-top: 1em;\n    -webkit-transform: translate(0, 0);\n    -ms-transform: translate(0, 0);\n    transform: translate(0, 0);\n  }\n}\n\n.nav__title {\n  margin: 0;\n  padding: 0.5rem 0.75rem;\n  font-family: $sans-serif-narrow;\n  font-size: $type-size-5;\n  font-weight: bold;\n}\n\n.nav__sub-title {\n  display: block;\n  margin: 0.5rem 0;\n  padding: 0.25rem 0;\n  font-family: $sans-serif-narrow;\n  font-size: $type-size-6;\n  font-weight: bold;\n  text-transform: uppercase;\n  border-bottom: 1px solid $border-color;\n}\n\n/*\n     Table of contents navigation\n     ========================================================================== */\n\n.toc {\n  font-family: $sans-serif-narrow;\n  color: $gray;\n  background-color: $background-color;\n  border: 1px solid $border-color;\n  border-radius: $border-radius;\n  -webkit-box-shadow: $box-shadow;\n  box-shadow: $box-shadow;\n\n  .nav__title {\n    color: #fff;\n    font-size: $type-size-6;\n    background: $primary-color;\n    border-top-left-radius: $border-radius;\n    border-top-right-radius: $border-radius;\n  }\n\n  // Scrollspy marks toc items as .active when they are in focus\n  .active a {\n    @include yiq-contrasted($active-color);\n  }\n}\n\n.toc__menu {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  list-style: none;\n  font-size: $type-size-6;\n\n  @include breakpoint($large) {\n    font-size: $type-size-7;\n  }\n\n  a {\n    display: block;\n    padding: 0.25rem 0.75rem;\n    color: $muted-text-color;\n    font-weight: bold;\n    line-height: 1.5;\n    border-bottom: 1px solid $border-color;\n\n    &:hover {\n      color: $text-color;\n    }\n  }\n\n  li ul > li a {\n    padding-left: 1.25rem;\n    font-weight: normal;\n  }\n\n  li ul li ul > li a {\n    padding-left: 1.75rem;\n  }\n\n  li ul li ul li ul > li a {\n    padding-left: 2.25rem;\n  }\n\n  li ul li ul li ul li ul > li a {\n    padding-left: 2.75rem;\n  }\n\n  li ul li ul li ul li ul li ul > li a {\n    padding-left: 3.25rem\n  }\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 97
|     Comment: 
|         /* ==========================================================================\n   MIXINS\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* using at-root to override .page-content h4 font size*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /*\n   Colors\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.Number.Hex */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /*\n   Breakpoints\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 84
|     Comment: 
|         <!-- end custom head snippets -->
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 72
|     Comment: 
|          // if true, add classes to parents of active link
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 79
|     Comment: 
|          // If we're forcing\n  @if not ($empty-media) or not ($first) {\n    $leader: 'and ';\n  }\n\n  @if breakpoint-get('transform resolutions') and $query-resolution {\n    $resolutions: breakpoint-make-resolutions($query-resolution);\n    $length: length($resolutions);\n    $query-holder: '';\n\n    @for $i from 1 through $length {\n      $query: '#{$query-print} #{$leader}#{nth($resolutions, $i)}';\n      @if $i == 1 {\n        $query-holder: $query;\n      }\n      @else {\n        $query-holder: '#{$query-holder}, #{$query}';\n      }\n    }\n\n    @return $query-holder;\n  }\n  @else {\n    // Return with attached resolution\n    @return $query-print;\n  }\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /*\n     Navigation list\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 97
|     Comment: 
|         /* Default*/
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 71
|     Comment: 
|          // Nested navigation
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Other */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 113
|     Comment: 
|          // @include breakpoint(max-width $large) {\n  //   /* fix z-index order of follow links */\n  //   position: relative;\n  //   z-index: 10;\n  //   -webkit-transform: translate3d(0, 0, 0);\n  //   transform: translate3d(0, 0, 0);\n  // }\n\n  @include breakpoint($large) {\n    float: left;\n    width: calc(#{$right-sidebar-width-narrow} - 1em);\n    opacity: 0.75;\n    -webkit-transition: opacity 0.2s ease-in-out;\n    transition: opacity 0.2s ease-in-out;\n\n    &:hover {\n      opacity: 1;\n    }\n\n    &.sticky {\n      overflow-y: auto;\n      /* calculate height of nav list\n         viewport height - nav height - masthead x-padding\n      */\n      max-height: calc(100vh - #{$nav-height} - 2em);\n    }\n  }\n\n  @include breakpoint($x-large) {\n    width: calc(#{$right-sidebar-width} - 1em);\n  }\n\n  > * {\n    margin-top: 1em;\n    margin-bottom: 1em;\n  }\n\n  h2,\n  h3,\n  h4,\n  h5,\n  h6 {\n    margin-bottom: 0;\n    font-family: $sans-serif-narrow;\n  }\n\n  p,\n  li {\n    font-family: $sans-serif;\n    font-size: $type-size-6;\n    line-height: 1.5;\n  }\n\n  img {\n    width: 100%;\n\n    &.emoji {\n      width: 20px;\n      height: 20px;\n    }\n  }\n}\n\n.sidebar__right {\n  margin-bottom: 1em;\n\n  @include breakpoint($large) {\n    position: absolute;\n    top: 0;\n    right: 0;\n    width: $right-sidebar-width-narrow;\n    margin-right: -1 * $right-sidebar-width-narrow;\n    padding-left: 1em;\n    z-index: 10;\n\n    &.sticky {\n      @include clearfix();\n      position: -webkit-sticky;\n      position: sticky;\n      top: 2em;\n      float: right;\n    }\n  }\n\n  @include breakpoint($x-large) {\n    width: $right-sidebar-width;\n    margin-right: -1 * $right-sidebar-width;\n  }\n}\n\n.splash .sidebar__right {\n  @include breakpoint($large) {\n    position: relative;\n    float: right;\n    margin-right: 0;\n  }\n\n  @include breakpoint($x-large) {\n    margin-right: 0;\n  }\n}\n\n/*\n   Author profile and links\n   ========================================================================== */\n\n.author__avatar {\n  display: table-cell;\n  vertical-align: top;\n  width: 36px;\n  height: 36px;\n\n  @include breakpoint($large) {\n    display: block;\n    width: auto;\n    height: auto;\n  }\n\n  img {\n    max-width: 110px;\n    border-radius: 50%;\n\n    @include breakpoint($large) {\n      padding: 5px;\n      border: 1px solid $border-color;\n    }\n  }\n}\n\n.author__content {\n  display: table-cell;\n  vertical-align: top;\n  padding-left: 15px;\n  padding-right: 25px;\n  line-height: 1;\n\n  @include breakpoint($large) {\n    display: block;\n    width: 100%;\n    padding-left: 0;\n    padding-right: 0;\n  }\n\n  a {\n    color: inherit;\n    text-decoration: none;\n  }\n}\n\n.author__name {\n  margin: 0;\n\n  @include breakpoint($large) {\n    margin-top: 10px;\n    margin-bottom: 10px;\n  }\n}\n.sidebar .author__name {\n  font-family: $sans-serif;\n  font-size: $type-size-5;\n}\n\n.author__bio {\n  margin: 0;\n\n  @include breakpoint($large) {\n    margin-top: 10px;\n    margin-bottom: 20px;\n  }\n}\n\n.author__urls-wrapper {\n  position: relative;\n  display: table-cell;\n  vertical-align: middle;\n  font-family: $sans-serif;\n  z-index: 20;\n  cursor: pointer;\n\n  li:last-child {\n    a {\n      margin-bottom: 0;\n    }\n  }\n\n  .author__urls {\n    span.label {\n      padding-left: 5px;\n    }\n  }\n\n  @include breakpoint($large) {\n    display: block;\n  }\n\n  button {\n    position: relative;\n    margin-bottom: 0;\n\n    &:before {\n      @supports (pointer-events: none) {\n        content: '';\n        position: fixed;\n        top: 0;\n        left: 0;\n        width: 100%;\n        height: 100%;\n        pointer-events: none;\n      }\n    }\n\n    &.open {\n      &:before {\n        pointer-events: auto;\n      }\n    }\n\n    @include breakpoint($large) {\n      display: none;\n    }\n  }\n}\n\n.author__urls {\n  display: none;\n  position: absolute;\n  right: 0;\n  margin-top: 15px;\n  padding: 10px;\n  list-style-type: none;\n  border: 1px solid $border-color;\n  border-radius: $border-radius;\n  background: $background-color;\n  box-shadow: 0 2px 4px 0 rgba(#000, 0.16), 0 2px 10px 0 rgba(#000, 0.12);\n  cursor: default;\n\n  &.is--visible {\n    display: block;\n  }\n\n  @include breakpoint($large) {\n    display: block;\n    position: relative;\n    margin: 0;\n    padding: 0;\n    border: 0;\n    background: transparent;\n    box-shadow: none;\n  }\n\n  &:before {\n    display: block;\n    content: \"\";\n    position: absolute;\n    top: -11px;\n    left: calc(50% - 10px);\n    width: 0;\n    border-style: solid;\n    border-width: 0 10px 10px;\n    border-color: $border-color transparent;\n    z-index: 0;\n\n    @include breakpoint($large) {\n      display: none;\n    }\n  }\n\n  &:after {\n    display: block;\n    content: \"\";\n    position: absolute;\n    top: -10px;\n    left: calc(50% - 10px);\n    width: 0;\n    border-style: solid;\n    border-width: 0 10px 10px;\n    border-color: $background-color transparent;\n    z-index: 1;\n\n    @include breakpoint($large) {\n      display: none;\n    }\n  }\n\n  ul {\n    padding: 10px;\n    list-style-type: none;\n  }\n\n  li {\n    white-space: nowrap;\n  }\n\n  a {\n    display: block;\n    margin-bottom: 5px;\n    padding-right: 5px;\n    padding-top: 2px;\n    padding-bottom: 2px;\n    color: inherit;\n    font-size: $type-size-5;\n    text-decoration: none;\n\n    &:hover {\n      text-decoration: underline;\n    }\n  }\n}\n\n/*\n   Wide Pages\n   ========================================================================== */\n\n.wide .sidebar__right {\n  margin-bottom: 1em;\n\n  @include breakpoint($large) {\n    position: initial;\n    top: initial;\n    right: initial;\n    width: initial;\n    margin-right: initial;\n    padding-left: initial;\n    z-index: initial;\n\n    &.sticky {\n      float: none;\n    }\n  }\n\n  @include breakpoint($x-large) {\n    width: initial;\n    margin-right: initial;\n  }\n}\n\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* serif typefaces */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 91
|     Comment: 
|         /* columns: #{susy-get('columns')} */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 105
|     Comment: 
|          // z-index: 20;\n}\n\n.site-subtitle {\n  display: block;\n  font-size: $type-size-8;\n}\n\n.masthead__menu {\n  float: left;\n  margin-left: 0;\n  margin-right: 0;\n  width: 100%;\n  clear: both;\n\n  .site-nav {\n    margin-left: 0;\n\n    @include breakpoint($small) {\n      float: right;\n    }\n  }\n\n  ul {\n    margin: 0;\n    padding: 0;\n    clear: both;\n    list-style-type: none;\n  }\n}\n\n.masthead__menu-item {\n  display: block;\n  list-style-type: none;\n  white-space: nowrap;\n\n  &--lg {\n    padding-right: 2em;\n    font-weight: 700;\n  }\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|          // avoid the WebKit bug in Android 4.0.* where (2) destroys native `audio` and `video` controls\ninput[type=\"reset\"],\ninput[type=\"submit\"] {\n    -webkit-appearance: button; /* corrects inability to style clickable `input` types in iOS*/\n    cursor: pointer; /* improves usability and consistency of cursor style between image-type `input` and others*/\n}\n\nlabel,\nselect,\nbutton,\ninput[type=\"button\"],\ninput[type=\"reset\"],\ninput[type=\"submit\"],\ninput[type=\"radio\"],\ninput[type=\"checkbox\"] {\n    cursor: pointer; /* improves usability and consistency of cursor style between image-type `input` and others*/\n}\n\ninput[type=\"search\"] { /* Appearance in Safari/Chrome*/\n  box-sizing: border-box;\n  -webkit-appearance: textfield;\n}\n\ninput[type=\"search\"]::-webkit-search-decoration,\ninput[type=\"search\"]::-webkit-search-cancel-button {\n  -webkit-appearance: none; /* inner-padding issues in Chrome OSX, Safari 5*/\n}\n\ntextarea {\n  overflow: auto; /* remove vertical scrollbar in IE6-9*/\n  vertical-align: top; /* readability and alignment cross-browser*/\n}",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1139
|     Comment: 
|         /* Icons ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* ==========================================================================\n   UTILITY CLASSES\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* sans serif typefaces */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Keyword.Reserved */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Comment */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 80
|     Comment: 
|         <!-- start custom head snippets -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 92
|     Comment: 
|          // Spread\n  @each $setting in ('spread', 'container-spread') {\n    $value: map-get($config, $setting);\n\n    @if $value {\n      $value: susy-normalize-spread($value);\n      $config: map-merge($config, ($setting: $value));\n    }\n  }\n\n  // Columns\n  $columns: map-get($config, 'columns');\n\n  @if $columns {\n    $columns: susy-normalize-columns($columns, $context);\n    $config: map-merge($config, ('columns': $columns));\n  }\n\n  @if not $columns {\n    $map: type-of($context) == 'map';\n    $columns: if($map, map-get($context, 'columns'), null);\n    $columns: $columns or susy-get('columns');\n  }\n\n  // Span\n  $span: map-get($config, 'span');\n\n  @if $span {\n    $span: susy-normalize-span($span, $columns);\n    $config: map-merge($config, ('span': $span));\n  }\n\n  // Location\n  $location: map-get($config, 'location');\n\n  @if $location {\n    $location: susy-normalize-location($span, $location, $columns);\n    $config: map-merge($config, ('location': $location));\n  }\n\n  @return $config;\n}\n\n\n\n// Normalize Span\n// --------------\n/// Normalize `span` shorthand for Su.\n/// Su span syntax allows an explicit length (e.g. `3em`),\n/// unitless column-span number (e.g. `3` columns),\n/// or an explicit list of columns (e.g. `(3 5 8)`).\n///\n/// Susy span syntax also allows the `all` keyword,\n/// which will be converted to a slice of the context\n/// in normalization.\n///\n/// @group x-normal\n///\n/// @param {number | list | 'all'} $span -\n///   Span value to normalize.\n/// @param {list} $columns -\n///   Normalized list of columns in the grid\n///\n/// @return {number | list} -\n///   Number or list value for `$span`\n@function susy-normalize-span(\n  $span,\n  $columns: susy-get('columns')\n) {\n  @if ($span == 'all') {\n    @return length($columns);\n  }\n\n  @return $span;\n}\n\n\n\n// Normalize Columns\n// -----------------\n/// Normalize `column` shorthand for Su.\n/// Su column syntax only allows column lists (e.g. `120px 1 1 1 120px`).\n///\n/// Susy span syntax also allows a unitless `slice` number (e.g `of 5`),\n/// which will be converted to a slice of the context\n/// in normalization.\n///\n/// @group x-normal\n///\n/// @param {list | integer} $columns -\n///   List of available columns,\n///   or unitless integer representing a slice of\n///   the available context.\n/// @param {map | null} $context [null] -\n///   Map of Susy configuration settings to use as global reference,\n///   or `null` to access global settings.\n///\n/// @return {list} -\n///   Columns list value, normalized for Su input.\n///\n/// @throws\n///   when attempting to access a slice of asymmetrical context\n@function susy-normalize-columns(\n  $columns,\n  $context: null\n) {\n  $context: $context or susy-settings();\n\n  @if type-of($columns) == 'list' {\n    @return _susy-flatten($columns);\n  }\n\n  @if (type-of($columns) == 'number') and (unitless($columns)) {\n    $span: $columns;\n    $context: map-get($context, 'columns');\n    $symmetrical: susy-repeat(length($context), nth($context, 1));\n\n    @if ($context == $symmetrical) {\n      @return susy-repeat($span, nth($context, 1));\n    } @else {\n      $actual: 'of `#{$span}`';\n      $columns: 'grid-columns `#{$context}`';\n      @return _susy-error(\n        'context-slice #{$actual} can not be determined based on #{$columns}.',\n        'susy-normalize-columns');\n    }\n  }\n\n  @return $columns;\n}\n\n\n\n// Normalize Spread\n// ----------------\n/// Normalize `spread` shorthand for Su.\n/// Su spread syntax only allows the numbers `-1`, `0`, or `1` \xE2\x80\x93\n/// representing the number of gutters covered\n/// in relation to columns spanned.\n///\n/// Susy spread syntax also allows keywords for each value \xE2\x80\x93\n/// `narrow` for `-1`, `wide` for `0`, or `wider` for `1` \xE2\x80\x93\n/// which will be converted to their respective integers\n/// in normalization.\n///\n/// @group x-normal\n///\n/// @param {0 | 1 | -1 | 'narrow' | 'wide' | 'wider'} $spread -\n///   Spread across adjacent gutters, relative to a column-count \xE2\x80\x94\n///   either `narrow` (-1), `wide` (0), or `wider` (1)\n///\n/// @return {number} -\n///   Numeric value for `$spread`\n@function susy-normalize-spread(\n  $spread\n) {\n  $normal-spread: (\n    'narrow': -1,\n    'wide': 0,\n    'wider': 1,\n  );\n\n  @return map-get($normal-spread, $spread) or $spread;\n}\n\n\n\n// Normalize Location\n// ------------------\n/// Normalize `location` shorthand for Su.\n/// Su location syntax requires the (1-indexed) number for a column.\n///\n/// Susy also allows the `first` and `last` keywords,\n/// where `first` is always `1`,\n/// and `last` is calculated based on span and column values.\n/// Both keywords are normalized into an integer index\n/// in normalization.\n///\n/// @group x-normal\n///\n/// @param {number} $span -\n///   Number of grid-columns to be spanned\n/// @param {integer | 'first' | 'last'} $location -\n///   Starting (1-indexed) column position of a span,\n///   or a named location keyword.\n/// @param {list} $columns -\n///   Already-normalized list of columns in the grid.\n///\n/// @return {integer} -\n///   Numeric value for `$location`\n@function susy-normalize-location(\n  $span,\n  $location,\n  $columns\n) {\n  $count: length($columns);\n  $normal-locations: (\n    'first': 1,\n    'alpha': 1,\n    'last': $count - $span + 1,\n    'omega': $count - $span + 1,\n  );\n\n  @return map-get($normal-locations, $location) or $location;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* Primary notice */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Generic.Prompt */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1611
|     Comment: 
|         /* Author profile and links ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Namespace */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Keyword.Constant */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Text.Whitespace */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 757
|     Comment: 
|         /* Priority plus navigation ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 97
|     Comment: 
|         /*\n   Compass YIQ Color Contrast\n   https://github.com/easy-designs/yiq-color-contrast\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 79
|     Comment: 
|          // Event support
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 102
|     Comment: 
|         /* ==========================================================================\n   ANIMATIONS\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* Figure captions */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 108
|     Comment: 
|         /* ==========================================================================\n   SEARCH\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* Success notice */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 73
|     Comment: 
|          // applied to the parent items
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Appearance in Safari/Chrome*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1091
|     Comment: 
|         /* Skip links ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 85
|     Comment: 
|          //\n////////////////////////\n\n// overlay\n$mfp-overlay-color:                   #000;                     // Color of overlay screen\n$mfp-overlay-opacity:                 0.8;                        // Opacity of overlay screen\n$mfp-shadow:                          0 0 8px rgba(0, 0, 0, 0.6); // Shadow on image or iframe\n\n// spacing\n$mfp-popup-padding-left:              8px;                        // Padding from left and from right side\n$mfp-popup-padding-left-mobile:       6px;                        // Same as above, but is applied when width of window is less than 800px\n\n$mfp-z-index-base:                    1040;                       // Base z-index of popup\n\n// controls\n$mfp-include-arrows:                  true;                       // Include styles for nav arrows\n$mfp-controls-opacity:                1;                          // Opacity of controls\n$mfp-controls-color:                  #fff;                     // Color of controls\n$mfp-controls-border-color:           #fff;                     // Border color of controls\n$mfp-inner-close-icon-color:          #fff;                     // Color of close button when inside\n$mfp-controls-text-color:             #ccc;                       // Color of preloader and \"1 of X\" indicator\n$mfp-controls-text-color-hover:       #fff;                     // Hover color of preloader and \"1 of X\" indicator\n$mfp-IE7support:                      true;                       // Very basic IE7 support\n\n// Iframe-type options\n$mfp-include-iframe-type:             true;                       // Enable Iframe-type popups\n$mfp-iframe-padding-top:              40px;                       // Iframe padding top\n$mfp-iframe-background:               #000;                       // Background color of iframes\n$mfp-iframe-max-width:                900px;                      // Maximum width of iframes\n$mfp-iframe-ratio:                    9/16;                       // Ratio of iframe (9/16 = widescreen, 3/4 = standard, etc.)\n\n// Image-type options\n$mfp-include-image-type:              true;                       // Enable Image-type popups\n$mfp-image-background:                #444 !default;\n$mfp-image-padding-top:               40px;                       // Image padding top\n$mfp-image-padding-bottom:            40px;                       // Image padding bottom\n$mfp-include-mobile-layout-for-image: true;                       // Removes paddings from top and bottom\n\n// Image caption options\n$mfp-caption-title-color:             #f3f3f3;                    // Caption title color\n$mfp-caption-subtitle-color:          #bdbdbd;                    // Caption subtitle color\n.mfp-counter { font-family: $serif; }                          // Caption font family\n\n// A11y\n$mfp-use-visuallyhidden:              false;",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Double */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Skip links\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* remove table borders widget */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* non-breaking space*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Comment.Special */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 97
|     Comment: 
|         /*\n  * Provides an easy way to include a clearfix for containing floats.\n  * link http://cssmojo.com/latest_new_clearfix_so_far/\n  *\n  * example scss - Usage\n  *\n  * .element {\n  *   @include clearfix;\n  * }\n  *\n  * example css - CSS Output\n  *\n  * .element::after {\n  *   clear: both;\n  *   content: \"\";\n  *   display: table;\n  * }\n*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /*\n     .form-group\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Builtin.Pseudo */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 82
|     Comment: 
|          // Just in case someone writes gibberish to the $breakpoints variable.\n    @warn \"Your breakpoints aren't a map! `respond-to` expects a map. Please check the value of $BREAKPOINTS variable.\";\n    @content;\n  }\n  @else if map-has-key($BREAKPOINTS, $context) {\n    @include breakpoint(map-get($BREAKPOINTS, $context), $no-query) {\n      @content;\n    }\n  }\n  @else if not map-has-key($BREAKPOINTS, $context) {\n    @warn \"`#{$context}` isn't a defined breakpoint! Please add it using `$breakpoints: add-breakpoint(`#{$context}`, $value);`\";\n    @content;\n  }\n  @else {\n    @warn \"You haven't created any breakpoints yet! Make some already! `@include add-breakpoint($name, $bkpt)`\";\n    @content;\n  }\n}\n\n//////////////////////////////\n// Add Breakpoint to Breakpoints\n// TODO: Remove function in next release\n//////////////////////////////\n@function add-breakpoint($name, $bkpt, $overwrite: false) {\n  $output: ($name: $bkpt);\n\n  @if length($breakpoints) == 0 {\n    @return $output;\n  }\n  @else {\n    @if map-has-key($breakpoints, $name) and $overwrite != true {\n      @warn \"You already have a breakpoint named `#{$name}`, please choose another breakpoint name, or pass in `$overwrite: true` to overwrite the previous breakpoint.\";\n      @return $breakpoints;\n    }\n    @else if not map-has-key($breakpoints, $name) or $overwrite == true {\n      @return map-merge($breakpoints, $output);\n    }\n  }\n}\n\n@mixin add-breakpoint($name, $bkpt, $overwrite: false) {\n  $output: ($name: $bkpt);\n\n  @if length($BREAKPOINTS) == 0 {\n    $BREAKPOINTS: $output !global;\n  }\n  @else {\n    @if map-has-key($BREAKPOINTS, $name) and $overwrite != true {\n      @warn \"You already have a breakpoint named `#{$name}`, please choose another breakpoint name, or pass in `$overwrite: true` to overwrite the previous breakpoint.\";\n      $BREAKPOINTS: $BREAKPOINTS !global;\n    }\n    @else if not map-has-key($BREAKPOINTS, $name) or $overwrite == true {\n      $BREAKPOINTS: map-merge($BREAKPOINTS, $output) !global;\n    }\n  }\n}\n\n@function get-breakpoint($name: false) {\n  @if $name == false {\n    @return $BREAKPOINTS;\n  }\n  @else {\n    @return map-get($BREAKPOINTS, $name);\n  }\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /*\n     .form-search\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 2
|     Comment: 
|         <!--
|           Minimal Mistakes Jekyll Theme 4.24.0 by Michael Rose
|           Copyright 2013-2020 Michael Rose - mademistakes.com | @mmistakes
|           Free for personal and commercial use under the MIT license
|           https://github.com/mmistakes/minimal-mistakes/blob/master/LICENSE
|         -->
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 66
|     Comment: 
|         <!-- https://t.co/dKP3o1e -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 80
|     Comment: 
|          // Find which is number\n    @if type-of(nth($resolution, 1)) == 'number' {\n      $value: nth($resolution, 1);\n    }\n    @else {\n      $value: nth($resolution, 2);\n    }\n\n    // Determine min/max/standard\n    @if index($resolution, 'min-resolution') {\n      $feature: 'min-';\n    }\n    @else if index($resolution, 'max-resolution') {\n      $feature: 'max-';\n    }\n\n    $standard: '(#{$feature}resolution: #{$value})';\n\n    // If we're not dealing with dppx,\n    @if unit($value) != 'dppx' {\n      $base: 96dpi;\n      @if unit($value) == 'dpcm' {\n        $base: 243.84dpcm;\n      }\n      // Write out feature tests\n      $webkit: '';\n      $moz: '';\n      $webkit: '(-webkit-#{$feature}device-pixel-ratio: #{$value / $base})';\n      $moz: '(#{$feature}-moz-device-pixel-ratio: #{$value / $base})';\n      // Append to output\n      $output: append($output, $standard, space);\n      $output: append($output, $webkit, space);\n      $output: append($output, $moz, space);\n    }\n    @else {\n      $webkit: '';\n      $moz: '';\n      $webkit: '(-webkit-#{$feature}device-pixel-ratio: #{$value / 1dppx})';\n      $moz: '(#{$feature}-moz-device-pixel-ratio: #{$value / 1dppx})';\n      $fallback: '(#{$feature}resolution: #{$value / 1dppx * 96dpi})';\n      // Append to output\n      $output: append($output, $standard, space);\n      $output: append($output, $webkit, space);\n      $output: append($output, $moz, space);\n      $output: append($output, $fallback, space);\n    }\n\n  }\n\n  @return $output;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 121
|     Comment: 
|          // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 78
|     Comment: 
|          // Sort into min and max\n  $min: min($first, $second);\n  $max: max($first, $second);\n\n  // Set Context\n  $context-setter: private-breakpoint-set-context(min-#{$feature}, $min);\n  $context-setter: private-breakpoint-set-context(max-#{$feature}, $max);\n\n  // Make them EMs if need be\n  @if (breakpoint-get('to ems') == true) {\n    $min: breakpoint-to-base-em($min);\n    $max: breakpoint-to-base-em($max);\n  }\n\n  @return '(min-#{$feature}: #{$min}) and (max-#{$feature}: #{$max})';\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 77
|     Comment: 
|          // If we're forcing\n  @if not ($empty-media) or not ($first) {\n    $leader: 'and ';\n  }\n\n  // separate the string features from the value numbers\n  $string: null;\n  $numbers: null;\n  @each $val in $feature {\n    @if type-of($val) == string {\n      $string: $val;\n    }\n    @else {\n      @if type-of($numbers) == 'null' {\n        $numbers: $val;\n      }\n      @else {\n        $numbers: append($numbers, $val);\n      }\n    }\n  }\n\n  $parsed: breakpoint-parse-triple-default($string, nth($numbers, 1), nth($numbers, 2));\n\n  @return $leader + $parsed;\n\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 92
|     Comment: 
|          //   if( $(window).width() < 500 ) {
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 76
|     Comment: 
|          // Set Context\n  $context-setter: private-breakpoint-set-context($feature, $value);\n\n  @if (breakpoint-get('to ems') == true) {\n    $value: breakpoint-to-base-em($value);\n  }\n\n  @return '(#{$feature}: #{$value})'\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 75
|     Comment: 
|          // Test to see which is the feature and which is the value\n  @if (breakpoint-string-value($first) == true) {\n    $feature: $first;\n    $value: $second;\n  }\n  @else if (breakpoint-string-value($second) == true) {\n    $feature: $second;\n    $value: $first;\n  }\n  @else {\n    @warn \"Neither #{$first} nor #{$second} is a valid media query name.\";\n  }\n\n  // Set Context\n  $context-setter: private-breakpoint-set-context($feature, $value);\n\n  @return '(#{$feature}: #{$value})';\n}",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 74
|     Comment: 
|          // Sort into min and max\n  $min: min($first, $second);\n  $max: max($first, $second);\n\n  // Set Context\n  $context-setter: private-breakpoint-set-context(min-#{$default}, $min);\n  $context-setter: private-breakpoint-set-context(max-#{$default}, $max);\n\n  // Make them EMs if need be\n  @if (breakpoint-get('to ems') == true) {\n    $min: breakpoint-to-base-em($min);\n    $max: breakpoint-to-base-em($max);\n  }\n\n  @return '(min-#{$default}: #{$min}) and (max-#{$default}: #{$max})';\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 71
|     Comment: 
|          // If we're forcing\n  @if not ($empty-media) or not ($first) {\n    $leader: 'and ';\n  }\n\n  // If it's a single feature that can stand alone, we let it\n  @if (breakpoint-single-string($feature)) {\n    $parsed: $feature;\n    // Set Context\n    $context-setter: private-breakpoint-set-context($feature, $feature);\n  }\n  // If it's not a stand alone feature, we pass it off to the default handler.\n  @else {\n    $parsed: breakpoint-parse-default($feature);\n  }\n\n  @return $leader + '(' + $parsed + ')';\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 70
|     Comment: 
|          // Parse features out of an individual query\n  $feature-holder: ();\n  $query-holder: ();\n  $length: length($query);\n\n  @if $length == 2 {\n    // If we've got a string/number, number/string, check to see if it's a valid string/number pair or two singles\n    @if (type-of(nth($query, 1)) == 'string' and type-of(nth($query, 2)) == 'number') or (type-of(nth($query, 1)) == 'number' and type-of(nth($query, 2)) == 'string') {\n\n      $number: '';\n      $value: '';\n\n      @if type-of(nth($query, 1)) == 'string' {\n        $number: nth($query, 2);\n        $value: nth($query, 1);\n      }\n      @else {\n        $number: nth($query, 1);\n        $value: nth($query, 2);\n      }\n\n      // If the string value can be a single value, check to see if the number passed in is a valid input for said single value. Fortunately, all current single-value options only accept unitless numbers, so this check is easy.\n      @if breakpoint-single-string($value) {\n        @if unitless($number) {\n          $feature-holder: append($value, $number, space);\n          $query-holder: append($query-holder, $feature-holder, comma);\n          @return $query-holder;\n        }\n      }\n      // If the string is a media type, split the query\n      @if breakpoint-is-media($value) {\n        $query-holder: append($query-holder, nth($query, 1));\n        $query-holder: append($query-holder, nth($query, 2));\n        @return $query-holder;\n      }\n      // If it's not a single feature, we're just going to assume it's a proper string/value pair, and roll with it.\n      @else {\n        $feature-holder: append($value, $number, space);\n        $query-holder: append($query-holder, $feature-holder, comma);\n        @return $query-holder;\n      }\n\n    }\n    // If they're both numbers, we assume it's a double and roll with that\n    @else if (type-of(nth($query, 1)) == 'number' and type-of(nth($query, 2)) == 'number') {\n      $feature-holder: append(nth($query, 1), nth($query, 2), space);\n      $query-holder: append($query-holder, $feature-holder, comma);\n      @return $query-holder;\n    }\n    // If they're both strings and neither are singles, we roll with that.\n    @else if (type-of(nth($query, 1)) == 'string' and type-of(nth($query, 2)) == 'string') {\n      @if not breakpoint-single-string(nth($query, 1)) and not breakpoint-single-string(nth($query, 2)) {\n        $feature-holder: append(nth($query, 1), nth($query, 2), space);\n        $query-holder: append($query-holder, $feature-holder, comma);\n        @return $query-holder;\n      }\n    }\n  }\n  @else if $length == 3 {\n    // If we've got three items and none is a list, we check to see\n    @if type-of(nth($query, 1)) != 'list' and type-of(nth($query, 2)) != 'list' and type-of(nth($query, 3)) != 'list' {\n      // If none of the items are single string values and none of the values are media values, we're good.\n      @if (not breakpoint-single-string(nth($query, 1)) and not breakpoint-single-string(nth($query, 2)) and not breakpoint-single-string(nth($query, 3))) and  ((not breakpoint-is-media(nth($query, 1)) and not breakpoint-is-media(nth($query, 2)) and not breakpoint-is-media(nth($query, 3)))) {\n        $feature-holder: append(nth($query, 1), nth($query, 2), space);\n        $feature-holder: append($feature-holder, nth($query, 3), space);\n        $query-holder: append($query-holder, $feature-holder, comma);\n        @return $query-holder;\n      }\n      // let's check to see if the first item is a media type\n      @else if breakpoint-is-media(nth($query, 1)) {\n        $query-holder: append($query-holder, nth($query, 1));\n        $feature-holder: append(nth($query, 2), nth($query, 3), space);\n        $query-holder: append($query-holder, $feature-holder);\n        @return $query-holder;\n      }\n    }\n  }\n\n  // If it's a single item, or if it's not a special case double or triple, we can simply return the query.\n  @return $query;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Tag */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 69
|     Comment: 
|          // Grab the Memo Output if Memoization can be a thing\n  @if $Memo-Exists {\n    $return: memo-get(breakpoint, breakpoint $query $contexts);\n\n    @if $return != null {\n      $run: false;\n    }\n  }\n\n  @if not $Memo-Exists or $run {\n    // Internal Variables\n    $query-string: '';\n    $query-fallback: false;\n    $return: ();\n\n    // Reserve Global Private Breakpoint Context\n    $holder-context: $private-breakpoint-context-holder;\n    $holder-query-count: $private-breakpoint-query-count;\n\n    // Reset Global Private Breakpoint Context\n    $private-breakpoint-context-holder: () !global;\n    $private-breakpoint-query-count: 0 !global;\n\n\n    // Test to see if it's a comma-separated list\n    $or-list: if(list-separator($query) == 'comma', true, false);\n\n\n    @if ($or-list == false and breakpoint-get('legacy syntax') == false) {\n      $query-string: breakpoint-parse($query);\n    }\n    @else {\n      $length: length($query);\n\n      $last: nth($query, $length);\n      $query-fallback: breakpoint-no-query($last);\n\n      @if ($query-fallback != false) {\n        $length: $length - 1;\n      }\n\n      @if (breakpoint-get('legacy syntax') == true) {\n        $mq: ();\n\n        @for $i from 1 through $length {\n          $mq: append($mq, nth($query, $i), comma);\n        }\n\n        $query-string: breakpoint-parse($mq);\n      }\n      @else {\n        $query-string: '';\n        @for $i from 1 through $length {\n          $query-string: $query-string + if($i == 1, '', ', ') + breakpoint-parse(nth($query, $i));\n        }\n      }\n    }\n\n    $return: ('query': $query-string,\n        'fallback': $query-fallback,\n        'context holder': $private-breakpoint-context-holder,\n        'query count': $private-breakpoint-query-count\n    );\n    @if length($contexts) > 0 and nth($contexts, 1) != false {\n      @if $query-fallback != false {\n        $context-setter: private-breakpoint-set-context('no-query', $query-fallback);\n      }\n      $context-map: ();\n      @each $context in $contexts {\n        $context-map: map-merge($context-map, ($context: breakpoint-get-context($context)));\n      }\n      $return: map-merge($return, (context: $context-map));\n    }\n\n    // Reset Global Private Breakpoint Context\n    $private-breakpoint-context-holder: () !global;\n    $private-breakpoint-query-count: 0 !global;\n\n    @if $Memo-Exists {\n      $holder: memo-set(breakpoint, breakpoint $query $contexts, $return);\n    }\n  }\n\n  @return $return;\n}\n\n//////////////////////////////\n// General Breakpoint Parser\n//////////////////////////////\n@function breakpoint-parse($query) {\n  // Increase number of 'and' queries\n  $private-breakpoint-query-count: $private-breakpoint-query-count + 1 !global;\n\n  // Set up Media Type\n  $query-print: '';\n\n  $force-all: ((breakpoint-get('force all media type') == true) and (breakpoint-get('default media') == 'all'));\n  $empty-media: true;\n  @if ($force-all == true) or (breakpoint-get('default media') != 'all') {\n    // Force the print of the default media type if (force all is true and default media type is all) or (default media type is not all)\n    $query-print: breakpoint-get('default media');\n    $empty-media: false;\n  }\n\n\n  $query-resolution: false;\n\n  $query-holder: breakpoint-parse-query($query);\n\n\n\n  // Loop over each parsed out query and write it to $query-print\n  $first: true;\n\n  @each $feature in $query-holder {\n    $length: length($feature);\n\n    // Parse a single feature\n    @if ($length == 1) {\n      // Feature is currently a list, grab the actual value\n      $feature: nth($feature, 1);\n\n      // Media Type must by convention be the first item, so it's safe to flat override $query-print, which right now should only be the default media type\n      @if (breakpoint-is-media($feature)) {\n        @if ($force-all == true) or ($feature != 'all') {\n          // Force the print of the default media type if (force all is true and default media type is all) or (default media type is not all)\n          $query-print: $feature;\n          $empty-media: false;\n\n          // Set Context\n          $context-setter: private-breakpoint-set-context(media, $query-print);\n        }\n      }\n      @else {\n        $parsed: breakpoint-parse-single($feature, $empty-media, $first);\n        $query-print: '#{$query-print} #{$parsed}';\n        $first: false;\n      }\n    }\n    // Parse a double feature\n    @else if ($length == 2) {\n      @if (breakpoint-is-resolution($feature) != false) {\n        $query-resolution: $feature;\n      }\n      @else {\n        $parsed: null;\n        // If it's a string/number pair,\n        // we check to see if one is a single-string value,\n        // then we parse it as a normal double\n        $alpha: nth($feature, 1);\n        $beta: nth($feature, 2);\n        @if breakpoint-single-string($alpha) or breakpoint-single-string($beta) {\n          $parsed: breakpoint-parse-single($alpha, $empty-media, $first);\n          $query-print: '#{$query-print} #{$parsed}';\n          $first: false;\n          $parsed: breakpoint-parse-single($beta, $empty-media, $first);\n          $query-print: '#{$query-print} #{$parsed}';\n        }\n        @else {\n          $parsed: breakpoint-parse-double($feature, $empty-media, $first);\n          $query-print: '#{$query-print} #{$parsed}';\n          $first: false;\n        }\n      }\n    }\n    // Parse a triple feature\n    @else if ($length == 3) {\n      $parsed: breakpoint-parse-triple($feature, $empty-media, $first);\n      $query-print: '#{$query-print} #{$parsed}';\n      $first: false;\n    }\n\n  }\n\n  @if ($query-resolution != false) {\n    $query-print: breakpoint-build-resolution($query-print, $query-resolution, $empty-media, $first);\n  }\n\n  // Loop through each feature that's been detected so far and append 'false' to the the value list to increment their counters\n  @each $f, $v in $private-breakpoint-context-holder {\n    $v-holder: $v;\n    $length: length($v-holder);\n    @if length($v-holder) < $private-breakpoint-query-count {\n      @for $i from $length to $private-breakpoint-query-count {\n        @if $f == 'media' {\n          $v-holder: append($v-holder, breakpoint-get('default media'));\n        }\n        @else {\n          $v-holder: append($v-holder, false);\n        }\n      }\n    }\n    $private-breakpoint-context-holder: map-merge($private-breakpoint-context-holder, ($f: $v-holder)) !global;\n  }\n\n  @return $query-print;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Footnotes\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Navicons\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* https://developer.yahoo.com/blogs/ydn/clip-hidden-content-better-accessibility-53456.html */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 673
|     Comment: 
|         /* ========================================================================== MASTHEAD ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 101
|     Comment: 
|         /* ==========================================================================\n   TABLES\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Variable */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /*\n   Wide Pages\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|          // true, false (default)\n$indent-var: 1.3em !default;\n\n/* system typefaces */\n$serif: Georgia, Times, serif !default;\n$sans-serif: -apple-system, BlinkMacSystemFont, \"Roboto\", \"Segoe UI\",\n  \"Helvetica Neue\", \"Lucida Grande\", Arial, sans-serif !default;\n$monospace: Monaco, Consolas, \"Lucida Console\", monospace !default;\n\n/* sans serif typefaces */\n$sans-serif-narrow: $sans-serif !default;\n$helvetica: Helvetica, \"Helvetica Neue\", Arial, sans-serif !default;\n\n/* serif typefaces */\n$georgia: Georgia, serif !default;\n$times: Times, serif !default;\n$bodoni: \"Bodoni MT\", serif !default;\n$calisto: \"Calisto MT\", serif !default;\n$garamond: Garamond, serif !default;\n\n$global-font-family: $sans-serif !default;\n$header-font-family: $sans-serif !default;\n$caption-font-family: $serif !default;\n\n/* type scale */\n$type-size-1: 2.441em !default; // ~39.056px\n$type-size-2: 1.953em !default; // ~31.248px\n$type-size-3: 1.563em !default; // ~25.008px\n$type-size-4: 1.25em !default; // ~20px\n$type-size-5: 1em !default; // ~16px\n$type-size-6: 0.75em !default; // ~12px\n$type-size-7: 0.6875em !default; // ~11px\n$type-size-8: 0.625em !default; // ~10px\n\n/* headline scale */\n$h-size-1: 1.563em !default; // ~25.008px\n$h-size-2: 1.25em !default; // ~20px\n$h-size-3: 1.125em !default; // ~18px\n$h-size-4: 1.0625em !default; // ~17px\n$h-size-5: 1.03125em !default; // ~16.5px\n$h-size-6: 1em !default; // ~16px\n\n/*\n   Colors\n   ========================================================================== */\n\n$gray: #7a8288 !default;\n$dark-gray: mix(#000, $gray, 50%) !default;\n$darker-gray: mix(#000, $gray, 60%) !default;\n$light-gray: mix(#fff, $gray, 50%) !default;\n$lighter-gray: mix(#fff, $gray, 90%) !default;\n\n$background-color: #fff !default;\n$code-background-color: #fafafa !default;\n$code-background-color-dark: $light-gray !default;\n$text-color: $dark-gray !default;\n$muted-text-color: mix(#fff, $text-color, 20%) !default;\n$border-color: $lighter-gray !default;\n$form-background-color: $lighter-gray !default;\n$footer-background-color: $lighter-gray !default;\n\n$primary-color: #6f777d !default;\n$success-color: #3fa63f !default;\n$warning-color: #d67f05 !default;\n$danger-color: #ee5f5b !default;\n$info-color: #3b9cba !default;\n$focus-color: $primary-color !default;\n$active-color: mix(#fff, $primary-color, 80%) !default;\n\n/* YIQ color contrast */\n$yiq-contrasted-dark-default: $dark-gray !default;\n$yiq-contrasted-light-default: #fff !default;\n$yiq-contrasted-threshold: 175 !default;\n$yiq-debug: false !default;\n\n/* brands */\n$behance-color: #1769ff !default;\n$bitbucket-color: #205081 !default;\n$dribbble-color: #ea4c89 !default;\n$facebook-color: #3b5998 !default;\n$flickr-color: #ff0084 !default;\n$foursquare-color: #0072b1 !default;\n$github-color: #171516 !default;\n$gitlab-color: #e24329 !default;\n$instagram-color: #517fa4 !default;\n$keybase-color: #ef7639 !default;\n$lastfm-color: #d51007 !default;\n$linkedin-color: #007bb6 !default;\n$mastodon-color: #2b90d9 !default;\n$pinterest-color: #cb2027 !default;\n$reddit-color: #ff4500 !default;\n$rss-color: #fa9b39 !default;\n$soundcloud-color: #ff3300 !default;\n$stackoverflow-color: #fe7a15 !default;\n$tumblr-color: #32506d !default;\n$twitter-color: #55acee !default;\n$vimeo-color: #1ab7ea !default;\n$vine-color: #00bf8f !default;\n$youtube-color: #bb0000 !default;\n$xing-color: #006567 !default;\n\n/* links */\n$link-color: mix(#000, $info-color, 20%) !default;\n$link-color-hover: mix(#000, $link-color, 25%) !default;\n$link-color-visited: mix(#fff, $link-color, 15%) !default;\n$masthead-link-color: $primary-color !default;\n$masthead-link-color-hover: mix(#000, $primary-color, 25%) !default;\n$navicon-link-color-hover: mix(#fff, $primary-color, 75%) !default;\n\n/* notices */\n$notice-background-mix: 80% !default;\n$code-notice-background-mix: 90% !default;\n\n/* syntax highlighting (base16) */\n$base00: #263238 !default;\n$base01: #2e3c43 !default;\n$base02: #314549 !default;\n$base03: #546e7a !default;\n$base04: #b2ccd6 !default;\n$base05: #eeffff !default;\n$base06: #eeffff !default;\n$base07: #ffffff !default;\n$base08: #f07178 !default;\n$base09: #f78c6c !default;\n$base0a: #ffcb6b !default;\n$base0b: #c3e88d !default;\n$base0c: #89ddff !default;\n$base0d: #82aaff !default;\n$base0e: #c792ea !default;\n$base0f: #ff5370 !default;\n\n/*\n   Breakpoints\n   ========================================================================== */\n\n$small: 600px !default;\n$medium: 768px !default;\n$medium-wide: 900px !default;\n$large: 1024px !default;\n$x-large: 1280px !default;\n$max-width: $x-large !default;\n\n/*\n   Grid\n   ========================================================================== */\n\n$right-sidebar-width-narrow: 200px !default;\n$right-sidebar-width: 300px !default;\n$right-sidebar-width-wide: 400px !default;\n\n/*\n   Other\n   ========================================================================== */\n\n$border-radius: 4px !default;\n$box-shadow: 0 1px 1px rgba(0, 0, 0, 0.125) !default;\n$nav-height: 2em !default;\n$nav-toggle-height: 2rem !default;\n$navicon-width: 1.5rem !default;\n$navicon-height: 0.25rem !default;\n$global-transition: all 0.2s ease-in-out !default;\n$intro-transition: intro 0.3s both !default;\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|          // Magnific Popup\n@import \"minimal-mistakes/vendor/susy/susy\";\n@import \"minimal-mistakes/mixins\";\n\n/* Core CSS */\n@import \"minimal-mistakes/reset\";\n@import \"minimal-mistakes/base\";\n@import \"minimal-mistakes/forms\";\n@import \"minimal-mistakes/tables\";\n@import \"minimal-mistakes/animations\";\n\n/* Components */\n@import \"minimal-mistakes/buttons\";\n@import \"minimal-mistakes/notices\";\n@import \"minimal-mistakes/masthead\";\n@import \"minimal-mistakes/navigation\";\n@import \"minimal-mistakes/footer\";\n@import \"minimal-mistakes/search\";\n@import \"minimal-mistakes/syntax\";\n\n/* Utility classes */\n@import \"minimal-mistakes/utilities\";\n\n/* Layout specific */\n@import \"minimal-mistakes/page\";\n@import \"minimal-mistakes/archive\";\n@import \"minimal-mistakes/sidebar\";\n@import \"minimal-mistakes/print\";\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* inner-padding issues in Chrome OSX, Safari 5*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 800
|     Comment: 
|         /* Navigation list ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Generic.Emph */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Constant */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /*\n     Table of contents navigation\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Consistent form font size in all browsers, margin changes, misc */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /* exaggerate max-height to accommodate tall lists*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 114
|     Comment: 
|         /* ==========================================================================\n   PRINT STYLES\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 113
|     Comment: 
|         /*\n   Author profile and links\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 113
|     Comment: 
|         /* ==========================================================================\n   SIDEBAR\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* FF3/4 have !important on line-height in UA stylesheet*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 465
|     Comment: 
|         /* ========================================================================== BUTTONS ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Function */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /*\n   Media and embeds\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* brands */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 25
|     Comment: 
|         /* Other ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1096
|     Comment: 
|         /* Type ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Comment.Preproc */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 113
|     Comment: 
|         /*\n   Default\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 113
|     Comment: 
|         /* calculate height of nav list\n         viewport height - nav height - masthead x-padding\n      */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 67
|     Comment: 
|          // Active classes
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Generic.Subheading */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /*\n   Grid view\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Google Custom Search Engine\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /*\n   List view\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 405
|     Comment: 
|         /* Help text ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 160
|     Comment: 
|         /* Compass YIQ Color Contrast https://github.com/easy-designs/yiq-color-contrast ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 65
|     Comment: 
|          // Reset contexts\n  @include private-breakpoint-reset-contexts();\n\n  $breakpoint: breakpoint($query, false);\n\n  $query-string: map-get($breakpoint, 'query');\n  $query-fallback: map-get($breakpoint, 'fallback');\n\n  $private-breakpoint-context-holder: map-get($breakpoint, 'context holder') !global;\n  $private-breakpoint-query-count: map-get($breakpoint, 'query count') !global;\n\n  // Allow for an as-needed override or usage of no query fallback.\n  @if $no-query != false {\n    $query-fallback: $no-query;\n  }\n\n  @if $query-fallback != false {\n    $context-setter: private-breakpoint-set-context('no-query', $query-fallback);\n  }\n\n  // Print Out Query String\n  @if not breakpoint-get('no queries') {\n    @media #{$query-string} {\n      @content;\n    }\n  }\n\n  @if breakpoint-get('no query fallbacks') != false or breakpoint-get('no queries') == true {\n\n    $type: type-of(breakpoint-get('no query fallbacks'));\n    $print: false;\n\n    @if ($type == 'bool') {\n      $print: true;\n    }\n    @else if ($type == 'string') {\n      @if $query-fallback == breakpoint-get('no query fallbacks') {\n        $print: true;\n      }\n    }\n    @else if ($type == 'list') {\n      @each $wrapper in breakpoint-get('no query fallbacks') {\n        @if $query-fallback == $wrapper {\n          $print: true;\n        }\n      }\n    }\n\n    // Write Fallback\n    @if ($query-fallback != false) and ($print == true) {\n      $type-fallback: type-of($query-fallback);\n\n      @if ($type-fallback != 'bool') {\n        #{$query-fallback} & {\n          @content;\n        }\n      }\n      @else {\n        @content;\n      }\n    }\n  }\n\n  @include private-breakpoint-reset-contexts();\n}\n\n\n@mixin mq($query, $no-query: false) {\n  @include breakpoint($query, $no-query) {\n    @content;\n  }\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /*\n   Related\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 335
|     Comment: 
|         /* Global animation transition ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* YIQ color contrast */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 19
|     Comment: 
|          // unfix
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Icons\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1494
|     Comment: 
|         /* Grid view ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /*\n   Page taxonomy\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /*\n   Social sharing\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* override white-space for nested lists */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /*\n   Page meta\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* links */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1221
|     Comment: 
|         /* Wells ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /* ==========================================================================\n   SINGLE PAGE/POST\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* file page content container */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* image align center */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Modals\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Wells\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Sticky, fixed to top content\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 68
|     Comment: 
|          // Will convert relative EMs into root EMs.\n  @if breakpoint-get('base font size') and type-of(breakpoint-get('base font size')) == 'number' and $value-unit == 'em' {\n    $base-unit: unit(breakpoint-get('base font size'));\n\n    @if $base-unit == 'px' or $base-unit == '%' or $base-unit == 'em' or $base-unit == 'pt' {\n      @return base-conversion($value) / base-conversion(breakpoint-get('base font size')) * 1em;\n    }\n    @else {\n      @warn '#{breakpoint-get(\\'base font size\\')} is not set in valid units for font size!';\n      @return false;\n    }\n  }\n  @else {\n    @return base-conversion($value);\n  }\n}\n\n@function base-conversion($value) {\n  $unit: unit($value);\n\n  @if $unit == 'px' {\n    @return $value / 16px * 1em;\n  }\n  @else if $unit == '%' {\n    @return $value / 100% * 1em;\n  }\n  @else if $unit == 'em' {\n    @return $value;\n  }\n  @else if $unit == 'pt' {\n    @return $value / 12pt * 1em;\n  }\n  @else {\n    @return $value;\n//    @warn 'Everything is terrible! What have you done?!';\n  }\n}\n\n//////////////////////////////\n// Returns whether the feature can have a min/max pair\n//////////////////////////////\n$breakpoint-min-max-features: 'color',\n                              'color-index',\n                              'aspect-ratio',\n                              'device-aspect-ratio',\n                              'device-height',\n                              'device-width',\n                              'height',\n                              'monochrome',\n                              'resolution',\n                              'width';\n\n@function breakpoint-min-max($feature) {\n  @each $item in $breakpoint-min-max-features {\n    @if $feature == $item {\n      @return true;\n    }\n  }\n  @return false;\n}\n\n//////////////////////////////\n// Returns whether the feature can have a string value\n//////////////////////////////\n$breakpoint-string-features:  'orientation',\n                              'scan',\n                              'color',\n                              'aspect-ratio',\n                              'device-aspect-ratio',\n                              'pointer',\n                              'luminosity';\n\n@function breakpoint-string-value($feature) {\n  @each $item in $breakpoint-string-features {\n    @if breakpoint-min-max($item) {\n      @if $feature == 'min-#{$item}' or $feature == 'max-#{$item}' {\n        @return true;\n      }\n    }\n    @else if $feature == $item {\n      @return true;\n    }\n  }\n  @return false;\n}\n\n//////////////////////////////\n// Returns whether the feature is a media type\n//////////////////////////////\n$breakpoint-media-types:  'all',\n                          'braille',\n                          'embossed',\n                          'handheld',\n                          'print',\n                          'projection',\n                          'screen',\n                          'speech',\n                          'tty',\n                          'tv';\n\n@function breakpoint-is-media($feature) {\n  @each $media in $breakpoint-media-types {\n    @if ($feature == $media) or ($feature == 'not #{$media}') or ($feature == 'only #{$media}') {\n      @return true;\n    }\n  }\n\n  @return false;\n}\n\n//////////////////////////////\n// Returns whether the feature can stand alone\n//////////////////////////////\n$breakpoint-single-string-features: 'color',\n                                    'color-index',\n                                    'grid',\n                                    'monochrome';\n\n@function breakpoint-single-string($feature) {\n  @each $item in $breakpoint-single-string-features {\n    @if $feature == $item {\n      @return true;\n    }\n  }\n  @return false;\n}\n\n//////////////////////////////\n// Returns whether the feature\n//////////////////////////////\n@function breakpoint-is-resolution($feature) {\n  $resolutions: 'device-pixel-ratio', 'dpr';\n\n  @if breakpoint-get('transform resolutions') {\n    $resolutions: append($resolutions, 'resolution');\n  }\n\n  @each $reso in $resolutions {\n    @if index($feature, $reso) or index($feature, 'min-#{$reso}') or index($feature, 'max-#{$reso}') {\n      @return true;\n    }\n  }\n\n  @return false;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /*\n   Comments\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Images\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Alignment\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Task lists\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /*\n   Visibility\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 94
|     Comment: 
|          // compile and normalize all user arguments and global settings\n///     $context: susy-compile($context, $config, 'context-only');\n///     // call `su-gutter` with the appropriate data\n///     @return su-call('su-gutter', $context);\n///   }\n///\n/// @example scss - Sample `span` mixin for floated grids\n///   @mixin span(\n///     $span,\n///     $config: ()\n///   ) {\n///     $context: susy-compile($span, $config);\n///     width: su-call('su-span', $context);\n///\n///     @if index($span, 'last') {\n///       float: right;\n///     } @else {\n///       float: left;\n///       margin-right: su-call('su-gutter', $context);\n///     }\n///   }\n\n\n\n// Compile\n// -------\n/// Susy's syntax layer has various moving parts,\n/// with syntax-parsing for the grid/span shorthand,\n/// and normalization for each of the resulting values.\n/// The compile function rolls this all together\n/// in a single call \xE2\x80\x93\n/// for quick access from our internal API functions,\n/// or any additional functions and mixins you add to your project.\n/// Pass user input and configuration maps to the compiler,\n/// and it will hand back a map of values ready for Su.\n/// Combine this with the `su-call` function\n/// to quickly parse, normalize, and process grid calculations.\n///\n/// @group plugin-utils\n/// @see su-call\n///\n/// @param {list | map} $shorthand -\n///   Shorthand expression to define the width of the span,\n///   optionally containing:\n///   - a count, length, or column-list span;\n///   - `at $n`, `first`, or `last` location on asymmetrical grids;\n///   - `narrow`, `wide`, or `wider` for optionally spreading\n///     across adjacent gutters;\n///   - `of $n <spread>` for available grid columns\n///     and spread of the container\n///     (span counts like `of 6` are only valid\n///     in the context of symmetrical grids);\n///   - and `set-gutters $n` to override global gutter settings\n/// @param {map} $config [null] -\n///   Optional map of Susy grid configuration settings\n/// @param {bool} $context-only [false] -\n///   Allow the parser to ignore span and span-spread values,\n///   only parsing context and container-spread\n///\n/// @return {map} -\n///   Parsed and normalized map of settings,\n///   based on global and local configuration,\n///   alongwith shorthad adjustments.\n///\n/// @example scss -\n///   $user-input: 3 wide of susy-repeat(6, 120px) set-gutters 10px;\n///   $grid-data: susy-compile($user-input, $susy);\n///\n///   @each $key, $value in $grid-data {\n///     /* #{$key}: #{$value}, */\n///   }\n@function susy-compile(\n  $short,\n  $config: null,\n  $context-only: false\n) {\n  // Get and normalize config\n  $config: if($config, susy-settings($config), susy-settings());\n  $normal-config: susy-normalize($config);\n\n  // Parse and normalize shorthand\n  @if (type-of($short) != 'map') and (length($short) > 0) {\n    $short: susy-parse($short, $context-only);\n  }\n\n  $normal-short: susy-normalize($short, $normal-config);\n\n  // Merge and return\n  @return map-merge($normal-config, $normal-short);\n}\n\n\n\n// Call\n// ----\n/// The Susy parsing and normalization process\n/// results in a map of configuration settings,\n/// much like the global `$susy` settings map.\n/// In order to pass that information along to Su math functions,\n/// the proper values have to be picked out,\n/// and converted to arguments.\n///\n/// The `su-call` function streamlines that process,\n/// weeding out the unnecessary data,\n/// and passing the rest along to Su in the proper format.\n/// Combine this with `susy-compile` to quickly parse,\n/// normalize, and process grid calculations.\n///\n/// @group plugin-utils\n///\n/// @require su-span\n/// @require su-gutter\n/// @require su-slice\n/// @see susy-compile\n///\n/// @param {'su-span' | 'su-gutter' | 'su-slice'} $name -\n///   Name of the Su math function to call.\n/// @param {map} $config -\n///   Parsed and normalized map of Susy configuration settings\n///   to use for math-function arguments.\n///\n/// @return {*} -\n///   Results of the function being called.\n///\n/// @example scss -\n///   $user-input: 3 wide of susy-repeat(6, 120px) set-gutters 10px;\n///   $grid-data: susy-compile($user-input, $susy);\n///\n///   .su-span {\n///     width: su-call('su-span', $grid-data);\n///   }\n@function su-call(\n  $name,\n  $config\n) {\n  $grid-function-args: (\n    'su-span': ('span', 'columns', 'gutters', 'spread', 'container-spread', 'location'),\n    'su-gutter': ('columns', 'gutters', 'container-spread'),\n    'su-slice': ('span', 'columns', 'location'),\n  );\n\n  $args: map-get($grid-function-args, $name);\n\n  @if not $args {\n    $options: 'Try one of these: #{map-keys($grid-function-args)}';\n    @return _susy-error(\n      '#{$name} is not a public Su function. #{$options}',\n      'su-call');\n  }\n\n  $call: if(function-exists('get-function'), get-function($name), $name);\n  $output: ();\n\n  @each $arg in $args {\n    $value: map-get($config, $arg);\n    $output: if($value, map-merge($output, ($arg: $value)), $output);\n  }\n\n  @return call($call, $output...);\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 75
|     Comment: 
|          // Offset & reflow
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Single */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 107
|     Comment: 
|         /* ==========================================================================\n   FOOTER\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* part 2: Scale the height according to the width, otherwise you get stretching*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /*\n     Priority plus navigation\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Keyword.Declaration */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /* blockquote citations */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* ==========================================================================\n   Variables\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 153
|     Comment: 
|         <!-- start custom footer snippets -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* code */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /* ==========================================================================\n   NAVIGATION\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1250
|     Comment: 
|         /* Required ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Display HTML5 elements in IE6-9 and FF3 */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 12
|     Comment: 
|         <!-- begin _includes/seo.html -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /*\n   Typography\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 9
|     Comment: 
|         /* ========================================================================== Variables ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* ==========================================================================\n   NOTICE TEXT BLOCKS\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 10
|     Comment: 
|         /* Typography ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* ==========================================================================\n   BUTTONS\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /* override margin*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* default */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 825
|     Comment: 
|         /* Table of contents navigation ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /*\n     .form-inline\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /*\n     Help text\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /*\n     Post pagination navigation links\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1343
|     Comment: 
|         /* Social sharing ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Variable.Class */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /*\n     Disabled state\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /* ==========================================================================\n   Forms\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Prevent max-width from affecting Google Maps */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 107
|     Comment: 
|          // Delay in milliseconds before popup is removed
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /**\n * Removes margins, padding, and bullet points from navigation lists\n *\n * Example usage:\n * <nav>\n *    <ul>\n *      <li><a href=\"#link-1\">Link 1</a></li>\n *      <li><a href=\"#link-2\">Link 2</a></li>\n *      <li><a href=\"#link-3\">Link 3</a></li>\n *    </ul>\n *  </nav>\n */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* ==========================================================================\n   STYLE RESETS\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 91
|     Comment: 
|         /* result: #{susy-get('columns')} */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* ==========================================================================\n   BASE ELEMENTS\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 97
|     Comment: 
|         /* Webkit*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 97
|     Comment: 
|         /*\n   em function\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* add scrollbars to wide code blocks*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* Warning notice */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* override for hidden text*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 95
|     Comment: 
|         /* $context: #{$context}; */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1684
|     Comment: 
|         /*# sourceMappingURL=main.css.map */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 94
|     Comment: 
|         /* #{$key}: #{$value}, */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 91
|     Comment: 
|         /* gutters: #{susy-get('gutters')} */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /*\n   Navigation lists\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1116
|     Comment: 
|         /* Alignment ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 88
|     Comment: 
|         /* #{_susy-flatten($list)} */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 88
|     Comment: 
|         /* #{$units}: #{$value} */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 293
|     Comment: 
|         /* Media and embeds ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /*\n   Other\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1361
|     Comment: 
|         /* Page taxonomy ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 105
|     Comment: 
|         /* ==========================================================================\n   MASTHEAD\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 100
|     Comment: 
|         /*\n     Focus & active state\n     ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|         /*!\n * Minimal Mistakes Jekyll Theme 4.24.0 by Michael Rose\n * Copyright 2013-2020 Michael Rose - mademistakes.com | @mmistakes\n * Licensed under MIT (https://github.com/mmistakes/minimal-mistakes/blob/master/LICENSE)\n*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* horizontal rule */
|     
|     Path: http://192.168.227.120:80/assets/css/?N=D
|     Line number: 12
|     Comment: 
|          //-->
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 113
|     Comment: 
|          // just a hack that adds mfp-anim class to markup
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 109
|     Comment: 
|          // make it unique to apply your CSS animations just to this exact popup
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 108
|     Comment: 
|          // Class that is added to body when popup is open.
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|         /* Layout specific */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* readability and alignment cross-browser*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1
|     Comment: 
|         /* ========================================================================== Dark skin ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1581
|     Comment: 
|         /* ========================================================================== SIDEBAR ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /*\n   Global animation transition\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 102
|     Comment: 
|          // Will preload 0 - before current, and 1 after the current image
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 96
|     Comment: 
|          // },
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 93
|     Comment: 
|          //     return false;
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Other */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* http://www.456bereastreet.com/archive/200711/screen_readers_sometimes_ignore_displaynone/ */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* rotate the lines to form the x shape*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Char */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 424
|     Comment: 
|         /* .form-search ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 89
|     Comment: 
|          // Magnific-Popup options
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Comment.Single */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 84
|     Comment: 
|          // add lightbox class to all image links
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 89
|     Comment: 
|          // Silent Failure\n  @if $silent-failure {\n    @return null;\n  }\n\n  // Error Message\n  $actual: '[#{type-of($columns)}] `#{inspect($columns)}`';\n\n  @return _susy-error(\n    '#{$actual} is not a valid list of numbers for $columns.',\n    'su-valid-columns');\n}\n\n\n\n// Valid Gutters\n// -------------\n/// Check that the `gutters` argument is a valid number\n///\n/// @group x-validation\n///\n/// @param {number} $gutters -\n///   Width of a gutter\n///\n/// @return {number} -\n///   Validated `$gutters` number\n///\n/// @throw\n///   when gutter value is not a number\n@function su-valid-gutters(\n  $gutters\n) {\n  $type: type-of($gutters);\n\n  @if ($type == 'number') {\n    @return $gutters;\n  }\n\n  $actual: '[#{$type}] `#{inspect($gutters)}`';\n  @return _susy-error(\n    '#{$actual} is not a number or length for $gutters.',\n    'su-valid-gutters');\n}\n\n\n\n// Valid Spread\n// ------------\n/// Check that the `spread` argument is a valid\n/// intiger between `-1` and `1`\n///\n/// @group x-validation\n///\n/// @param {0 | 1 | -1} $spread -\n///   Number of gutters to include in a span,\n///   relative to the number columns\n///\n/// @return {0 | 1 | -1} -\n///   Validated `$spread` number\n///\n/// @throw\n///   when spread value is not a valid spread\n@function su-valid-spread(\n  $spread\n) {\n  @if index(0 1 -1, $spread) {\n    @return $spread;\n  }\n\n  $actual: '[#{type-of($spread)}] `#{inspect($spread)}`';\n  @return _susy-error(\n    '#{$actual} is not a normalized [0 | 1 | -1] value for `$spread`.',\n    'su-valid-spread');\n}\n\n\n\n// Valid Location\n// --------------\n/// Check that the `location` argument is a valid number,\n/// within the scope of available columns\n///\n/// @group x-validation\n///\n/// @param {number} $span -\n///   Number of grid-columns to be spanned\n/// @param {integer | string} $location -\n///   Starting (1-indexed) column-position of that span\n/// @param {list} $columns -\n///   List of available columns in the grid\n///\n/// @return {integer} -\n///   Validated `$location` intiger\n///\n/// @throw\n///   when location value is not a valid index,\n///   given the context and span.\n@function su-valid-location(\n  $span,\n  $location,\n  $columns\n) {\n  $count: length($columns);\n\n  @if $location {\n    @if (type-of($location) != 'number') or (not unitless($location)) {\n      $actual: '[#{type-of($location)}] `#{$location}`';\n      @return _susy-error(\n        '#{$actual} is not a unitless number for $location.',\n        'su-valid-location');\n    } @else if (round($location) != $location) {\n      @return _susy-error(\n        'Location (`#{$location}`) must be a 1-indexed intiger position.',\n        'su-valid-location');\n    } @else if ($location > $count) or ($location < 1) {\n      @return _susy-error(\n        'Position `#{$location}` does not exist in grid `#{$columns}`.',\n        'su-valid-location');\n    } @else if ($location + $span - 1 > $count) {\n      $details: 'grid `#{$columns}` for span `#{$span}` at `#{$location}`';\n      @return _susy-error(\n        'There are not enough columns in #{$details}.',\n        'su-valid-location');\n    }\n  }\n\n  @return $location;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* headline scale */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 77
|     Comment: 
|          // if true, listen for reflows
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 68
|     Comment: 
|          // applied to the nav list item
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /*\n   Features\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 322
|     Comment: 
|         /** Removes margins, padding, and bullet points from navigation lists Example usage: <nav> <ul> <li><a href="#link-1">Link 1</a></li> <li><a href="#link-2">Link 2</a></li> <li><a href="#link-3">Link 3</a></li> </ul> </nav> */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* image align right */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* when primary navigation is visible, the content in the background won't scroll */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 30
|     Comment: 
|          // Follow menu drop down
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 6
|     Comment: 
|          // FitVids init
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 84
|     Comment: 
|         /* Magnific Popup CSS */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1427
|     Comment: 
|         /* Related ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/main.min.js
|     Line number: 1
|     Comment: 
|         /*!
|          * Minimal Mistakes Jekyll Theme 4.24.0 by Michael Rose
|          * Copyright 2013-2021 Michael Rose - mademistakes.com | @mmistakes
|          * Licensed under MIT
|          */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1587
|     Comment: 
|         /* calculate height of nav list viewport height - nav height - masthead x-padding */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|         /* Variables */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 108
|     Comment: 
|         /* Algolia search */
|     
|     Path: http://192.168.227.120:80/assets/css/?N=D
|     Line number: 6
|     Comment: 
|         <!--
|             .name, .mtime { text-align: left; }
|             .size { text-align: right; }
|             td { text-overflow: ellipsis; white-space: nowrap; overflow: hidden; }
|             table { border-collapse: collapse; }
|             tr th { border-bottom: 2px groove; }
|             //-->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|         /* Components */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 705
|     Comment: 
|         /* Breadcrumb navigation links ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 466
|     Comment: 
|         /* Default button ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 400
|     Comment: 
|         /* Focus & active state ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 23
|     Comment: 
|         /* Breakpoints ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* hide the middle line*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 84
|     Comment: 
|         /* Main image in popup */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* syntax highlighting (base16) */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 106
|     Comment: 
|         /* on hover show expand*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 397
|     Comment: 
|         /* Disabled state ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* img border in anchor's and image quality */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 104
|     Comment: 
|         /* Default notice */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.Number */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Comment.Multiline */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 704
|     Comment: 
|         /* ========================================================================== NAVIGATION ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* Apply focus state */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 91
|     Comment: 
|          // disableOn: function() {
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 84
|     Comment: 
|         /**\n       * Remove all paddings around the image on small screen\n       */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* blockquotes */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* corrects inability to style clickable `input` types in iOS*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* improves usability and consistency of cursor style between image-type `input` and others*/
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 82
|     Comment: 
|         <!-- insert favicons. use https://realfavicongenerator.net/ -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Class */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Backtick */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 67
|     Comment: 
|          // Special handling of no-query from get side so /false/ prepends aren't returned\n    @if $feature == 'no-query' {\n      @if type-of($get) == 'list' and length($get) > 1 and nth($get, 1) == false {\n        $get: nth($get, length($get));\n      }\n    }\n    @return $get;\n  }\n  @else {\n    @if breakpoint-has-context() and $feature == 'media' {\n      @return breakpoint-get('default media');\n    }\n    @else {\n      @return false;\n    }\n  }\n}\n\n//////////////////////////////\n// Private function to set context\n//////////////////////////////\n@function private-breakpoint-set-context($feature, $value) {\n  @if $value == 'monochrome' {\n    $feature: 'monochrome';\n  }\n\n  $current: map-get($private-breakpoint-context-holder, $feature);\n  @if $current and length($current) == $private-breakpoint-query-count {\n    @warn \"You have already queried against `#{$feature}`. Unexpected things may happen if you query against the same feature more than once in the same `and` query. Breakpoint is overwriting the current context with `#{$value}`\";\n  }\n\n  @if not map-has-key($private-breakpoint-context-holder, $feature) {\n    $v-holder: ();\n    @for $i from 1 to $private-breakpoint-query-count {\n      @if $feature == 'media' {\n        $v-holder: append($v-holder, breakpoint-get('default media'));\n      }\n      @else {\n        $v-holder: append($v-holder, false);\n      }\n    }\n    $v-holder: append($v-holder, $value);\n    $private-breakpoint-context-holder: map-merge($private-breakpoint-context-holder, ($feature: $v-holder)) !global;\n  }\n  @else {\n    $v-holder: map-get($private-breakpoint-context-holder, $feature);\n    $length: length($v-holder);\n    @for $i from $length to $private-breakpoint-query-count - 1 {\n      @if $feature == 'media' {\n        $v-holder: append($v-holder, breakpoint-get('default media'));\n      }\n      @else {\n        $v-holder: append($v-holder, false);\n      }\n    }\n    $v-holder: append($v-holder, $value);\n    $private-breakpoint-context-holder: map-merge($private-breakpoint-context-holder, ($feature: $v-holder)) !global;\n  }\n\n  @return true;\n}\n\n//////////////////////////////\n// Private function to reset context\n//////////////////////////////\n@mixin private-breakpoint-reset-contexts {\n  $private-breakpoint-context-holder: () !global;\n  $private-breakpoint-query-count: 0 !global;\n}",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Label */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 59
|     Comment: 
|         <!-- end _includes/seo.html -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Exception */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Punctuation */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Builtin */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Operator.Word */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 435
|     Comment: 
|         /* .form--loading ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /* paragraph indents */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1073
|     Comment: 
|         /* ========================================================================== UTILITY CLASSES ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 73
|     Comment: 
|         <!-- For all browsers -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /* Place inside a single layout */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.Number.Float */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 154
|     Comment: 
|         /* ========================================================================== MIXINS ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 850
|     Comment: 
|         /* ========================================================================== FOOTER ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 112
|     Comment: 
|         /* ==========================================================================\n   ARCHIVE\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 338
|     Comment: 
|         /* ========================================================================== Forms ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 90
|     Comment: 
|          // Calculate column-sum\n  $column-sum: 0;\n  @each $column in $columns {\n    $column-sum: $column-sum + $column;\n  }\n\n  $gutter-sum: (ceil(length($columns)) + $spread) * $gutters;\n  $total: if(($gutter-sum > 0), $column-sum + $gutter-sum, $column-sum);\n\n  @return $total;\n}\n\n\n\n// Su Calc\n// -------\n/// Return a usable span width as a `calc()` function,\n/// in order to create mixed-unit grids.\n///\n/// @group su-math\n/// @access private\n///\n/// @param {number | list} $span -\n///   Pre-sliced list of grid columns to span\n/// @param {list} $columns -\n///   List of columns available\n/// @param {number} $gutters -\n///   Width of a gutter in column-comparable units\n/// @param {0 | 1 | -1} $spread -\n///   Number of gutters spanned,\n///   relative to `span` count\n/// @param {0 | 1 | -1} $container-spread [$spread] -\n///   Number of gutters spanned,\n///   relative to `columns` count\n/// @param {bool} $validate [true] -\n///   Check that arguments are valid before proceeding\n///\n/// @return {length} -\n///   Relative or static length of a span on the grid\n@function _su-calc-span(\n  $span,\n  $columns,\n  $gutters,\n  $spread,\n  $container-spread: $spread,\n  $validate: true\n) {\n  @if $validate {\n    $span: su-valid-span($span);\n    $columns: su-valid-columns($columns);\n    $gutters: su-valid-gutters($gutters);\n    $spread: su-valid-spread($spread);\n    $container-spread: su-valid-spread($container-spread);\n  }\n\n  // Span and context\n  $span: _su-calc-sum($span, $gutters, $spread, not 'validate');\n  $context: _su-calc-sum($columns, $gutters, $container-spread, not 'validate');\n\n  // Fixed and fluid\n  $fixed-span: map-get($span, 'fixed');\n  $fluid-span: map-get($span, 'fluid');\n  $fixed-context: map-get($context, 'fixed');\n  $fluid-context: map-get($context, 'fluid');\n\n  $calc: '#{$fixed-span}';\n  $fluid-calc: '(100% - #{$fixed-context})';\n\n  // Fluid-values\n  @if (not $fluid-span) {\n    $fluid-calc: null;\n  } @else if ($fluid-span != $fluid-context) {\n    $fluid-span: '* #{$fluid-span}';\n    $fluid-context: if($fluid-context, '/ #{$fluid-context}', '');\n    $fluid-calc: '(#{$fluid-calc $fluid-context $fluid-span})';\n  }\n\n  @if $fluid-calc {\n    $calc: if(($calc != ''), '#{$calc} + ', '');\n    $calc: '#{$calc + $fluid-calc}';\n  }\n\n  @return calc(#{unquote($calc)});\n}\n\n\n\n// Su Calc-Sum\n// -----------\n/// Get the total sum of fixed and fluid column-units\n/// for creating a mixed-unit layout with `calc()` values.\n///\n/// @group su-math\n/// @access private\n///\n/// @param {list} $columns -\n///   List of columns available\n/// @param {number} $gutters -\n///   Width of a gutter in column-comparable units\n/// @param {0 | 1 | -1} $spread -\n///   Number of gutters spanned,\n///   relative to `span` count\n/// @param {bool} $validate [true] -\n///   Check that arguments are valid before proceeding\n///\n/// @return {map} -\n///   Map with `fixed` and `fluid` keys\n///   containing the proper math as strings\n@function _su-calc-sum(\n  $columns,\n  $gutters,\n  $spread,\n  $validate: true\n) {\n  @if $validate {\n    $columns: su-valid-span($columns);\n    $gutters: su-valid-gutters($gutters);\n    $spread: su-valid-spread($spread);\n  }\n\n  $fluid: 0;\n  $fixed: ();\n  $calc: null;\n\n  // Gutters\n  $gutters:  $gutters * (length($columns) + $spread);\n\n  // Columns\n  @each $col in append($columns, $gutters) {\n    @if unitless($col) {\n      $fluid: $fluid + $col;\n    } @else {\n      $fixed: _su-map-add-units($fixed, $col);\n    }\n  }\n\n  // Compile Fixed Units\n  @each $unit, $total in $fixed {\n    @if ($total != (0 * $total)) {\n      $calc: if($calc, '#{$calc} + #{$total}', '#{$total}');\n    }\n  }\n\n  // Calc null or string\n  @if $calc {\n    $calc: if(str-index($calc, '+'), '(#{$calc})', '#{$calc}');\n  }\n\n  // Fluid 0 => null\n  $fluid: if(($fluid == 0), null, $fluid);\n\n\n  // Return map\n  $return: (\n    'fixed': $calc,\n    'fluid': $fluid,\n  );\n\n  @return $return;\n}\n\n\n\n// Needs Calc\n// ----------\n/// Check if `calc()` will be needed in defining a span,\n/// if the necessary units in a grid are not comparable.\n///\n/// @group su-math\n/// @access private\n///\n/// @param {list} $span -\n///   Slice of columns to span\n/// @param {list} $columns -\n///   List of available columns in the grid\n/// @param {number} $gutters -\n///   Width of a gutter\n/// @param {0 | 1 | -1} $spread -\n///   Number of gutters spanned,\n///   relative to `span` count\n/// @param {bool} $validate [true] -\n///   Check that arguments are valid before proceeding\n///\n/// @return {bool} -\n///   `True` when units do not match, and `calc()` will be required\n@function _su-needs-calc-output(\n  $span,\n  $columns,\n  $gutters,\n  $spread,\n  $validate: true\n) {\n  @if $validate {\n    $span: su-valid-span($span);\n    $columns: su-valid-columns($columns);\n    $gutters: su-valid-gutters($gutters);\n  }\n\n  $has-gutter: if((length($span) > 1) or ($spread >= 0), true, false);\n  $check: if($has-gutter, append($span, $gutters), $span);\n  $safe-span: _su-is-comparable($check...);\n\n  @if ($safe-span == 'static') {\n    @return false;\n  } @else if (not $safe-span) {\n    @return true;\n  }\n\n  $safe-fluid: _su-is-comparable($gutters, $columns...);\n\n  @return not $safe-fluid;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 63
|     Comment: 
|         /* Core CSS */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Error */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* large button */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 83
|     Comment: 
|          //////////////////////////////\n  // Hand correct each setting\n  //////////////////////////////\n  @if global-variable-exists('breakpoint-default-media') and $breakpoint-default-media != breakpoint-get('default media') {\n    @include breakpoint-set('default media', $breakpoint-default-media);\n  }\n  @if global-variable-exists('breakpoint-default-feature') and $breakpoint-default-feature != breakpoint-get('default feature') {\n    @include breakpoint-set('default feature', $breakpoint-default-feature);\n  }\n  @if global-variable-exists('breakpoint-force-media-all') and $breakpoint-force-media-all != breakpoint-get('force all media type') {\n    @include breakpoint-set('force all media type', $breakpoint-force-media-all);\n  }\n  @if global-variable-exists('breakpoint-to-ems') and $breakpoint-to-ems != breakpoint-get('to ems') {\n    @include breakpoint-set('to ems', $breakpoint-to-ems);\n  }\n  @if global-variable-exists('breakpoint-resolutions') and $breakpoint-resolutions != breakpoint-get('transform resolutions') {\n    @include breakpoint-set('transform resolutions', $breakpoint-resolutions);\n  }\n  @if global-variable-exists('breakpoint-no-queries') and $breakpoint-no-queries != breakpoint-get('no queries') {\n    @include breakpoint-set('no queries', $breakpoint-no-queries);\n  }\n  @if global-variable-exists('breakpoint-no-query-fallbacks') and $breakpoint-no-query-fallbacks != breakpoint-get('no query fallbacks') {\n    @include breakpoint-set('no query fallbacks', $breakpoint-no-query-fallbacks);\n  }\n  @if global-variable-exists('breakpoint-base-font-size') and $breakpoint-base-font-size != breakpoint-get('base font size') {\n    @include breakpoint-set('base font size', $breakpoint-base-font-size);\n  }\n  @if global-variable-exists('breakpoint-legacy-syntax') and $breakpoint-legacy-syntax != breakpoint-get('legacy syntax') {\n    @include breakpoint-set('legacy syntax', $breakpoint-legacy-syntax);\n  }\n}",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Generic.Deleted */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 7
|     Comment: 
|         /*! Minimal Mistakes Jekyll Theme 4.24.0 by Michael Rose Copyright 2013-2020 Michael Rose - mademistakes.com | @mmistakes Licensed under MIT (https://github.com/mmistakes/minimal-mistakes/blob/master/LICENSE) */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Regex */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1218
|     Comment: 
|         /* Sticky, fixed to top content ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.Date */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 24
|     Comment: 
|         /* Grid ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Operator */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* Fix IE9 SVG bug */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 64
|     Comment: 
|          // Gumshoe scroll spy init
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 64
|     Comment: 
|         /* paragraph indention */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Property */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 162
|     Comment: 
|         /* ========================================================================== STYLE RESETS ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 140
|     Comment: 
|         /** Remove all paddings around the image on small screen */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* button colors */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 415
|     Comment: 
|         /* .form-inline ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.String.Doc */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* Figures and images */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Keyword.Pseudo */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* inner spacing ie IE6/7*/
|     
|     Path: http://192.168.227.120:80/assets/js/%25url%25
|     Line number: 155
|     Comment: 
|         <!-- end custom footer snippets -->
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Entity */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 103
|     Comment: 
|         /* small button */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 110
|     Comment: 
|         /* for preloading images */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 321
|     Comment: 
|         /* Navigation lists ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 91
|     Comment: 
|          // 4 symmetrical, fluid columns\n///   // gutters are 1/4 the size of a column\n///   // elements span 1 less gutter than columns\n///   // containers span 1 less gutter as well\n///   $susy: (\n///     'columns': susy-repeat(4),\n///     'gutters': 0.25,\n///     'spread': 'narrow',\n///     'container-spread': 'narrow',\n///   );\n///\n/// @example scss - inside-static gutters\n///   // 6 symmetrical, fluid columns\xE2\x80\xA6\n///   // gutters are static, triggering calc()\xE2\x80\xA6\n///   // elements span equal columns & gutters\xE2\x80\xA6\n///   // containers span equal columns & gutters\xE2\x80\xA6\n///   $susy: (\n///     'columns': susy-repeat(6),\n///     'gutters': 0.5em,\n///     'spread': 'wide',\n///     'container-spread': 'wide',\n///   );\n$susy: () !default;\n\n\n\n// Susy Repeat\n// -----------\n/// Similar to the `repeat(<count>, <value>)` function\n/// that is available in native CSS Grid templates,\n/// the `susy-repeat()` function helps generate repetative layouts\n/// by repeating any value a given number of times.\n/// Where Susy previously allowed `8` as a column definition\n/// for 8 equal columns, you should now use `susy-repeat(8)`.\n///\n/// @group a-config\n///\n/// @param {integer} $count -\n///   The number of repetitions, e.g. `12` for a 12-column grid.\n/// @param {*} $value [1] -\n///   The value to be repeated.\n///   Technically any value can be repeated here,\n///   but the function exists to repeat column-width descriptions:\n///   e.g. the default `1` for single-fraction fluid columns,\n///   `5em` for a static column,\n///   or even `5em 120px` if you are alternating column widths.\n///\n/// @return {list} -\n///   List of repeated values\n///\n/// @example scss\n///   // 12 column grid, with 5em columns\n///   $susy: (\n///     columns: susy-repeat(12, 5em),\n///   );\n///\n/// @example scss\n///   // asymmetrical 5-column grid\n///   $susy: (\n///     columns: 20px susy-repeat(3, 100px) 20px,\n///   );\n///\n///   /* result: #{susy-get('columns')} */\n@function susy-repeat(\n  $count,\n  $value: 1\n) {\n  $return: ();\n\n  @for $i from 1 through $count {\n    $return: join($return, $value);\n  }\n\n  @return $return;\n}\n\n\n\n// Susy Defaults\n// -------------\n/// Configuration map of Susy factory defaults.\n/// Do not override this map directly \xE2\x80\x93\n/// use `$susy` for user and project setting overrides.\n///\n/// @access private\n/// @type Map\n///\n/// @see $susy\n///\n/// @prop {number | list} columns [susy-repeat(4)]\n/// @prop {number} gutters [0.25]\n/// @prop {string} spread ['narrow']\n/// @prop {string} container-spread ['narrow']\n$_susy-defaults: (\n  'columns': susy-repeat(4),\n  'gutters': 0.25,\n  'spread': 'narrow',\n  'container-spread': 'narrow',\n);\n\n\n\n// Susy Settings\n// -------------\n/// Return a combined map of Susy settings,\n/// based on the factory defaults (`$_susy-defaults`),\n/// user-defined project configuration (`$susy`),\n/// and any local overrides required \xE2\x80\x93\n/// such as a configuration map passed into a function.\n///\n/// @group a-config\n///\n/// @param {maps} $overrides\xE2\x80\xA6 -\n///   Optional map override of global configuration settings.\n///   See `$susy` above for properties.\n///\n/// @return {map} -\n///   Combined map of Susy configuration settings,\n///   in order of specificity:\n///   any `$overrides...`,\n///   then `$susy` project settings,\n///   and finally the `$_susy-defaults`\n///\n/// @example scss - global settings\n///   @each $key, $value in susy-settings() {\n///     /* #{$key}: #{$value} */\n///   }\n///\n/// @example scss - local settings\n///   $local: ('columns': 1 2 3 5 8);\n///\n///   @each $key, $value in susy-settings($local) {\n///     /* #{$key}: #{$value} */\n///   }\n@function susy-settings(\n  $overrides...\n) {\n  $settings: map-merge($_susy-defaults, $susy);\n\n  @each $config in $overrides {\n    $settings: map-merge($settings, $config);\n  }\n\n  @return $settings;\n}\n\n\n\n// Susy Get\n// --------\n/// Return the current global value of any Susy setting\n///\n/// @group a-config\n///\n/// @param {string} $key -\n///   Setting to retrieve from the configuration.\n///\n/// @return {*} -\n///   Value mapped to `$key` in the configuration maps,\n///   in order of specificity:\n///   `$susy`, then `$_susy-defaults`\n///\n/// @example scss -\n///   /* columns: #{susy-get('columns')} */\n///   /* gutters: #{susy-get('gutters')} */\n@function susy-get(\n  $key\n) {\n  $settings: susy-settings();\n\n  @if not map-has-key($settings, $key) {\n    @return _susy-error(\n      'There is no Susy setting called `#{$key}`',\n      'susy-get');\n  }\n\n  @return map-get($settings, $key);\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 88
|     Comment: 
|          // add a comparable unit\n///   $map: _su-map-add-units($map, 3vw); // add a new unit\n///\n///   @each $units, $value in $map {\n///     /* #{$units}: #{$value} */\n///   }\n@function _su-map-add-units(\n  $map,\n  $value\n) {\n  $unit: $value * 0;\n  $has: map-get($map, $unit) or 0;\n\n  @if ($has == 0) {\n    @each $try, $could in $map {\n      $match: comparable($try, $value);\n      $unit: if($match, $try, $unit);\n      $has: if($match, $could, $has);\n    }\n  }\n\n  @return map-merge($map, ($unit: $has + $value));\n}\n\n\n// Susy Flatten\n// ------------\n/// Flatten a multidimensional list\n///\n/// @group x-utility\n/// @access private\n///\n/// @param {list} $list -\n///   The list to be flattened\n/// @return {list} -\n///   The flattened list\n///\n/// @example scss -\n///   $list: 120px (30em 30em) 120px;\n///   /* #{_susy-flatten($list)} */\n@function _susy-flatten(\n  $list\n) {\n  $flat: ();\n\n  // Don't iterate over maps\n  @if (type-of($list) == 'map') {\n    @return $list;\n  }\n\n  // Iterate over lists (or single items)\n  @each $item in $list {\n    @if (type-of($item) == 'list') {\n      $item: _susy-flatten($item);\n      $flat: join($flat, $item);\n    } @else {\n      $flat: append($flat, $item);\n    }\n  }\n\n  // Return flattened list\n  @return $flat;\n}\n",
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1107
|     Comment: 
|         /* Task lists ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* part 1: Set a maximum relative to the parent*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 99
|     Comment: 
|         /* lists */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 1264
|     Comment: 
|         /* ========================================================================== SINGLE PAGE/POST ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/js/_main.js
|     Line number: 36
|     Comment: 
|          // Close search screen with Esc key
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 111
|     Comment: 
|         /* sibling indentation*/
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Keyword.Type */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 113
|     Comment: 
|         /* fix z-index order of follow links */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 62
|     Comment: 
|         /* Colors */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Name.Decorator */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 98
|     Comment: 
|         /* apply a natural box layout model to all elements */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 114
|     Comment: 
|         /*\n   Hide the following elements on print\n   ========================================================================== */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css.map
|     Line number: 109
|     Comment: 
|         /* Literal.Number.Integer.Long */
|     
|     Path: http://192.168.227.120:80/assets/css/main.css
|     Line number: 444
|     Comment: 
|_        /* ========================================================================== TABLES ========================================================================== */
| http-enum: 
|   /robots.txt: Robots file
|_  /index/: Potentially interesting folder

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 29 08:03:57 2024 -- 1 IP address (1 host up) scanned in 485.39 seconds

```
