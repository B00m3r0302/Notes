```bash
nmap -vv --reason -Pn -T4 -sV -p 49666 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/tcp_49666_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/tcp_49666_rpc_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/tcp_49666_rpc_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:19:14 2024 as: nmap -vv --reason -Pn -T4 -sV -p 49666 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/tcp_49666_rpc_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml 192.168.185.141
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.089s latency).
Scanned at 2024-08-05 22:19:15 EDT for 71s

PORT      STATE SERVICE REASON          VERSION
49666/tcp open  msrpc   syn-ack ttl 125 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:20:26 2024 -- 1 IP address (1 host up) scanned in 71.60 seconds

```
