```bash
nmap -vv --reason -Pn -T4 -sV -p 49664 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49664/tcp_49664_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49664/xml/tcp_49664_rpc_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49664/tcp_49664_rpc_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49664/tcp_49664_rpc_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:38:05 2024 as: nmap -vv --reason -Pn -T4 -sV -p 49664 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49664/tcp_49664_rpc_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp49664/xml/tcp_49664_rpc_nmap.xml 192.168.196.141
Nmap scan report for 192.168.196.141
Host is up, received user-set (0.43s latency).
Scanned at 2024-08-21 13:38:11 EDT for 69s

PORT      STATE SERVICE REASON          VERSION
49664/tcp open  unknown syn-ack ttl 125

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:39:20 2024 -- 1 IP address (1 host up) scanned in 74.97 seconds

```