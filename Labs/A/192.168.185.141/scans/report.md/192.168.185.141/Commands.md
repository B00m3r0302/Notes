```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_quick_tcp_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_full_tcp_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/xml/_top_100_udp_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.185.141

feroxbuster -u http://192.168.185.141:80/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.185.141:80/.well-known/security.txt

curl -sSikf http://192.168.185.141:80/robots.txt

curl -sSik http://192.168.185.141:80/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.185.141:80 2>&1 | tee "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.185.141

whatweb --color=never --no-errors -a 3 -v http://192.168.185.141:80 2>&1

wkhtmltoimage --format png http://192.168.185.141:80/ /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_screenshot.png

feroxbuster -u http://192.168.185.141:81/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.185.141:81/.well-known/security.txt

curl -sSikf http://192.168.185.141:81/robots.txt

curl -sSik http://192.168.185.141:81/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.185.141:81 2>&1 | tee "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 81 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/xml/tcp_81_http_nmap.xml" 192.168.185.141

whatweb --color=never --no-errors -a 3 -v http://192.168.185.141:81 2>&1

wkhtmltoimage --format png http://192.168.185.141:81/ /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_screenshot.png

impacket-getArch -target 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 192.168.185.141

impacket-rpcdump -port 135 192.168.185.141

enum4linux-ng -A -d -v 192.168.185.141 2>&1

nbtscan -rvh 192.168.185.141 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/xml/tcp_139_smb_nmap.xml" 192.168.185.141

smbclient -L //192.168.185.141 -N -I 192.168.185.141 2>&1

smbmap -H 192.168.185.141 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp445/xml/tcp_445_smb_nmap.xml" 192.168.185.141

smbmap -H 192.168.185.141 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 3306 --script="banner,(mysql* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/tcp_3306_mysql_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp3306/xml/tcp_3306_mysql_nmap.xml" 192.168.185.141

smbmap -u null -p "" -H 192.168.185.141 -P 139 2>&1

smbmap -u null -p "" -H 192.168.185.141 -P 445 2>&1

smbmap -H 192.168.185.141 -P 139 -r 2>&1

smbmap -u null -p "" -H 192.168.185.141 -P 139 -r 2>&1

smbmap -H 192.168.185.141 -P 445 -r 2>&1

smbmap -H 192.168.185.141 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 192.168.185.141 -P 445 -r 2>&1

smbmap -u null -p "" -H 192.168.185.141 -P 139 -x "ipconfig /all" 2>&1

smbmap -H 192.168.185.141 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 192.168.185.141 -P 445 -x "ipconfig /all" 2>&1

feroxbuster -u http://192.168.185.141:47001/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.185.141:47001/.well-known/security.txt

curl -sSikf http://192.168.185.141:47001/robots.txt

curl -sSik http://192.168.185.141:47001/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.185.141:47001 2>&1 | tee "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 192.168.185.141

whatweb --color=never --no-errors -a 3 -v http://192.168.185.141:47001 2>&1

wkhtmltoimage --format png http://192.168.185.141:47001/ /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 49664 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49664/tcp_49664_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49664/xml/tcp_49664_rpc_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 49665 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49665/tcp_49665_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49665/xml/tcp_49665_rpc_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 49666 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/tcp_49666_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 49667 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49667/tcp_49667_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49667/xml/tcp_49667_rpc_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 49668 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49668/tcp_49668_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49668/xml/tcp_49668_rpc_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 49669 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49669/tcp_49669_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49669/xml/tcp_49669_rpc_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 49670 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49670/tcp_49670_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49670/xml/tcp_49670_rpc_nmap.xml" 192.168.185.141

nmap -vv --reason -Pn -T4 -sV -p 52783 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp52783/tcp_52783_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp52783/xml/tcp_52783_rpc_nmap.xml" 192.168.185.141


```