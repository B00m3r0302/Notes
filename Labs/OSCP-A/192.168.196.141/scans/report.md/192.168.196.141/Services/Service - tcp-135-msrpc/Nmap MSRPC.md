```bash
nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp135/tcp_135_rpc_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp135/tcp_135_rpc_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:08 2024 as: nmap -vv --reason -Pn -T4 -sV -p 135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp135/tcp_135_rpc_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/tcp135/xml/tcp_135_rpc_nmap.xml 192.168.196.141
Nmap scan report for 192.168.196.141
Host is up, received user-set (0.46s latency).
Scanned at 2024-08-21 13:02:15 EDT for 27s

PORT    STATE SERVICE REASON          VERSION
135/tcp open  msrpc   syn-ack ttl 125 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:02:42 2024 -- 1 IP address (1 host up) scanned in 34.17 seconds

```
