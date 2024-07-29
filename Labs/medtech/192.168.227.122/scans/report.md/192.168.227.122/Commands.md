```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/xml/_quick_tcp_nmap.xml" 192.168.227.122

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/xml/_full_tcp_nmap.xml" 192.168.227.122

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/xml/_top_100_udp_nmap.xml" 192.168.227.122

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.227.122


```