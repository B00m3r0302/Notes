```bash
nmap -vv --reason -Pn -T4 -sV -p 443 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/xml/tcp_443_https_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:21:29 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 443 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp443/tcp_443_https_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp443/xml/tcp_443_https_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.055s latency).
Scanned at 2025-02-11 10:21:29 EST for 681s

PORT    STATE SERVICE  REASON          VERSION
443/tcp open  ssl/http syn-ack ttl 127 Microsoft IIS httpd 10.0
|_http-title: Site doesn't have a title (text/html).
|_ssl-date: 2025-02-11T15:32:41+00:00; -1s from scanner time.
| ssl-enum-ciphers: 
|   TLSv1.0: 
|     ciphers: 
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_RSA_WITH_RC4_128_SHA (rsa 2048) - C
|       TLS_RSA_WITH_RC4_128_MD5 (rsa 2048) - C
|     compressors: 
|       NULL
|     cipher preference: server
|     warnings: 
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|       Broken cipher RC4 is deprecated by RFC 7465
|       Ciphersuite uses MD5 for message integrity
|   TLSv1.1: 
|     ciphers: 
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_RSA_WITH_RC4_128_SHA (rsa 2048) - C
|       TLS_RSA_WITH_RC4_128_MD5 (rsa 2048) - C
|     compressors: 
|       NULL
|     cipher preference: server
|     warnings: 
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|       Broken cipher RC4 is deprecated by RFC 7465
|       Ciphersuite uses MD5 for message integrity
|   TLSv1.2: 
|     ciphers: 
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (dh 2048) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 2048) - A
|       TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_RSA_WITH_RC4_128_SHA (rsa 2048) - C
|       TLS_RSA_WITH_RC4_128_MD5 (rsa 2048) - C
|     compressors: 
|       NULL
|     cipher preference: server
|     warnings: 
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|       Broken cipher RC4 is deprecated by RFC 7465
|       Ciphersuite uses MD5 for message integrity
|_  least strength: C
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-date: Tue, 11 Feb 2025 15:21:57 GMT; 0s from local time.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-vhosts: 
|_128 names had status 200
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|     /images/
|       gif: 1
|   Longest directory structure:
|     Depth: 1
|     Dir: /images/
|   Total files found (by extension):
|_    Other: 1; gif: 1
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-feed: Couldn't find any feeds.
| http-php-version: Logo query returned unknown hash 4dbbfe6aa4e77727db30e3fd5d6ed2f0
|_Credits query returned unknown hash 4dbbfe6aa4e77727db30e3fd5d6ed2f0
|_http-chrono: Request times for /; avg: 305.25ms; min: 301.95ms; max: 309.87ms
|_http-devframework: ASP.NET detected. Found related header.
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-comments-displayer: Couldn't find any comments.
| http-security-headers: 
|   Strict_Transport_Security: 
|_    HSTS not configured in HTTPS Server
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-errors: Couldn't find any error pages.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| ssl-cert: Subject: commonName=sizzle.htb.local
| Issuer: commonName=HTB-SIZZLE-CA/domainComponent=HTB
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2018-07-03T17:58:55
| Not valid after:  2020-07-02T17:58:55
| MD5:   240b:1eff:5a65:ad8d:c64d:855e:aeb5:9e6b
| SHA-1: 77bb:3f67:1b6b:3e09:b8f9:6503:ddc1:0bbf:0b75:0c72
| -----BEGIN CERTIFICATE-----
| MIIFPTCCBCWgAwIBAgITaQAAAAXvru32D6T3IQAAAAAABTANBgkqhkiG9w0BAQsF
| ADBEMRUwEwYKCZImiZPyLGQBGRYFTE9DQUwxEzARBgoJkiaJk/IsZAEZFgNIVEIx
| FjAUBgNVBAMTDUhUQi1TSVpaTEUtQ0EwHhcNMTgwNzAzMTc1ODU1WhcNMjAwNzAy
| MTc1ODU1WjAbMRkwFwYDVQQDExBzaXp6bGUuaHRiLmxvY2FsMIIBIjANBgkqhkiG
| 9w0BAQEFAAOCAQ8AMIIBCgKCAQEAogsEbJGsO9cNsHH5GLS45qckSAP0UrNRszgZ
| R10DbNB3vV7hSciCIhlo/Mu7MhrtuB4IKtWp5O31vq5kPwO0xV2jfNtO6MH2c7iG
| PH9Ix0mTFLqDN9DYjdWUIjhMatiVHtdQmMs1+xCIROPXGVs3U3IxyfLXrkRniu6s
| lnvGaRn3XTEVr6JHUoLWCws0+C2MmZHFZs5V5NVLmP00QLtR7hDm9lrV1ehvCW5O
| xAVFp95z0+mgwpAatG2UYfsjiydYXBhi1zLa/yvXOkYROJC/A2OakNlUESAplsPl
| 00SaS02NpfaRwj/VnfEuRs1k0LkbTCvEXVsGhIGxjqFhGvsr6QIDAQABo4ICTzCC
| AkswPAYJKwYBBAGCNxUHBC8wLQYlKwYBBAGCNxUI5pJfgvm/E4epnz7ahB+Br/MJ
| gWCD/sNihcXjWQIBZAIBBDATBgNVHSUEDDAKBggrBgEFBQcDATAOBgNVHQ8BAf8E
| BAMCBaAwGwYJKwYBBAGCNxUKBA4wDDAKBggrBgEFBQcDATAdBgNVHQ4EFgQUXPQP
| a29/mSK4aX3p1g/auVJ8R2cwHwYDVR0jBBgwFoAUQAbkVLM3mLwiLg4ZNgoYoLHe
| C4owgcgGA1UdHwSBwDCBvTCBuqCBt6CBtIaBsWxkYXA6Ly8vQ049SFRCLVNJWlpM
| RS1DQSxDTj1zaXp6bGUsQ049Q0RQLENOPVB1YmxpYyUyMEtleSUyMFNlcnZpY2Vz
| LENOPVNlcnZpY2VzLENOPUNvbmZpZ3VyYXRpb24sREM9SFRCLERDPUxPQ0FMP2Nl
| cnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFzcz1jUkxEaXN0
| cmlidXRpb25Qb2ludDCBvQYIKwYBBQUHAQEEgbAwga0wgaoGCCsGAQUFBzAChoGd
| bGRhcDovLy9DTj1IVEItU0laWkxFLUNBLENOPUFJQSxDTj1QdWJsaWMlMjBLZXkl
| MjBTZXJ2aWNlcyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPUhUQixE
| Qz1MT0NBTD9jQUNlcnRpZmljYXRlP2Jhc2U/b2JqZWN0Q2xhc3M9Y2VydGlmaWNh
| dGlvbkF1dGhvcml0eTANBgkqhkiG9w0BAQsFAAOCAQEAFaiP/3IAxom3OvWWMrsE
| jR2AV7qiLZw39AxTsYRVERC011TMTV5DBzScb1dA6ne4Su0EEzetNkqmWdOHqJbx
| tQuZYcD/CBfVAveKdLCEGh3gONk8sY+gnbJ7J3hucHIWtjamq+Kys2qXMRWSikkS
| jG4txpZTg5nXlWvV0U2E8RdKjmFuolfPvrIMEuyzdq/0Cw+xhJfiLD67obIP+EmF
| FbKnTQiGAipk0dIsHN6ckA6l3IXm1M5kqKfj4bXASLN49SvBVKOGcuKVam/0zLdR
| 8E+4FEEjhjQPdbLkSof1KnO23fiO+T2uZjLcKDMdO6griGwDwpBkORV0vatQbpi0
| QQ==
|_-----END CERTIFICATE-----
|_http-server-header: Microsoft-IIS/10.0
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-headers: 
|   Content-Length: 60
|   Content-Type: text/html
|   Last-Modified: Thu, 12 Jul 2018 17:39:25 GMT
|   Accept-Ranges: bytes
|   ETag: "56f2784671ad41:0"
|   Server: Microsoft-IIS/10.0
|   X-Powered-By: ASP.NET
|   Date: Tue, 11 Feb 2025 15:21:55 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-malware-host: Host appears to be clean
|_http-mobileversion-checker: No mobile version detected.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:32:50 2025 -- 1 IP address (1 host up) scanned in 681.21 seconds

```
