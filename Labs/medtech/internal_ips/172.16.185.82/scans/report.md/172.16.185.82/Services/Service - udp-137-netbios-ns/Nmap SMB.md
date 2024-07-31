```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/udp_137_smb_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/xml/udp_137_smb_nmap.xml" 172.16.185.82
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/udp_137_smb_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/udp_137_smb_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 13:08:16 2024 as: nmap -vv --reason -Pn -T4 -sU -sV -p 137 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/udp_137_smb_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/udp137/xml/udp_137_smb_nmap.xml 172.16.185.82
Nmap scan report for 172.16.185.82
Host is up, received user-set (0.26s latency).
Scanned at 2024-07-31 13:08:17 EDT for 0s

PORT    STATE SERVICE    REASON              VERSION
137/udp open  netbios-ns udp-response ttl 64 Microsoft Windows or Samba netbios-ns (workgroup: MEDTECH)
Service Info: Host: CLIENT01

Host script results:
| nbstat: NetBIOS name: CLIENT01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:0c:26 (VMware)
| Names:
|   CLIENT01<20>         Flags: <unique><active>
|   CLIENT01<00>         Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:0c:26:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 13:08:17 2024 -- 1 IP address (1 host up) scanned in 1.01 seconds

```
