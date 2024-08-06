```bash
[*] domain on tcp/53

	[-] Use dnsrecon to bruteforce subdomains of a DNS domain.

		dnsrecon -n 192.168.145.145 -d <DOMAIN-NAME> -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t brt 2>&1 | tee /home/kali/Notes/Labs/A/192.168.145.145/scans/tcp53/tcp_53_dnsrecon_subdomain_bruteforce.txt

	[-] Use dnsrecon to automatically query data from the DNS server. You must specify the target domain name.

		dnsrecon -n 192.168.145.145 -d <DOMAIN-NAME> 2>&1 | tee /home/kali/Notes/Labs/A/192.168.145.145/scans/tcp53/tcp_53_dnsrecon_default_manual.txt

[*] domain on udp/53

	[-] Use dnsrecon to bruteforce subdomains of a DNS domain.

		dnsrecon -n 192.168.145.145 -d <DOMAIN-NAME> -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t brt 2>&1 | tee /home/kali/Notes/Labs/A/192.168.145.145/scans/udp53/udp_53_dnsrecon_subdomain_bruteforce.txt

	[-] Use dnsrecon to automatically query data from the DNS server. You must specify the target domain name.

		dnsrecon -n 192.168.145.145 -d <DOMAIN-NAME> 2>&1 | tee /home/kali/Notes/Labs/A/192.168.145.145/scans/udp53/udp_53_dnsrecon_default_manual.txt


```