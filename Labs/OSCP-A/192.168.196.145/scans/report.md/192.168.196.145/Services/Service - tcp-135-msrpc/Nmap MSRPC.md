```bash
nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 192.168.196.145
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp135/tcp_135_rpc_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp135/tcp_135_rpc_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:39 2024 as: nmap -vv --reason -Pn -T4 -sV -p 135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp135/tcp_135_rpc_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp135/xml/tcp_135_rpc_nmap.xml 192.168.196.145
Nmap scan report for 192.168.196.145
Host is up, received user-set.
Scanned at 2024-08-21 13:02:41 EDT for 1s

PORT    STATE    SERVICE REASON      VERSION
135/tcp filtered msrpc   no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:02:42 2024 -- 1 IP address (1 host up) scanned in 3.99 seconds

```