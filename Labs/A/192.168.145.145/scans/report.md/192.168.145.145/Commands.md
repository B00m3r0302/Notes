```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/A/192.168.145.145/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.145/scans/xml/_quick_tcp_nmap.xml" 192.168.145.145

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.145.145/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.145/scans/xml/_full_tcp_nmap.xml" 192.168.145.145

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/A/192.168.145.145/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.145/scans/xml/_top_100_udp_nmap.xml" 192.168.145.145

dig -p 53 -x 192.168.145.145 @192.168.145.145

dig AXFR -p 53 @192.168.145.145

nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.145.145/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.145/scans/tcp53/xml/tcp_53_dns_nmap.xml" 192.168.145.145

dig -p 53 -x 192.168.145.145 @192.168.145.145

dig AXFR -p 53 @192.168.145.145

nmap -vv --reason -Pn -T4 -sU -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.145.145/scans/udp53/udp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.145/scans/udp53/xml/udp_53_dns_nmap.xml" 192.168.145.145


```