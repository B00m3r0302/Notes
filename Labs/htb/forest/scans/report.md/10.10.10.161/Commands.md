```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/forest/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/xml/_quick_tcp_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/forest/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/xml/_full_tcp_nmap.xml" 10.10.10.161

dig -p 53 -x 10.10.10.161 @10.10.10.161

dig AXFR -p 53 @10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.161

impacket-getArch -target 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.161

impacket-rpcdump -port 135 10.10.10.161

enum4linux-ng -A -d -v 10.10.10.161 2>&1

nbtscan -rvh 10.10.10.161 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.10.161

smbclient -L //10.10.10.161 -N -I 10.10.10.161 2>&1

smbmap -H 10.10.10.161 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.161

smbmap -H 10.10.10.161 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 10.10.10.161

impacket-rpcdump -port 593 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 3268 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp3268/tcp_3268_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp3268/xml/tcp_3268_ldap_nmap.xml" 10.10.10.161

smbmap -u null -p "" -H 10.10.10.161 -P 139 2>&1

smbmap -u null -p "" -H 10.10.10.161 -P 445 2>&1

smbmap -H 10.10.10.161 -P 139 -r 2>&1

smbmap -H 10.10.10.161 -P 445 -r 2>&1

smbmap -u null -p "" -H 10.10.10.161 -P 139 -r 2>&1

smbmap -u null -p "" -H 10.10.10.161 -P 445 -r 2>&1

smbmap -H 10.10.10.161 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.161 -P 139 -x "ipconfig /all" 2>&1

smbmap -H 10.10.10.161 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.161 -P 445 -x "ipconfig /all" 2>&1

feroxbuster -u http://10.10.10.161:47001/ -t 10 -w /home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.161:47001/.well-known/security.txt

curl -sSikf http://10.10.10.161:47001/robots.txt

curl -sSik http://10.10.10.161:47001/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.10.161:47001 2>&1 | tee "/home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 10.10.10.161

whatweb --color=never --no-errors -a 3 -v http://10.10.10.161:47001 2>&1

wkhtmltoimage --format png http://10.10.10.161:47001/ /home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 49664 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49664/tcp_49664_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49664/xml/tcp_49664_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49665 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49665/tcp_49665_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49665/xml/tcp_49665_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49666 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49666/tcp_49666_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49667 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49667/tcp_49667_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49667/xml/tcp_49667_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49671 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49671/tcp_49671_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49671/xml/tcp_49671_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49677 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49677/tcp_49677_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49677/xml/tcp_49677_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49684 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49684/tcp_49684_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49684/xml/tcp_49684_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49706 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49706/tcp_49706_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49706/xml/tcp_49706_rpc_nmap.xml" 10.10.10.161

nmap -vv --reason -Pn -T4 -sV -p 49979 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49979/tcp_49979_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49979/xml/tcp_49979_rpc_nmap.xml" 10.10.10.161


```