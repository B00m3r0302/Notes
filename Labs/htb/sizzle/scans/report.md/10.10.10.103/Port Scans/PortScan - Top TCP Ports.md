```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/htb/sizzle/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sizzle/scans/xml/_quick_tcp_nmap.xml" 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Tue Feb 11 10:19:22 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/htb/sizzle/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/htb/sizzle/scans/xml/_quick_tcp_nmap.xml 10.10.10.103
Nmap scan report for 10.10.10.103
Host is up, received user-set (0.057s latency).
Scanned at 2025-02-11 10:19:22 EST for 126s
Not shown: 985 filtered tcp ports (no-response)
PORT     STATE SERVICE       REASON          VERSION
21/tcp   open  ftp           syn-ack ttl 127 Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
53/tcp   open  domain        syn-ack ttl 127 Simple DNS Plus
80/tcp   open  http          syn-ack ttl 127 Microsoft IIS httpd 10.0
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
135/tcp  open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp  open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
|_ssl-date: 2025-02-11T15:21:20+00:00; 0s from scanner time.
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
443/tcp  open  ssl/http      syn-ack ttl 127 Microsoft IIS httpd 10.0
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
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Microsoft-IIS/10.0
|_ssl-date: 2025-02-11T15:21:20+00:00; 0s from scanner time.
| tls-alpn: 
|   h2
|_  http/1.1
445/tcp  open  microsoft-ds? syn-ack ttl 127
464/tcp  open  kpasswd5?     syn-ack ttl 127
593/tcp  open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      syn-ack ttl 127
|_ssl-date: 2025-02-11T15:21:20+00:00; 0s from scanner time.
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
3268/tcp open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
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
|_ssl-date: 2025-02-11T15:21:20+00:00; 0s from scanner time.
3269/tcp open  ssl/ldap      syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
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
|_ssl-date: 2025-02-11T15:21:20+00:00; 0s from scanner time.
5985/tcp open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
5986/tcp open  ssl/http      syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
| tls-alpn: 
|   h2
|_  http/1.1
|_ssl-date: 2025-02-11T15:21:20+00:00; 0s from scanner time.
|_http-title: Not Found
| ssl-cert: Subject: commonName=sizzle.HTB.LOCAL
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:sizzle.HTB.LOCAL
| Issuer: commonName=HTB-SIZZLE-CA/domainComponent=HTB
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2018-07-02T20:26:23
| Not valid after:  2019-07-02T20:26:23
| MD5:   acd1:5e32:da9d:89e2:cde5:7b46:ca12:1d5e
| SHA-1: 06b2:0070:6600:2651:4c70:054f:b1aa:9c15:cadd:f233
| -----BEGIN CERTIFICATE-----
| MIIF1TCCBL2gAwIBAgITaQAAAAI7KZCOX7qGWQAAAAAAAjANBgkqhkiG9w0BAQsF
| ADBEMRUwEwYKCZImiZPyLGQBGRYFTE9DQUwxEzARBgoJkiaJk/IsZAEZFgNIVEIx
| FjAUBgNVBAMTDUhUQi1TSVpaTEUtQ0EwHhcNMTgwNzAyMjAyNjIzWhcNMTkwNzAy
| MjAyNjIzWjAbMRkwFwYDVQQDExBzaXp6bGUuSFRCLkxPQ0FMMIIBIjANBgkqhkiG
| 9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7LZ90vlcwcqtTW2c66J262dbt5UGPP84ozIU
| AelGkpVgnRQmEWTZ89SlFqtNi7hrzWzrkJgVuXGs8YRBklwotpC2hpJRHA9Kb7sV
| /eKJmeBMfp+vA4WAFR7aFn0wWN+8yaok3+6cZeCWsEjB0QLljtZWHR7TixwahPUC
| T8LOKDliEZ2pUUYS4QkzC2yQf9wfMPH3zWDBft0WiI/MxR90C55DW7+ykYMTB4VI
| dkcdhIG/zDO6k/oV8zhR+kR6ZRQw4ufuVqACmOvZ8LyIIY49V1RQJp18p9o4jIpU
| MJUjgDWC66wnWCjYgvPHpb7S/0IMfffbqdYYP+jiS0Nu5zH4xQIDAQABo4IC5zCC
| AuMwLwYJKwYBBAGCNxQCBCIeIABEAG8AbQBhAGkAbgBDAG8AbgB0AHIAbwBsAGwA
| ZQByMB0GA1UdJQQWMBQGCCsGAQUFBwMCBggrBgEFBQcDATAOBgNVHQ8BAf8EBAMC
| BaAweAYJKoZIhvcNAQkPBGswaTAOBggqhkiG9w0DAgICAIAwDgYIKoZIhvcNAwQC
| AgCAMAsGCWCGSAFlAwQBKjALBglghkgBZQMEAS0wCwYJYIZIAWUDBAECMAsGCWCG
| SAFlAwQBBTAHBgUrDgMCBzAKBggqhkiG9w0DBzAdBgNVHQ4EFgQUZunJxVZWJI+k
| P5f9akPZiXujIkUwHwYDVR0jBBgwFoAUQAbkVLM3mLwiLg4ZNgoYoLHeC4owgcgG
| A1UdHwSBwDCBvTCBuqCBt6CBtIaBsWxkYXA6Ly8vQ049SFRCLVNJWlpMRS1DQSxD
| Tj1zaXp6bGUsQ049Q0RQLENOPVB1YmxpYyUyMEtleSUyMFNlcnZpY2VzLENOPVNl
| cnZpY2VzLENOPUNvbmZpZ3VyYXRpb24sREM9SFRCLERDPUxPQ0FMP2NlcnRpZmlj
| YXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFzcz1jUkxEaXN0cmlidXRp
| b25Qb2ludDCBvQYIKwYBBQUHAQEEgbAwga0wgaoGCCsGAQUFBzAChoGdbGRhcDov
| Ly9DTj1IVEItU0laWkxFLUNBLENOPUFJQSxDTj1QdWJsaWMlMjBLZXklMjBTZXJ2
| aWNlcyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPUhUQixEQz1MT0NB
| TD9jQUNlcnRpZmljYXRlP2Jhc2U/b2JqZWN0Q2xhc3M9Y2VydGlmaWNhdGlvbkF1
| dGhvcml0eTA8BgNVHREENTAzoB8GCSsGAQQBgjcZAaASBBB7YfekKJKyQJ4UWzrt
| tIm9ghBzaXp6bGUuSFRCLkxPQ0FMMA0GCSqGSIb3DQEBCwUAA4IBAQCG0Wqi5HRj
| 0/eYGCjnodhwwNG3ZGaS6BeNh04fK0/e/BqkoIhgARti+IMdaBHZNek9lya9zJAv
| l/y8QnTYMM6xsJskEDfjIS/9vkLUYMFEjxQzBBhDMqkSk0L1tHCv++CLmZVnUVsJ
| s+g7IJlq+M1zk2kzleMh7v3QUuxuaHyz/zjyjtlFyYx13IMyBuC4wFu7pVS5dRZ8
| 5cUHmD/QtkrdxfPrRaQdqjAx+g2KOyH9Ea6j5ArDQQl8q/DuK3r8WmMCvfBD28lI
| z527nTRznihiyXeRshPduOUUODwPFQ4vWwtj0+UsPIUjaT5OvI7kdW/1TOVK/lMi
| FmhL2FFDGeEJ
|_-----END CERTIFICATE-----
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2012|2016|2008|7 (91%)
OS CPE: cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2016 cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_7
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows Server 2012 R2 (91%), Microsoft Windows Server 2016 (91%), Microsoft Windows 7 or Windows Server 2008 R2 (85%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.95%E=4%D=2/11%OT=21%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=67AB6AF8%P=x86_64-pc-linux-gnu)
SEQ(SP=102%GCD=1%ISR=108%TI=I%II=I%SS=S%TS=A)
SEQ(SP=105%GCD=1%ISR=103%TI=I%II=I%SS=S%TS=A)
OPS(O1=M53CNW8ST11%O2=M53CNW8ST11%O3=M53CNW8NNT11%O4=M53CNW8ST11%O5=M53CNW8ST11%O6=M53CST11)
WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=2000)
ECN(R=Y%DF=Y%TG=80%W=2000%O=M53CNW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Uptime guess: 0.003 days (since Tue Feb 11 10:17:34 2025)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: SIZZLE; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb2-time: 
|   date: 2025-02-11T15:20:43
|_  start_date: 2025-02-11T15:17:56
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 30362/tcp): CLEAN (Timeout)
|   Check 2 (port 44477/tcp): CLEAN (Timeout)
|   Check 3 (port 34054/udp): CLEAN (Timeout)
|   Check 4 (port 29161/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

TRACEROUTE (using port 445/tcp)
HOP RTT      ADDRESS
1   57.73 ms 10.10.14.1
2   58.47 ms 10.10.10.103

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 11 10:21:28 2025 -- 1 IP address (1 host up) scanned in 126.11 seconds

```
