```bash
snmpwalk -c public -v 1 192.168.196.145 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk.txt):

```
iso.3.6.1.2.1.1.1.0 = STRING: "Hardware: AMD64 Family 23 Model 1 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 19041 Multiprocessor Free)"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.311.1.1.3.1.1
iso.3.6.1.2.1.1.3.0 = Timeticks: (691394759) 80 days, 0:32:27.59
iso.3.6.1.2.1.1.4.0 = STRING: "zachary"
iso.3.6.1.2.1.1.5.0 = STRING: "oscp"
iso.3.6.1.2.1.1.6.0 = STRING: "localhost"
iso.3.6.1.2.1.1.7.0 = INTEGER: 79
iso.3.6.1.2.1.2.1.0 = INTEGER: 23
iso.3.6.1.2.1.2.2.1.1.1 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.1.2 = INTEGER: 2
iso.3.6.1.2.1.2.2.1.1.3 = INTEGER: 3
iso.3.6.1.2.1.2.2.1.1.4 = INTEGER: 4
iso.3.6.1.2.1.2.2.1.1.5 = INTEGER: 5
iso.3.6.1.2.1.2.2.1.1.6 = INTEGER: 6
iso.3.6.1.2.1.2.2.1.1.7 = INTEGER: 7
iso.3.6.1.2.1.2.2.1.1.8 = INTEGER: 8
iso.3.6.1.2.1.2.2.1.1.9 = INTEGER: 9
iso.3.6.1.2.1.2.2.1.1.10 = INTEGER: 10
iso.3.6.1.2.1.2.2.1.1.11 = INTEGER: 11
iso.3.6.1.2.1.2.2.1.1.12 = INTEGER: 12
iso.3.6.1.2.1.2.2.1.1.13 = INTEGER: 13
iso.3.6.1.2.1.2.2.1.1.14 = INTEGER: 14
iso.3.6.1.2.1.2.2.1.1.15 = INTEGER: 15
iso.3.6.1.2.1.2.2.1.1.16 = INTEGER: 16
iso.3.6.1.2.1.2.2.1.1.17 = INTEGER: 17
iso.3.6.1.2.1.2.2.1.1.18 = INTEGER: 18
iso.3.6.1.2.1.2.2.1.1.19 = INTEGER: 19
iso.3.6.1.2.1.2.2.1.1.20 = INTEGER: 20
iso.3.6.1.2.1.2.2.1.1.21 = INTEGER: 21
iso.3.6.1.2.1.2.2.1.1.22 = INTEGER: 22
iso.3.6.1.2.1.2.2.1.1.23 = INTEGER: 23
iso.3.6.1.2.1.2.2.1.2.1 = Hex-STRING: 53 6F 66 74 77 61 72 65 20 4C 6F 6F 70 62 61 63
6B 20 49 6E 74 65 72 66 61 63 65 20 31 00
iso.3.6.1.2.1.2.2.1.2.2 = Hex-STRING: 4D 69 63 72 6F 73 6F 66 74 20 36 74 6F 34 20 41
64 61 70 74 65 72 00
iso.3.6.1.2.1.2.2.1.2.3 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 50 50
54 50 29 00
iso.3.6.1.2.1.2.2.1.2.4 = Hex-STRING: 4D 69 63 72 6F 73 6F 66 74 20 4B 65 72 6E 65 6C
20 44 65 62 75 67 20 4E 65 74 77 6F 72 6B 20 41
64 61 70 74 65 72 00
iso.3.6.1.2.1.2.2.1.2.5 = Hex-STRING: 4D 69 63 72 6F 73 6F 66 74 20 49 50 2D 48 54 54
50 53 20 50 6C 61 74 66 6F 72 6D 20 41 64 61 70
74 65 72 00
iso.3.6.1.2.1.2.2.1.2.6 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 49 50
76 36 29 00
iso.3.6.1.2.1.2.2.1.2.7 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 49 50
29 00
iso.3.6.1.2.1.2.2.1.2.8 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 4E 65
74 77 6F 72 6B 20 4D 6F 6E 69 74 6F 72 29 00
iso.3.6.1.2.1.2.2.1.2.9 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 4C 32
54 50 29 00
iso.3.6.1.2.1.2.2.1.2.10 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 50 50
50 4F 45 29 00
iso.3.6.1.2.1.2.2.1.2.11 = Hex-STRING: 4D 69 63 72 6F 73 6F 66 74 20 54 65 72 65 64 6F
20 54 75 6E 6E 65 6C 69 6E 67 20 41 64 61 70 74
65 72 00
iso.3.6.1.2.1.2.2.1.2.12 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 49 4B
45 76 32 29 00
iso.3.6.1.2.1.2.2.1.2.13 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 53 53
54 50 29 00
iso.3.6.1.2.1.2.2.1.2.14 = Hex-STRING: 76 6D 78 6E 65 74 33 20 45 74 68 65 72 6E 65 74
20 41 64 61 70 74 65 72 00
iso.3.6.1.2.1.2.2.1.2.15 = Hex-STRING: 76 6D 78 6E 65 74 33 20 45 74 68 65 72 6E 65 74
20 41 64 61 70 74 65 72 2D 57 46 50 20 4E 61 74
69 76 65 20 4D 41 43 20 4C 61 79 65 72 20 4C 69
67 68 74 57 65 69 67 68 74 20 46 69 6C 74 65 72
2D 30 30 30 30 00
iso.3.6.1.2.1.2.2.1.2.16 = Hex-STRING: 76 6D 78 6E 65 74 33 20 45 74 68 65 72 6E 65 74
20 41 64 61 70 74 65 72 2D 51 6F 53 20 50 61 63
6B 65 74 20 53 63 68 65 64 75 6C 65 72 2D 30 30
30 30 00
iso.3.6.1.2.1.2.2.1.2.17 = Hex-STRING: 76 6D 78 6E 65 74 33 20 45 74 68 65 72 6E 65 74
20 41 64 61 70 74 65 72 2D 57 46 50 20 38 30 32
2E 33 20 4D 41 43 20 4C 61 79 65 72 20 4C 69 67
68 74 57 65 69 67 68 74 20 46 69 6C 74 65 72 2D
30 30 30 30 00
iso.3.6.1.2.1.2.2.1.2.18 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 49 50
29 2D 57 46 50 20 4E 61 74 69 76 65 20 4D 41 43
20 4C 61 79 65 72 20 4C 69 67 68 74 57 65 69 67
68 74 20 46 69 6C 74 65 72 2D 30 30 30 30 00
iso.3.6.1.2.1.2.2.1.2.19 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 49 50
29 2D 51 6F 53 20 50 61 63 6B 65 74 20 53 63 68
65 64 75 6C 65 72 2D 30 30 30 30 00Timeout: No Response from 192.168.196.145

iso.3.6.1.2.1.2.2.1.2.20 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 49 50
76 36 29 2D 57 46 50 20 4E 61 74 69 76 65 20 4D
41 43 20 4C 61 79 65 72 20 4C 69 67 68 74 57 65
69 67 68 74 20 46 69 6C 74 65 72 2D 30 30 30 30
00
iso.3.6.1.2.1.2.2.1.2.21 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 49 50
76 36 29 2D 51 6F 53 20 50 61 63 6B 65 74 20 53
63 68 65 64 75 6C 65 72 2D 30 30 30 30 00
iso.3.6.1.2.1.2.2.1.2.22 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 4E 65
74 77 6F 72 6B 20 4D 6F 6E 69 74 6F 72 29 2D 57
46 50 20 4E 61 74 69 76 65 20 4D 41 43 20 4C 61
79 65 72 20 4C 69 67 68 74 57 65 69 67 68 74 20
46 69 6C 74 65 72 2D 30 30 30 30 00
iso.3.6.1.2.1.2.2.1.2.23 = Hex-STRING: 57 41 4E 20 4D 69 6E 69 70 6F 72 74 20 28 4E 65
74 77 6F 72 6B 20 4D 6F 6E 69 74 6F 72 29 2D 51
6F 53 20 50 61 63 6B 65 74 20 53 63 68 65 64 75
6C 65 72 2D 30 30 30 30 00


```
```bash
snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.1.6.0 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_system_processes.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_system_processes.txt):

```
Timeout: No Response from 192.168.196.145


```
```bash
snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.4.2.1.2 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_running_processes.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_running_processes.txt):

```
Timeout: No Response from 192.168.196.145
iso.3.6.1.2.1.25.4.2.1.2.1 = STRING: "System Idle Process"
iso.3.6.1.2.1.25.4.2.1.2.4 = STRING: "System"
iso.3.6.1.2.1.25.4.2.1.2.92 = STRING: "Registry"
iso.3.6.1.2.1.25.4.2.1.2.368 = STRING: "smss.exe"
iso.3.6.1.2.1.25.4.2.1.2.460 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.468 = STRING: "csrss.exe"
iso.3.6.1.2.1.25.4.2.1.2.472 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.572 = STRING: "wininit.exe"
iso.3.6.1.2.1.25.4.2.1.2.580 = STRING: "csrss.exe"
iso.3.6.1.2.1.25.4.2.1.2.664 = STRING: "winlogon.exe"
iso.3.6.1.2.1.25.4.2.1.2.700 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.704 = STRING: "services.exe"
iso.3.6.1.2.1.25.4.2.1.2.712 = STRING: "lsass.exe"
iso.3.6.1.2.1.25.4.2.1.2.820 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.828 = STRING: "fontdrvhost.exe"
iso.3.6.1.2.1.25.4.2.1.2.836 = STRING: "fontdrvhost.exe"
iso.3.6.1.2.1.25.4.2.1.2.904 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.948 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1000 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1084 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1156 = STRING: "vm3dservice.exe"
iso.3.6.1.2.1.25.4.2.1.2.1196 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1212 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1224 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1288 = STRING: "Memory Compression"
iso.3.6.1.2.1.25.4.2.1.2.1340 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1428 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1444 = STRING: "dwm.exe"
iso.3.6.1.2.1.25.4.2.1.2.1456 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1464 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1484 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1504 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1592 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1600 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1624 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1636 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1760 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1776 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1892 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1916 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1932 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1948 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.1996 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2008 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2104 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2136 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2200 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2232 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2240 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2248 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2296 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2300 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2348 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2440 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2476 = STRING: "spoolsv.exe"
iso.3.6.1.2.1.25.4.2.1.2.2524 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2568 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2604 = STRING: "vmtoolsd.exe"
iso.3.6.1.2.1.25.4.2.1.2.2616 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2672 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2688 = STRING: "snmp.exe"
iso.3.6.1.2.1.25.4.2.1.2.2800 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2844 = STRING: "MsMpEng.exe"
iso.3.6.1.2.1.25.4.2.1.2.2876 = STRING: "VGAuthService.exe"
iso.3.6.1.2.1.25.4.2.1.2.2912 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2924 = STRING: "svchost.exe"
iso.3.6.1.2.1.25.4.2.1.2.2936 = STRING: "svchost.exe"


```
```bash
snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.4.2.1.4 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_process_paths.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_process_paths.txt):

```
Timeout: No Response from 192.168.196.145
iso.3.6.1.2.1.25.4.2.1.4.1 = ""
iso.3.6.1.2.1.25.4.2.1.4.4 = ""
iso.3.6.1.2.1.25.4.2.1.4.92 = ""
iso.3.6.1.2.1.25.4.2.1.4.368 = ""
iso.3.6.1.2.1.25.4.2.1.4.460 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.468 = ""
iso.3.6.1.2.1.25.4.2.1.4.472 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.572 = ""
iso.3.6.1.2.1.25.4.2.1.4.580 = ""
iso.3.6.1.2.1.25.4.2.1.4.664 = ""
iso.3.6.1.2.1.25.4.2.1.4.700 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.704 = ""
iso.3.6.1.2.1.25.4.2.1.4.712 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.820 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.828 = ""
iso.3.6.1.2.1.25.4.2.1.4.836 = ""
iso.3.6.1.2.1.25.4.2.1.4.904 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.948 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1000 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1084 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1156 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1196 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1212 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1224 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.1288 = ""
iso.3.6.1.2.1.25.4.2.1.4.1340 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1428 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.1444 = ""
iso.3.6.1.2.1.25.4.2.1.4.1456 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1464 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1484 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.1504 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.1592 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.1600 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1624 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1636 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1760 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1776 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1892 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1916 = STRING: "C:\\WINDOWS\\System32\\"
iso.3.6.1.2.1.25.4.2.1.4.1932 = STRING: "C:\\WINDOWS\\system32\\"
iso.3.6.1.2.1.25.4.2.1.4.1948 = STRING: "C:\\WINDOWS\\system32\\"


```
```bash
snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.2.3.1.4 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_storage_units.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_storage_units.txt):

```
Timeout: No Response from 192.168.196.145
iso.3.6.1.2.1.25.2.3.1.4.1 = INTEGER: 4096
iso.3.6.1.2.1.25.2.3.1.4.2 = INTEGER: 0
iso.3.6.1.2.1.25.2.3.1.4.3 = INTEGER: 65536


```
```bash
snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.2.3.1.4 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_software_names.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_software_names.txt):

```
Timeout: No Response from 192.168.196.145


```
```bash
snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.4.1.77.1.2.25 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_user_accounts.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_user_accounts.txt):

```
iso.3.6.1.4.1.77.1.2.25.1.1.5.71.117.101.115.116 = STRING: "Guest"
iso.3.6.1.4.1.77.1.2.25.1.1.6.111.102.102.115.101.99 = STRING: "offsec"
iso.3.6.1.4.1.77.1.2.25.1.1.7.122.97.99.104.97.114.121 = STRING: "zachary"
iso.3.6.1.4.1.77.1.2.25.1.1.13.65.100.109.105.110.105.115.116.114.97.116.111.114 = STRING: "Administrator"
iso.3.6.1.4.1.77.1.2.25.1.1.14.68.101.102.97.117.108.116.65.99.99.111.117.110.116 = STRING: "DefaultAccount"
iso.3.6.1.4.1.77.1.2.25.1.1.18.87.68.65.71.85.116.105.108.105.116.121.65.99.99.111.117.110.116 = STRING: "WDAGUtilityAccount"


```
```bash
snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.6.13.1.3 2>&1
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_tcp_ports.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/udp161/udp_161_snmp_snmpwalk_tcp_ports.txt):

```
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.21.0.0.0.0.0 = INTEGER: 21
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.80.0.0.0.0.0 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.135.0.0.0.0.0 = INTEGER: 135
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.445.0.0.0.0.0 = INTEGER: 445
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.1978.0.0.0.0.0 = INTEGER: 1978
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.3389.0.0.0.0.0 = INTEGER: 3389
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.5040.0.0.0.0.0 = INTEGER: 5040
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.49664.0.0.0.0.0 = INTEGER: 49664
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.49665.0.0.0.0.0 = INTEGER: 49665
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.49666.0.0.0.0.0 = INTEGER: 49666
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.49667.0.0.0.0.0 = INTEGER: 49667
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.49668.0.0.0.0.0 = INTEGER: 49668
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.49669.0.0.0.0.0 = INTEGER: 49669
iso.3.6.1.2.1.6.13.1.3.0.0.0.0.49670.0.0.0.0.0 = INTEGER: 49670
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.21.192.168.45.234.34371 = INTEGER: 21
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.21.192.168.45.234.34372 = INTEGER: 21
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.21.192.168.45.234.34373 = INTEGER: 21
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60038 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60042 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60046 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60048 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60066 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60068 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60072 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60076 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60086 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60102 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60114 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60128 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60144 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60150 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60156 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60164 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.80.192.168.45.234.60170 = INTEGER: 80
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.135.192.168.45.234.37148 = INTEGER: 135
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.135.192.168.45.234.60054 = INTEGER: 135
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.139.0.0.0.0.0 = INTEGER: 139
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.139.192.168.45.234.34954 = INTEGER: 139
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.139.192.168.45.234.44554 = INTEGER: 139
iso.3.6.1.2.1.6.13.1.3.192.168.196.145.60782.52.226.139.121.443 = INTEGER: 60782


```
