```bash
[*] ftp on tcp/21

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp21/tcp_21_ftp_hydra.txt" ftp://10.10.10.103

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 21 -O "/home/kali/Notes/Labs/htb/sizzle/scans/tcp21/tcp_21_ftp_medusa.txt" -M ftp -h 10.10.10.103

[*] domain on tcp/53

	[-] Use dnsrecon to bruteforce subdomains of a DNS domain.

		dnsrecon -n 10.10.10.103 -d <DOMAIN-NAME> -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t brt 2>&1 | tee /home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dnsrecon_subdomain_bruteforce.txt

	[-] Use dnsrecon to automatically query data from the DNS server. You must specify the target domain name.

		dnsrecon -n 10.10.10.103 -d <DOMAIN-NAME> 2>&1 | tee /home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dnsrecon_default_manual.txt

[*] http on tcp/80

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://10.10.10.103:80 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_auth_hydra.txt" http-get://10.10.10.103/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_auth_medusa.txt" -M http -h 10.10.10.103 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_form_hydra.txt" http-post-form://10.10.10.103/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_form_medusa.txt" -M web-form -h 10.10.10.103 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://10.10.10.103:80/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_wpscan.txt"

[*] msrpc on tcp/135

	[-] RPC Client:

		rpcclient -p 135 -U "" 10.10.10.103

[*] netbios-ssn on tcp/139

	[-] Bruteforce SMB

		crackmapexec smb 10.10.10.103 --port=139 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 139 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp139/tcp_139_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp139/xml/tcp_139_smb_vulnerabilities.xml" 10.10.10.103

[*] ldap on tcp/389

	[-] ldapsearch command (modify before running):

		ldapsearch -x -D "<username>" -w "<password>" -H ldap://10.10.10.103:389 -b "dc=example,dc=com" -s sub "(objectclass=*)" 2>&1 | tee > "/home/kali/Notes/Labs/htb/sizzle/scans/tcp389/tcp_389_ldap_all-entries.txt"

[*] http on tcp/443

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u https://10.10.10.103:443 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 443 -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_auth_hydra.txt" https-get://10.10.10.103/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 443 -O "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_auth_medusa.txt" -M http -h 10.10.10.103 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 443 -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_form_hydra.txt" https-post-form://10.10.10.103/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 443 -O "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_form_medusa.txt" -M web-form -h 10.10.10.103 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url https://10.10.10.103:443/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_wpscan.txt"

[*] microsoft-ds on tcp/445

	[-] Bruteforce SMB

		crackmapexec smb 10.10.10.103 --port=445 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Lookup SIDs

		impacket-lookupsid '[username]:[password]@10.10.10.103'

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp445/tcp_445_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp445/xml/tcp_445_smb_vulnerabilities.xml" 10.10.10.103

[*] ldap on tcp/636

	[-] ldapsearch command (modify before running):

		ldapsearch -x -D "<username>" -w "<password>" -H ldap://10.10.10.103:636 -b "dc=example,dc=com" -s sub "(objectclass=*)" 2>&1 | tee > "/home/kali/Notes/Labs/htb/sizzle/scans/tcp636/tcp_636_ldap_all-entries.txt"

[*] ldap on tcp/3268

	[-] ldapsearch command (modify before running):

		ldapsearch -x -D "<username>" -w "<password>" -H ldap://10.10.10.103:3268 -b "dc=example,dc=com" -s sub "(objectclass=*)" 2>&1 | tee > "/home/kali/Notes/Labs/htb/sizzle/scans/tcp3268/tcp_3268_ldap_all-entries.txt"

[*] ldap on tcp/3269

	[-] ldapsearch command (modify before running):

		ldapsearch -x -D "<username>" -w "<password>" -H ldap://10.10.10.103:3269 -b "dc=example,dc=com" -s sub "(objectclass=*)" 2>&1 | tee > "/home/kali/Notes/Labs/htb/sizzle/scans/tcp3269/tcp_3269_ldap_all-entries.txt"

[*] wsman on tcp/5985

	[-] Bruteforce logins:

		crackmapexec winrm 10.10.10.103 -d '<domain>' -u '/usr/share/seclists/Usernames/top-usernames-shortlist.txt' -p '/usr/share/seclists/Passwords/darkweb2017-top100.txt'

	[-] Check login (requires credentials):

		crackmapexec winrm 10.10.10.103 -d '<domain>' -u '<username>' -p '<password>'

	[-] Evil WinRM (gem install evil-winrm):

		evil-winrm -u '<user>' -p '<password>' -i 10.10.10.103

		evil-winrm -u '<user>' -H '<hash>' -i 10.10.10.103

[*] wsman on tcp/5986

	[-] Bruteforce logins:

		crackmapexec winrm 10.10.10.103 -d '<domain>' -u '/usr/share/seclists/Usernames/top-usernames-shortlist.txt' -p '/usr/share/seclists/Passwords/darkweb2017-top100.txt'

	[-] Check login (requires credentials):

		crackmapexec winrm 10.10.10.103 -d '<domain>' -u '<username>' -p '<password>'

	[-] Evil WinRM (gem install evil-winrm):

		evil-winrm -u '<user>' -p '<password>' -i 10.10.10.103

		evil-winrm -u '<user>' -H '<hash>' -i 10.10.10.103

[*] http on tcp/47001

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://10.10.10.103:47001 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 47001 -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_auth_hydra.txt" http-get://10.10.10.103/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 47001 -O "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_auth_medusa.txt" -M http -h 10.10.10.103 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 47001 -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_form_hydra.txt" http-post-form://10.10.10.103/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 47001 -O "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_form_medusa.txt" -M web-form -h 10.10.10.103 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] Bruteforce logins:

		crackmapexec winrm 10.10.10.103 -d '<domain>' -u '/usr/share/seclists/Usernames/top-usernames-shortlist.txt' -p '/usr/share/seclists/Passwords/darkweb2017-top100.txt'

	[-] Check login (requires credentials):

		crackmapexec winrm 10.10.10.103 -d '<domain>' -u '<username>' -p '<password>'

	[-] Evil WinRM (gem install evil-winrm):

		evil-winrm -u '<user>' -p '<password>' -i 10.10.10.103

		evil-winrm -u '<user>' -H '<hash>' -i 10.10.10.103

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://10.10.10.103:47001/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_wpscan.txt"

[*] msrpc on tcp/49664

	[-] RPC Client:

		rpcclient -p 49664 -U "" 10.10.10.103

[*] msrpc on tcp/49665

	[-] RPC Client:

		rpcclient -p 49665 -U "" 10.10.10.103

[*] msrpc on tcp/49666

	[-] RPC Client:

		rpcclient -p 49666 -U "" 10.10.10.103

[*] msrpc on tcp/49669

	[-] RPC Client:

		rpcclient -p 49669 -U "" 10.10.10.103

[*] msrpc on tcp/49673

	[-] RPC Client:

		rpcclient -p 49673 -U "" 10.10.10.103

[*] msrpc on tcp/49691

	[-] RPC Client:

		rpcclient -p 49691 -U "" 10.10.10.103

[*] msrpc on tcp/49693

	[-] RPC Client:

		rpcclient -p 49693 -U "" 10.10.10.103

[*] msrpc on tcp/49696

	[-] RPC Client:

		rpcclient -p 49696 -U "" 10.10.10.103

[*] msrpc on tcp/49708

	[-] RPC Client:

		rpcclient -p 49708 -U "" 10.10.10.103

[*] msrpc on tcp/49714

	[-] RPC Client:

		rpcclient -p 49714 -U "" 10.10.10.103


```