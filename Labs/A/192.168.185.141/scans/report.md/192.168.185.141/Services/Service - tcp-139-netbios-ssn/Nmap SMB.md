```bash
nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/xml/tcp_139_smb_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/tcp_139_smb_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/tcp_139_smb_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:09:33 2024 as: nmap -vv --reason -Pn -T4 -sV -p 139 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/tcp_139_smb_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/xml/tcp_139_smb_nmap.xml 192.168.185.141
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.073s latency).
Scanned at 2024-08-05 22:09:35 EDT for 41s

PORT    STATE SERVICE     REASON          VERSION
139/tcp open  netbios-ssn syn-ack ttl 125 Microsoft Windows netbios-ssn
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-protocols: No dialects accepted. Something may be blocking the responses
|_smb-mbenum: ERROR: Script execution failed (use -d to debug)
|_smb2-capabilities: SMB: Couldn't find a NetBIOS name that works for the server. Sorry!
|_smb-vuln-ms10-061: SMB: Couldn't find a NetBIOS name that works for the server. Sorry!
|_smb-print-text: false
|_smb2-time: ERROR: Script execution failed (use -d to debug)
|_smb2-security-mode: SMB: Couldn't find a NetBIOS name that works for the server. Sorry!

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:10:16 2024 -- 1 IP address (1 host up) scanned in 43.76 seconds

```