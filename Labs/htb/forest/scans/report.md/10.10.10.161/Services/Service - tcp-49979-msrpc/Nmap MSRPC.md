```bash
nmap -vv --reason -Pn -T4 -sV -p 49979 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp49979/tcp_49979_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp49979/xml/tcp_49979_rpc_nmap.xml" 10.10.10.161
```

[/home/kali/Notes/Labs/htb/forest/scans/tcp49979/tcp_49979_rpc_nmap.txt](file:///home/kali/Notes/Labs/htb/forest/scans/tcp49979/tcp_49979_rpc_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 20 12:52:44 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 49979 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/htb/forest/scans/tcp49979/tcp_49979_rpc_nmap.txt -oX /home/kali/Notes/Labs/htb/forest/scans/tcp49979/xml/tcp_49979_rpc_nmap.xml 10.10.10.161
Nmap scan report for forest.htb.local (10.10.10.161)
Host is up, received user-set (0.052s latency).
Scanned at 2025-01-20 12:52:44 EST for 70s

PORT      STATE SERVICE REASON          VERSION
49979/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 20 12:53:54 2025 -- 1 IP address (1 host up) scanned in 70.20 seconds

```
