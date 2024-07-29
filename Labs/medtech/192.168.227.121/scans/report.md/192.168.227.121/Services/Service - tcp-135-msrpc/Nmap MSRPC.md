```bash
nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 192.168.227.121
```

[/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp135/tcp_135_rpc_nmap.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp135/tcp_135_rpc_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Jul 29 07:57:02 2024 as: nmap -vv --reason -Pn -T4 -sV -p 135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp135/tcp_135_rpc_nmap.txt -oX /home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp135/xml/tcp_135_rpc_nmap.xml 192.168.227.121
Nmap scan report for 192.168.227.121
Host is up, received user-set (0.078s latency).
Scanned at 2024-07-29 07:57:03 EDT for 23s

PORT    STATE SERVICE REASON          VERSION
135/tcp open  msrpc   syn-ack ttl 125 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 29 07:57:26 2024 -- 1 IP address (1 host up) scanned in 23.26 seconds

```
