```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/xml/_full_tcp_nmap.xml" 192.168.196.143
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/xml/_full_tcp_nmap.xml 192.168.196.143
Nmap scan report for 192.168.196.143
Host is up, received user-set (0.49s latency).
Scanned at 2024-08-21 13:00:02 EDT for 1385s
Not shown: 65525 filtered tcp ports (no-response)
PORT     STATE SERVICE    REASON         VERSION
21/tcp   open  ftp        syn-ack ttl 61 vsftpd 3.0.3
22/tcp   open  ssh        syn-ack ttl 61 OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 23:4c:6f:ff:b8:52:29:65:3d:d1:4e:38:eb:fe:01:c1 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCi/7Md8C4Np6BJgxvw5Jb8jJ+RYx+s7Wc7jWxTHhTMURFOTc6HH2XC0rvbZukvws+KficflBsI/B7RVgY454RK1NOGOqVd5FSIY3qol4MGH2/Sq03mfjcc8aMgni5OZd2DNZY7e8auGa3fDOci6PXOZaYxwwjn52Vt/iNZu8sAv3rf1sRLAikvk5fGlEbxLu1+zXDCySqP0IgeR+i7JcWUp8+xiwp2ZmURcAsFkM0TBm07MJKD+T+zPru2YxvsICXMMG37rV22KFqmk2p/8PF18WUqJpDPnPYEKZwGjbxa71STgQfUcFXeXU9QX3ofz/g0ZpxEg8wk2O9fNvYdZ454isgPWtxhHe9wii18eq4DBizwfHao1OI8iKpPbkQlrKmOrPqU55LXJR84n68cCPp8yH8Pd8Mv+AzV+9h0/u72XB/0AaFcgT5u7SnGoiTrx5e2eMzI+lFkm5xY+KJw5ZvTaC3MnD3LJugV6axmAH+9L6LDrLV8dkLq6kV8KpS9Ej0=
|   256 0d:fd:36:d8:05:69:83:ef:ae:a0:fe:4b:82:03:32:ed (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLKaSNQY+Y3BFhxGXMm8uTdQnXJ1VbZEwFMoa1MUkYgu0vSwafvy6ffXVglWIlroS4axopq6HkpSA+2wnjp2E8s=
|   256 cc:76:17:1e:8e:c5:57:b2:1f:45:28:09:05:5a:eb:39 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC3D5QMyrcUNcOicavOsnzna2L1/Fg2N7w7okmegpssB
80/tcp   open  http       syn-ack ttl 61 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: HEAD POST OPTIONS
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.41 (Ubuntu)
81/tcp   open  http       syn-ack ttl 61 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Test Page for the Nginx HTTP Server on Fedora
443/tcp  open  http       syn-ack ttl 61 Apache httpd 2.4.41
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
3000/tcp open  ppp?       syn-ack ttl 61
3001/tcp open  nessus?    syn-ack ttl 61
3003/tcp open  cgms?      syn-ack ttl 61
3306/tcp open  mysql      syn-ack ttl 61 MySQL (unauthorized)
5432/tcp open  postgresql syn-ack ttl 61 PostgreSQL DB 9.6.0 or later
| fingerprint-strings: 
|   Kerberos: 
|     SFATAL
|     VFATAL
|     C0A000
|     Munsupported frontend protocol 27265.28208: server supports 2.0 to 3.0
|     Fpostmaster.c
|     L2113
|     RProcessStartupPacket
|   SMBProgNeg: 
|     SFATAL
|     VFATAL
|     C0A000
|     Munsupported frontend protocol 65363.19778: server supports 2.0 to 3.0
|     Fpostmaster.c
|     L2113
|     RProcessStartupPacket
|   ZendJavaBridge: 
|_    EFATAL: unsupported frontend protocol 0.0: server supports 2.0 to 3.0
| ssl-cert: Subject: commonName=aero
| Subject Alternative Name: DNS:aero
| Issuer: commonName=aero
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-05-10T22:20:48
| Not valid after:  2031-05-08T22:20:48
| MD5:   0cbe:58c4:2d38:4109:72c9:e3c4:fe39:ca8d
| SHA-1: ad85:4984:c180:ba73:e010:83f8:c44f:18b9:d176:2fd8
| -----BEGIN CERTIFICATE-----
| MIICyjCCAbKgAwIBAgIUUhXFOA5R7/D70TfWErlFqDzV4qcwDQYJKoZIhvcNAQEL
| BQAwDzENMAsGA1UEAwwEYWVybzAeFw0yMTA1MTAyMjIwNDhaFw0zMTA1MDgyMjIw
| NDhaMA8xDTALBgNVBAMMBGFlcm8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
| AoIBAQC+NK0VFeRa53b9bPj/fQnkDeN7CTVCPozCfNAO+gJ5EY7IN8F6bzVzY1Y9
| Mz69ffZqvU8Ye311NehHdfR4zboP2dy1kdwNsBpPTjzkOOUHCTeI0U8F/RGws0Gp
| hBWImghgHa+7h2TH7rjt7IsXBsMDOQF39+E4gyQorFkuJ3wBrxJrVkY3ZBzNFD2r
| 11Olh3zX+zLi8/NvrQGh3MNC2yrjRBvPPfmijul/Y1ekDLJzBnWa+YwddfnuL27E
| 3OFZpFGXs3OCo4rBYHBhovfH9fYaU1epOPbz5ms0cdW6ISrmOvYeCL2mP6vTOA66
| y7DnL0op7sst6uORHV3KwTosjQZvAgMBAAGjHjAcMAkGA1UdEwQCMAAwDwYDVR0R
| BAgwBoIEYWVybzANBgkqhkiG9w0BAQsFAAOCAQEArU2QhS00+7OedCclrx+Tktu4
| kV3Z26wzHvTl0TXaoQPK+8MsZMPKcgf9QWGJoaIXynlQ49UZv6ePe0ZQiPxTqJoK
| Blz8NOfCZQz8Dg4/PBHXBRU42rSsZHbah4B44sDhzSVBJX+V8HIyR7gCYjuuRo/E
| hEXHW5evojRmajVg90vtDkBwSzVRbiorF8WRpTnWNyLeQlZ/qa/DQK5DvdKwOfNO
| fSNhUu1u6yCIX9zJjVigxoNqvV+d18qZauUQ+jNuSu7NWG1WEyGaBEFB2PQwAh7I
| fkzb++Msr8hanm/ts+atP6mqaWgoFTlKVpOoXAPibTvEqhYeZqMDCmc9/TTA/Q==
|_-----END CERTIFICATE-----
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3003-TCP:V=7.94SVN%I=9%D=8/21%Time=66C62019%P=aarch64-unknown-linux
SF:-gnu%r(GenericLines,1,"\n")%r(GetRequest,1,"\n")%r(HTTPOptions,1,"\n")%
SF:r(RTSPRequest,1,"\n")%r(Hello,1,"\n")%r(Help,1,"\n")%r(SSLSessionReq,1,
SF:"\n")%r(TerminalServerCookie,1,"\n")%r(SSLv23SessionReq,1,"\n")%r(Kerbe
SF:ros,1,"\n")%r(FourOhFourRequest,1,"\n")%r(LPDString,1,"\n")%r(LDAPSearc
SF:hReq,1,"\n")%r(SIPOptions,1,"\n")%r(NessusTPv12,1,"\n")%r(NessusTPv11,1
SF:,"\n")%r(NessusTPv10,1,"\n")%r(mydoom,1,"\n")%r(WWWOFFLEctrlstat,1,"\n"
SF:)%r(Verifier,1,"\n")%r(VerifierAdvanced,1,"\n")%r(Socks5,1,"\n")%r(Offi
SF:ceScan,1,"\n")%r(HELP4STOMP,1,"\n")%r(Memcache,1,"\n")%r(firebird,1,"\n
SF:")%r(ajp,1,"\n")%r(hp-pjl,1,"\n")%r(SqueezeCenter_CLI,1,"\n")%r(dominoc
SF:onsole,1,"\n")%r(apple-iphoto,1,"\n")%r(metasploit-xmlrpc,1,"\n")%r(red
SF:is-server,1,"\n")%r(tarantool,1,"\n")%r(metasploit-msgrpc,1,"\n")%r(haz
SF:elcast-http,1,"\n")%r(teamspeak-tcpquery-ver,1,"\n")%r(xmlsysd,1,"\n")%
SF:r(docker,1,"\n")%r(TLS-PSK,1,"\n")%r(niagara-fox,1,"\n")%r(NoMachine,1,
SF:"\n")%r(JMON,1,"\n")%r(LibreOfficeImpressSCPair,1,"\n")%r(LSCP,1,"\n")%
SF:r(rotctl,1,"\n")%r(SharpTV,1,"\n")%r(piholeVersion,1,"\n")%r(teamtalk-l
SF:ogin,1,"\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5432-TCP:V=7.94SVN%I=9%D=8/21%Time=66C62016%P=aarch64-unknown-linux
SF:-gnu%r(SMBProgNeg,8C,"E\0\0\0\x8bSFATAL\0VFATAL\0C0A000\0Munsupported\x
SF:20frontend\x20protocol\x2065363\.19778:\x20server\x20supports\x202\.0\x
SF:20to\x203\.0\0Fpostmaster\.c\0L2113\0RProcessStartupPacket\0\0")%r(Kerb
SF:eros,8C,"E\0\0\0\x8bSFATAL\0VFATAL\0C0A000\0Munsupported\x20frontend\x2
SF:0protocol\x2027265\.28208:\x20server\x20supports\x202\.0\x20to\x203\.0\
SF:0Fpostmaster\.c\0L2113\0RProcessStartupPacket\0\0")%r(ZendJavaBridge,48
SF:,"EFATAL:\x20\x20unsupported\x20frontend\x20protocol\x200\.0:\x20server
SF:\x20supports\x202\.0\x20to\x203\.0\n\0");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=21%CT=%CU=%PV=Y%DS=4%DC=T%G=N%TM=66C6227B%P=aarch64-unknown-linux-gnu)
SEQ(SP=104%GCD=1%ISR=10B%TI=Z%TS=A)
SEQ(SP=104%GCD=2%ISR=10B%TI=Z%TS=A)
OPS(O1=M551ST11NW8%O2=M551ST11NW8%O3=M551NNT11NW8%O4=M551ST11NW8%O5=M551ST11NW8%O6=M551ST11)
WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)
ECN(R=Y%DF=Y%TG=40%W=FAF0%O=M551NNSNW8%CC=Y%Q=)
T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Uptime guess: 30.871 days (since Sun Jul 21 16:29:05 2024)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Host: 127.0.0.2; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 3306/tcp)
HOP RTT       ADDRESS
1   469.16 ms 192.168.45.1
2   469.13 ms 192.168.45.254
3   469.21 ms 192.168.251.1
4   469.29 ms 192.168.196.143

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:23:07 2024 -- 1 IP address (1 host up) scanned in 1386.81 seconds

```
