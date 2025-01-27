```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/resolute/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/xml/_quick_tcp_nmap.xml" 10.10.10.169

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/resolute/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/xml/_full_tcp_nmap.xml" 10.10.10.169

dig -p 53 -x 10.10.10.169 @10.10.10.169

dig AXFR -p 53 @10.10.10.169

nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp53/xml/tcp_53_dns_nmap.xml" 10.10.10.169

nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.169

impacket-getArch -target 10.10.10.169

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.169

impacket-rpcdump -port 135 10.10.10.169

enum4linux-ng -A -d -v 10.10.10.169 2>&1

nbtscan -rvh 10.10.10.169 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.10.169

smbclient -L //10.10.10.169 -N -I 10.10.10.169 2>&1

smbmap -H 10.10.10.169 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.10.169

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.169

smbmap -H 10.10.10.169 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 10.10.10.169

impacket-rpcdump -port 593 10.10.10.169

nmap -vv --reason -Pn -T4 -sV -p 3268 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp3268/tcp_3268_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp3268/xml/tcp_3268_ldap_nmap.xml" 10.10.10.169

smbmap -u null -p "" -H 10.10.10.169 -P 139 2>&1

smbmap -u null -p "" -H 10.10.10.169 -P 445 2>&1

smbmap -H 10.10.10.169 -P 139 -r 2>&1

smbmap -H 10.10.10.169 -P 445 -r 2>&1

smbmap -u null -p "" -H 10.10.10.169 -P 139 -r 2>&1

smbmap -u null -p "" -H 10.10.10.169 -P 445 -r 2>&1

smbmap -H 10.10.10.169 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.169 -P 139 -x "ipconfig /all" 2>&1

smbmap -H 10.10.10.169 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.169 -P 445 -x "ipconfig /all" 2>&1


```