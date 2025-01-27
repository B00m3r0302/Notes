```bash
nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp135/tcp_135_rpc_nmap.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp135/tcp_135_rpc_nmap.txt):

```
# Nmap 7.95 scan initiated Sun Jan 26 20:15:40 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/htb/resolute/scans/tcp135/tcp_135_rpc_nmap.txt -oX /home/kali/Notes/Labs/htb/resolute/scans/tcp135/xml/tcp_135_rpc_nmap.xml 10.10.10.169
Nmap scan report for 10.10.10.169
Host is up, received user-set (0.053s latency).
Scanned at 2025-01-26 20:15:41 EST for 21s

PORT    STATE SERVICE REASON          VERSION
135/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jan 26 20:16:02 2025 -- 1 IP address (1 host up) scanned in 21.65 seconds

```
