```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/A/192.168.114.141/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.114.141/scans/xml/_quick_tcp_nmap.xml" 192.168.114.141

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.114.141/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.114.141/scans/xml/_full_tcp_nmap.xml" 192.168.114.141

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/A/192.168.114.141/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.114.141/scans/xml/_top_100_udp_nmap.xml" 192.168.114.141


```