```bash
nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/sauna/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/sauna/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.10.175
```

[/home/kali/Notes/Labs/htb/sauna/scans/tcp389/tcp_389_ldap_nmap.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/tcp389/tcp_389_ldap_nmap.txt):

```
# Nmap 7.95 scan initiated Wed Jan 22 09:52:00 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 389 "--script=banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/sauna/scans/tcp389/tcp_389_ldap_nmap.txt -oX /home/kali/Notes/Labs/htb/sauna/scans/tcp389/xml/tcp_389_ldap_nmap.xml 10.10.10.175
Nmap scan report for 10.10.10.175
Host is up, received user-set (0.048s latency).
Scanned at 2025-01-22 09:52:11 EST for 17s

PORT    STATE SERVICE REASON          VERSION
389/tcp open  ldap    syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: EGOTISTICAL-BANK.LOCAL, Site: Default-First-Site-Name)
| ldap-rootdse: 
| LDAP Results
|   <ROOT>
|       domainFunctionality: 7
|       forestFunctionality: 7
|       domainControllerFunctionality: 7
|       rootDomainNamingContext: DC=EGOTISTICAL-BANK,DC=LOCAL
|       ldapServiceName: EGOTISTICAL-BANK.LOCAL:sauna$@EGOTISTICAL-BANK.LOCAL
|       isGlobalCatalogReady: TRUE
|       supportedSASLMechanisms: GSSAPI
|       supportedSASLMechanisms: GSS-SPNEGO
|       supportedSASLMechanisms: EXTERNAL
|       supportedSASLMechanisms: DIGEST-MD5
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
|       supportedControl: 1.2.840.113556.1.4.2330
|       supportedControl: 1.2.840.113556.1.4.2354
|       supportedCapabilities: 1.2.840.113556.1.4.800
|       supportedCapabilities: 1.2.840.113556.1.4.1670
|       supportedCapabilities: 1.2.840.113556.1.4.1791
|       supportedCapabilities: 1.2.840.113556.1.4.1935
|       supportedCapabilities: 1.2.840.113556.1.4.2080
|       supportedCapabilities: 1.2.840.113556.1.4.2237
|       subschemaSubentry: CN=Aggregate,CN=Schema,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|       serverName: CN=SAUNA,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|       schemaNamingContext: CN=Schema,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|       namingContexts: DC=EGOTISTICAL-BANK,DC=LOCAL
|       namingContexts: CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|       namingContexts: CN=Schema,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|       namingContexts: DC=DomainDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL
|       namingContexts: DC=ForestDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL
|       isSynchronized: TRUE
|       highestCommittedUSN: 98491
|       dsServiceName: CN=NTDS Settings,CN=SAUNA,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|       dnsHostName: SAUNA.EGOTISTICAL-BANK.LOCAL
|       defaultNamingContext: DC=EGOTISTICAL-BANK,DC=LOCAL
|       currentTime: 20250122225219.0Z
|_      configurationNamingContext: CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
| ldap-search: 
|   Context: DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: DC=EGOTISTICAL-BANK,DC=LOCAL
|         objectClass: top
|         objectClass: domain
|         objectClass: domainDNS
|         distinguishedName: DC=EGOTISTICAL-BANK,DC=LOCAL
|         instanceType: 5
|         whenCreated: 2020/01/23 05:44:25 UTC
|         whenChanged: 2025/01/22 00:11:10 UTC
|         subRefs: DC=ForestDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL
|         subRefs: DC=DomainDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL
|         subRefs: CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|         uSNCreated: 4099
|         dSASignature: \x01\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xBE\xE0\xB3\xC6%\xECD\xB2\xB9\x9F\xF8\D\xB2\xEC
|         uSNChanged: 98336
|         name: EGOTISTICAL-BANK
|         objectGUID: 504e6ec-c122-a143-93c0-cf487f83363
|         replUpToDateVector: \x02\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00F\xC6\xFFTH\x85uJ\xBF	\xC2\xD4\x05j\xE2\x8F\x16\x80\x01\x00\x00\x00\x00\x00\x9B\xC8\xA0\x1D\x03\x00\x00\x00\xAB\x8C\xEFx\xD1I\x85D\xB2\xC2\xED\x9Ce\xFE\xAF\xAD\x0C\xE0\x00\x00\x00\x00\x00\x00(8\xFE\x16\x03\x00\x00\x00\xDC\xD1T\x81\xF1a.B\xB4D
|         @	\xE6\x84u\x15p\x01\x00\x00\x00\x00\x00\xD4n\x0F\x17\x03\x00\x00\x00\xFDZ\x85\x92F\xDE^A\xAAVnj@#\xF6\x0C\x0B\xD0\x00\x00\x00\x00\x00\x00\xD0\xF0
|         \x15\x03\x00\x00\x00\x9B\xF0\xC5\x9Fl\x1D|E\x8B\x15\xFA/\x1A>\x13N\x14`\x01\x00\x00\x00\x00\x00\x10\xD5\x00\x17\x03\x00\x00\x00@\xBE\xE0\xB3\xC6%\xECD\xB2\xB9\x9F\xF8\D\xB2\xEC	\xB0\x00\x00\x00\x00\x00\x00\xD4\x04R\x14\x03\x00\x00\x00
|         creationTime: 133819782702322205
|         forceLogoff: -9223372036854775808
|         lockoutDuration: -18000000000
|         lockOutObservationWindow: -18000000000
|         lockoutThreshold: 0
|         maxPwdAge: -36288000000000
|         minPwdAge: -864000000000
|         minPwdLength: 7
|         modifiedCountAtLastProm: 0
|         nextRid: 1000
|         pwdProperties: 1
|         pwdHistoryLength: 24
|         objectSid: 1-5-21-2966785786-3096785034-1186376766
|         serverState: 1
|         uASCompat: 1
|         modifiedCount: 1
|         auditingPolicy: \x00\x01
|         nTMixedDomain: 0
|         rIDManagerReference: CN=RID Manager$,CN=System,DC=EGOTISTICAL-BANK,DC=LOCAL
|         fSMORoleOwner: CN=NTDS Settings,CN=SAUNA,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|         systemFlags: -1946157056
|         wellKnownObjects: B:32:6227F0AF1FC2410D8E3BB10615BB5B0F:CN=NTDS Quotas,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:F4BE92A4C777485E878E9421D53087DB:CN=Microsoft,CN=Program Data,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:09460C08AE1E4A4EA0F64AEE7DAA1E5A:CN=Program Data,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:22B70C67D56E4EFB91E9300FCA3DC1AA:CN=ForeignSecurityPrincipals,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:18E2EA80684F11D2B9AA00C04F79F805:CN=Deleted Objects,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:2FBAC1870ADE11D297C400C04FD8D5CD:CN=Infrastructure,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:AB8153B7768811D1ADED00C04FD8D5CD:CN=LostAndFound,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:AB1D30F3768811D1ADED00C04FD8D5CD:CN=System,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:A361B2FFFFD211D1AA4B00C04FD7D83A:OU=Domain Controllers,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:AA312825768811D1ADED00C04FD8D5CD:CN=Computers,DC=EGOTISTICAL-BANK,DC=LOCAL
|         wellKnownObjects: B:32:A9D1CA15768811D1ADED00C04FD8D5CD:CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL
|         objectCategory: CN=Domain-DNS,CN=Schema,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|         isCriticalSystemObject: TRUE
|         gPLink: [LDAP://CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=EGOTISTICAL-BANK,DC=LOCAL;0]
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|         otherWellKnownObjects: B:32:683A24E2E8164BD3AF86AC3C2CF3F981:CN=Keys,DC=EGOTISTICAL-BANK,DC=LOCAL
|         otherWellKnownObjects: B:32:1EB93889E40C45DF9F0C64D23BBB6237:CN=Managed Service Accounts,DC=EGOTISTICAL-BANK,DC=LOCAL
|         masteredBy: CN=NTDS Settings,CN=SAUNA,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|         ms-DS-MachineAccountQuota: 10
|         msDS-Behavior-Version: 7
|         msDS-PerUserTrustQuota: 1
|         msDS-AllUsersTrustQuota: 1000
|         msDS-PerUserTrustTombstonesQuota: 10
|         msDs-masteredBy: CN=NTDS Settings,CN=SAUNA,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|         msDS-IsDomainFor: CN=NTDS Settings,CN=SAUNA,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
|         msDS-NcType: 0
|         msDS-ExpirePasswordsOnSmartCardOnlyAccounts: TRUE
|         dc: EGOTISTICAL-BANK
|     dn: CN=Users,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=Computers,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: OU=Domain Controllers,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=System,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=LostAndFound,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=Infrastructure,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=ForeignSecurityPrincipals,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=Program Data,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=NTDS Quotas,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=Managed Service Accounts,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=Keys,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=TPM Devices,DC=EGOTISTICAL-BANK,DC=LOCAL
|     dn: CN=Builtin,DC=EGOTISTICAL-BANK,DC=LOCAL
|_    dn: CN=Hugo Smith,DC=EGOTISTICAL-BANK,DC=LOCAL
Service Info: Host: SAUNA; OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan 22 09:52:28 2025 -- 1 IP address (1 host up) scanned in 27.96 seconds

```
