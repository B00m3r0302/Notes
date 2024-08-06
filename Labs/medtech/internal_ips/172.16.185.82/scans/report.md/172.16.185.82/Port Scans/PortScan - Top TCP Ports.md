```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/xml/_quick_tcp_nmap.xml" 172.16.185.82
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:30:46 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.82/scans/xml/_quick_tcp_nmap.xml 172.16.185.82
Nmap scan report for 172.16.185.82
Host is up, received user-set (0.10s latency).
Scanned at 2024-07-31 12:30:46 EDT for 131s
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE       REASON         VERSION
135/tcp  open  msrpc         syn-ack ttl 64 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 64 Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack ttl 64
3389/tcp open  ms-wbt-server syn-ack ttl 64 Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: MEDTECH
|   NetBIOS_Domain_Name: MEDTECH
|   NetBIOS_Computer_Name: CLIENT01
|   DNS_Domain_Name: medtech.com
|   DNS_Computer_Name: CLIENT01.medtech.com
|   DNS_Tree_Name: medtech.com
|   Product_Version: 10.0.22000
|_  System_Time: 2024-07-31T16:32:17+00:00
|_ssl-date: 2024-07-31T16:32:56+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=CLIENT01.medtech.com
| Issuer: commonName=CLIENT01.medtech.com
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-03-27T17:51:36
| Not valid after:  2024-09-26T17:51:36
| MD5:   9743:a548:0c0b:e2e5:2e18:7b43:0001:0590
| SHA-1: 19ee:9922:08a3:66cd:5131:85da:1464:0b3a:9bca:f38a
| -----BEGIN CERTIFICATE-----
| MIIC7DCCAdSgAwIBAgIQHsNrvwlTSqJNpCcAGClo7TANBgkqhkiG9w0BAQsFADAf
| MR0wGwYDVQQDExRDTElFTlQwMS5tZWR0ZWNoLmNvbTAeFw0yNDAzMjcxNzUxMzZa
| Fw0yNDA5MjYxNzUxMzZaMB8xHTAbBgNVBAMTFENMSUVOVDAxLm1lZHRlY2guY29t
| MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8tXN5KHieP7QofCQlJnO
| FzR1qh5rPzLM1hi6GKUdwwDhQ6ve2q13GLh2a6Ht2UPfm468Bhi/kNL2Ul4pygOC
| ijoiyJGdgkHoTJCA6p7rfRfpQgkyowBmglfIzAm4CTyqp23gfhuHtF9gJmgQeS+F
| 6PD9Rs+lDbtHNRfWDZyBttiCeEe1VQxC9L+rlcJm0lnY5kCfv74/pd5H4l4ddnRp
| qhIN3sIX9Iyp45Awpt7I7ZGKweMBc7iVoUew0wva28ReNy9QzgbPaykXyTcwJKun
| XYC2GsPYoKhC9kTX05VXZr5DmveGXnFgcfyG1pCwleWkAlb6JHnjIKqQ2WYh1/tC
| kQIDAQABoyQwIjATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJ
| KoZIhvcNAQELBQADggEBACJHO5/xF5ccTlTq5D9x1Bjpf7g57vmo6rDDQviZ9pcZ
| 4rQcPSbGYiqqLNMtNz/QMhJG05pz1WKHCPDM/m5v/T23p9aJTMZ5QtDVdMm+molm
| 6o32Ib5NLezgVoSuf2DmT1JbmhaZtbt3SCuA021BTNqlhxS11VorvNOHKlccgJUG
| eMavduRT38pCWWi/wA9P7lSO0jvZJ5hUVNYlkbkf8hibiYikEUZTpO4e4L7a1mfM
| YBHvol1GKVoEnpzPdjSv/K/30qCiekM33h7YCGawbBd7wFoAUS0xqWKbGJsw+SlT
| qUe6WZOyjVTkP+2c9+5wdJBp3vu8xj0W8EU69BBpDug=
|_-----END CERTIFICATE-----
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=7/31%OT=135%CT=%CU=%PV=Y%G=N%TM=66AA6739%P=x86_64-pc-linux-gnu)
SEQ(SP=106%GCD=1%ISR=108%TI=I%CI=I%II=RI%TS=A)
SEQ(SP=106%GCD=1%ISR=108%TI=I%CI=I%II=RI%SS=S%TS=A)
OPS(O1=M5B4NNT11NW7%O2=M5B4NNT11NW7%O3=M5B4NNT11NW7%O4=M5B4NNT11NW7%O5=M5B4NNT11NW7%O6=M5B4NNT11)
WIN(W1=7200%W2=7200%W3=7200%W4=7200%W5=7200%W6=7200)
ECN(R=Y%DF=N%TG=40%W=7200%O=M5B4NW7%CC=N%Q=)
T1(R=Y%DF=N%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=Y%DF=N%TG=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)
T3(R=Y%DF=N%TG=40%W=7200%S=O%A=S+%F=AS%O=M5B4NNT11NW7%RD=0%Q=)
T4(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T6(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=N%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=S%TG=40%CD=S)

Uptime guess: 36.671 days (since Mon Jun 24 20:26:42 2024)
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: Incrementing by 2
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 46974/tcp): CLEAN (Timeout)
|   Check 2 (port 56816/tcp): CLEAN (Timeout)
|   Check 3 (port 20973/udp): CLEAN (Timeout)
|   Check 4 (port 46486/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-07-31T16:32:17
|_  start_date: N/A
| nbstat: NetBIOS name: CLIENT01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:0c:26 (VMware)
| Names:
|   CLIENT01<20>         Flags: <unique><active>
|   CLIENT01<00>         Flags: <unique><active>
|   MEDTECH<00>          Flags: <group><active>
| Statistics:
|   00:50:56:bf:0c:26:00:00:00:00:00:00:00:00:00:00:00
|   00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_  00:00:00:00:00:00:00:00:00:00:00:00:00:00
|_clock-skew: mean: -1s, deviation: 0s, median: -1s

TRACEROUTE
HOP RTT       ADDRESS
1   100.14 ms 172.16.185.82

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 12:32:57 2024 -- 1 IP address (1 host up) scanned in 131.30 seconds

```
