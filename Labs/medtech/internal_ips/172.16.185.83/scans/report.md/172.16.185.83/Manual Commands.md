```bash
[*] msrpc on tcp/135

	[-] RPC Client:

		rpcclient -p 135 -U "" 172.16.185.83

[*] netbios-ssn on tcp/139

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.83 --port=139 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 139 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/tcp_139_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/xml/tcp_139_smb_vulnerabilities.xml" 172.16.185.83

[*] microsoft-ds on tcp/445

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.83 --port=445 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Lookup SIDs

		impacket-lookupsid '[username]:[password]@172.16.185.83'

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp445/tcp_445_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp445/xml/tcp_445_smb_vulnerabilities.xml" 172.16.185.83

[*] netbios-ns on udp/137

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.83 --port=137 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/udp137/udp_137_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/udp137/xml/udp_137_smb_vulnerabilities.xml" 172.16.185.83


```