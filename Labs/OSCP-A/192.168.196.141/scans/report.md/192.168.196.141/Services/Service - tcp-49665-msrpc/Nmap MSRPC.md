```bash
nmap -vv --reason -Pn -T4 -sV -p 49665 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49665/tcp_49665_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49665/xml/tcp_49665_rpc_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49665/tcp_49665_rpc_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49665/tcp_49665_rpc_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:38:05 2024 as: nmap -vv --reason -Pn -T4 -sV -p 49665 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49665/tcp_49665_rpc_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49665/xml/tcp_49665_rpc_nmap.xml 192.168.196.141
Nmap scan report for 192.168.196.141
Host is up, received user-set.
Scanned at 2024-08-21 13:38:07 EDT for 2s

PORT      STATE    SERVICE REASON      VERSION
49665/tcp filtered unknown no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:38:09 2024 -- 1 IP address (1 host up) scanned in 3.83 seconds

```