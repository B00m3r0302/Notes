```bash
nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sizzle/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp389/tcp_389_ldap_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp389/tcp_389_ldap_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:21:29 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 389 "--script=banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/sizzle/scans/tcp389/tcp_389_ldap_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/tcp389/xml/tcp_389_ldap_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.056s latency).
Scanned at 2025-02-11 10:21:29 EST for 27s

PORT    STATE SERVICE REASON          VERSION
389/tcp open  ldap    syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
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
| ldap-rootdse: 
| LDAP Results
|   <ROOT>
|       currentTime: 20250211152135.0Z
|       subschemaSubentry: CN=Aggregate,CN=Schema,CN=Configuration,DC=HTB,DC=LOCAL
|       dsServiceName: CN=NTDS Settings,CN=SIZZLE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=HTB,DC=LOCAL
|       namingContexts: DC=HTB,DC=LOCAL
|       namingContexts: CN=Configuration,DC=HTB,DC=LOCAL
|       namingContexts: CN=Schema,CN=Configuration,DC=HTB,DC=LOCAL
|       namingContexts: DC=DomainDnsZones,DC=HTB,DC=LOCAL
|       namingContexts: DC=ForestDnsZones,DC=HTB,DC=LOCAL
|       defaultNamingContext: DC=HTB,DC=LOCAL
|       schemaNamingContext: CN=Schema,CN=Configuration,DC=HTB,DC=LOCAL
|       configurationNamingContext: CN=Configuration,DC=HTB,DC=LOCAL
|       rootDomainNamingContext: DC=HTB,DC=LOCAL
|       supportedControl: 1.2.840.113556.1.4.319
|       supportedControl: 1.2.840.113556.1.4.801
|       supportedControl: 1.2.840.113556.1.4.473
|       supportedControl: 1.2.840.113556.1.4.528
|       supportedControl: 1.2.840.113556.1.4.417
|       supportedControl: 1.2.840.113556.1.4.619
|       supportedControl: 1.2.840.113556.1.4.841
|       supportedControl: 1.2.840.113556.1.4.529
|       supportedControl: 1.2.840.113556.1.4.805
|       supportedControl: 1.2.840.113556.1.4.521
|       supportedControl: 1.2.840.113556.1.4.970
|       supportedControl: 1.2.840.113556.1.4.1338
|       supportedControl: 1.2.840.113556.1.4.474
|       supportedControl: 1.2.840.113556.1.4.1339
|       supportedControl: 1.2.840.113556.1.4.1340
|       supportedControl: 1.2.840.113556.1.4.1413
|       supportedControl: 2.16.840.1.113730.3.4.9
|       supportedControl: 2.16.840.1.113730.3.4.10
|       supportedControl: 1.2.840.113556.1.4.1504
|       supportedControl: 1.2.840.113556.1.4.1852
|       supportedControl: 1.2.840.113556.1.4.802
|       supportedControl: 1.2.840.113556.1.4.1907
|       supportedControl: 1.2.840.113556.1.4.1948
|       supportedControl: 1.2.840.113556.1.4.1974
|       supportedControl: 1.2.840.113556.1.4.1341
|       supportedControl: 1.2.840.113556.1.4.2026
|       supportedControl: 1.2.840.113556.1.4.2064
|       supportedControl: 1.2.840.113556.1.4.2065
|       supportedControl: 1.2.840.113556.1.4.2066
|       supportedControl: 1.2.840.113556.1.4.2090
|       supportedControl: 1.2.840.113556.1.4.2205
|       supportedControl: 1.2.840.113556.1.4.2204
|       supportedControl: 1.2.840.113556.1.4.2206
|       supportedControl: 1.2.840.113556.1.4.2211
|       supportedControl: 1.2.840.113556.1.4.2239
|       supportedControl: 1.2.840.113556.1.4.2255
|       supportedControl: 1.2.840.113556.1.4.2256
|       supportedControl: 1.2.840.113556.1.4.2309
|       supportedLDAPVersion: 3
|       supportedLDAPVersion: 2
|       supportedLDAPPolicies: MaxPoolThreads
|       supportedLDAPPolicies: MaxPercentDirSyncRequests
|       supportedLDAPPolicies: MaxDatagramRecv
|       supportedLDAPPolicies: MaxReceiveBuffer
|       supportedLDAPPolicies: InitRecvTimeout
|       supportedLDAPPolicies: MaxConnections
|       supportedLDAPPolicies: MaxConnIdleTime
|       supportedLDAPPolicies: MaxPageSize
|       supportedLDAPPolicies: MaxBatchReturnMessages
|       supportedLDAPPolicies: MaxQueryDuration
|       supportedLDAPPolicies: MaxDirSyncDuration
|       supportedLDAPPolicies: MaxTempTableSize
|       supportedLDAPPolicies: MaxResultSetSize
|       supportedLDAPPolicies: MinResultSets
|       supportedLDAPPolicies: MaxResultSetsPerConn
|       supportedLDAPPolicies: MaxNotificationPerConn
|       supportedLDAPPolicies: MaxValRange
|       supportedLDAPPolicies: MaxValRangeTransitive
|       supportedLDAPPolicies: ThreadMemoryLimit
|       supportedLDAPPolicies: SystemMemoryLimitPercent
|       highestCommittedUSN: 143485
|       supportedSASLMechanisms: GSSAPI
|       supportedSASLMechanisms: GSS-SPNEGO
|       supportedSASLMechanisms: EXTERNAL
|       supportedSASLMechanisms: DIGEST-MD5
|       dnsHostName: sizzle.HTB.LOCAL
|       ldapServiceName: HTB.LOCAL:sizzle$@HTB.LOCAL
|       serverName: CN=SIZZLE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=HTB,DC=LOCAL
|       supportedCapabilities: 1.2.840.113556.1.4.800
|       supportedCapabilities: 1.2.840.113556.1.4.1670
|       supportedCapabilities: 1.2.840.113556.1.4.1791
|       supportedCapabilities: 1.2.840.113556.1.4.1935
|       supportedCapabilities: 1.2.840.113556.1.4.2080
|       supportedCapabilities: 1.2.840.113556.1.4.2237
|       isSynchronized: TRUE
|       isGlobalCatalogReady: TRUE
|       domainFunctionality: 7
|       forestFunctionality: 7
|_      domainControllerFunctionality: 7
|_ssl-date: 2025-02-11T15:21:45+00:00; -1s from scanner time.
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
Service Info: Host: SIZZLE; OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:21:56 2025 -- 1 IP address (1 host up) scanned in 27.45 seconds

```
