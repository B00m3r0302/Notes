```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/reel/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/xml/_quick_tcp_nmap.xml" 10.10.10.77
```

[/home/kali/Notes/Labs/htb/reel/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/htb/reel/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 27 20:43:02 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/htb/reel/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/htb/reel/scans/xml/_quick_tcp_nmap.xml 10.10.10.77
Nmap scan report for 10.10.10.77
Host is up, received user-set (0.052s latency).
Scanned at 2025-01-27 20:43:02 EST for 583s
Not shown: 992 filtered tcp ports (no-response)
PORT      STATE SERVICE      REASON          VERSION
21/tcp    open  ftp          syn-ack ttl 127 Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_05-28-18  11:19PM       <DIR>          documents
22/tcp    open  ssh          syn-ack ttl 127 OpenSSH 7.6 (protocol 2.0)
| ssh-hostkey: 
|   2048 82:20:c3:bd:16:cb:a2:9c:88:87:1d:6c:15:59:ed:ed (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQkehAZGj87mZluxFiVu+GPAAnC/OQ9QKUF2wlIwvefrD2L4zWyGXlAgSbUq/MqujR/efrTIjPYWK+5Mlxc7gEoZBylGAPbdxFivL8YQs3dQPt6aHNF0v+ABS01L2qZ4ewd1sTi1TlT6LtWHehX2PBJ6S3LWG09v+E/3ue97y9gaOjfA6BCMWgQ7K3yvQeHrRpBSk/vQxfCh4TINwV3EGbGTfbs8VvvR+Et7weB5EOifgXfHbyh04KemONkceFSAnjRRYOgwvtXai9imsDJ8KtS2RMR197VK4MBhsY7+h0nOvUMgm76RcRc6N8GW1mn6gWp98Ds9VeymzAmQvprs97
|   256 23:2b:b8:0a:8c:1c:f4:4d:8d:7e:5e:64:58:80:33:45 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAw2CYanDlTRpGqzVXrfGTcAYVe/vUnnkWicQPzdfix5gFsv4nOGNUM+Fko7QAW0jqCFQKc8anGAwJjFGLTB00k=
|   256 ac:8b:de:25:1d:b7:d8:38:38:9b:9c:16:bf:f6:3f:ed (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICdDfn+n5xueGtHP20/aPkI8pvCfxb2UZA3RQdqnpjBk
25/tcp    open  smtp?        syn-ack ttl 127
| smtp-commands: REEL, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, SSLv23SessionReq, TLSSessionReq, X11Probe: 
|     220 Mail Service ready
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, RTSPRequest: 
|     220 Mail Service ready
|     sequence of commands
|     sequence of commands
|   Hello: 
|     220 Mail Service ready
|     EHLO Invalid domain address.
|   Help: 
|     220 Mail Service ready
|     DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
|   SIPOptions: 
|     220 Mail Service ready
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|   TerminalServerCookie: 
|     220 Mail Service ready
|_    sequence of commands
135/tcp   open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds syn-ack ttl 127 Windows Server 2012 R2 Standard 9600 microsoft-ds (workgroup: HTB)
593/tcp   open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49159/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port25-TCP:V=7.95%I=9%D=1/27%Time=67983637%P=x86_64-pc-linux-gnu%r(NULL
SF:,18,"220\x20Mail\x20Service\x20ready\r\n")%r(Hello,3A,"220\x20Mail\x20S
SF:ervice\x20ready\r\n501\x20EHLO\x20Invalid\x20domain\x20address\.\r\n")%
SF:r(Help,54,"220\x20Mail\x20Service\x20ready\r\n211\x20DATA\x20HELO\x20EH
SF:LO\x20MAIL\x20NOOP\x20QUIT\x20RCPT\x20RSET\x20SAML\x20TURN\x20VRFY\r\n"
SF:)%r(GenericLines,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\x20s
SF:equence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands\r
SF:\n")%r(GetRequest,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\x20
SF:sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands\
SF:r\n")%r(HTTPOptions,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\x
SF:20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20command
SF:s\r\n")%r(RTSPRequest,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad
SF:\x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20comma
SF:nds\r\n")%r(RPCCheck,18,"220\x20Mail\x20Service\x20ready\r\n")%r(DNSVer
SF:sionBindReqTCP,18,"220\x20Mail\x20Service\x20ready\r\n")%r(DNSStatusReq
SF:uestTCP,18,"220\x20Mail\x20Service\x20ready\r\n")%r(SSLSessionReq,18,"2
SF:20\x20Mail\x20Service\x20ready\r\n")%r(TerminalServerCookie,36,"220\x20
SF:Mail\x20Service\x20ready\r\n503\x20Bad\x20sequence\x20of\x20commands\r\
SF:n")%r(TLSSessionReq,18,"220\x20Mail\x20Service\x20ready\r\n")%r(SSLv23S
SF:essionReq,18,"220\x20Mail\x20Service\x20ready\r\n")%r(Kerberos,18,"220\
SF:x20Mail\x20Service\x20ready\r\n")%r(SMBProgNeg,18,"220\x20Mail\x20Servi
SF:ce\x20ready\r\n")%r(X11Probe,18,"220\x20Mail\x20Service\x20ready\r\n")%
SF:r(FourOhFourRequest,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\x
SF:20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20command
SF:s\r\n")%r(LPDString,18,"220\x20Mail\x20Service\x20ready\r\n")%r(LDAPSea
SF:rchReq,18,"220\x20Mail\x20Service\x20ready\r\n")%r(LDAPBindReq,18,"220\
SF:x20Mail\x20Service\x20ready\r\n")%r(SIPOptions,162,"220\x20Mail\x20Serv
SF:ice\x20ready\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad\
SF:x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20comman
SF:ds\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequenc
SF:e\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503\
SF:x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x2
SF:0commands\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad\x20
SF:sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands\
SF:r\n");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2012|2008|7 (97%)
OS CPE: cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_7
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows Server 2012 R2 (97%), Microsoft Windows 7 or Windows Server 2008 R2 (91%), Microsoft Windows Server 2012 or Windows Server 2012 R2 (89%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.95%E=4%D=1/27%OT=21%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=6798386D%P=x86_64-pc-linux-gnu)
SEQ(SP=100%GCD=1%ISR=10A%TI=I%II=I%SS=S%TS=7)
SEQ(SP=102%GCD=1%ISR=10F%TI=I%II=I%SS=S%TS=7)
OPS(O1=M53CNW8ST11%O2=M53CNW8ST11%O3=M53CNW8NNT11%O4=M53CNW8ST11%O5=M53CNW8ST11%O6=M53CST11)
WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=2000)
ECN(R=Y%DF=Y%TG=80%W=2000%O=M53CNW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Uptime guess: 0.393 days (since Mon Jan 27 11:26:55 2025)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: REEL; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-os-discovery: 
|   OS: Windows Server 2012 R2 Standard 9600 (Windows Server 2012 R2 Standard 6.3)
|   OS CPE: cpe:/o:microsoft:windows_server_2012::-
|   Computer name: REEL
|   NetBIOS computer name: REEL\x00
|   Domain name: HTB.LOCAL
|   Forest name: HTB.LOCAL
|   FQDN: REEL.HTB.LOCAL
|_  System time: 2025-01-28T01:52:06+00:00
| smb2-security-mode: 
|   3:0:2: 
|_    Message signing enabled and required
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
|_clock-skew: mean: 0s, deviation: 1s, median: -1s
| smb2-time: 
|   date: 2025-01-28T01:52:05
|_  start_date: 2025-01-27T16:27:13
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 24595/tcp): CLEAN (Timeout)
|   Check 2 (port 56197/tcp): CLEAN (Timeout)
|   Check 3 (port 32588/udp): CLEAN (Timeout)
|   Check 4 (port 41856/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE (using port 135/tcp)
HOP RTT      ADDRESS
1   51.12 ms 10.10.14.1
2   51.24 ms 10.10.10.77

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 27 20:52:45 2025 -- 1 IP address (1 host up) scanned in 582.88 seconds

```
