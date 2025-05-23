```bash
[*] domain on tcp/53

	[-] Use dnsrecon to bruteforce subdomains of a DNS domain.

		dnsrecon -n 172.16.185.10 -d <DOMAIN-NAME> -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t brt 2>&1 | tee /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dnsrecon_subdomain_bruteforce.txt

	[-] Use dnsrecon to automatically query data from the DNS server. You must specify the target domain name.

		dnsrecon -n 172.16.185.10 -d <DOMAIN-NAME> 2>&1 | tee /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp53/tcp_53_dnsrecon_default_manual.txt

[*] msrpc on tcp/135

	[-] RPC Client:

		rpcclient -p 135 -U "" 172.16.185.10

[*] netbios-ssn on tcp/139

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.10 --port=139 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 139 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/tcp_139_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp139/xml/tcp_139_smb_vulnerabilities.xml" 172.16.185.10

[*] ldap on tcp/389

	[-] ldapsearch command (modify before running):

		ldapsearch -x -D "<username>" -w "<password>" -H ldap://172.16.185.10:389 -b "dc=example,dc=com" -s sub "(objectclass=*)" 2>&1 | tee > "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp389/tcp_389_ldap_all-entries.txt"

[*] microsoft-ds on tcp/445

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.10 --port=445 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Lookup SIDs

		impacket-lookupsid '[username]:[password]@172.16.185.10'

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp445/tcp_445_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp445/xml/tcp_445_smb_vulnerabilities.xml" 172.16.185.10

[*] ldap on tcp/3268

	[-] ldapsearch command (modify before running):

		ldapsearch -x -D "<username>" -w "<password>" -H ldap://172.16.185.10:3268 -b "dc=example,dc=com" -s sub "(objectclass=*)" 2>&1 | tee > "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/tcp3268/tcp_3268_ldap_all-entries.txt"

[*] domain on udp/53

	[-] Use dnsrecon to bruteforce subdomains of a DNS domain.

		dnsrecon -n 172.16.185.10 -d <DOMAIN-NAME> -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t brt 2>&1 | tee /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp53/udp_53_dnsrecon_subdomain_bruteforce.txt

	[-] Use dnsrecon to automatically query data from the DNS server. You must specify the target domain name.

		dnsrecon -n 172.16.185.10 -d <DOMAIN-NAME> 2>&1 | tee /home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp53/udp_53_dnsrecon_default_manual.txt

[*] netbios-ns on udp/137

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.10 --port=137 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp137/udp_137_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/results/172.16.185.10/scans/udp137/xml/udp_137_smb_vulnerabilities.xml" 172.16.185.10


```