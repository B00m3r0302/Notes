```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 161 --script="banner,(snmp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp-nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/xml/udp_161_snmp_nmap.xml" 192.168.196.145
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp-nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp-nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:38:06 2024 as: nmap -vv --reason -Pn -T4 -sU -sV -p 161 "--script=banner,(snmp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp-nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/xml/udp_161_snmp_nmap.xml 192.168.196.145
Nmap scan report for 192.168.196.145
Host is up, received user-set (0.35s latency).
Scanned at 2024-08-21 13:38:11 EDT for 52s

Bug in snmp-win32-software: no string output.
PORT    STATE SERVICE REASON               VERSION
161/udp open  snmp    udp-response ttl 125 SNMPv1 server (public)
| snmp-win32-users: 
|   Administrator
|   DefaultAccount
|   Guest
|   WDAGUtilityAccount
|   offsec
|_  zachary
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
|   948: 
|   1000: 
|   1084: 
|   1156: 
|   1196: 
|   1212: 
|   1224: 
|   1288: 
|   1340: 
|   1428: 
|   1444: 
|   1456: 
|   1464: 
|   1484: 
|   1504: 
|   1592: 
|   1600: 
|   1624: 
|   1636: 
|   1760: 
|   1776: 
|   1892: 
|   1916: 
|   1932: 
|   1948: 
|_  1996: 
| snmp-win32-services: 
|   AVCTP service
|   Base Filtering Engine
|   CNG Key Isolation
|   COM+ Event System
|   Contact Data_66f74
|   CoreMessaging
|   Credential Manager
|   Cryptographic Services
|   DHCP Client
|   DNS Client
|   Data Sharing Service
|   Data Usage
|   Device Setup Manager
|   IP Helper
|   IPsec Policy Agent
|   Local Session Manager
|   Microsoft FTP Service
|   Network Connections
|   Network List Service
|   Plug and Play
|   Power
|   Print Spooler
|   RPC Endpoint Mapper
|   SNMP Service
|   SSDP Discovery
|   Security Center
|   Server
|   Storage Service
|   Sync Host_66f74
|   SysMain
|   System Events Broker
|   TCP/IP NetBIOS Helper
|   Task Scheduler
|   Themes
|   Time Broker
|   User Manager
|   User Profile Service
|   VMware Tools
|   Web Account Manager
|   Windows Audio
|   Windows Event Log
|   Windows Search
|_  Workstation
| snmp-sysdescr: Hardware: AMD64 Family 23 Model 1 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 19041 Multiprocessor Free)
|_  System uptime: 80d00h32m32.69s (691395269 timeticks)
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
|   UDP  0.0.0.0:161          *:*
|   UDP  0.0.0.0:2007         *:*
|_  UDP  0.0.0.0:3389         *:*
Service Info: Host: oscp

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:39:04 2024 -- 1 IP address (1 host up) scanned in 58.48 seconds

```
