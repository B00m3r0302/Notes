```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/xml/_quick_tcp_nmap.xml" 172.16.185.12

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/xml/_full_tcp_nmap.xml" 172.16.185.12

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/xml/_top_100_udp_nmap.xml" 172.16.185.12

impacket-getArch -target 172.16.185.12

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 172.16.185.12

impacket-rpcdump -port 135 172.16.185.12

enum4linux-ng -A -d -v 172.16.185.12 2>&1

nbtscan -rvh 172.16.185.12 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp139/xml/tcp_139_smb_nmap.xml" 172.16.185.12

smbclient -L //172.16.185.12 -N -I 172.16.185.12 2>&1

smbmap -H 172.16.185.12 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp445/xml/tcp_445_smb_nmap.xml" 172.16.185.12

smbmap -H 172.16.185.12 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 3389 --script="banner,(rdp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/tcp_3389_rdp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/xml/tcp_3389_rdp_nmap.xml" 172.16.185.12

smbmap -u null -p "" -H 172.16.185.12 -P 139 2>&1

smbmap -H 172.16.185.12 -P 139 -r 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 445 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 139 -r 2>&1

smbmap -H 172.16.185.12 -P 445 -r 2>&1

smbmap -H 172.16.185.12 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 445 -r 2>&1

smbmap -H 172.16.185.12 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 445 -x "ipconfig /all" 2>&1

nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/udp137/udp_137_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/udp137/xml/udp_137_smb_nmap.xml" 172.16.185.12

smbmap -H 172.16.185.12 -P 137 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 137 2>&1

smbmap -H 172.16.185.12 -P 137 -r 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 137 -r 2>&1

smbmap -H 172.16.185.12 -P 137 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 172.16.185.12 -P 137 -x "ipconfig /all" 2>&1


```