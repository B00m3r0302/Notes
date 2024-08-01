```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/xml/_quick_tcp_nmap.xml" 172.16.185.10

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/xml/_full_tcp_nmap.xml" 172.16.185.10

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/xml/_top_100_udp_nmap.xml" 172.16.185.10

dig -p 53 -x 172.16.185.10 @172.16.185.10

dig AXFR -p 53 @172.16.185.10

nmap -vv --reason -Pn -T4 -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/xml/tcp_53_dns_nmap.xml" 172.16.185.10

nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 172.16.185.10

impacket-getArch -target 172.16.185.10

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 172.16.185.10

impacket-rpcdump -port 135 172.16.185.10

enum4linux-ng -A -d -v 172.16.185.10 2>&1

nbtscan -rvh 172.16.185.10 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/xml/tcp_139_smb_nmap.xml" 172.16.185.10

smbclient -L //172.16.185.10 -N -I 172.16.185.10 2>&1

smbmap -H 172.16.185.10 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 172.16.185.10

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp445/xml/tcp_445_smb_nmap.xml" 172.16.185.10

smbmap -H 172.16.185.10 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 172.16.185.10

impacket-rpcdump -port 593 172.16.185.10

nmap -vv --reason -Pn -T4 -sV -p 3268 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp3268/tcp_3268_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp3268/xml/tcp_3268_ldap_nmap.xml" 172.16.185.10

smbmap -u null -p "" -H 172.16.185.10 -P 139 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 445 2>&1

smbmap -H 172.16.185.10 -P 139 -r 2>&1

smbmap -H 172.16.185.10 -P 445 -r 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 139 -r 2>&1

smbmap -H 172.16.185.10 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 445 -r 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 139 -x "ipconfig /all" 2>&1

smbmap -H 172.16.185.10 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 445 -x "ipconfig /all" 2>&1

dig -p 53 -x 172.16.185.10 @172.16.185.10

dig AXFR -p 53 @172.16.185.10

nmap -vv --reason -Pn -T4 -sU -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp53/udp_53_dns_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp53/xml/udp_53_dns_nmap.xml" 172.16.185.10

nmap -vv --reason -Pn -T4 -sU -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/udp_88_kerberos_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp88/xml/udp_88_kerberos_nmap.xml" 172.16.185.10

nmap -vv --reason -Pn -T4 -sU -sV -p 123 --script="banner,(ntp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/udp_123_ntp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp123/xml/udp_123_ntp_nmap.xml" 172.16.185.10

nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp137/udp_137_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp137/xml/udp_137_smb_nmap.xml" 172.16.185.10

smbmap -H 172.16.185.10 -P 137 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 137 2>&1

smbmap -H 172.16.185.10 -P 137 -r 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 137 -r 2>&1

smbmap -H 172.16.185.10 -P 137 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 172.16.185.10 -P 137 -x "ipconfig /all" 2>&1


```