```bash
nmap -vv --reason -Pn -T4 -sV -p 3389 --script="banner,(rdp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/tcp_3389_rdp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/xml/tcp_3389_rdp_nmap.xml" 172.16.185.12
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/tcp_3389_rdp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/tcp_3389_rdp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:33:11 2024 as: nmap -vv --reason -Pn -T4 -sV -p 3389 "--script=banner,(rdp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/tcp_3389_rdp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp3389/xml/tcp_3389_rdp_nmap.xml 172.16.185.12
Nmap scan report for 172.16.185.12
Host is up, received user-set (0.16s latency).
Scanned at 2024-07-31 12:33:12 EDT for 45s

PORT     STATE SERVICE       REASON         VERSION
3389/tcp open  ms-wbt-server syn-ack ttl 64 Microsoft Terminal Services
| ssl-cert: Subject: commonName=DEV04.medtech.com
| Issuer: commonName=DEV04.medtech.com
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-03-27T16:42:35
| Not valid after:  2024-09-26T16:42:35
| MD5:   803b:ae23:b24f:09a9:eb0f:80ba:66ed:3cf9
| SHA-1: 44a6:ffb3:588c:eb5f:3cf8:6196:7eb1:dd34:939b:c0f5
| -----BEGIN CERTIFICATE-----
| MIIC5jCCAc6gAwIBAgIQJm901NTO1apHis4EZCIUTzANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDExFERVYwNC5tZWR0ZWNoLmNvbTAeFw0yNDAzMjcxNjQyMzVaFw0y
| NDA5MjYxNjQyMzVaMBwxGjAYBgNVBAMTEURFVjA0Lm1lZHRlY2guY29tMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvIFTa7TBQIlgDDYoq1gc3lduoG5e
| 8AtHjB7RxRLC/z0ZGeFKRhQBlspqwryL2R/3Br7q6DtyJ1swTNj0XH3IAmNYtm88
| mwDPTpLgFE/BCvFZJFcD8oFbtC2H7Xn0/S6rSYhkWif0qHGQjLLomrLv6gcy8C5W
| 47ozjcCq/ft/FFbbKojISztlQVxfclOzZZMIig/VBK5M062Vp8S9SVDgVCSZxHSx
| zkSLslgvWDcZ0je2i+t65jYdAy5s2n97ltk+xDk1oXRCYHFG2/XDc+q7UlGdHmj/
| +DjJ7P200J/03YC5jsGkEZBqAQUzLOWsejA5VPIY3mCkNi5x57um819MZQIDAQAB
| oyQwIjATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcN
| AQELBQADggEBAEv1jx+KhH2e7IGvTLGw7H0tfKUx+kGlyRlxY4CLxW/bjIpU6zAR
| H96GeI+EuIsDshIYAmb4WXWJm4aHAqxnTTYtBJyAtwS+OBKdVTMHwSW+o4RSKcnF
| e1tGc87UQLnSN63V8G3XQYmV0ktGiJbjctQRvmPq2AXhznzm41u9y0lytH/KxzYj
| SKnoBvlpm49DlkOILVgNpAdF9NLCeiZffpr9RVvC1eB29fQ/XxaHd77SQE+Ps8V3
| Pl22KglhAm/KgSVl3jpUVaVq0aFxZlSnwL/fMtjeE3kVLv0w70qIwbAKtY3A5XPJ
| SjI7zYEYzxh3m1hpV+zEGwVwUjEqcu2zpbA=
|_-----END CERTIFICATE-----
| rdp-ntlm-info: 
|   Target_Name: MEDTECH
|   NetBIOS_Domain_Name: MEDTECH
|   NetBIOS_Computer_Name: DEV04
|   DNS_Domain_Name: medtech.com
|   DNS_Computer_Name: DEV04.medtech.com
|   DNS_Tree_Name: medtech.com
|   Product_Version: 10.0.20348
|_  System_Time: 2024-07-31T16:33:19+00:00
| rdp-enum-encryption: 
|   Security layer
|     CredSSP (NLA): SUCCESS
|     CredSSP with Early User Auth: SUCCESS
|_    RDSTLS: SUCCESS
|_ssl-date: 2024-07-31T16:33:39+00:00; 0s from scanner time.
| ssl-enum-ciphers: 
|   TLSv1.0: 
|     ciphers: 
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp384r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
|     compressors: 
|       NULL
|     cipher preference: server
|     warnings: 
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|   TLSv1.1: 
|     ciphers: 
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp384r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
|     compressors: 
|       NULL
|     cipher preference: server
|     warnings: 
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|   TLSv1.2: 
|     ciphers: 
|       TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp384r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (dh 2048) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp384r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp384r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
|     compressors: 
|       NULL
|     cipher preference: server
|     warnings: 
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|_  least strength: C
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 12:33:57 2024 -- 1 IP address (1 host up) scanned in 45.64 seconds

```
