```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/reel/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/xml/_quick_tcp_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/reel/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/xml/_full_tcp_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 25 --script="banner,(smtp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp25/tcp_25_smtp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp25/xml/tcp_25_smtp_nmap.xml" 10.10.10.77

hydra smtp-enum://10.10.10.77:25/vrfy -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" 2>&1

impacket-getArch -target 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.77

impacket-rpcdump -port 135 10.10.10.77

enum4linux-ng -A -d -v 10.10.10.77 2>&1

nbtscan -rvh 10.10.10.77 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.10.77

smbclient -L //10.10.10.77 -N -I 10.10.10.77 2>&1

smbmap -H 10.10.10.77 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.77

smbmap -H 10.10.10.77 -P 445 2>&1

impacket-rpcdump -port 593 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 49159 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp49159/tcp_49159_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp49159/xml/tcp_49159_rpc_nmap.xml" 10.10.10.77

hydra smtp-enum://10.10.10.77:25/expn -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" 2>&1

smbmap -u null -p "" -H 10.10.10.77 -P 139 2>&1

smbmap -u null -p "" -H 10.10.10.77 -P 445 2>&1

smbmap -H 10.10.10.77 -P 139 -r 2>&1

smbmap -H 10.10.10.77 -P 445 -r 2>&1

smbmap -u null -p "" -H 10.10.10.77 -P 139 -r 2>&1

smbmap -u null -p "" -H 10.10.10.77 -P 445 -r 2>&1

smbmap -H 10.10.10.77 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.77 -P 139 -x "ipconfig /all" 2>&1

smbmap -H 10.10.10.77 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.77 -P 445 -x "ipconfig /all" 2>&1


```