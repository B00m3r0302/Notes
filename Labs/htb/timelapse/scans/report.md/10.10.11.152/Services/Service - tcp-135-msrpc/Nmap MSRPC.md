```bash
nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/htb/timelapse/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/htb/timelapse/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.11.152
```

[/home/kali/Notes/Labs/htb/timelapse/scans/tcp135/tcp_135_rpc_nmap.txt](file:///home/kali/Notes/Labs/htb/timelapse/scans/tcp135/tcp_135_rpc_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 12:38:11 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/htb/timelapse/scans/tcp135/tcp_135_rpc_nmap.txt -oX /home/kali/Notes/Labs/htb/timelapse/scans/tcp135/xml/tcp_135_rpc_nmap.xml 10.10.11.152
Nmap scan report for 10.10.11.152
Host is up, received user-set (0.097s latency).
Scanned at 2025-01-13 12:38:11 EST for 22s

PORT    STATE SERVICE REASON          VERSION
135/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 12:38:33 2025 -- 1 IP address (1 host up) scanned in 21.92 seconds

```
