```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/xml/_quick_tcp_nmap.xml" 172.16.185.14

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/xml/_full_tcp_nmap.xml" 172.16.185.14

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/xml/_top_100_udp_nmap.xml" 172.16.185.14

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 172.16.185.14

nmap -vv --reason -Pn -T4 -sU -sV -p 123 --script="banner,(ntp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/udp123/udp_123_ntp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/udp123/xml/udp_123_ntp_nmap.xml" 172.16.185.14


```