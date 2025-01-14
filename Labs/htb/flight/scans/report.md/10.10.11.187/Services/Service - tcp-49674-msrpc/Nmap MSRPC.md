```bash
nmap -vv --reason -Pn -T4 -sV -p 49674 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/flight/scans/tcp49674/tcp_49674_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/flight/scans/tcp49674/xml/tcp_49674_rpc_nmap.xml" 10.10.11.187
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp49674/tcp_49674_rpc_nmap.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp49674/tcp_49674_rpc_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 18:22:57 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 49674 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/htb/flight/scans/tcp49674/tcp_49674_rpc_nmap.txt -oX /home/kali/Notes/Labs/htb/flight/scans/tcp49674/xml/tcp_49674_rpc_nmap.xml 10.10.11.187
Nmap scan report for 10.10.11.187
Host is up, received user-set (0.054s latency).
Scanned at 2025-01-13 18:22:57 EST for 70s

PORT      STATE SERVICE REASON          VERSION
49674/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 18:24:07 2025 -- 1 IP address (1 host up) scanned in 70.10 seconds

```
