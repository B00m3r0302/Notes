```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/sizzle/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/xml/_quick_tcp_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/sizzle/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/xml/_full_tcp_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 10.10.10.103

dig -p 53 -x 10.10.10.103 @10.10.10.103

dig AXFR -p 53 @10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.10.103

feroxbuster -u http://10.10.10.103:80/ -t 10 -w /home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.103:80/.well-known/security.txt

curl -sSikf http://10.10.10.103:80/robots.txt

curl -sSik http://10.10.10.103:80/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.10.103:80 2>&1 | tee "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.103

whatweb --color=never --no-errors -a 3 -v http://10.10.10.103:80 2>&1

wkhtmltoimage --format png http://10.10.10.103:80/ /home/kali/Notes/Labs/htb/sizzle/scans/tcp80/tcp_80_http_screenshot.png

impacket-getArch -target 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.103

impacket-rpcdump -port 135 10.10.10.103

enum4linux-ng -A -d -v 10.10.10.103 2>&1

nbtscan -rvh 10.10.10.103 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.10.103

smbclient -L //10.10.10.103 -N -I 10.10.10.103 2>&1

smbmap -H 10.10.10.103 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.10.103

feroxbuster -u https://10.10.10.103:443/ -t 10 -w /home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_feroxbuster_dirbuster.txt"

curl -sSikf https://10.10.10.103:443/.well-known/security.txt

curl -sSikf https://10.10.10.103:443/robots.txt

curl -sSik https://10.10.10.103:443/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host https://10.10.10.103:443 2>&1 | tee "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 443 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/xml/tcp_443_https_nmap.xml" 10.10.10.103

sslscan --show-certificate --no-colour 10.10.10.103:443 2>&1

whatweb --color=never --no-errors -a 3 -v https://10.10.10.103:443 2>&1

wkhtmltoimage --format png https://10.10.10.103:443/ /home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.103

smbmap -H 10.10.10.103 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 10.10.10.103

impacket-rpcdump -port 593 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 636 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp636/tcp_636_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp636/xml/tcp_636_ldap_nmap.xml" 10.10.10.103

sslscan --show-certificate --no-colour 10.10.10.103:636 2>&1

nmap -vv --reason -Pn -T4 -sV -p 3268 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp3268/tcp_3268_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp3268/xml/tcp_3268_ldap_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 3269 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp3269/tcp_3269_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp3269/xml/tcp_3269_ldap_nmap.xml" 10.10.10.103

sslscan --show-certificate --no-colour 10.10.10.103:3269 2>&1

sslscan --show-certificate --no-colour 10.10.10.103:5986 2>&1

smbmap -u null -p "" -H 10.10.10.103 -P 139 2>&1

smbmap -u null -p "" -H 10.10.10.103 -P 445 2>&1

smbmap -H 10.10.10.103 -P 139 -r 2>&1

smbmap -H 10.10.10.103 -P 445 -r 2>&1

smbmap -u null -p "" -H 10.10.10.103 -P 139 -r 2>&1

smbmap -H 10.10.10.103 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.103 -P 445 -r 2>&1

smbmap -u null -p "" -H 10.10.10.103 -P 139 -x "ipconfig /all" 2>&1

smbmap -H 10.10.10.103 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.103 -P 445 -x "ipconfig /all" 2>&1

feroxbuster -u http://10.10.10.103:47001/ -t 10 -w /home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.103:47001/.well-known/security.txt

curl -sSikf http://10.10.10.103:47001/robots.txt

curl -sSik http://10.10.10.103:47001/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.10.103:47001 2>&1 | tee "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 10.10.10.103

whatweb --color=never --no-errors -a 3 -v http://10.10.10.103:47001 2>&1

wkhtmltoimage --format png http://10.10.10.103:47001/ /home/kali/Notes/Labs/htb/sizzle/scans/tcp47001/tcp_47001_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 49664 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49664/tcp_49664_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49664/xml/tcp_49664_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49665 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49665/tcp_49665_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49665/xml/tcp_49665_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49666 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49666/tcp_49666_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49669 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49669/tcp_49669_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49669/xml/tcp_49669_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49673 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49673/tcp_49673_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49673/xml/tcp_49673_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49691 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49691/tcp_49691_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49691/xml/tcp_49691_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49693 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49693/tcp_49693_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49693/xml/tcp_49693_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49696 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49696/tcp_49696_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49696/xml/tcp_49696_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49708 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/tcp_49708_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/xml/tcp_49708_rpc_nmap.xml" 10.10.10.103

nmap -vv --reason -Pn -T4 -sV -p 49714 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49714/tcp_49714_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49714/xml/tcp_49714_rpc_nmap.xml" 10.10.10.103


```