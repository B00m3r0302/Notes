```bash
nmap -vv --reason -Pn -T4 -sV -p 3268 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/forest/scans/tcp3268/tcp_3268_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/forest/scans/tcp3268/xml/tcp_3268_ldap_nmap.xml" 10.10.10.161
```

[/home/kali/Notes/Labs/htb/forest/scans/tcp3268/tcp_3268_ldap_nmap.txt](file:///home/kali/Notes/Labs/htb/forest/scans/tcp3268/tcp_3268_ldap_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 20 12:44:00 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 3268 "--script=banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/forest/scans/tcp3268/tcp_3268_ldap_nmap.txt -oX /home/kali/Notes/Labs/htb/forest/scans/tcp3268/xml/tcp_3268_ldap_nmap.xml 10.10.10.161
Nmap scan report for forest.htb.local (10.10.10.161)
Host is up, received user-set (0.054s latency).
Scanned at 2025-01-20 12:44:01 EST for 16s

PORT     STATE SERVICE REASON          VERSION
3268/tcp open  ldap    syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
| ldap-rootdse: 
| LDAP Results
|   <ROOT>
|       currentTime: 20250120175059.0Z
|       subschemaSubentry: CN=Aggregate,CN=Schema,CN=Configuration,DC=htb,DC=local
|       dsServiceName: CN=NTDS Settings,CN=FOREST,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=htb,DC=local
|       namingContexts: DC=htb,DC=local
|       namingContexts: CN=Configuration,DC=htb,DC=local
|       namingContexts: CN=Schema,CN=Configuration,DC=htb,DC=local
|       namingContexts: DC=DomainDnsZones,DC=htb,DC=local
|       namingContexts: DC=ForestDnsZones,DC=htb,DC=local
|       defaultNamingContext: DC=htb,DC=local
|       schemaNamingContext: CN=Schema,CN=Configuration,DC=htb,DC=local
|       configurationNamingContext: CN=Configuration,DC=htb,DC=local
|       rootDomainNamingContext: DC=htb,DC=local
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
|       highestCommittedUSN: 16229489
|       supportedSASLMechanisms: GSSAPI
|       supportedSASLMechanisms: GSS-SPNEGO
|       supportedSASLMechanisms: EXTERNAL
|       supportedSASLMechanisms: DIGEST-MD5
|       dnsHostName: FOREST.htb.local
|       ldapServiceName: htb.local:forest$@HTB.LOCAL
|       serverName: CN=FOREST,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=htb,DC=local
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
| ldap-search: 
|   Context: DC=htb,DC=local
|     dn: DC=htb,DC=local
|         objectClass: top
|         objectClass: domain
|         objectClass: domainDNS
|         distinguishedName: DC=htb,DC=local
|         instanceType: 5
|         whenCreated: 2019/09/18 17:45:49 UTC
|         whenChanged: 2025/01/17 13:22:16 UTC
|         subRefs: DC=ForestDnsZones,DC=htb,DC=local
|         subRefs: DC=DomainDnsZones,DC=htb,DC=local
|         subRefs: CN=Configuration,DC=htb,DC=local
|         uSNCreated: 4099
|         uSNChanged: 888873
|         name: htb
|         objectGUID: dff0c71a-49a9-264b-8c7b-52e3e2cb6eab
|         replUpToDateVector: \x02\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x80+\xBA\x07\xA0+|B\x8E\x91\xB7\x8C\xE2\xAFM\x9B
|         \x00\x00\x00\x00\x00\xD4\xBD>\x17\x03\x00\x00\x00i\xB5Y\x1F\xFA\x8B\xA9G\xB3\xB0R.\xA0\xD4b\xEC\x16P\x03\x00\x00\x00\x00\x00\x01\xD5\xAA\x13\x03\x00\x00\x00:\xA3k#YyAJ\xB9Y_\x82h\x9A\x08q\x05\xA0\x00\x00\x00\x00\x00\x00_!\x99\x13\x03\x00\x00\x00\xFD!?9\xEE\x966L\xB0C\xBC\x0Fp\x8Du\xBA\x19\x10\x04\x00\x00\x00\x00\x00n\xC9=\x17\x03\x00\x00\x00\x10<\x01A\xB4\x8C\x9DE\x88\xE2z\xBC\x05\x8E\xE3\xD7\x150\x03\x00\x00\x00\x00\x00\xD5\xD7\xA6\x13\x03\x00\x00\x00\xB50\xC6a\xA2A\xB0E\xB14A\x1A\xB5N1c\x08\xD0\x00\x00\x00\x00\x00\x00\x9F=\x99\x13\x03\x00\x00\x00N|cxf\x16\xECI\xAB\x9C\xCDQ\xEE`H\x81\x13p\x02\x00\x00\x00\x00\x00\xDDm\xA0\x13\x03\x00\x00\x001\xF4\xC6\x8BEpyC\xA6\x9B\x99\xF2\xB4\x8D&p\x0C\x10\x01\x00\x00\x00\x00\x00\x86\xC5\x99\x13\x03\x00\x00\x00\xB7\x02\xFE\x8F
|         \x00\x00\x00\x00\x00\x99\xC5>\x17\x03\x00\x00\x00\x12\xE3\xA9\xF1\xC0\xBA\xB7O\xAEj\x87\xBC\xDE:\xA7-\x07\xC0\x00\x00\x00\x00\x00\x00\xC37\x99\x13\x03\x00\x00\x00\x9E\xBD\x80\xF9D\x13\xFBE\xBA\xD8\x01
|         \xE0\x8E\x1B\x8F\x1C\xD0\x0C\x00\x00\x00\x00\x00\xB1\xAF>\x17\x03\x00\x00\x00
|         objectSid: 1-5-21-3072663084-364016917-1341370565
|         nTMixedDomain: 0
|         wellKnownObjects: B:32:6227F0AF1FC2410D8E3BB10615BB5B0F:CN=NTDS Quotas,DC=htb,DC=local
|         wellKnownObjects: B:32:F4BE92A4C777485E878E9421D53087DB:CN=Microsoft,CN=Program Data,DC=htb,DC=local
|         wellKnownObjects: B:32:09460C08AE1E4A4EA0F64AEE7DAA1E5A:CN=Program Data,DC=htb,DC=local
|         wellKnownObjects: B:32:22B70C67D56E4EFB91E9300FCA3DC1AA:CN=ForeignSecurityPrincipals,DC=htb,DC=local
|         wellKnownObjects: B:32:18E2EA80684F11D2B9AA00C04F79F805:CN=Deleted Objects,DC=htb,DC=local
|         wellKnownObjects: B:32:2FBAC1870ADE11D297C400C04FD8D5CD:CN=Infrastructure,DC=htb,DC=local
|         wellKnownObjects: B:32:AB8153B7768811D1ADED00C04FD8D5CD:CN=LostAndFound,DC=htb,DC=local
|         wellKnownObjects: B:32:AB1D30F3768811D1ADED00C04FD8D5CD:CN=System,DC=htb,DC=local
|         wellKnownObjects: B:32:A361B2FFFFD211D1AA4B00C04FD7D83A:OU=Domain Controllers,DC=htb,DC=local
|         wellKnownObjects: B:32:AA312825768811D1ADED00C04FD8D5CD:CN=Computers,DC=htb,DC=local
|         wellKnownObjects: B:32:A9D1CA15768811D1ADED00C04FD8D5CD:CN=Users,DC=htb,DC=local
|         objectCategory: CN=Domain-DNS,CN=Schema,CN=Configuration,DC=htb,DC=local
|         gPLink: [LDAP://CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=htb,DC=local;0]
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|         masteredBy: CN=NTDS Settings,CN=FOREST,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=htb,DC=local
|         msDs-masteredBy: CN=NTDS Settings,CN=FOREST,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=htb,DC=local
|         msDS-IsDomainFor: CN=NTDS Settings,CN=FOREST,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=htb,DC=local
|         dc: htb
|     dn: CN=Configuration,DC=htb,DC=local
|     dn: CN=Users,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Users
|         description: Default container for upgraded user accounts
|         distinguishedName: CN=Users,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 5888
|         uSNChanged: 94253
|         name: Users
|         objectGUID: 28cbed1a-9b7f-1e49-9fce-a053e95892cd
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=Computers,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Computers
|         description: Default container for upgraded computer accounts
|         distinguishedName: CN=Computers,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 5889
|         uSNChanged: 94358
|         name: Computers
|         objectGUID: 5b37dcc-7dd4-c46-a9ca-922785b235ed
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:11 UTC
|         dSCorePropagationData: 2025/01/20 13:22:11 UTC
|         dSCorePropagationData: 2025/01/20 13:22:11 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: OU=Domain Controllers,DC=htb,DC=local
|         objectClass: top
|         objectClass: organizationalUnit
|         ou: Domain Controllers
|         description: Default container for domain controllers
|         distinguishedName: OU=Domain Controllers,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 6031
|         uSNChanged: 94364
|         name: Domain Controllers
|         objectGUID: 9213180-6637-b24b-ba74-30dec65b543f
|         objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=htb,DC=local
|         gPLink: [LDAP://CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC=htb,DC=local;0]
|         dSCorePropagationData: 2025/01/20 13:22:11 UTC
|         dSCorePropagationData: 2025/01/20 13:22:11 UTC
|         dSCorePropagationData: 2025/01/20 13:22:11 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=System,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: System
|         description: Builtin system settings
|         distinguishedName: CN=System,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 5890
|         uSNChanged: 94382
|         name: System
|         objectGUID: 67d6aff2-1c1c-e749-bb38-347466ed90a0
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=LostAndFound,DC=htb,DC=local
|         objectClass: top
|         objectClass: lostAndFound
|         cn: LostAndFound
|         description: Default container for orphaned objects
|         distinguishedName: CN=LostAndFound,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/18 17:45:57 UTC
|         uSNCreated: 5886
|         uSNChanged: 5886
|         name: LostAndFound
|         objectGUID: affa7481-4f3c-b943-9768-50bfbbab170
|         objectCategory: CN=Lost-And-Found,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 2025/01/20 13:22:01 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=Infrastructure,DC=htb,DC=local
|         objectClass: top
|         objectClass: infrastructureUpdate
|         cn: Infrastructure
|         distinguishedName: CN=Infrastructure,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:16 UTC
|         uSNCreated: 6032
|         uSNChanged: 94878
|         name: Infrastructure
|         objectGUID: 8d39cfb7-eb9-ee4b-b610-a65092fa6116
|         objectCategory: CN=Infrastructure-Update,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:15 UTC
|         dSCorePropagationData: 2025/01/20 13:22:15 UTC
|         dSCorePropagationData: 2025/01/20 13:22:15 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=ForeignSecurityPrincipals,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: ForeignSecurityPrincipals
|         description: Default container for security identifiers (SIDs) associated with objects from external, trusted domains
|         distinguishedName: CN=ForeignSecurityPrincipals,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:16 UTC
|         uSNCreated: 6033
|         uSNChanged: 94881
|         name: ForeignSecurityPrincipals
|         objectGUID: a477a65d-a1f2-994e-a898-19db9fe9b833
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:15 UTC
|         dSCorePropagationData: 2025/01/20 13:22:15 UTC
|         dSCorePropagationData: 2025/01/20 13:22:15 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=Program Data,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Program Data
|         description: Default location for storage of application data.
|         distinguishedName: CN=Program Data,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:16 UTC
|         uSNCreated: 6034
|         uSNChanged: 94959
|         name: Program Data
|         objectGUID: 1d92bace-e528-4d43-b0f9-d79a5ffdd984
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=Microsoft,CN=Program Data,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Microsoft
|         description: Default location for storage of Microsoft application data.
|         distinguishedName: CN=Microsoft,CN=Program Data,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:16 UTC
|         uSNCreated: 6035
|         uSNChanged: 94962
|         name: Microsoft
|         objectGUID: 43e1245-94ce-2447-a37e-32b7816f8890
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=NTDS Quotas,DC=htb,DC=local
|         objectClass: top
|         objectClass: msDS-QuotaContainer
|         cn: NTDS Quotas
|         description: Quota specifications container
|         distinguishedName: CN=NTDS Quotas,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:16 UTC
|         uSNCreated: 6036
|         uSNChanged: 94965
|         name: NTDS Quotas
|         objectGUID: ca57256f-107a-54d-b14d-f4d9a01c1d7f
|         objectCategory: CN=ms-DS-Quota-Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=Managed Service Accounts,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Managed Service Accounts
|         description: Default container for managed service accounts
|         distinguishedName: CN=Managed Service Accounts,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:16 UTC
|         uSNCreated: 6037
|         uSNChanged: 94968
|         name: Managed Service Accounts
|         objectGUID: 7032895e-f174-8b49-9383-782c69206e2f
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:16 UTC
|         dSCorePropagationData: 2025/01/20 13:22:10 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=Keys,DC=htb,DC=local
|     dn: CN=Schema,CN=Configuration,DC=htb,DC=local
|     dn: CN=WinsockServices,CN=System,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         cn: WinsockServices
|         distinguishedName: CN=WinsockServices,CN=System,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 5891
|         uSNChanged: 94385
|         name: WinsockServices
|         objectGUID: 8c2e61b-ae0-fa42-a4fe-9fd92b172f8
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=RpcServices,CN=System,DC=htb,DC=local
|         objectClass: top
|         objectClass: container
|         objectClass: rpcContainer
|         cn: RpcServices
|         distinguishedName: CN=RpcServices,CN=System,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 5892
|         uSNChanged: 94388
|         name: RpcServices
|         objectGUID: 4b38ee81-ccf4-d74a-a8f4-298649a6158b
|         objectCategory: CN=Rpc-Container,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=FileLinks,CN=System,DC=htb,DC=local
|         objectClass: top
|         objectClass: fileLinkTracking
|         cn: FileLinks
|         distinguishedName: CN=FileLinks,CN=System,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 5893
|         uSNChanged: 94391
|         name: FileLinks
|         objectGUID: fd83217-f5ac-314f-b92a-3ab34629222
|         objectCategory: CN=File-Link-Tracking,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|     dn: CN=VolumeTable,CN=FileLinks,CN=System,DC=htb,DC=local
|     dn: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=htb,DC=local
|         objectClass: top
|         objectClass: fileLinkTracking
|         objectClass: linkTrackObjectMoveTable
|         cn: ObjectMoveTable
|         distinguishedName: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=htb,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/18 17:45:57 UTC
|         whenChanged: 2019/09/23 22:51:14 UTC
|         uSNCreated: 5895
|         uSNChanged: 94397
|         name: ObjectMoveTable
|         objectGUID: e3c8cd1f-ec7f-3a48-87c8-e8dea40e68a
|         objectCategory: CN=Link-Track-Object-Move-Table,CN=Schema,CN=Configuration,DC=htb,DC=local
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 2025/01/20 13:22:12 UTC
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
| 
| 
|_Result limited to 20 objects (see ldap.maxobjects)
Service Info: Host: FOREST; OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 20 12:44:17 2025 -- 1 IP address (1 host up) scanned in 17.44 seconds

```
