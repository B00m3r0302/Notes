```bash
nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/resolute/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp389/tcp_389_ldap_nmap.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp389/tcp_389_ldap_nmap.txt):

```
# Nmap 7.95 scan initiated Sun Jan 26 20:15:40 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 389 "--script=banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/resolute/scans/tcp389/tcp_389_ldap_nmap.txt -oX /home/kali/Notes/Labs/htb/resolute/scans/tcp389/xml/tcp_389_ldap_nmap.xml 10.10.10.169
Nmap scan report for 10.10.10.169
Host is up, received user-set (0.054s latency).
Scanned at 2025-01-26 20:15:40 EST for 17s

PORT    STATE SERVICE REASON          VERSION
389/tcp open  ldap    syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: megabank.local, Site: Default-First-Site-Name)
| ldap-rootdse: 
| LDAP Results
|   <ROOT>
|       currentTime: 20250127012248.0Z
|       subschemaSubentry: CN=Aggregate,CN=Schema,CN=Configuration,DC=megabank,DC=local
|       dsServiceName: CN=NTDS Settings,CN=RESOLUTE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=megabank,DC=local
|       namingContexts: DC=megabank,DC=local
|       namingContexts: CN=Configuration,DC=megabank,DC=local
|       namingContexts: CN=Schema,CN=Configuration,DC=megabank,DC=local
|       namingContexts: DC=DomainDnsZones,DC=megabank,DC=local
|       namingContexts: DC=ForestDnsZones,DC=megabank,DC=local
|       defaultNamingContext: DC=megabank,DC=local
|       schemaNamingContext: CN=Schema,CN=Configuration,DC=megabank,DC=local
|       configurationNamingContext: CN=Configuration,DC=megabank,DC=local
|       rootDomainNamingContext: DC=megabank,DC=local
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
|       highestCommittedUSN: 151718
|       supportedSASLMechanisms: GSSAPI
|       supportedSASLMechanisms: GSS-SPNEGO
|       supportedSASLMechanisms: EXTERNAL
|       supportedSASLMechanisms: DIGEST-MD5
|       dnsHostName: Resolute.megabank.local
|       ldapServiceName: megabank.local:resolute$@MEGABANK.LOCAL
|       serverName: CN=RESOLUTE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=megabank,DC=local
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
|   Context: DC=megabank,DC=local
|     dn: DC=megabank,DC=local
|         objectClass: top
|         objectClass: domain
|         objectClass: domainDNS
|         distinguishedName: DC=megabank,DC=local
|         instanceType: 5
|         whenCreated: 2019/09/25 13:28:22 UTC
|         whenChanged: 2025/01/27 01:13:42 UTC
|         subRefs: DC=ForestDnsZones,DC=megabank,DC=local
|         subRefs: DC=DomainDnsZones,DC=megabank,DC=local
|         subRefs: CN=Configuration,DC=megabank,DC=local
|         uSNCreated: 4099
|         \x19\x9A\xF2\xBC
|         uSNChanged: 151597
|         name: megabank
|         objectGUID: b4e0e946-e7cb-b742-8fa0-5c4cec2fe5aa
|         replUpToDateVector: \x02\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00;\xFE\xC7\x0EMO\x9F@\x81\xB6~\xC4\x91\xD3R\x8C\x1A\xC0\x01\x00\x00\x00\x00\x00\x0Cs\xF7\x13\x03\x00\x00\x00\xC2\x1D)\x1D\xC8\x1B\xD9G\xA2\xBCRK\xE1\x0F\x10d\x08\xA0\x00\x00\x00\x00\x00\x00\x115\x9F\x13\x03\x00\x00\x00p\x11cD\x9C\x9F\xC9N\xA6k\<\xDE\xBB\xAB|\x1C\xE0\x01\x00\x00\x00\x00\x00F{\xF7\x13\x03\x00\x00\x00\xAA8\x88adCkM\xB6\xD63\x9EGMk\xC8\x07\x90\x00\x00\x00\x00\x00\x00Z0\x9F\x13\x03\x00\x00\x00\x05\xA2\xB2b\xFB)\x86A\xB05\xFD\xBE\x97\xF4\xCEq	\xB0\x00\x00\x00\x00\x00\x00\xD07\x9F\x13\x03\x00\x00\x00`\x9D\x0Ee\xB3T\xBDE\xB4g\x88\x07\x05\xFCI\xE1\x05p\x00\x00\x00\x00\x00\x00< \x9F\x13\x03\x00\x00\x00\xD9
|         cjy\xA3\xC2I\x89d\xE1om\x86\xB0Y\x1F\x10\x02\x00\x00\x00\x00\x00\xF1.\xF8\x13\x03\x00\x00\x0068\xC9\x82\x1E\xBD\xD2N\x92\x1CL\xAF\xF2=\xC6o\x0C\xE0\x00\x00\x00\x00\x00\x00@\x1F\xE6\x13\x03\x00\x00\x00\x11:\x85\x83#\x98\xDAJ\xAA\x83\xE6\xF7%{w\xC1\x18\xA0\x01\x00\x00\x00\x00\x00
|         i\xF7\x13\x03\x00\x00\x00\xD0\xBBK\x8B\xF5\xB5\xD5D\xBE\xF9\xD7\x92\xCEz?;\x1B\xD0\x01\x00\x00\x00\x00\x00vw\xF7\x13\x03\x00\x00\x00
|         n\xF7\x13\x03\x00\x00\x00%}:\xF7\xE0\xF6\xEFM\xB2\xE2\xDD\x80.\xF0*\xB3\x17\x90\x01\x00\x00\x00\x00\x00\xBB`\xF7\x13\x03\x00\x00\x00\xF90\xC0\xFF\x9Df\xB6K\x939WR\x81\xC5P\xA6\x1E\x00\x02\x00\x00\x00\x00\x00\x07\x1D\xF8\x13\x03\x00\x00\x00
|         creationTime: 133824140229435464
|         forceLogoff: -9223372036854775808
|         lockoutDuration: -18000000000
|         lockOutObservationWindow: -18000000000
|         lockoutThreshold: 0
|         maxPwdAge: -9223372036854775808
|         minPwdAge: -864000000000
|         minPwdLength: 7
|         modifiedCountAtLastProm: 0
|         nextRid: 1000
|         pwdProperties: 0
|         pwdHistoryLength: 24
|         objectSid: 1-5-21-1392959593-3013219662-3596683436
|         serverState: 1
|         uASCompat: 1
|         modifiedCount: 1
|         auditingPolicy: \x00\x01
|         nTMixedDomain: 0
|         rIDManagerReference: CN=RID Manager$,CN=System,DC=megabank,DC=local
|         fSMORoleOwner: CN=NTDS Settings,CN=RESOLUTE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=megabank,DC=local
|         systemFlags: -1946157056
|         wellKnownObjects: B:32:6227F0AF1FC2410D8E3BB10615BB5B0F:CN=NTDS Quotas,DC=megabank,DC=local
|         wellKnownObjects: B:32:F4BE92A4C777485E878E9421D53087DB:CN=Microsoft,CN=Program Data,DC=megabank,DC=local
|         wellKnownObjects: B:32:09460C08AE1E4A4EA0F64AEE7DAA1E5A:CN=Program Data,DC=megabank,DC=local
|         wellKnownObjects: B:32:22B70C67D56E4EFB91E9300FCA3DC1AA:CN=ForeignSecurityPrincipals,DC=megabank,DC=local
|         wellKnownObjects: B:32:18E2EA80684F11D2B9AA00C04F79F805:CN=Deleted Objects,DC=megabank,DC=local
|         wellKnownObjects: B:32:2FBAC1870ADE11D297C400C04FD8D5CD:CN=Infrastructure,DC=megabank,DC=local
|         wellKnownObjects: B:32:AB8153B7768811D1ADED00C04FD8D5CD:CN=LostAndFound,DC=megabank,DC=local
|         wellKnownObjects: B:32:AB1D30F3768811D1ADED00C04FD8D5CD:CN=System,DC=megabank,DC=local
|         wellKnownObjects: B:32:A361B2FFFFD211D1AA4B00C04FD7D83A:OU=Domain Controllers,DC=megabank,DC=local
|         wellKnownObjects: B:32:AA312825768811D1ADED00C04FD8D5CD:CN=Computers,DC=megabank,DC=local
|         wellKnownObjects: B:32:A9D1CA15768811D1ADED00C04FD8D5CD:CN=Users,DC=megabank,DC=local
|         objectCategory: CN=Domain-DNS,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         gPLink: [LDAP://CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=megabank,DC=local;0]
|         dSCorePropagationData: 1601/01/01 00:00:00 UTC
|         otherWellKnownObjects: B:32:683A24E2E8164BD3AF86AC3C2CF3F981:CN=Keys,DC=megabank,DC=local
|         otherWellKnownObjects: B:32:1EB93889E40C45DF9F0C64D23BBB6237:CN=Managed Service Accounts,DC=megabank,DC=local
|         masteredBy: CN=NTDS Settings,CN=RESOLUTE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=megabank,DC=local
|         ms-DS-MachineAccountQuota: 10
|         msDS-Behavior-Version: 7
|         msDS-PerUserTrustQuota: 1
|         msDS-AllUsersTrustQuota: 1000
|         msDS-PerUserTrustTombstonesQuota: 10
|         msDs-masteredBy: CN=NTDS Settings,CN=RESOLUTE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=megabank,DC=local
|         msDS-IsDomainFor: CN=NTDS Settings,CN=RESOLUTE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=megabank,DC=local
|         msDS-NcType: 0
|         msDS-ExpirePasswordsOnSmartCardOnlyAccounts: TRUE
|         dc: megabank
|     dn: CN=Users,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Users
|         description: Default container for upgraded user accounts
|         distinguishedName: CN=Users,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5888
|         uSNChanged: 5888
|         showInAdvancedViewOnly: FALSE
|         name: Users
|         objectGUID: d0ed52a-e080-9841-81d6-302cdfab7cf
|         systemFlags: -1946157056
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:19 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=Computers,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Computers
|         description: Default container for upgraded computer accounts
|         distinguishedName: CN=Computers,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5889
|         uSNChanged: 5889
|         showInAdvancedViewOnly: FALSE
|         name: Computers
|         objectGUID: 41e2c5ff-1512-be45-9ca1-488358ad588
|         systemFlags: -1946157056
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: OU=Domain Controllers,DC=megabank,DC=local
|         objectClass: top
|         objectClass: organizationalUnit
|         ou: Domain Controllers
|         description: Default container for domain controllers
|         distinguishedName: OU=Domain Controllers,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 6031
|         uSNChanged: 6031
|         showInAdvancedViewOnly: FALSE
|         name: Domain Controllers
|         objectGUID: 12316bd2-27fe-3a41-90d0-471b6f5e7497
|         systemFlags: -1946157056
|         objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         gPLink: [LDAP://CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC=megabank,DC=local;0]
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=System,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: System
|         description: Builtin system settings
|         distinguishedName: CN=System,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5890
|         uSNChanged: 5890
|         showInAdvancedViewOnly: TRUE
|         name: System
|         objectGUID: 40f9d21f-49e-f54f-bf31-ad83fbc454
|         systemFlags: -1946157056
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=LostAndFound,DC=megabank,DC=local
|         objectClass: top
|         objectClass: lostAndFound
|         cn: LostAndFound
|         description: Default container for orphaned objects
|         distinguishedName: CN=LostAndFound,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5886
|         uSNChanged: 5886
|         showInAdvancedViewOnly: TRUE
|         name: LostAndFound
|         objectGUID: f0581973-33c1-5a4b-aeff-69c8231b4c20
|         systemFlags: -1946157056
|         objectCategory: CN=Lost-And-Found,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=Infrastructure,DC=megabank,DC=local
|         objectClass: top
|         objectClass: infrastructureUpdate
|         cn: Infrastructure
|         distinguishedName: CN=Infrastructure,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 6032
|         uSNChanged: 6032
|         showInAdvancedViewOnly: TRUE
|         name: Infrastructure
|         objectGUID: 261c42dd-8a5-8848-9933-acc8d9b31e21
|         fSMORoleOwner: CN=NTDS Settings,CN=RESOLUTE,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=megabank,DC=local
|         systemFlags: -1946157056
|         objectCategory: CN=Infrastructure-Update,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=ForeignSecurityPrincipals,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: ForeignSecurityPrincipals
|         description: Default container for security identifiers (SIDs) associated with objects from external, trusted domains
|         distinguishedName: CN=ForeignSecurityPrincipals,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 6033
|         uSNChanged: 6033
|         showInAdvancedViewOnly: FALSE
|         name: ForeignSecurityPrincipals
|         objectGUID: 34d72428-e5c-7b46-9f90-963f6f91eeb
|         systemFlags: -1946157056
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=Program Data,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Program Data
|         description: Default location for storage of application data.
|         distinguishedName: CN=Program Data,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 6034
|         uSNChanged: 6034
|         showInAdvancedViewOnly: TRUE
|         name: Program Data
|         objectGUID: ced5275f-fd9-5f43-b6e-6938b4e19a81
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=Microsoft,CN=Program Data,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Microsoft
|         description: Default location for storage of Microsoft application data.
|         distinguishedName: CN=Microsoft,CN=Program Data,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 6035
|         uSNChanged: 6035
|         showInAdvancedViewOnly: TRUE
|         name: Microsoft
|         objectGUID: 30ca5855-6b3e-3740-a918-ea7e5ecfffd5
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/01/01 18:16:33 UTC
|     dn: CN=NTDS Quotas,DC=megabank,DC=local
|         objectClass: top
|         objectClass: msDS-QuotaContainer
|         cn: NTDS Quotas
|         description: Quota specifications container
|         distinguishedName: CN=NTDS Quotas,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 6036
|         uSNChanged: 6036
|         showInAdvancedViewOnly: TRUE
|         name: NTDS Quotas
|         objectGUID: 91fa8980-4347-7647-936a-1b5967503a9b
|         systemFlags: -2147483648
|         objectCategory: CN=ms-DS-Quota-Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|         msDS-TombstoneQuotaFactor: 100
|     dn: CN=Managed Service Accounts,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: Managed Service Accounts
|         description: Default container for managed service accounts
|         distinguishedName: CN=Managed Service Accounts,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 6037
|         uSNChanged: 6037
|         showInAdvancedViewOnly: FALSE
|         name: Managed Service Accounts
|         objectGUID: 5ca0ec93-8f9d-5d42-80fe-8e5dd33415ce
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/26 12:35:01 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/07/14 04:24:33 UTC
|     dn: CN=Keys,DC=megabank,DC=local
|     dn: CN=WinsockServices,CN=System,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         cn: WinsockServices
|         distinguishedName: CN=WinsockServices,CN=System,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5891
|         uSNChanged: 5891
|         showInAdvancedViewOnly: TRUE
|         name: WinsockServices
|         objectGUID: 5eca97f7-852f-3a45-bdcf-3e80e3385d69
|         objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:19 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/01/01 18:16:33 UTC
|     dn: CN=RpcServices,CN=System,DC=megabank,DC=local
|         objectClass: top
|         objectClass: container
|         objectClass: rpcContainer
|         cn: RpcServices
|         distinguishedName: CN=RpcServices,CN=System,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5892
|         uSNChanged: 5892
|         showInAdvancedViewOnly: TRUE
|         name: RpcServices
|         objectGUID: c1e4561a-408c-c84e-b995-70bb8b17da5
|         systemFlags: -1946157056
|         objectCategory: CN=Rpc-Container,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:19 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/01/01 18:16:33 UTC
|     dn: CN=FileLinks,CN=System,DC=megabank,DC=local
|         objectClass: top
|         objectClass: fileLinkTracking
|         cn: FileLinks
|         distinguishedName: CN=FileLinks,CN=System,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5893
|         uSNChanged: 5893
|         showInAdvancedViewOnly: TRUE
|         name: FileLinks
|         objectGUID: 8c677be4-1aaf-e74b-b4b4-a38dc418ead
|         systemFlags: -1946157056
|         objectCategory: CN=File-Link-Tracking,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:19 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/01/01 18:16:33 UTC
|     dn: CN=VolumeTable,CN=FileLinks,CN=System,DC=megabank,DC=local
|     dn: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=megabank,DC=local
|         objectClass: top
|         objectClass: fileLinkTracking
|         objectClass: linkTrackObjectMoveTable
|         cn: ObjectMoveTable
|         distinguishedName: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5895
|         uSNChanged: 5895
|         showInAdvancedViewOnly: TRUE
|         name: ObjectMoveTable
|         objectGUID: e16ba9f4-c9f-449-88d8-65e65e9cfdb1
|         systemFlags: -1946157056
|         objectCategory: CN=Link-Track-Object-Move-Table,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:19 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/01/01 18:16:33 UTC
|     dn: CN=Default Domain Policy,CN=System,DC=megabank,DC=local
|         objectClass: top
|         objectClass: leaf
|         objectClass: domainPolicy
|         cn: Default Domain Policy
|         distinguishedName: CN=Default Domain Policy,CN=System,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5896
|         uSNChanged: 5896
|         showInAdvancedViewOnly: TRUE
|         name: Default Domain Policy
|         objectGUID: 1f79146-3c59-342-ae76-ff643dfce95
|         objectCategory: CN=Domain-Policy,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/01/01 18:16:33 UTC
|     dn: CN=AppCategories,CN=Default Domain Policy,CN=System,DC=megabank,DC=local
|         objectClass: top
|         objectClass: classStore
|         cn: AppCategories
|         distinguishedName: CN=AppCategories,CN=Default Domain Policy,CN=System,DC=megabank,DC=local
|         instanceType: 4
|         whenCreated: 2019/09/25 13:28:31 UTC
|         whenChanged: 2019/09/25 13:28:31 UTC
|         uSNCreated: 5897
|         uSNChanged: 5897
|         showInAdvancedViewOnly: TRUE
|         name: AppCategories
|         objectGUID: 44976634-b987-744c-8d2e-866227fe20a2
|         objectCategory: CN=Class-Store,CN=Schema,CN=Configuration,DC=megabank,DC=local
|         isCriticalSystemObject: TRUE
|         dSCorePropagationData: 2019/09/27 22:10:48 UTC
|         dSCorePropagationData: 2019/09/27 10:52:18 UTC
|         dSCorePropagationData: 2019/09/25 13:29:12 UTC
|         dSCorePropagationData: 1601/01/01 18:16:33 UTC
| 
| 
|_Result limited to 20 objects (see ldap.maxobjects)
Service Info: Host: RESOLUTE; OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jan 26 20:15:57 2025 -- 1 IP address (1 host up) scanned in 16.94 seconds

```
