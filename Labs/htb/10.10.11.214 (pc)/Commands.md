```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/htb/pc/scans/_quick_tcp_nmap.txt" -oX "/home/kali/htb/pc/scans/xml/_quick_tcp_nmap.xml" 10.10.11.214

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/htb/pc/scans/_full_tcp_nmap.txt" -oX "/home/kali/htb/pc/scans/xml/_full_tcp_nmap.xml" 10.10.11.214

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/htb/pc/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/htb/pc/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 10.10.11.214


```