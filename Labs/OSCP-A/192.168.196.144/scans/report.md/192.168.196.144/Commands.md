```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_quick_tcp_nmap.xml" 192.168.196.144

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_full_tcp_nmap.xml" 192.168.196.144

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_top_100_udp_nmap.xml" 192.168.196.144

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_quick_tcp_nmap.xml" 192.168.196.144

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_full_tcp_nmap.xml" 192.168.196.144

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_top_100_udp_nmap.xml" 192.168.196.144

nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 192.168.196.144

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.196.144

feroxbuster -u http://192.168.196.144:80/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.196.144:80/.well-known/security.txt

curl -sSikf http://192.168.196.144:80/robots.txt

curl -sSik http://192.168.196.144:80/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.196.144:80 2>&1 | tee "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.196.144

whatweb --color=never --no-errors -a 3 -v http://192.168.196.144:80 2>&1

wkhtmltoimage --format png http://192.168.196.144:80/ /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_screenshot.png


```