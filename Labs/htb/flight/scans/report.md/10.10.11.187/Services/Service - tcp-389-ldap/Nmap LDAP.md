```bash
nmap -vv --reason -Pn -T4 -sV -p 389 --script="banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Notes/Labs/htb/flight/scans/tcp389/tcp_389_ldap_nmap.txt" -oX "/home/kali/Notes/Labs/htb/flight/scans/tcp389/xml/tcp_389_ldap_nmap.xml" 10.10.11.187
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp389/tcp_389_ldap_nmap.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp389/tcp_389_ldap_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 13 18:21:21 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 389 "--script=banner,(ldap* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Notes/Labs/htb/flight/scans/tcp389/tcp_389_ldap_nmap.txt -oX /home/kali/Notes/Labs/htb/flight/scans/tcp389/xml/tcp_389_ldap_nmap.xml 10.10.11.187
Nmap scan report for 10.10.11.187
Host is up, received user-set (0.091s latency).
Scanned at 2025-01-13 18:21:22 EST for 17s

PORT    STATE SERVICE REASON          VERSION
389/tcp open  ldap    syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: flight.htb, Site: Default-First-Site-Name)
| ldap-rootdse: 
| LDAP Results
|   <ROOT>
|       domainFunctionality: 7
|       forestFunctionality: 7
|       domainControllerFunctionality: 7
|       rootDomainNamingContext: DC=flight,DC=htb
|       ldapServiceName: flight.htb:g0$@FLIGHT.HTB
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
|       subschemaSubentry: CN=Aggregate,CN=Schema,CN=Configuration,DC=flight,DC=htb
|       serverName: CN=G0,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=flight,DC=htb
|       schemaNamingContext: CN=Schema,CN=Configuration,DC=flight,DC=htb
|       namingContexts: DC=flight,DC=htb
|       namingContexts: CN=Configuration,DC=flight,DC=htb
|       namingContexts: CN=Schema,CN=Configuration,DC=flight,DC=htb
|       namingContexts: DC=DomainDnsZones,DC=flight,DC=htb
|       namingContexts: DC=ForestDnsZones,DC=flight,DC=htb
|       isSynchronized: TRUE
|       highestCommittedUSN: 122981
|       dsServiceName: CN=NTDS Settings,CN=G0,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=flight,DC=htb
|       dnsHostName: g0.flight.htb
|       defaultNamingContext: DC=flight,DC=htb
|       currentTime: 20250114062128.0Z
|_      configurationNamingContext: CN=Configuration,DC=flight,DC=htb
Service Info: Host: G0; OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 13 18:21:39 2025 -- 1 IP address (1 host up) scanned in 18.69 seconds

```
