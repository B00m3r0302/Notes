```bash
nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/flight/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Notes/Labs/htb/flight/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.11.187
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp139/tcp_139_smb_nmap.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp139/tcp_139_smb_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 18:21:21 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 139 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/flight/scans/tcp139/tcp_139_smb_nmap.txt -oX /home/kali/Notes/Labs/htb/flight/scans/tcp139/xml/tcp_139_smb_nmap.xml 10.10.11.187
Nmap scan report for 10.10.11.187
Host is up, received user-set (0.069s latency).
Scanned at 2025-01-13 18:21:22 EST for 41s

PORT    STATE SERVICE     REASON          VERSION
139/tcp open  netbios-ssn syn-ack ttl 127 Microsoft Windows netbios-ssn
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-capabilities: SMB: Couldn't find a NetBIOS name that works for the server. Sorry!
|_smb2-security-mode: SMB: Couldn't find a NetBIOS name that works for the server. Sorry!
|_smb-print-text: false
|_smb-mbenum: ERROR: Script execution failed (use -d to debug)
|_smb2-time: ERROR: Script execution failed (use -d to debug)
|_smb-protocols: No dialects accepted. Something may be blocking the responses
|_smb-vuln-ms10-061: SMB: Couldn't find a NetBIOS name that works for the server. Sorry!

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 18:22:03 2025 -- 1 IP address (1 host up) scanned in 42.16 seconds

```
