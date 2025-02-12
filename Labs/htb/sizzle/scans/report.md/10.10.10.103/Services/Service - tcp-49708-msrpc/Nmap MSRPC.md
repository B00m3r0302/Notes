```bash
nmap -vv --reason -Pn -T4 -sV -p 49708 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/tcp_49708_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/xml/tcp_49708_rpc_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/tcp_49708_rpc_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/tcp_49708_rpc_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:23:35 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 49708 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/tcp_49708_rpc_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp49708/xml/tcp_49708_rpc_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.054s latency).
Scanned at 2025-02-11 10:23:38 EST for 70s

PORT      STATE SERVICE REASON          VERSION
49708/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:24:48 2025 -- 1 IP address (1 host up) scanned in 72.56 seconds

```
