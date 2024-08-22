```bash
[*] ftp on tcp/21

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp21/tcp_21_ftp_hydra.txt" ftp://192.168.196.143

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 21 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp21/tcp_21_ftp_medusa.txt" -M ftp -h 192.168.196.143

[*] ssh on tcp/22

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/tcp_22_ssh_hydra.txt" ssh://192.168.196.143

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 22 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/tcp_22_ssh_medusa.txt" -M ssh -h 192.168.196.143

[*] http on tcp/80

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://192.168.196.143:80 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_auth_hydra.txt" http-get://192.168.196.143/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_auth_medusa.txt" -M http -h 192.168.196.143 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_form_hydra.txt" http-post-form://192.168.196.143/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_form_medusa.txt" -M web-form -h 192.168.196.143 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://192.168.196.143:80/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_wpscan.txt"

[*] http on tcp/81

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://192.168.196.143:81 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 81 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_auth_hydra.txt" http-get://192.168.196.143/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 81 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_auth_medusa.txt" -M http -h 192.168.196.143 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 81 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_form_hydra.txt" http-post-form://192.168.196.143/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 81 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_form_medusa.txt" -M web-form -h 192.168.196.143 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://192.168.196.143:81/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_wpscan.txt"

[*] http on tcp/443

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://192.168.196.143:443 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 443 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_auth_hydra.txt" http-get://192.168.196.143/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 443 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_auth_medusa.txt" -M http -h 192.168.196.143 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 443 -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_form_hydra.txt" http-post-form://192.168.196.143/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 443 -O "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_form_medusa.txt" -M web-form -h 192.168.196.143 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://192.168.196.143:443/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp443/tcp_443_http_wpscan.txt"

[*] mysql on tcp/3306

	[-] (sqsh) interactive database shell:

		sqsh -U <username> -P <password> -S 192.168.196.143:3306


```