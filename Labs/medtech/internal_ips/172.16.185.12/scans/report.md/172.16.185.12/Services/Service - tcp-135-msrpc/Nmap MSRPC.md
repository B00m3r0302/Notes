```bash
nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 172.16.185.12
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/tcp_135_rpc_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/tcp_135_rpc_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:33:11 2024 as: nmap -vv --reason -Pn -T4 -sV -p 135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/tcp_135_rpc_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/xml/tcp_135_rpc_nmap.xml 172.16.185.12
Nmap scan report for 172.16.185.12
Host is up, received user-set (0.090s latency).
Scanned at 2024-07-31 12:33:11 EDT for 23s

PORT    STATE SERVICE REASON         VERSION
135/tcp open  msrpc   syn-ack ttl 64 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 12:33:34 2024 -- 1 IP address (1 host up) scanned in 22.54 seconds

```
