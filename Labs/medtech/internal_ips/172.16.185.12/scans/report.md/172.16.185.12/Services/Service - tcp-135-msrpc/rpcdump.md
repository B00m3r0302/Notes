```bash
impacket-rpcdump -port 135 172.16.185.12
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/tcp_135_rpc_rpcdump.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.12/scans/tcp135/tcp_135_rpc_rpcdump.txt):

```
Impacket v0.12.0.dev1 - Copyright 2023 Fortra

[*] Retrieving endpoint list from 172.16.185.12
Protocol: N/A
Provider: N/A
UUID    : 51A227AE-825B-41F2-B4A9-1AC9557A1018 v1.0 Ngc Pop Key Service
Bindings:
          ncacn_ip_tcp:172.16.185.12[49669]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:172.16.185.12[49664]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[LSA_IDPEXT_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\DEV04[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : 8FB74744-B2FF-4C00-BE0D-9EF9A191FE1B v1.0 Ngc Pop Key Service
Bindings:
          ncacn_ip_tcp:172.16.185.12[49669]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:172.16.185.12[49664]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[LSA_IDPEXT_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\DEV04[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : B25A52BF-E5DD-4F4A-AEA6-8CA7272A0E86 v2.0 KeyIso
Bindings:
          ncacn_ip_tcp:172.16.185.12[49669]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:172.16.185.12[49664]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[LSA_IDPEXT_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\DEV04[\pipe\lsass]

Protocol: [MS-RAA]: Remote Authorization API Protocol
Provider: N/A
UUID    : 0B1C2170-5732-4E0E-8CD3-D9B16F3B84D7 v0.0 RemoteAccessCheck
Bindings:
          ncacn_ip_tcp:172.16.185.12[49669]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:172.16.185.12[49664]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[LSA_IDPEXT_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\DEV04[\pipe\lsass]
          ncacn_ip_tcp:172.16.185.12[49669]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:172.16.185.12[49664]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[LSA_IDPEXT_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\DEV04[\pipe\lsass]

Protocol: [MS-SAMR]: Security Account Manager (SAM) Remote Protocol
Provider: samsrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AC v1.0
Bindings:
          ncacn_ip_tcp:172.16.185.12[49664]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[LSA_IDPEXT_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\DEV04[\pipe\lsass]

Protocol: [MS-RSP]: Remote Shutdown Protocol
Provider: wininit.exe
UUID    : D95AFE70-A6D5-4259-822E-2C84DA1DDB0D v1.0
Bindings:
          ncacn_ip_tcp:172.16.185.12[49665]
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\DEV04[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc096AC0]

Protocol: N/A
Provider: winlogon.exe
UUID    : 76F226C3-EC14-4325-8A99-6A46348418AF v1.0
Bindings:
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\DEV04[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc096AC0]
          ncalrpc:[WMsgKRpc098601]

Protocol: N/A
Provider: N/A
UUID    : FC48CD89-98D6-4628-9839-86F7A3E4161A v1.0
Bindings:
          ncalrpc:[dabrpc]
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-600dfaaa2905b5ab16]
          ncalrpc:[LRPC-b4137389e7171189df]
          ncalrpc:[LRPC-8f9dd5fae3aea583ea]
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : D09BDEB5-6171-4A34-BFE2-06FA82652568 v1.0
Bindings:
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-600dfaaa2905b5ab16]
          ncalrpc:[LRPC-b4137389e7171189df]
          ncalrpc:[LRPC-8f9dd5fae3aea583ea]
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-b4137389e7171189df]
          ncalrpc:[LRPC-8f9dd5fae3aea583ea]
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-8f9dd5fae3aea583ea]
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-9a60d1771feeadf804]
          ncalrpc:[LRPC-d6cf9b94bec0a98b21]

Protocol: N/A
Provider: N/A
UUID    : 697DCDA9-3BA9-4EB2-9247-E11F1901B0D2 v1.0
Bindings:
          ncalrpc:[LRPC-600dfaaa2905b5ab16]
          ncalrpc:[LRPC-b4137389e7171189df]
          ncalrpc:[LRPC-8f9dd5fae3aea583ea]
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 9B008953-F195-4BF9-BDE0-4471971E58ED v1.0
Bindings:
          ncalrpc:[LRPC-b4137389e7171189df]
          ncalrpc:[LRPC-8f9dd5fae3aea583ea]
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 0D47017B-B33B-46AD-9E18-FE96456C5078 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 95406F0B-B239-4318-91BB-CEA3A46FF0DC v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 4ED8ABCC-F1E2-438B-981F-BB0E8ABC010C v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 0FF1F646-13BB-400A-AB50-9A78F2B7A85A v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 6982A06E-5FE2-46B1-B39C-A2C545BFA069 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 082A3471-31B6-422A-B931-A54401960C62 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : FAE436B0-B864-4A87-9EDA-298547CD82F2 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : E53D94CA-7464-4839-B044-09A2FB8B3AE5 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 178D84BE-9291-4994-82C6-3F909ACA5A03 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 4DACE966-A243-4450-AE3F-9B7BCB5315B8 v2.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 1832BCF6-CAB8-41D4-85D2-C9410764F75A v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : C521FACF-09A9-42C5-B155-72388595CBF0 v0.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2C7FD9CE-E706-4B40-B412-953107EF9BB0 v0.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 88ABCBC3-34EA-76AE-8215-767520655A23 v0.0
Bindings:
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 76C217BC-C8B4-4201-A745-373AD9032B1A v1.0
Bindings:
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 55E6B932-1979-45D6-90C5-7F6270724112 v1.0
Bindings:
          ncalrpc:[LRPC-8f8752f87e4421ad8c]
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 857FB1BE-084F-4FB5-B59C-4B2C4BE5F0CF v1.0
Bindings:
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 20C40295-8DBA-48E6-AEBF-3E78EF3BB144 v2.0
Bindings:
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2513BCBE-6CD4-4348-855E-7EFB3C336DD3 v2.0
Bindings:
          ncalrpc:[OLE66F2C1324424A6346547BCA8B934]
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 0D3E2735-CEA0-4ECC-A9E2-41A2D81AED4E v1.0
Bindings:
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : C605F9FB-F0A3-4E2A-A073-73560F8D9E3E v1.0
Bindings:
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 1B37CA91-76B1-4F5E-A3C7-2ABFC61F2BB0 v1.0
Bindings:
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 8BFC3BE1-6DEF-4E2D-AF74-7C47CD0ADE4A v1.0
Bindings:
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2D98A740-581D-41B9-AA0D-A88B9D5CE938 v1.0
Bindings:
          ncalrpc:[LRPC-dcf49042128a70e4aa]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : DD59071B-3215-4C59-8481-972EDADC0F6A v1.0
Bindings:
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 0361AE94-0316-4C6C-8AD8-C594375800E2 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 5824833B-3C1A-4AD2-BDFD-C31D19E23ED2 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : BDAA0970-413B-4A3E-9E5D-F6DC9D7E0760 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 3B338D89-6CFA-44B8-847E-531531BC9992 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 8782D3B9-EBBD-4644-A3D8-E8725381919B v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 085B0334-E454-4D91-9B8C-4134F9E793F3 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 4BEC6BB8-B5C2-4B6F-B2C1-5DA5CF92D0D9 v1.0
Bindings:
          ncalrpc:[umpo]

Protocol: N/A
Provider: sysntfy.dll
UUID    : C9AC6DB5-82B7-4E55-AE8A-E464ED7B4277 v1.0 Impl friendly name
Bindings:
          ncalrpc:[LRPC-c45438b57d95c44779]
          ncalrpc:[IUserProfile2]
          ncalrpc:[LRPC-f254fb7e3dfaf4ec03]
          ncalrpc:[LRPC-2033b89f723542c0d8]
          ncalrpc:[senssvc]
          ncalrpc:[LRPC-11cbceb7d13e35fda8]

Protocol: N/A
Provider: nsisvc.dll
UUID    : 7EA70BCF-48AF-4F6A-8968-6A440754D5FA v1.0 NSI server endpoint
Bindings:
          ncalrpc:[LRPC-f779e5cde42a4c7b44]

Protocol: N/A
Provider: N/A
UUID    : A500D4C6-0DD1-4543-BC0C-D5F93486EAF8 v1.0
Bindings:
          ncalrpc:[LRPC-42b82c1fbd080a5b67]
          ncalrpc:[LRPC-9a60d1771feeadf804]

Protocol: N/A
Provider: N/A
UUID    : E40F7B57-7A25-4CD3-A135-7F7D3DF9D16B v1.0
Bindings:
          ncalrpc:[LRPC-5989dfca1ac94646d4]

Protocol: N/A
Provider: N/A
UUID    : 880FD55E-43B9-11E0-B1A8-CF4EDFD72085 v1.0 KAPI Service endpoint
Bindings:
          ncalrpc:[LRPC-15e27d685087c070e6]
          ncalrpc:[OLE2949869F2A2A816F9EC12C77E742]
          ncalrpc:[LRPC-d6cf9b94bec0a98b21]

Protocol: N/A
Provider: N/A
UUID    : 5222821F-D5E2-4885-84F1-5F6185A0EC41 v1.0
Bindings:
          ncalrpc:[LRPC-54a43c944c14dbe9bb]

Protocol: N/A
Provider: dhcpcsvc.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D5 v1.0 DHCP Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc]
          ncalrpc:[dhcpcsvc6]

Protocol: N/A
Provider: dhcpcsvc6.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D6 v1.0 DHCPv6 Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc6]

Protocol: N/A
Provider: nrpsrv.dll
UUID    : 30ADC50C-5CBC-46CE-9A0E-91914789E23C v1.0 NRP server endpoint
Bindings:
          ncalrpc:[LRPC-a481058c29236d0ee1]
          ncalrpc:[DNSResolver]

Protocol: [MS-EVEN6]: EventLog Remoting Protocol
Provider: wevtsvc.dll
UUID    : F6BEAFF7-1E19-4FBB-9F8F-B89E2018337C v1.0 Event log TCPIP
Bindings:
          ncacn_ip_tcp:172.16.185.12[49666]
          ncacn_np:\\DEV04[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: N/A
Provider: gpsvc.dll
UUID    : 2EB08E3E-639F-4FBA-97B1-14F878961076 v1.0 Group Policy RPC Interface
Bindings:
          ncalrpc:[LRPC-19d3b99bc1f0934ad8]

Protocol: N/A
Provider: N/A
UUID    : 3A9EF155-691D-4449-8D05-09AD57031823 v1.0
Bindings:
          ncacn_ip_tcp:172.16.185.12[49667]
          ncalrpc:[LRPC-7f7be23d8323448537]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\DEV04[\PIPE\atsvc]
          ncalrpc:[LRPC-aeb33ce09f0689f7ee]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: schedsvc.dll
UUID    : 86D35949-83C9-4044-B424-DB363231FD0C v1.0
Bindings:
          ncacn_ip_tcp:172.16.185.12[49667]
          ncalrpc:[LRPC-7f7be23d8323448537]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\DEV04[\PIPE\atsvc]
          ncalrpc:[LRPC-aeb33ce09f0689f7ee]

Protocol: N/A
Provider: N/A
UUID    : 33D84484-3626-47EE-8C6F-E7E98B113BE1 v2.0
Bindings:
          ncalrpc:[LRPC-7f7be23d8323448537]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\DEV04[\PIPE\atsvc]
          ncalrpc:[LRPC-aeb33ce09f0689f7ee]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 378E52B0-C0A9-11CF-822D-00AA0051E40F v1.0
Bindings:
          ncacn_np:\\DEV04[\PIPE\atsvc]
          ncalrpc:[LRPC-aeb33ce09f0689f7ee]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 1FF70682-0A51-30E8-076D-740BE8CEE98B v1.0
Bindings:
          ncacn_np:\\DEV04[\PIPE\atsvc]
          ncalrpc:[LRPC-aeb33ce09f0689f7ee]

Protocol: N/A
Provider: schedsvc.dll
UUID    : 0A74EF1C-41A4-4E06-83AE-DC74FB1CDD53 v1.0
Bindings:
          ncalrpc:[LRPC-aeb33ce09f0689f7ee]

Protocol: N/A
Provider: N/A
UUID    : 3F787932-3452-4363-8651-6EA97BB373BB v1.0 NSP Rpc Interface
Bindings:
          ncalrpc:[LRPC-ef49d7e17ea09002ea]
          ncalrpc:[OLE70E9728D6A6ED988E0BB2CEA5064]

Protocol: N/A
Provider: N/A
UUID    : 7F1343FE-50A9-4927-A778-0C5859517BAC v1.0 DfsDs service
Bindings:
          ncacn_np:\\DEV04[\PIPE\wkssvc]
          ncalrpc:[LRPC-a8fa6df8d0e2a82ab8]

Protocol: N/A
Provider: N/A
UUID    : EB081A0D-10EE-478A-A1DD-50995283E7A8 v3.0 Witness Client Test Interface
Bindings:
          ncalrpc:[LRPC-a8fa6df8d0e2a82ab8]

Protocol: N/A
Provider: N/A
UUID    : F2C9B409-C1C9-4100-8639-D8AB1486694A v1.0 Witness Client Upcall Server
Bindings:
          ncalrpc:[LRPC-a8fa6df8d0e2a82ab8]

Protocol: N/A
Provider: N/A
UUID    : 3473DD4D-2E88-4006-9CBA-22570909DD10 v5.1 WinHttp Auto-Proxy Service
Bindings:
          ncalrpc:[27c99237-d09c-4960-99aa-0185c6c58f97]
          ncalrpc:[LRPC-6fd94d330f0163892c]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 2FB92682-6599-42DC-AE13-BD2CA89BD11C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-ce9b4352c9895514ae]
          ncalrpc:[LRPC-3df9c3678efd411b94]
          ncalrpc:[LRPC-76ed32a6aaa5e6d559]
          ncalrpc:[LRPC-edde97c13478b8d1ea]

Protocol: N/A
Provider: N/A
UUID    : F47433C3-3E9D-4157-AAD4-83AA1F5C2D4C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-3df9c3678efd411b94]
          ncalrpc:[LRPC-76ed32a6aaa5e6d559]
          ncalrpc:[LRPC-edde97c13478b8d1ea]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 7F9D11BF-7FB9-436B-A812-B2D50C5D4C03 v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-76ed32a6aaa5e6d559]
          ncalrpc:[LRPC-edde97c13478b8d1ea]

Protocol: N/A
Provider: BFE.DLL
UUID    : DD490425-5325-4565-B774-7E27D6C09C24 v1.0 Base Firewall Engine API
Bindings:
          ncalrpc:[LRPC-edde97c13478b8d1ea]

Protocol: N/A
Provider: certprop.dll
UUID    : 30B044A5-A225-43F0-B3A4-E060DF91F9C1 v1.0
Bindings:
          ncalrpc:[LRPC-8e0e8c99fd5c4bd82b]

Protocol: N/A
Provider: N/A
UUID    : 29770A8F-829B-4158-90A2-78CD488501F7 v1.0
Bindings:
          ncacn_ip_tcp:172.16.185.12[49668]
          ncacn_np:\\DEV04[\pipe\SessEnvPublicRpc]
          ncalrpc:[SessEnvPrivateRpc]
          ncalrpc:[LRPC-11cbceb7d13e35fda8]

Protocol: N/A
Provider: N/A
UUID    : C49A5A70-8A7F-4E70-BA16-1E8F1F193EF1 v1.0 Adh APIs
Bindings:
          ncalrpc:[OLEC586F4C61E63045485146A115B30]
          ncalrpc:[TeredoControl]
          ncalrpc:[TeredoDiagnostics]
          ncalrpc:[LRPC-741758e9cf6c671987]

Protocol: N/A
Provider: N/A
UUID    : C36BE077-E14B-4FE9-8ABC-E856EF4F048B v1.0 Proxy Manager client server endpoint
Bindings:
          ncalrpc:[TeredoControl]
          ncalrpc:[TeredoDiagnostics]
          ncalrpc:[LRPC-741758e9cf6c671987]

Protocol: N/A
Provider: N/A
UUID    : 2E6035B2-E8F1-41A7-A044-656B439C4C34 v1.0 Proxy Manager provider server endpoint
Bindings:
          ncalrpc:[TeredoControl]
          ncalrpc:[TeredoDiagnostics]
          ncalrpc:[LRPC-741758e9cf6c671987]

Protocol: N/A
Provider: iphlpsvc.dll
UUID    : 552D076A-CB29-4E44-8B6A-D15E59E2C0AF v1.0 IP Transition Configuration endpoint
Bindings:
          ncalrpc:[LRPC-741758e9cf6c671987]

Protocol: N/A
Provider: N/A
UUID    : 13560FA9-8C09-4B56-A1FD-04D083B9B2A1 v1.0
Bindings:
          ncalrpc:[LRPC-dca595bf87f34a6752]
          ncalrpc:[OLE5E6597B537E5A1133550825A23D4]

Protocol: N/A
Provider: N/A
UUID    : C2D1B5DD-FA81-4460-9DD6-E7658B85454B v1.0
Bindings:
          ncalrpc:[LRPC-dca595bf87f34a6752]
          ncalrpc:[OLE5E6597B537E5A1133550825A23D4]

Protocol: N/A
Provider: N/A
UUID    : F44E62AF-DAB1-44C2-8013-049A9DE417D6 v1.0
Bindings:
          ncalrpc:[LRPC-dca595bf87f34a6752]
          ncalrpc:[OLE5E6597B537E5A1133550825A23D4]

Protocol: N/A
Provider: N/A
UUID    : B37F900A-EAE4-4304-A2AB-12BB668C0188 v1.0
Bindings:
          ncalrpc:[LRPC-dca595bf87f34a6752]
          ncalrpc:[OLE5E6597B537E5A1133550825A23D4]

Protocol: N/A
Provider: N/A
UUID    : ABFB6CA3-0C5E-4734-9285-0AEE72FE8D1C v1.0
Bindings:
          ncalrpc:[LRPC-dca595bf87f34a6752]
          ncalrpc:[OLE5E6597B537E5A1133550825A23D4]

Protocol: N/A
Provider: N/A
UUID    : 509BC7AE-77BE-4EE8-B07C-0D096BB44345 v1.0
Bindings:
          ncalrpc:[LRPC-9252c461ad7dd68353]
          ncalrpc:[OLEE947176914AE32587B635A58BB37]

Protocol: N/A
Provider: sysmain.dll
UUID    : B58AA02E-2884-4E97-8176-4EE06D794184 v1.0
Bindings:
          ncalrpc:[LRPC-3782e492f25053826c]

Protocol: N/A
Provider: IKEEXT.DLL
UUID    : A398E520-D59A-4BDD-AA7A-3C1E0303A511 v1.0 IKE/Authip API
Bindings:
          ncalrpc:[LRPC-1817380725beec8709]

Protocol: N/A
Provider: N/A
UUID    : 1A0D010F-1C33-432C-B0F5-8CF4E8053099 v1.0 IdSegSrv service
Bindings:
          ncalrpc:[LRPC-61f1855d14a86a18ef]

Protocol: N/A
Provider: srvsvc.dll
UUID    : 98716D03-89AC-44C7-BB8C-285824E51C4A v1.0 XactSrv service
Bindings:
          ncalrpc:[LRPC-61f1855d14a86a18ef]

Protocol: [MS-SCMR]: Service Control Manager Remote Protocol
Provider: services.exe
UUID    : 367ABB81-9844-35F1-AD32-98F038001003 v2.0
Bindings:
          ncacn_ip_tcp:172.16.185.12[49670]

Protocol: N/A
Provider: N/A
UUID    : 0D3C7F20-1C8D-4654-A1B3-51563B298BDA v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-c112d30b2af349f66c]
          ncalrpc:[OLE20067E59CA6AF4614FF776EC7719]

Protocol: N/A
Provider: N/A
UUID    : B18FBAB6-56F8-4702-84E0-41053293A869 v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-c112d30b2af349f66c]
          ncalrpc:[OLE20067E59CA6AF4614FF776EC7719]

Protocol: N/A
Provider: N/A
UUID    : 98CD761E-E77D-41C8-A3C0-0FB756D90EC2 v1.0
Bindings:
          ncalrpc:[LRPC-b1214a3c974e053522]
          ncalrpc:[OLE86F967A68E1974DBB412970490F4]

Protocol: N/A
Provider: N/A
UUID    : D22895EF-AFF4-42C5-A5B2-B14466D34AB4 v1.0
Bindings:
          ncalrpc:[LRPC-b1214a3c974e053522]
          ncalrpc:[OLE86F967A68E1974DBB412970490F4]

Protocol: N/A
Provider: N/A
UUID    : E38F5360-8572-473E-B696-1B46873BEEAB v1.0
Bindings:
          ncalrpc:[LRPC-b1214a3c974e053522]
          ncalrpc:[OLE86F967A68E1974DBB412970490F4]

Protocol: N/A
Provider: N/A
UUID    : 95095EC8-32EA-4EB0-A3E2-041F97B36168 v1.0
Bindings:
          ncalrpc:[LRPC-b1214a3c974e053522]
          ncalrpc:[OLE86F967A68E1974DBB412970490F4]

Protocol: N/A
Provider: N/A
UUID    : FD8BE72B-A9CD-4B2C-A9CA-4DED242FBE4D v1.0
Bindings:
          ncalrpc:[LRPC-b1214a3c974e053522]
          ncalrpc:[OLE86F967A68E1974DBB412970490F4]

Protocol: N/A
Provider: N/A
UUID    : 4C9DBF19-D39E-4BB9-90EE-8F7179B20283 v1.0
Bindings:
          ncalrpc:[LRPC-b1214a3c974e053522]
          ncalrpc:[OLE86F967A68E1974DBB412970490F4]

Protocol: N/A
Provider: N/A
UUID    : D4051BDE-9CDD-4910-B393-4AA85EC3C482 v1.0
Bindings:
          ncalrpc:[LRPC-b1214a3c974e053522]
          ncalrpc:[OLE86F967A68E1974DBB412970490F4]

Protocol: N/A
Provider: N/A
UUID    : 7DF1CEAE-DE4E-4E6F-AB14-49636E7C2052 v1.0
Bindings:
          ncalrpc:[LRPC-6eb7f83f0b016de782]

Protocol: N/A
Provider: N/A
UUID    : 650A7E26-EAB8-5533-CE43-9C1DFCE11511 v1.0 Vpn APIs
Bindings:
          ncalrpc:[LRPC-223d1d331b3a84fa5e]
          ncalrpc:[VpnikeRpc]
          ncalrpc:[RasmanLrpc]
          ncacn_np:\\DEV04[\PIPE\ROUTER]

Protocol: [MS-FASP]: Firewall and Advanced Security Protocol
Provider: FwRemoteSvr.dll
UUID    : 6B5BDD1E-528C-422C-AF8C-A4079BE4FE48 v1.0 Remote Fw APIs
Bindings:
          ncacn_ip_tcp:172.16.185.12[49671]
          ncalrpc:[ipsec]

Protocol: [MS-CMPO]: MSDTC Connection Manager:
Provider: msdtcprx.dll
UUID    : 906B0CE0-C70B-1067-B317-00DD010662DA v1.0
Bindings:
          ncalrpc:[LRPC-86119ef16ffdc2d806]
          ncalrpc:[OLE45A622E23D10A0109AFDCF01E08D]
          ncalrpc:[LRPC-148601dbdb732200ef]
          ncalrpc:[LRPC-148601dbdb732200ef]
          ncalrpc:[LRPC-148601dbdb732200ef]

Protocol: N/A
Provider: winlogon.exe
UUID    : 12E65DD8-887F-41EF-91BF-8D816C42C2E7 v1.0 Secure Desktop LRPC interface
Bindings:
          ncalrpc:[WMsgKRpc098601]

Protocol: N/A
Provider: N/A
UUID    : D249BD56-4CC0-4FD3-8CE6-6FE050D590CB v0.0
Bindings:
          ncalrpc:[LRPC-9f253a22a9c0d5704c]

Protocol: N/A
Provider: N/A
UUID    : D8140E00-5C46-4AE6-80AC-2F9A76DF224C v0.0
Bindings:
          ncalrpc:[LRPC-9f253a22a9c0d5704c]

Protocol: N/A
Provider: N/A
UUID    : B1EF227E-DFA5-421E-82BB-67A6A129C496 v0.0
Bindings:
          ncalrpc:[LRPC-ddde2e6e71d1587ff5]
          ncalrpc:[OLE179A99AD0A8C4AFECC663C242915]

Protocol: N/A
Provider: N/A
UUID    : 0FC77B1A-95D8-4A2E-A0C0-CFF54237462B v0.0
Bindings:
          ncalrpc:[LRPC-ddde2e6e71d1587ff5]
          ncalrpc:[OLE179A99AD0A8C4AFECC663C242915]

Protocol: N/A
Provider: N/A
UUID    : 8EC21E98-B5CE-4916-A3D6-449FA428A007 v0.0
Bindings:
          ncalrpc:[LRPC-ddde2e6e71d1587ff5]
          ncalrpc:[OLE179A99AD0A8C4AFECC663C242915]

Protocol: N/A
Provider: appinfo.dll
UUID    : 58E604E8-9ADB-4D2E-A464-3B0683FB1480 v1.0 AppInfo
Bindings:
          ncalrpc:[LRPC-8a9bb8dd923394cd42]

Protocol: N/A
Provider: appinfo.dll
UUID    : FD7A0523-DC70-43DD-9B2E-9C5ED48225B1 v1.0 AppInfo
Bindings:
          ncalrpc:[LRPC-8a9bb8dd923394cd42]

Protocol: N/A
Provider: appinfo.dll
UUID    : 5F54CE7D-5B79-4175-8584-CB65313A0E98 v1.0 AppInfo
Bindings:
          ncalrpc:[LRPC-8a9bb8dd923394cd42]

Protocol: N/A
Provider: appinfo.dll
UUID    : 201EF99A-7FA0-444C-9399-19BA84F12A1A v1.0 AppInfo
Bindings:
          ncalrpc:[LRPC-8a9bb8dd923394cd42]

Protocol: N/A
Provider: N/A
UUID    : 0497B57D-2E66-424F-A0C6-157CD5D41700 v1.0 AppInfo
Bindings:
          ncalrpc:[LRPC-8a9bb8dd923394cd42]

Protocol: N/A
Provider: pcasvc.dll
UUID    : 0767A036-0D22-48AA-BA69-B619480F38CB v1.0 PcaSvc
Bindings:
          ncalrpc:[LRPC-4814ae967e5c45ba9e]

Protocol: N/A
Provider: N/A
UUID    : A4B8D482-80CE-40D6-934D-B22A01A44FE7 v1.0 LicenseManager
Bindings:
          ncalrpc:[LicenseServiceEndpoint]

Protocol: N/A
Provider: N/A
UUID    : BF4DC912-E52F-4904-8EBE-9317C1BDD497 v1.0
Bindings:
          ncalrpc:[LRPC-0f38c67258a72bb0bd]
          ncalrpc:[OLE97EC4EEEB472F416797A46CF0390]

[*] Received 350 endpoints.


```
