```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.196.141:81 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp81/tcp_81_http_nikto.txt"
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp81/tcp_81_http_nikto.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp81/tcp_81_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.196.141
+ Target Hostname:    192.168.196.141
+ Target Port:        81
+ Start Time:         2024-08-21 13:02:15 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.51 (Win64) PHP/7.4.26
+ /: Retrieved x-powered-by header: PHP/7.4.26.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ Apache/2.4.51 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ PHP/7.4.26 appears to be outdated (current is at least 8.1.5), PHP 7.4.28 for the 7.4 branch.
+ /index: Uncommon header 'tcn' found, with contents: list.
+ /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.php. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
+ /scripts/handler.cgi: Variation of Irix Handler? Has been seen from other CGI scanners.
+ /scripts/finger: finger other users, may be other commands?.
+ /scripts/finger.pl: finger other users, may be other commands?.
+ /scripts/get32.exe: This can allow attackers to execute arbitrary commands remotely.
+ /scripts/gm-authors.cgi: GreyMatter 'password' file, that controls who can post. This contains login and password information and is installed mode 666 by default. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0324 http://www.attrition.org/~jericho/works/security/greymatter.html
+ /scripts/guestbook/passwd: GuestBook r4 from lasource.r2.ru stores the admin password in a plain text file.
+ /scripts/photo/protected/manage.cgi: My Photo Gallery management interface. May allow full access to photo galleries and more. Versions before 3.8 allowed anyone to view contents of any directory on systems.
+ /scripts/wrap.cgi: possible variation: comes with IRIX 6.2; allows to view directories.
+ /scripts/visadmin.exe: This CGI allows an attacker to crash the web server. Remove it from the CGI directory.
+ /scripts/html2chtml.cgi: Html2Wml < 0.4.8 access local files via CGI, and more.
+ /scripts/html2wml.cgi: Html2Wml < 0.4.8 access local files via CGI, and more.
+ /scripts/echo.bat?&dir+c:\\: This batch file may allow attackers to execute remote commands.
+ /scripts/guestbook.cgi: May allow attackers to execute commands as the web daemon.
+ /scripts/guestbook.pl: May allow attackers to execute commands as the web daemon.
+ /scripts/ss: Mediahouse Statistics Server may allow attackers to execute remote commands. Upgrade to the latest version or remove from the CGI directory.
+ /scripts/gH.cgi: Web backdoor by gH.
+ /scripts/gm-cplog.cgi: GreyMatter log file defaults to mode 666 and contains login and passwords used to update the GM site. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0324 http://www.attrition.org/~jericho/works/security/greymatter.html
+ /scripts/gm.cgi: GreyMatter blogger may reveal user IDs/passwords through a gmrightclick-######.reg files (# are numbers), possibly in /archive or other archive location. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0324 http://www.attrition.org/~jericho/works/security/greymatter.html
+ /scripts/AT-admin.cgi: Admin interface.
+ /scripts/auth_data/auth_user_file.txt: The DCShop installation allows credit card numbers to be viewed remotely. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0821 https://packetstormsecurity.com/files/32406/xmas.txt.html
+ /scripts/mt-static/mt-check.cgi: Movable Type weblog diagnostic script found. Reveals docroot path, operating system, Perl version, and modules.
+ /scripts/mt/mt-check.cgi: Movable Type weblog diagnostic script found. Reveals docroot path, operating system, Perl version, and modules.
+ /scripts/banner.cgi: This CGI may allow attackers to read any file on the system.
+ /scripts/bannereditor.cgi: This CGI may allow attackers to read any file on the system.
+ /scripts/architext_query.pl: Versions older than 1.1 of Excite for Web Servers allow attackers to execute arbitrary commands.
+ /scripts/bizdb1-search.cgi: This CGI may allow attackers to execute commands remotely. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0287
+ /scripts/blog/: A blog was found. May contain security problems in CGIs, weak passwords, and more.
+ /scripts/blog/mt-load.cgi: Movable Type weblog installation CGI found. May be able to reconfigure or reload.
+ /scripts/iisadmin/bdir.htr: This default script shows host info, may allow file browsing and buffer a overrun in the Chunked Encoding data transfer mechanism, request /scripts/iisadmin/bdir.htr??c:\<dir>. See: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2002/MS02-028
+ /scripts/iisadmin/ism.dll: Allows you to mount a brute force attack on passwords.
+ /scripts/tools/ctss.idc: This CGI allows remote users to view and modify SQL DB contents, server paths, docroot and more.
+ /scripts/Carello/Carello.dll: Carello 1.3 may allow commands to be executed on the server by replacing hidden form elements. This could not be tested by Nikto. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0614
+ /scripts/tools/dsnform.exe: Allows creation of ODBC Data Source.
+ /scripts/tools/dsnform: Allows creation of ODBC Data Source.
+ /scripts/httpodbc.dll: Possible IIS backdoor found.
+ /scripts/proxy/w3proxy.dll: MSProxy v1.0 installed.
+ /scripts/astrocam.cgi: Astrocam 1.4.1 contained buffer overflow. Prior to 2.1.3 contained unspecified security bugs. See: http://www.securityfocus.com/bid/4684
+ /scripts/badmin.cgi: BannerWheel v1.0 is vulnerable to a local buffer overflow. If this is version 1.0 it should be upgraded.
+ /scripts/boozt/admin/index.cgi?section=5&input=1: Boozt CGI may have a buffer overflow. Upgrade to a version newer than 0.9.8alpha. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0098
+ /scripts/ezadmin.cgi: Some versions of this CGI are vulnerable to a buffer overflow.
+ /scripts/ezboard.cgi: Some versions of this CGI are vulnerable to a buffer overflow.
+ /scripts/ezman.cgi: Some versions of this CGI are vulnerable to a buffer overflow.
+ /scripts/foxweb.dll: Foxweb 2.5 and below is vulnerable to a buffer overflow (not tested or confirmed). Verify Foxweb is the latest available version. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-0762
+ /scripts/foxweb.exe: Foxweb 2.5 and below is vulnerable to a buffer overflow (not tested or confirmed). Verify Foxweb is the latest available version. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-0762
+ /scripts/mgrqcgi: This CGI from Magic Enterprise 8.30-5 and earlier is vulnerable to multiple buffer overflows. Upgrade to 9.x.
+ /scripts/wconsole.dll: It may be possible to overflow this dll with 1024 bytes of data.
+ /scripts/uploader.exe: This CGI allows attackers to upload files to the server and then execute them.
+ /scripts/cpshost.dll: Posting acceptor possibly allows you to upload files.
+ /scripts/fpsrvadm.exe: Potentially vulnerable CGI program.
+ /scripts/.cobalt: May allow remote admin of CGI scripts.
+ /scripts/mailit.pl: Sambar may allow anonymous email to be sent from any host via this CGI. See: https://vulners.com/nessus/SAMBAR_MAILIT.NASL
+ /scripts/.access: Contains authorization information.
+ /scripts/MsmMask.exe: MondoSearch 4.4 may allow source code viewing by requesting MsmMask.exe?mask=/filename.asp where 'filename.asp' is a real ASP file. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1528
+ /scripts/addbanner.cgi: This CGI may allow attackers to read any file on the system.
+ /scripts/shtml.dll: This may allow attackers to retrieve document source.
+ /scripts/aglimpse.cgi: This CGI may allow attackers to execute remote commands.
+ /scripts/aglimpse: This CGI may allow attackers to execute remote commands.
+ /scripts/architext_query.cgi: Versions older than 1.1 of Excite for Web Servers allow attackers to execute arbitrary commands.
+ /scripts/cmd.exe?/c+dir: cmd.exe can execute arbitrary commands.
+ /scripts/cmd1.exe?/c+dir: cmd1.exe can execute arbitrary commands.
+ /scripts/hello.bat?&dir+c:\\: This batch file may allow attackers to execute remote commands.
+ /scripts/post32.exe|dir%20c:\\: post32 can execute arbitrary commands.
+ /scripts/archie: Gateway to the unix command, may be able to submit extra commands.
+ /scripts/calendar.pl: Gateway to the unix command, may be able to submit extra commands.
+ /scripts/calendar: Gateway to the unix command, may be able to submit extra commands.
+ /scripts/date: Gateway to the unix command, may be able to submit extra commands.
+ /scripts/fortune: Gateway to the unix command, may be able to submit extra commands.
+ /scripts/redirect: Redirects via URL from form.
+ /scripts/uptime: Gateway to the unix command, may be able to submit extra commands.
+ /scripts/wais.pl: Gateway to the unix command, may be able to submit extra commands.
+ /scripts/mail: Simple Perl mailing script to send form data to a pre-configured email address.
+ /scripts/nph-error.pl: Gives more information in error messages.
+ /scripts/query: Echoes back result of your GET.
+ /scripts/test-cgi.tcl: May echo environment variables or give directory listings.
+ /scripts/test-env: May echo environment variables or give directory listings.
+ /scripts/orders/orders.txt: The DCShop installation allows credit card numbers to be viewed remotely. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0821 https://packetstormsecurity.com/files/32406/xmas.txt.html
+ /scripts/cgitest.exe: This CGI allows remote users to download other CGI source code. May have a buffer overflow in the User-Agent header.
+ /scripts/hpnst.exe?c=p+i=SrvSystemInfo.html: HP Instant TopTools may be vulnerable to a DoS by requesting hpnst.exe?c=p+i=hpnst.exe multiple times. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-0169
+ /scripts/Pbcgi.exe: Sambar may be vulnerable to a DOS when a long string is passed to Pbcgi.exe (not attempted). Default CGI should be removed from web servers. See: OSVDB-55370
+ /scripts/testcgi.exe: Sambar may be vulnerable to a DOS when a long string is passed to testcgi.exe (not attempted). Default CGI should be removed from web servers. See: OSVDB-55369
+ /scripts/snorkerz.bat: Arguments passed to DOS CGI without checking.
+ /scripts/snorkerz.cmd: Arguments passed to DOS CGI without checking.
+ /scripts/webfind.exe?keywords=01234567890123456789: May be vulnerable to a buffer overflow (request 2000 bytes of data). Upgrade to WebSitePro 2.5 or greater.
+ /scripts/sbcgi/sitebuilder.cgi: SITEBUILDER v1.4 may allow retrieval of any file. With a valid username and password, request: /<CGIDIR>/sbcgi/sitebuilder.cgi?username=<user>&password=<password>&selectedpage=../../../../../../../../../../etc/passwd. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-0756
+ /scripts/classifieds/index.cgi: My Classifieds pre 2.12 is vulnerable to SQL injection attacks.
+ /scripts/probecontrol.cgi?command=enable&userNikto=cancer&password=killer: This might be interesting: has been seen in web logs from a scanner.
+ /scripts/probecontrol.cgi?command=enable&username=cancer&password=killer: This might be interesting: has been seen in web logs from a scanner.
+ /scripts/retrieve_password.pl: retrieve_password.pl in DCForum 6.x and 2000 generates predictable new passwords based on a sessionID. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0226
+ /scripts/wwwadmin.pl: Administration CGI?.
+ /scripts/webmap.cgi: nmap front end... could be fun.
+ /scripts/admin/admin.cgi: May be ImageFolio Pro administration CGI. Default login is Admin/ImageFolio.
+ /scripts/admin/setup.cgi: May be ImageFolio Pro setup CGI. Default login is Admin/ImageFolio.
+ /scripts/mt-static/mt-load.cgi: Movable Type weblog installation CGI found. May be able to reconfigure or reload.
+ /scripts/mt/mt-load.cgi: Movable Type weblog installation CGI found. May be able to reconfigure or reload.
+ /scripts/dbman/db.cgi?db=no-db: This CGI allows remote attackers to view system information.
+ /scripts/dcshop/auth_data/auth_user_file.txt: The DCShop installation allows credit card numbers to be viewed remotely. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0821 https://packetstormsecurity.com/files/32406/xmas.txt.html
+ /scripts/dcshop/orders/orders.txt: The DCShop installation allows credit card numbers to be viewed remotely. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0821 https://packetstormsecurity.com/files/32406/xmas.txt.html
+ /scripts/dumpenv.pl: This CGI gives a lot of information to attackers.
+ /scripts/mkilog.exe: This CGI can give an attacker a lot of information.
+ /scripts/mkplog.exe: This CGI can give an attacker a lot of information.
+ /scripts/processit.pl: This CGI returns environment variables, giving attackers valuable information.
+ /scripts/rpm_query: This CGI allows anyone to see the installed RPMs.
+ /scripts/shop/orders/orders.txt: The DCShop installation allows credit card numbers to be viewed remotely. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0821
+ /scripts/ws_ftp.ini: Can contain saved passwords for ftp sites.
+ /scripts/WS_FTP.ini: Can contain saved passwords for ftp sites.
+ /scripts/view-source?view-source: This allows remote users to view source code.
+ /scripts/ibill.pm: iBill.pm is installed. This may allow brute forcing of passwords. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0839
+ /scripts/scoadminreg.cgi: This script (part of UnixWare WebTop) may have a local root exploit. It is also an system admin script and should be protected via the web. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0311
+ /scripts/SGB_DIR/superguestconfig: Super GuestBook 1.0 from lasource.r2.ru stores the admin password in a plain text file. See: OSVDB-4663
+ /scripts/icat: Multiple versions of icat allow attackers to read arbitrary files. Make sure the latest version is running.
+ /scripts/nph-showlogs.pl?files=../../&filter=.*&submit=Go&linecnt=500&refresh=0: nCUBE Server Manager 1.0 nph-showlogs.pl directory traversal bug.
+ /scripts/update.dpgs: Duma Photo Gallery System may allow remote users to write to any file on the system. This could not be remotely tested. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1411
+ /scripts/view-source: This may allow remote arbitrary file retrieval.
+ /scripts/wrap: This CGI lets users read any file with 755 perms. It should not be in the CGI directory.
+ /scripts/cgiwrap: Some versions of cgiwrap allow anyone to execute commands remotely.
+ /scripts/Count.cgi: This may allow attackers to execute arbitrary commands on the server.
+ /scripts/echo.bat: This CGI may allow attackers to execute remote commands.
+ /scripts/ImageFolio/admin/admin.cgi: ImageFolio (default account Admin/ImageFolio) may allow files to be deleted via URLs like: ?cgi=remove.pl&uid=111.111.111.111&rmstep=2&category=../../../../../../../../../../../etc/. See: OSVDB-4571
+ /scripts/info2www: This CGI allows attackers to execute commands.
+ /scripts/infosrch.cgi: This CGI allows attackers to execute commands.
+ /scripts/listrec.pl: This CGI allows attackers to execute commands on the host.
+ /scripts/mailnews.cgi: Some versions allow attacker to execute commands as http daemon. Upgrade or remove.
+ /scripts/mmstdod.cgi: May allow attacker to execute remote commands. Upgrade to version 3.0.26 or higher.
+ /scripts/pagelog.cgi: Some versions of this allow you to create system files. Request 'pagelog.cgi?name=../../../../.././tmp/filename' to try.
+ /scripts/perl?-v: Perl is installed in the CGI directory. This essentially gives attackers a system shell. Remove Perl from the CGI dir.
+ /scripts/perl.exe?-v: Perl is installed in the CGI directory. This essentially gives attackers a system shell. Remove perl.exe from the CGI dir.
+ /scripts/perl.exe: Perl is installed in the CGI directory. This essentially gives attackers a system shell. Remove Perl from the CGI dir.
+ /scripts/perl: Perl is installed in the CGI directory. This essentially gives attackers a system shell. Remove Perl from the CGI dir.
+ /scripts/plusmail: This CGI may allow attackers to execute commands remotely.
+ /scripts/scripts/slxweb.dll/getfile?type=Library&file=invalidfileNikto: SalesLogix WebClient may allow attackers to execute arbitrary commands on the host. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-1607 http://www.securityfocus.com/archive/1/378637
+ /scripts/scripts/slxweb.dll/getfile?type=Library&file=invalidfilename: SalesLogix WebClient may allow attackers to execute arbitrary commands on the host. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-1607 http://www.securityfocus.com/archive/1/378637
+ /scripts/smartsearch.cgi?keywords=|/bin/cat%20/etc/passwd|: To check for remote execution vulnerability use ?keywords=|/bin/ls| or your favorite command.
+ /scripts/smartsearch/smartsearch.cgi?keywords=|/bin/cat%20/etc/passwd|: To check for remote execution vulnerability use ?keywords=|/bin/ls| or your favorite command.
+ /scripts/spin_client.cgi?aaaaaaaa: This CGI may be vulnerable to remote execution by sending 8000 x 'a' characters (check to see if you get a 500 error message). See: https://www.tenable.com/plugins/nessus/10393
+ /scripts/sscd_suncourier.pl: Sunsolve CD script may allow users to execute arbitrary commands. The script was confirmed to exist, but the test was not done. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0436
+ /scripts/viralator.cgi: May be vulnerable to command injection, upgrade to 0.9pre2 or newer. This flaw could not be confirmed. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0849
+ /scripts/virgil.cgi: The Virgil CGI Scanner 0.9 allows remote users to gain a system shell. This could not be confirmed (try syntax such as virgil.cgi?tar=-lp&zielport=31337 to open a connection on port 31337. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1938
+ /scripts/vpasswd.cgi: Some versions of this CGI allow attackers to execute system commands. See: https://seclists.org/bugtraq/2002/Oct/362
+ /scripts/webgais: The webgais allows attackers to execute commands. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0176
+ /scripts/websendmail: This CGI may allow attackers to execute arbitrary commands remotely. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0196
+ /scripts/wwwwais: wwwais has a vulnerability that lets attackers run commands as http daemon owner. Request 'CGIDIR/wwwais?version=version=123&' and 4096 bytes of garbage.
+ /scripts/common/listrec.pl: This CGI allows attackers to execute commands on the host.
+ /scripts/cachemgr.cgi: Manager for squid proxy; problem with RedHat 6 making it public, can allow attacker to perform port scans. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0710
+ /scripts/ppdscgi.exe: PowerPlay Web Edition may allow unauthenticated users to view pages. See: BID-491
+ /scripts/webif.cgi: HNS's webif.cgi is vulnerable to allow remote users to rewrite diary entries if 'direct mode' is enabled in version 2.00 and earlier, and Lite 0.8 and earlier.
+ /scripts/.cobalt/siteUserMod/siteUserMod.cgi: Older versions of this CGI allow any user to change the administrator password.
+ /scripts/webdriver: This CGI often allows anyone to access the Informix DB on the host.
+ /scripts/c32web.exe/ChangeAdminPassword: This CGI may contain a backdoor and may allow attackers to change the Cart32 admin password.
+ /scripts/cgi-lib.pl: CGI Library. If retrieved check to see if it is outdated, it may have vulns.
+ /scripts/log/nether-log.pl?checkit: Default Pass: nethernet-rules.
+ /scripts/mini_logger.cgi: Default password: guest.
+ /scripts/mt-static/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /scripts/mt/: Movable Type weblog found. May contain security problems in CGIs, weak passwords, and more. Default login 'Melody' with password 'Nelson'.
+ /scripts/nimages.php: Alpha versions of the Nimages package vulnerable to non-specific 'major' security bugs.
+ /scripts/robadmin.cgi: Default password: roblog.
+ /scripts/netpad.cgi: netpad.cgi may be an indication of a malicious user on the system, as it allows web access to the file system. It may also have remote vulnerabilities itself. This should be removed or protected.
+ /scripts/troops.cgi: This CGI may be a leftover from a hacked site; may be used to attempt to hack other sites. It should be investigated further.
+ /scripts/unlg1.1: web backdoor by ULG.
+ /scripts/unlg1.2: web backdoor by ULG.
+ /scripts/rwwwshell.pl: THC reverse www shell.
+ /scripts/photo/manage.cgi: My Photo Gallery management interface. May allow full access to photo galleries and more.
+ /scripts/wsisa.dll/WService=anything?WSMadmin: Allows Webspeed to be remotely administered. Edit unbroker.properties and set AllowMsngrCmds to 0. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0127
+ /scripts/ccbill-local.pl?cmd=MENU: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/ccbill-local.cgi?cmd=MENU: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/mastergate/search.cgi?search=0&search_on=all: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/Backup/add-passwd.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/gbook/gbook.cgi?_MAILTO=xx;ls: gbook.cgi allows command execution. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-1131
+ /scripts/bslist.cgi?email=x;ls: BSList allows command execution. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0100
+ /scripts/bsguest.cgi?email=x;ls: BSGuest allows command execution. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0099
+ /scripts/phf: This allows attackers to read arbitrary files on the system and perhaps execute commands. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0067
+ /scripts/upload.cgi: The upload.cgi allows attackers to upload arbitrary files to the server. See: OSVDB-228
+ /scripts/nph-publish.cgi: This CGI may allow attackers to execute arbitrary commands on the server. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-1177
+ /scripts/nph-test-cgi: This CGI lets attackers get a directory listing of the CGI directory. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0045
+ /scripts/photo/: My Photo Gallery pre 3.6 contains multiple vulnerabilities including directory traversal, unspecified vulnerabilities and remote management interface access. See: OSVDB-2695
+ /scripts/include/new-visitor.inc.php: Les Visiteurs 2.0.1 and prior are vulnerable to remote command execution. BID 8902 for exploit example. See: OSVDB-2717
+ /scripts/musicqueue.cgi: Musicqueue 1.20 is vulnerable to a buffer overflow. Ensure the latest version is installed (exploit not attempted). See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1140,http://musicqueue.sourceforge.net/
+ /scripts/tools/newdsn.exe: This can be used to make DSNs, useful in use with an ODBC exploit and the RDS exploit (with msadcs.dll). Also may allow files to be created on the server. See: http://www.securityfocus.com/bid/1818 http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0191 http://attrition.org/security/advisory/individual/rfp/rfp.9901.nt_odbc
+ /scripts/windmail: Some versions are vulnerable. Request 'windmail?-n%20c:\boot.ini%20you@youraddress.com' (replace your address) and see if you get the boot.ini file. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0242
+ /scripts/windmail.exe: Some versions are vulnerable. Request 'windmail.exe?-n%20c:\boot.ini%20you@youraddress.com' (replace your address) and see if you get the boot.ini file. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0242
+ /scripts/gbadmin.cgi?action=change_adminpass: RNN Guestbook 1.2 contains multiple vulnerabilities including remotely changing administrative password, deleting posts, changing the setup, remotely executing commands, and more. By default, the admin password is either 'admin' or 'demo'. See Nov 26, 200. See: OSVDB-2873
+ /scripts/gbadmin.cgi?action=change_automail: RNN Guestbook 1.2 contains multiple vulnerabilities including remotely changing administrative password, deleting posts, changing the setup, remotely executing commands, and more. By default, the admin password is either 'admin' or 'demo'. See Nov 26, 200. See: OSVDB-2873
+ /scripts/gbadmin.cgi?action=colors: RNN Guestbook 1.2 contains multiple vulnerabilities including remotely changing administrative password, deleting posts, changing the setup, remotely executing commands, and more. By default, the admin password is either 'admin' or 'demo'. See Nov 26, 200. See: OSVDB-2873
+ /scripts/gbadmin.cgi?action=setup: RNN Guestbook 1.2 contains multiple vulnerabilities including remotely changing administrative password, deleting posts, changing the setup, remotely executing commands, and more. By default, the admin password is either 'admin' or 'demo'. See Nov 26, 200. See: OSVDB-2873
+ /scripts/gbpass.pl: RNN Guestbook 1.2 password storage file. Administrative password should be stored in plaintext. Access gbadmin.cgi in the same directory to (ab)use. By default, the admin password is either 'admin' or 'demo'. See Nov 26, 2003 BugTraq post by brainrawt@ha. See: OSVDB-2915
+ /scripts/addalink.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/cgiecho: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/cgiemail: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/countedit: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/domainredirect.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/entropybanner.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/helpdesk.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/mchat.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/randhtml.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/realhelpdesk.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/realsignup.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/scgiwrap: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/signup.cgi: Default CGI, often with a hosting manager. No known problems, but host managers allow sys admin via web.
+ /scripts/GW5/GWWEB.EXE: Groupwise web interface.
+ /admin/: This might be interesting.
+ /scripts/dbmlparser.exe: This might be interesting.
+ /db/: Directory indexing found.
+ /db/: This might be interesting.
+ /scripts/weblog: This might be interesting.
+ /scripts/.fhp: This might be interesting.
+ /scripts/add_ftp.cgi: This might be interesting.
+ /scripts/admin.cgi: This might be interesting.
+ /scripts/admin.php: This might be interesting.
+ /scripts/admin.php3: This might be interesting.
+ /scripts/admin.pl: This might be interesting.
+ /scripts/adminhot.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/adminwww.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/AnyBoard.cgi: This might be interesting.
+ /scripts/AnyForm: This might be interesting.
+ /scripts/AnyForm2: This might be interesting.
+ /scripts/ash: This might be interesting: possibly a system shell found.
+ /scripts/ax-admin.cgi: This might be interesting.
+ /scripts/ax.cgi: This might be interesting.
+ /scripts/axs.cgi: This might be interesting.
+ /scripts/bash: This might be interesting: possibly a system shell found.
+ /scripts/bnbform: This might be interesting.
+ /scripts/bnbform.cgi: This might be interesting.
+ /scripts/cart.pl: This might be interesting.
+ /scripts/cgimail.exe: This might be interesting.
+ /scripts/classifieds: This might be interesting.
+ /scripts/classifieds.cgi: This might be interesting.
+ /scripts/clickcount.pl?view=test: This might be interesting.
+ /scripts/code.php: This might be interesting.
+ /scripts/code.php3: This might be interesting.
+ /scripts/count.cgi: This might be interesting.
+ /scripts/csh: This might be interesting: possibly a system shell found.
+ /scripts/cstat.pl: This might be interesting.
+ /scripts/c_download.cgi: This might be interesting.
+ /scripts/dasp/fm_shell.asp: This might be interesting.
+ /scripts/day5datacopier.cgi: This might be interesting.
+ /scripts/dfire.cgi: This might be interesting.
+ /scripts/dig.cgi: This might be interesting.
+ /scripts/displayTC.pl: This might be interesting.
+ /scripts/edit.pl: This might be interesting.
+ /scripts/enter.cgi: This might be interesting.
+ /scripts/environ.cgi: This might be interesting.
+ /scripts/environ.pl: This might be interesting.
+ /scripts/ex-logger.pl: This might be interesting.
+ /scripts/excite: This might be interesting.
+ /scripts/filemail: This might be interesting.
+ /scripts/filemail.pl: This might be interesting.
+ /scripts/ftp.pl: This might be interesting: is file transfer allowed?.
+ /scripts/ftpsh: This might be interesting: possibly a system shell found.
+ /scripts/getdoc.cgi: This might be interesting.
+ /scripts/glimpse: This might be interesting.
+ /scripts/hitview.cgi: This might be interesting.
+ /scripts/jailshell: This might be interesting: possibly a system shell found.
+ /scripts/jj: Allows attackers to execute commands as http daemon. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0260
+ /scripts/ksh: This might be interesting: possibly a system shell found.
+ /scripts/log-reader.cgi: This might be interesting.
+ /scripts/log/: This might be interesting.
+ /scripts/login.cgi: This might be interesting.
+ /scripts/login.pl: This might be interesting.
+ /scripts/logit.cgi: This might be interesting.
+ /scripts/logs.pl: This might be interesting.
+ /scripts/logs/: This might be interesting.
+ /scripts/logs/access_log: This might be interesting.
+ /scripts/logs/error_log: This might be interesting.
+ /scripts/lookwho.cgi: This might be interesting.
+ /scripts/maillist.cgi: This might be interesting.
+ /scripts/maillist.pl: This might be interesting.
+ /scripts/man.sh: This might be interesting.
+ /scripts/meta.pl: This might be interesting.
+ /scripts/minimal.exe: This might be interesting.
+ /scripts/nlog-smb.cgi: This might be interesting.
+ /scripts/nlog-smb.pl: This might be interesting.
+ /scripts/noshell: This might be interesting: possibly a system shell found.
+ /scripts/nph-publish: This might be interesting.
+ /scripts/ntitar.pl: This might be interesting.
+ /scripts/pass: This might be interesting.
+ /scripts/passwd: This might be interesting.
+ /scripts/passwd.txt: This might be interesting.
+ /scripts/password: This might be interesting.
+ /scripts/post_query: This might be interesting.
+ /scripts/pu3.pl: This might be interesting.
+ /scripts/ratlog.cgi: This might be interesting.
+ /scripts/responder.cgi: This might be interesting.
+ /scripts/rguest.exe: This might be interesting.
+ /scripts/rksh: This might be interesting: possibly a system shell found.
+ /scripts/rsh: This might be interesting: possibly a system shell found.
+ /scripts/search.cgi: This might be interesting.
+ /scripts/search.pl: This might be interesting.
+ /scripts/session/adminlogin: This might be interesting.
+ /scripts/sh: This might be interesting: possibly a system shell found.
+ /scripts/show.pl: This might be interesting.
+ /scripts/stat/: This might be interesting.
+ /scripts/stats-bin-p/reports/index.html: This might be interesting.
+ /scripts/stats.pl: This might be interesting.
+ /scripts/stats.prf: This might be interesting.
+ /scripts/stats/: This might be interesting.
+ /scripts/statsconfig: This might be interesting.
+ /scripts/stats_old/: This might be interesting.
+ /scripts/statview.pl: This might be interesting.
+ /scripts/survey: This might be interesting.
+ /scripts/survey.cgi: This might be interesting.
+ /scripts/tablebuild.pl: This might be interesting.
+ /scripts/tcsh: This might be interesting: possibly a system shell found.
+ /scripts/test.cgi: This might be interesting.
+ /scripts/test/test.cgi: This might be interesting.
+ /scripts/textcounter.pl: This might be interesting.
+ /scripts/tidfinder.cgi: This might be interesting.
+ /scripts/tigvote.cgi: This might be interesting.
+ /scripts/tpgnrock: This might be interesting.
+ /scripts/ultraboard.cgi: This might be interesting.
+ /scripts/ultraboard.pl: This might be interesting.
+ /scripts/viewlogs.pl: This might be interesting.
+ /scripts/visitor.exe: This might be interesting.
+ /scripts/w3-msql: This might be interesting.
+ /scripts/w3-sql: This might be interesting.
+ /scripts/webais: This might be interesting.
+ /scripts/webbbs.cgi: This might be interesting.
+ /scripts/webbbs.exe: This might be interesting.
+ /scripts/webutil.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/webutils.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/webwho.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/wguest.exe: This might be interesting.
+ /scripts/www-sql: This might be interesting.
+ /scripts/wwwboard.cgi.cgi: This might be interesting.
+ /scripts/wwwboard.pl: This might be interesting.
+ /scripts/wwwstats.pl: This might be interesting.
+ /scripts/wwwthreads/3tvars.pm: This might be interesting.
+ /scripts/wwwthreads/w3tvars.pm: This might be interesting.
+ /scripts/zsh: This might be interesting: possibly a system shell found.
+ /scripts/counter.exe: This might be interesting.
+ /scripts/cphost.dll: cphost.dll may have a DoS and a traversal issue. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1769
+ /scripts/fpadmcgi.exe: This might be interesting.
+ /scripts/postinfo.asp: This might be interesting.
+ /scripts/samples/ctguestb.idc: This might be interesting.
+ /scripts/samples/search/webhits.exe: This might be interesting.
+ /scripts/convert.bas: This might be interesting.
+ /admin/index.php: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/tradecli.dll: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/tradecli.dll?template=nonexistfile?template=..\..\..\..\..\winnt\system32\cmd.exe?/c+dir: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/adduser.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/amadmin.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/anyboard.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/AT-generate.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/auctiondeluxe/auction.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/awl/auctionweaver.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/bb-ack.sh: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/bb-histlog.sh: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/bb-rep.sh: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/bb-replog.sh: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/bbs_forum.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/build.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/bulk/bulk.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/cached_feed.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/calender_admin.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/cartmanager.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/cbmc/forums.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/cgforum.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/change-your-password.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/clickresponder.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/commandit.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/counter-ord: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/counterbanner: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/counterbanner-ord: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/counterfiglet-ord: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/counterfiglet/nc/: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/CSMailto.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/CSMailto/CSMailto.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/csNews.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/csPassword.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/csPassword/csPassword.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/cutecast/members/: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/day5datanotifier.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/db2www/library/document.d2w/show: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/db_manager.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/DCFORMS98.CGI: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/dnewsweb: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/donothing: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/ezshopper2/loadpage.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/ezshopper3/loadpage.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/if/admin/nph-build.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/ikonboard/help.cgi?: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/imageFolio.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/imagefolio/admin/admin.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/journal.cgi?folder=journal.cgi%00: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/majordomo.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/mojo/mojo.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/ncommerce3/ExecMacro/macro.d2w/%0a%0a: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/ncommerce3/ExecMacro/macro.d2w/NOEXISTINGHTMLBLOCK: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/non-existent.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/nph-exploitscanget.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/nph-maillist.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/parse-file: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/php-cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/pollssi.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/postcards.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/profile.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/quikstore.cfg: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/register.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/replicator/webpage.cgi/: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/rightfax/fuwww.dll/?: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/rmp_query: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/robpoll.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/scripts/*%0a.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/simplestguest.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/simplestmail.cgi: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/statusconfig.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/sws/manager.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/texis/phine: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/Upload.pl: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/utm/admin: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/utm/utm_stat: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/_vti_bin/fpcount.exe?Page=default.htm|Image=3|Digits=15: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/_vti_pvt/doctodep.btr: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/cfgwiz.exe: cfgwiz.exe is a Norton Anti-Virus file and should not be available via the web site.
+ /scripts/Cgitest.exe: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/mailform.exe: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/ms_proxy_auth_query/: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/post16.exe: This might be interesting: has been seen in web logs from an unknown scanner.
+ /scripts/.htaccess: Contains authorization information.
+ /scripts/.htaccess.old: Backup/Old copy of .htaccess - Contains authorization information.
+ /scripts/.htaccess.save: Backup/Old copy of .htaccess - Contains authorization information.
+ /scripts/.htaccess~: Backup/Old copy of .htaccess - Contains authorization information.
+ /scripts/.htpasswd: Contains authorization information.
+ /scripts/.passwd: Contains authorization information.
+ /scripts/.wwwacl: Contains authorization information.
+ /scripts/.www_acl: Contains authorization information.
+ /scripts/test-cgi.bat: This is an Apache for Win default. If Apache is lower than 1.3.23, this can be exploited as in test-cgi.bat?|dir+c:+>..\htdocs\listing.txt, but may not allow data sent back to the browser. See: CWE-552
+ /scripts/admin.pl: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/cfgwiz.exe: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/CGImail.exe: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/contents.htm: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/fpadmin.htm: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/fpcount.exe: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/fpremadm.exe: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/fpsrvadm.exe: Default FrontPage CGI found. See: https://en.wikipedia.org/wiki/Microsoft_FrontPage
+ /scripts/cgi-test.exe: Default CGI found. See: CWE-552
+ /icons/: Directory indexing found.
+ /images/: Directory indexing found.
+ /scripts/imagemap: imagemap.exe was found. Many versions from different vendors contain flaws. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0951
+ /scripts/imagemap.exe: imagemap.exe was found. Many versions from different vendors contain flaws. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0951
+ /scripts/htimage.exe: htimage.exe may be vulnerable to a buffer overflow in the mapname portion. https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/MS00-028. http://www.securityfocus.com/bid/1117. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0256
+ /scripts/tools/getdrvrs.exe: MS Jet database engine can be used to make DSNs, useful with an ODBC exploit and the RDS exploit (with msadcs.dll) which mail allow command execution. See: http://attrition.org/security/advisory/individual/rfp/rfp.9901.nt_odbc
+ /scripts/vote.cgi: Mike's Vote CGI contains a bug which allows arbitrary command execution (version 1.2). See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1628
+ /scripts/quizme.cgi: Mike's Quiz Me! CGI contains a bug which allows arbitrary command execution (version 0.5). See: OSVDB-3515
+ /scripts/sendform.cgi: This CGI by Rod Clark (v1.4.4 and below) may allow arbitrary file reading via email or allow spam to be sent. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0710
+ /scripts/gettransbitmap: Sun Answerbook2 is vulnerable to a buffer overflow in the gettransbitmap CGI. All default CGIs should be disabled or removed, and Answerbook2 should be disabled if not being used. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0360
+ /scripts/VsSetCookie.exe?: A flaw in VsSetCookie.exe may allow attackers to guess a correct user name & gain access to the Lucent system. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0236
+ /scripts/Webnews.exe: Some versions of WebNews are vulnerable to a buffer overflow. See: https://seclists.org/bugtraq/2002/Feb/250
+ /scripts/webnews.pl: WebNews may contain some default users in the binary: testweb/newstest, alwn3845/imaptest, alwi3845/wtest3452, testweb2/wtest4879. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0310 http://www.securityfocus.com/bid/4156
+ /scripts/sensepost.exe?/c+dir: The presence of sensepost.exe indicates the system is/was vulnerable to a Unicode flaw and was compromised with a test script from SensePost. The sensepost.exe allows command execution (it is a copy of cmd.exe), as did the original unicode exploit. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0884 https://docs.microsoft.com/en-us/security-updates/securitybulletins/2000/MS00-078
+ /scripts/.nsconfig: Contains authorization information. See: OSVDB-5709
+ /scripts/ion-p.exe?page=c:\winnt\repair\sam: Ion-P allows remote file retrieval. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1559
+ /scripts/rwcgi60: Oracle report server reveals system information without authorization. See Oracle note 133957.1 - Restricting Access to the Reports Server Environment and Output. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1089
+ /scripts/rwcgi60/showenv: Oracle report server reveals system information without authorization. See Oracle note 133957.1 - Restricting Access to the Reports Server Environment and Output. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1089
+ /scripts/classifieds/classifieds.cgi: Mike's Classifieds CGI contains a bug that allows arbitrary command execution on the server (untested). See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0935
+ /scripts/calendar/index.cgi: Mike's Calendar CGI contains a bug that allows arbitrary command execution (version 1.4). See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0432
+ /scripts/c32web.exe/GetImage?ImageName=CustomerEmail.txt%00.pdf: Cart32 contains a null byte directory traversal in the ImageName variable. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-5253
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /Admin/: This might be interesting.
+ ERROR: Error limit (20) reached for host, giving up. Last error: 
+ Scan terminated: 0 error(s) and 467 item(s) reported on remote host
+ End Time:           2024-08-21 13:58:18 (GMT-4) (3363 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
