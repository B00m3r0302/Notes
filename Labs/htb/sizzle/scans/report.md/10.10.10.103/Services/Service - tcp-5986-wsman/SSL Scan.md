```bash
sslscan --show-certificate --no-colour 10.10.10.103:5986 2>&1
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp5986/tcp_5986_sslscan.html](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp5986/tcp_5986_sslscan.html):

```
Version: 2.1.5
OpenSSL 3.4.0 22 Oct 2024

Connected to 10.10.10.103

Testing SSL server 10.10.10.103 on port 5986 using SNI name 10.10.10.103

  SSL/TLS Protocols:
SSLv2     disabled
SSLv3     disabled
TLSv1.0   enabled
TLSv1.1   enabled
TLSv1.2   enabled
TLSv1.3   disabled

  TLS Fallback SCSV:
Server does not support TLS Fallback SCSV

  TLS renegotiation:
Secure session renegotiation supported

  TLS Compression:
Compression disabled

  Heartbleed:
TLSv1.2 not vulnerable to heartbleed
TLSv1.1 not vulnerable to heartbleed
TLSv1.0 not vulnerable to heartbleed

  Supported Server Cipher(s):
Preferred TLSv1.2  256 bits  ECDHE-RSA-AES256-GCM-SHA384   Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-GCM-SHA256   Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-GCM-SHA384     DHE 2048 bits
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-GCM-SHA256     DHE 2048 bits
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA256       Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA          Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  DHE-RSA-AES256-SHA            DHE 2048 bits
Accepted  TLSv1.2  128 bits  DHE-RSA-AES128-SHA            DHE 2048 bits
Accepted  TLSv1.2  256 bits  AES256-GCM-SHA384
Accepted  TLSv1.2  128 bits  AES128-GCM-SHA256
Accepted  TLSv1.2  256 bits  AES256-SHA256
Accepted  TLSv1.2  128 bits  AES128-SHA256
Accepted  TLSv1.2  256 bits  AES256-SHA
Accepted  TLSv1.2  128 bits  AES128-SHA
Accepted  TLSv1.2  112 bits  TLS_RSA_WITH_3DES_EDE_CBC_SHA
Accepted  TLSv1.2  128 bits  TLS_RSA_WITH_RC4_128_SHA
Accepted  TLSv1.2  128 bits  TLS_RSA_WITH_RC4_128_MD5
Preferred TLSv1.1  256 bits  ECDHE-RSA-AES256-SHA          Curve 25519 DHE 253
Accepted  TLSv1.1  128 bits  ECDHE-RSA-AES128-SHA          Curve 25519 DHE 253
Accepted  TLSv1.1  256 bits  DHE-RSA-AES256-SHA            DHE 2048 bits
Accepted  TLSv1.1  128 bits  DHE-RSA-AES128-SHA            DHE 2048 bits
Accepted  TLSv1.1  256 bits  AES256-SHA
Accepted  TLSv1.1  128 bits  AES128-SHA
Accepted  TLSv1.1  112 bits  TLS_RSA_WITH_3DES_EDE_CBC_SHA
Accepted  TLSv1.1  128 bits  TLS_RSA_WITH_RC4_128_SHA
Accepted  TLSv1.1  128 bits  TLS_RSA_WITH_RC4_128_MD5
Preferred TLSv1.0  256 bits  ECDHE-RSA-AES256-SHA          Curve 25519 DHE 253
Accepted  TLSv1.0  128 bits  ECDHE-RSA-AES128-SHA          Curve 25519 DHE 253
Accepted  TLSv1.0  256 bits  DHE-RSA-AES256-SHA            DHE 2048 bits
Accepted  TLSv1.0  128 bits  DHE-RSA-AES128-SHA            DHE 2048 bits
Accepted  TLSv1.0  256 bits  AES256-SHA
Accepted  TLSv1.0  128 bits  AES128-SHA
Accepted  TLSv1.0  112 bits  TLS_RSA_WITH_3DES_EDE_CBC_SHA
Accepted  TLSv1.0  128 bits  TLS_RSA_WITH_RC4_128_SHA
Accepted  TLSv1.0  128 bits  TLS_RSA_WITH_RC4_128_MD5

  Server Key Exchange Group(s):
TLSv1.2  128 bits  secp256r1 (NIST P-256)
TLSv1.2  192 bits  secp384r1 (NIST P-384)
TLSv1.2  128 bits  x25519

  SSL Certificate:
    Certificate blob:
-----BEGIN CERTIFICATE-----
MIIF1TCCBL2gAwIBAgITaQAAAAI7KZCOX7qGWQAAAAAAAjANBgkqhkiG9w0BAQsF
ADBEMRUwEwYKCZImiZPyLGQBGRYFTE9DQUwxEzARBgoJkiaJk/IsZAEZFgNIVEIx
FjAUBgNVBAMTDUhUQi1TSVpaTEUtQ0EwHhcNMTgwNzAyMjAyNjIzWhcNMTkwNzAy
MjAyNjIzWjAbMRkwFwYDVQQDExBzaXp6bGUuSFRCLkxPQ0FMMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7LZ90vlcwcqtTW2c66J262dbt5UGPP84ozIU
AelGkpVgnRQmEWTZ89SlFqtNi7hrzWzrkJgVuXGs8YRBklwotpC2hpJRHA9Kb7sV
/eKJmeBMfp+vA4WAFR7aFn0wWN+8yaok3+6cZeCWsEjB0QLljtZWHR7TixwahPUC
T8LOKDliEZ2pUUYS4QkzC2yQf9wfMPH3zWDBft0WiI/MxR90C55DW7+ykYMTB4VI
dkcdhIG/zDO6k/oV8zhR+kR6ZRQw4ufuVqACmOvZ8LyIIY49V1RQJp18p9o4jIpU
MJUjgDWC66wnWCjYgvPHpb7S/0IMfffbqdYYP+jiS0Nu5zH4xQIDAQABo4IC5zCC
AuMwLwYJKwYBBAGCNxQCBCIeIABEAG8AbQBhAGkAbgBDAG8AbgB0AHIAbwBsAGwA
ZQByMB0GA1UdJQQWMBQGCCsGAQUFBwMCBggrBgEFBQcDATAOBgNVHQ8BAf8EBAMC
BaAweAYJKoZIhvcNAQkPBGswaTAOBggqhkiG9w0DAgICAIAwDgYIKoZIhvcNAwQC
AgCAMAsGCWCGSAFlAwQBKjALBglghkgBZQMEAS0wCwYJYIZIAWUDBAECMAsGCWCG
SAFlAwQBBTAHBgUrDgMCBzAKBggqhkiG9w0DBzAdBgNVHQ4EFgQUZunJxVZWJI+k
P5f9akPZiXujIkUwHwYDVR0jBBgwFoAUQAbkVLM3mLwiLg4ZNgoYoLHeC4owgcgG
A1UdHwSBwDCBvTCBuqCBt6CBtIaBsWxkYXA6Ly8vQ049SFRCLVNJWlpMRS1DQSxD
Tj1zaXp6bGUsQ049Q0RQLENOPVB1YmxpYyUyMEtleSUyMFNlcnZpY2VzLENOPVNl
cnZpY2VzLENOPUNvbmZpZ3VyYXRpb24sREM9SFRCLERDPUxPQ0FMP2NlcnRpZmlj
YXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFzcz1jUkxEaXN0cmlidXRp
b25Qb2ludDCBvQYIKwYBBQUHAQEEgbAwga0wgaoGCCsGAQUFBzAChoGdbGRhcDov
Ly9DTj1IVEItU0laWkxFLUNBLENOPUFJQSxDTj1QdWJsaWMlMjBLZXklMjBTZXJ2
aWNlcyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPUhUQixEQz1MT0NB
TD9jQUNlcnRpZmljYXRlP2Jhc2U/b2JqZWN0Q2xhc3M9Y2VydGlmaWNhdGlvbkF1
dGhvcml0eTA8BgNVHREENTAzoB8GCSsGAQQBgjcZAaASBBB7YfekKJKyQJ4UWzrt
tIm9ghBzaXp6bGUuSFRCLkxPQ0FMMA0GCSqGSIb3DQEBCwUAA4IBAQCG0Wqi5HRj
0/eYGCjnodhwwNG3ZGaS6BeNh04fK0/e/BqkoIhgARti+IMdaBHZNek9lya9zJAv
l/y8QnTYMM6xsJskEDfjIS/9vkLUYMFEjxQzBBhDMqkSk0L1tHCv++CLmZVnUVsJ
s+g7IJlq+M1zk2kzleMh7v3QUuxuaHyz/zjyjtlFyYx13IMyBuC4wFu7pVS5dRZ8
5cUHmD/QtkrdxfPrRaQdqjAx+g2KOyH9Ea6j5ArDQQl8q/DuK3r8WmMCvfBD28lI
z527nTRznihiyXeRshPduOUUODwPFQ4vWwtj0+UsPIUjaT5OvI7kdW/1TOVK/lMi
FmhL2FFDGeEJ
-----END CERTIFICATE-----
    Version: 2
    Serial Number: 69:00:00:00:02:3b:29:90:8e:5f:ba:86:59:00:00:00:00:00:02
    Signature Algorithm: sha256WithRSAEncryption
    Issuer: /DC=LOCAL/DC=HTB/CN=HTB-SIZZLE-CA
    Not valid before: Jul  2 20:26:23 2018 GMT
    Not valid after: Jul  2 20:26:23 2019 GMT
    Subject: /CN=sizzle.HTB.LOCAL
    Public Key Algorithm: NULL
    RSA Public Key: (2048 bit)
      RSA Public-Key: (2048 bit)
      Modulus:
          00:ec:b6:7d:d2:f9:5c:c1:ca:ad:4d:6d:9c:eb:a2:
          76:eb:67:5b:b7:95:06:3c:ff:38:a3:32:14:01:e9:
          46:92:95:60:9d:14:26:11:64:d9:f3:d4:a5:16:ab:
          4d:8b:b8:6b:cd:6c:eb:90:98:15:b9:71:ac:f1:84:
          41:92:5c:28:b6:90:b6:86:92:51:1c:0f:4a:6f:bb:
          15:fd:e2:89:99:e0:4c:7e:9f:af:03:85:80:15:1e:
          da:16:7d:30:58:df:bc:c9:aa:24:df:ee:9c:65:e0:
          96:b0:48:c1:d1:02:e5:8e:d6:56:1d:1e:d3:8b:1c:
          1a:84:f5:02:4f:c2:ce:28:39:62:11:9d:a9:51:46:
          12:e1:09:33:0b:6c:90:7f:dc:1f:30:f1:f7:cd:60:
          c1:7e:dd:16:88:8f:cc:c5:1f:74:0b:9e:43:5b:bf:
          b2:91:83:13:07:85:48:76:47:1d:84:81:bf:cc:33:
          ba:93:fa:15:f3:38:51:fa:44:7a:65:14:30:e2:e7:
          ee:56:a0:02:98:eb:d9:f0:bc:88:21:8e:3d:57:54:
          50:26:9d:7c:a7:da:38:8c:8a:54:30:95:23:80:35:
          82:eb:ac:27:58:28:d8:82:f3:c7:a5:be:d2:ff:42:
          0c:7d:f7:db:a9:d6:18:3f:e8:e2:4b:43:6e:e7:31:
          f8:c5
      Exponent: 65537 (0x10001)
    X509v3 Extensions:
      1.3.6.1.4.1.311.20.2:
        . .D.o.m.a.i.n.C.o.n.t.r.o.l.l.e.r
      X509v3 Extended Key Usage:
        TLS Web Client Authentication, TLS Web Server Authentication
      X509v3 Key Usage: critical
        Digital Signature, Key Encipherment
      S/MIME Capabilities:
        0i0...*.H..
......0...*.H..
......0...`.H.e...*0...`.H.e...-0...`.H.e....0...`.H.e....0...+....0
..*.H..
..
      X509v3 Subject Key Identifier:
        66:E9:C9:C5:56:56:24:8F:A4:3F:97:FD:6A:43:D9:89:7B:A3:22:45
      X509v3 Authority Key Identifier:
        40:06:E4:54:B3:37:98:BC:22:2E:0E:19:36:0A:18:A0:B1:DE:0B:8A
      X509v3 CRL Distribution Points:
        Full Name:
          URI:ldap:///CN=HTB-SIZZLE-CA,CN=sizzle,CN=CDP,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=HTB,DC=LOCAL?certificateRevocationList?base?objectClass=cRLDistributionPoint
      Authority Information Access:
        CA Issuers - URI:ldap:///CN=HTB-SIZZLE-CA,CN=AIA,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=HTB,DC=LOCAL?cACertificate?base?objectClass=certificationAuthority
      X509v3 Subject Alternative Name:
        othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:sizzle.HTB.LOCAL
  Verify m:
    unable to get local issuer certificate

  SSL Certificate:
Signature Algorithm: sha256WithRSAEncryption
RSA Key Strength:    2048

Subject:  sizzle.HTB.LOCAL
Altnames: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:sizzle.HTB.LOCAL
Issuer:   HTB-SIZZLE-CA

Not valid before: Jul  2 20:26:23 2018 GMT
Not valid after:  Jul  2 20:26:23 2019 GMT


```
