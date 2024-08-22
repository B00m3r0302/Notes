```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/xml/_top_100_udp_nmap.xml" 192.168.196.145
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:02:09 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/xml/_top_100_udp_nmap.xml 192.168.196.145
Nmap scan report for 192.168.196.145
Host is up, received user-set (0.66s latency).
Scanned at 2024-08-21 13:02:15 EDT for 2138s
Not shown: 99 open|filtered udp ports (no-response)
PORT    STATE SERVICE REASON               VERSION
161/udp open  snmp    udp-response ttl 125 SNMPv1 server (public)
| snmp-win32-users: 
|   Administrator
|   DefaultAccount
|   Guest
|   WDAGUtilityAccount
|   offsec
|_  zachary
|_snmp-win32-software: ERROR: Script execution failed (use -d to debug)
| snmp-sysdescr: Hardware: AMD64 Family 23 Model 1 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 19041 Multiprocessor Free)
|_  System uptime: 80d00h03m50.92s (691223092 timeticks)
| snmp-netstat: 
|   TCP  0.0.0.0:21           0.0.0.0:0
|   TCP  0.0.0.0:80           0.0.0.0:0
|   TCP  0.0.0.0:135          0.0.0.0:0
|   TCP  0.0.0.0:445          0.0.0.0:0
|   TCP  0.0.0.0:1978         0.0.0.0:0
|   TCP  0.0.0.0:3389         0.0.0.0:0
|   TCP  0.0.0.0:5040         0.0.0.0:0
|   TCP  0.0.0.0:49664        0.0.0.0:0
|   TCP  0.0.0.0:49665        0.0.0.0:0
|   TCP  0.0.0.0:49666        0.0.0.0:0
|   TCP  0.0.0.0:49667        0.0.0.0:0
|   TCP  0.0.0.0:49668        0.0.0.0:0
|   TCP  0.0.0.0:49669        0.0.0.0:0
|   TCP  0.0.0.0:49670        0.0.0.0:0
|   TCP  192.168.196.145:80   192.168.45.234:33838
|   TCP  192.168.196.145:80   192.168.45.234:33854
|   TCP  192.168.196.145:80   192.168.45.234:33856
|   TCP  192.168.196.145:80   192.168.45.234:33866
|   TCP  192.168.196.145:80   192.168.45.234:33874
|   UDP  0.0.0.0:161          *:*
|   UDP  0.0.0.0:2007         *:*
|   UDP  0.0.0.0:3389         *:*
|   UDP  0.0.0.0:5050         *:*
|   UDP  0.0.0.0:5353         *:*
|   UDP  0.0.0.0:5355         *:*
|   UDP  127.0.0.1:1900       *:*
|   UDP  127.0.0.1:62195      *:*
|   UDP  127.0.0.1:65442      *:*
|   UDP  192.168.196.145:137  *:*
|   UDP  192.168.196.145:138  *:*
|   UDP  192.168.196.145:1900 *:*
|_  UDP  192.168.196.145:65441 *:*
| snmp-win32-services: 
|   AVCTP service
|   CNG Key Isolation
|   COM+ Event System
|   Contact Data_66f74
|   CoreMessaging
|   Credential Manager
|   DHCP Client
|   DNS Client
|   Data Usage
|   IP Helper
|   IPsec Policy Agent
|   Plug and Play
|   Power
|   Print Spooler
|   SNMP Service
|   SSDP Discovery
|   Security Center
|   Server
|   Storage Service
|   Sync Host_66f74
|   SysMain
|   Task Scheduler
|   Themes
|   Time Broker
|   User Manager
|   VMware Tools
|   Windows Audio
|   Windows Event Log
|   Windows Search
|_  Workstation
| snmp-processes: 
|   1: 
|   4: 
|   92: 
|   368: 
|   460: 
|   468: 
|   472: 
|   572: 
|   580: 
|   664: 
|   700: 
|   704: 
|   712: 
|   820: 
|   828: 
|   836: 
|   904: 
|_  948: 
| snmp-interfaces: 
|   Software Loopback Interface 1\x00
|     IP address: 127.0.0.1  Netmask: 255.0.0.0
|   vmxnet3 Ethernet Adapter\x00
|_    IP address: 192.168.196.145  Netmask: 255.255.255.0
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=%CT=%CU=%PV=Y%DS=4%DC=T%G=N%TM=66C625F1%P=aarch64-unknown-linux-gnu)
SEQ()
U1(R=N)
IE(R=N)

Network Distance: 4 hops
Service Info: Host: oscp

TRACEROUTE (using port 161/udp)
HOP RTT       ADDRESS
1   124.53 ms 192.168.45.1
2   124.36 ms 192.168.45.254
3   125.17 ms 192.168.251.1
4   125.35 ms 192.168.196.145

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:37:53 2024 -- 1 IP address (1 host up) scanned in 2144.97 seconds

```
