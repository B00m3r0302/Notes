```bash
nmap -vv --reason -Pn -T4 -sV -p 49159 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp49159/tcp_49159_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp49159/xml/tcp_49159_rpc_nmap.xml" 10.10.10.77
```

[/home/kali/Notes/Labs/htb/reel/scans/tcp49159/tcp_49159_rpc_nmap.txt](file:///home/kali/Notes/Labs/htb/reel/scans/tcp49159/tcp_49159_rpc_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 27 20:52:45 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 49159 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/htb/reel/scans/tcp49159/tcp_49159_rpc_nmap.txt -oX /home/kali/Notes/Labs/htb/reel/scans/tcp49159/xml/tcp_49159_rpc_nmap.xml 10.10.10.77
Nmap scan report for 10.10.10.77
Host is up, received user-set (0.054s latency).
Scanned at 2025-01-27 20:52:46 EST for 70s

PORT      STATE SERVICE REASON          VERSION
49159/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 27 20:53:56 2025 -- 1 IP address (1 host up) scanned in 70.43 seconds

```
