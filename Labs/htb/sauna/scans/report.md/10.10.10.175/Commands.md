```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/sauna/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/xml/_quick_tcp_nmap.xml" 10.10.10.175

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/sauna/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/xml/_full_tcp_nmap.xml" 10.10.10.175

dig -p 53 -x 10.10.10.175 @10.10.10.175

dig AXFR -p 53 @10.10.10.175

nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.10.175

feroxbuster -u http://10.10.10.175:80/ -t 10 -w /home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.175:80/.well-known/security.txt

curl -sSikf http://10.10.10.175:80/robots.txt

curl -sSik http://10.10.10.175:80/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.10.175:80 2>&1 | tee "/home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.175

whatweb --color=never --no-errors -a 3 -v http://10.10.10.175:80 2>&1

wkhtmltoimage --format png http://10.10.10.175:80/ /home/kali/Notes/Labs/htb/sauna/scans/tcp80/tcp_80_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.175

impacket-getArch -target 10.10.10.175

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.175

impacket-rpcdump -port 135 10.10.10.175

enum4linux-ng -A -d -v 10.10.10.175 2>&1

nbtscan -rvh 10.10.10.175 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.10.175

smbclient -L //10.10.10.175 -N -I 10.10.10.175 2>&1

smbmap -H 10.10.10.175 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.10.175

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.175

smbmap -H 10.10.10.175 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 10.10.10.175

impacket-rpcdump -port 593 10.10.10.175

nmap -vv --reason -Pn -T4 -sV -p 3268 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp3268/tcp_3268_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp3268/xml/tcp_3268_ldap_nmap.xml" 10.10.10.175

smbmap -u null -p "" -H 10.10.10.175 -P 139 2>&1

smbmap -u null -p "" -H 10.10.10.175 -P 445 2>&1

smbmap -H 10.10.10.175 -P 139 -r 2>&1

smbmap -H 10.10.10.175 -P 445 -r 2>&1

smbmap -u null -p "" -H 10.10.10.175 -P 139 -r 2>&1

smbmap -u null -p "" -H 10.10.10.175 -P 445 -r 2>&1

smbmap -H 10.10.10.175 -P 139 -x "ipconfig /all" 2>&1

smbmap -H 10.10.10.175 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.175 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.175 -P 445 -x "ipconfig /all" 2>&1


```