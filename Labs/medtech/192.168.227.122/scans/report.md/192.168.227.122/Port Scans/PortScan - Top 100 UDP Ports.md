```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/xml/_top_100_udp_nmap.xml" 192.168.227.122
```

[/home/kali/Notes/Labs/medtech/192.168.227.122/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.122/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Jul 29 07:55:21 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/medtech/192.168.227.122/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/medtech/192.168.227.122/scans/xml/_top_100_udp_nmap.xml 192.168.227.122
Nmap scan report for 192.168.227.122
Host is up, received user-set (0.094s latency).
Scanned at 2024-07-29 07:55:22 EDT for 528s
Not shown: 94 open|filtered udp ports (no-response)
PORT      STATE  SERVICE        REASON              VERSION
19/udp    closed chargen        port-unreach ttl 61
69/udp    closed tftp           port-unreach ttl 61
593/udp   closed http-rpc-epmap port-unreach ttl 61
4444/udp  closed krb524         port-unreach ttl 61
49186/udp closed unknown        port-unreach ttl 61
49191/udp closed unknown        port-unreach ttl 61
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.18
OS details: Linux 2.6.18, Linux 2.6.30
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/29%OT=%CT=%CU=19%PV=Y%DS=4%DC=T%G=N%TM=66A7853A%P
OS:=x86_64-pc-linux-gnu)SEQ(II=I)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0
OS:%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=E5F5%RUD=G)I
OS:E(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops

TRACEROUTE (using port 49186/udp)
HOP RTT      ADDRESS
1   78.52 ms 192.168.45.1
2   78.19 ms 192.168.45.254
3   78.97 ms 192.168.251.1
4   79.31 ms 192.168.227.122

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 29 08:04:10 2024 -- 1 IP address (1 host up) scanned in 528.73 seconds

```
