```bash
impacket-rpcdump -port 135 10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp135/tcp_135_rpc_rpcdump.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp135/tcp_135_rpc_rpcdump.txt):

```
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Retrieving endpoint list from 10.10.10.169
Protocol: [MS-RSP]: Remote Shutdown Protocol
Provider: wininit.exe
UUID    : D95AFE70-A6D5-4259-822E-2C84DA1DDB0D v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.169[49664]
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\RESOLUTE[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc07E380]

Protocol: N/A
Provider: winlogon.exe
UUID    : 76F226C3-EC14-4325-8A99-6A46348418AF v1.0
Bindings:
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\RESOLUTE[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc07E380]
          ncalrpc:[WMsgKRpc07EB61]

Protocol: N/A
Provider: N/A
UUID    : D09BDEB5-6171-4A34-BFE2-06FA82652568 v1.0
Bindings:
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-b0e1a71e2880e5763e]
          ncalrpc:[LRPC-847638a3be4588eafe]
          ncacn_np:\\RESOLUTE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-fe5099d69106c48d0a]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-847638a3be4588eafe]
          ncacn_np:\\RESOLUTE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-fe5099d69106c48d0a]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-1f98e993e546ed33ef]
          ncalrpc:[LRPC-7aebf6781d586a4002]
          ncacn_ip_tcp:10.10.10.169[49665]
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]
          ncacn_np:\\RESOLUTE[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: N/A
Provider: N/A
UUID    : 697DCDA9-3BA9-4EB2-9247-E11F1901B0D2 v1.0
Bindings:
          ncalrpc:[LRPC-b0e1a71e2880e5763e]
          ncalrpc:[LRPC-847638a3be4588eafe]
          ncacn_np:\\RESOLUTE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-fe5099d69106c48d0a]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: sysntfy.dll
UUID    : C9AC6DB5-82B7-4E55-AE8A-E464ED7B4277 v1.0 Impl friendly name
Bindings:
          ncalrpc:[LRPC-fe5099d69106c48d0a]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]
          ncalrpc:[IUserProfile2]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE066639720FBA1BFC04535D12CFD2]
          ncacn_ip_tcp:10.10.10.169[49667]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\RESOLUTE[\pipe\lsass]

Protocol: [MS-PCQ]: Performance Counter Query Protocol
Provider: regsvc.dll
UUID    : DA5A86C5-12C2-4943-AB30-7F74A813D853 v1.0 RemoteRegistry Perflib Interface
Bindings:
          ncacn_np:\\RESOLUTE[\PIPE\winreg]

Protocol: [MS-RRP]: Windows Remote Registry Protocol
Provider: regsvc.dll
UUID    : 338CD001-2244-31F1-AAAA-900038001003 v1.0 RemoteRegistry Interface
Bindings:
          ncacn_np:\\RESOLUTE[\PIPE\winreg]

Protocol: N/A
Provider: N/A
UUID    : 3473DD4D-2E88-4006-9CBA-22570909DD10 v5.1 WinHttp Auto-Proxy Service
Bindings:
          ncalrpc:[OLE28BB3FCCA20C9CB114B86E0C2906]
          ncalrpc:[LRPC-324c9fe7793c51304f]

Protocol: N/A
Provider: nsisvc.dll
UUID    : 7EA70BCF-48AF-4F6A-8968-6A440754D5FA v1.0 NSI server endpoint
Bindings:
          ncalrpc:[LRPC-324c9fe7793c51304f]

Protocol: N/A
Provider: N/A
UUID    : 0D3C7F20-1C8D-4654-A1B3-51563B298BDA v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-3166d2bba7188df3ad]
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: N/A
UUID    : B18FBAB6-56F8-4702-84E0-41053293A869 v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-3166d2bba7188df3ad]
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: N/A
UUID    : C49A5A70-8A7F-4E70-BA16-1E8F1F193EF1 v1.0 Adh APIs
Bindings:
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: N/A
UUID    : C36BE077-E14B-4FE9-8ABC-E856EF4F048B v1.0 Proxy Manager client server endpoint
Bindings:
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: N/A
UUID    : 2E6035B2-E8F1-41A7-A044-656B439C4C34 v1.0 Proxy Manager provider server endpoint
Bindings:
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: iphlpsvc.dll
UUID    : 552D076A-CB29-4E44-8B6A-D15E59E2C0AF v1.0 IP Transition Configuration endpoint
Bindings:
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: IKEEXT.DLL
UUID    : A398E520-D59A-4BDD-AA7A-3C1E0303A511 v1.0 IKE/Authip API
Bindings:
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: N/A
UUID    : 3A9EF155-691D-4449-8D05-09AD57031823 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: schedsvc.dll
UUID    : 86D35949-83C9-4044-B424-DB363231FD0C v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.169[49666]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 378E52B0-C0A9-11CF-822D-00AA0051E40F v1.0
Bindings:
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 1FF70682-0A51-30E8-076D-740BE8CEE98B v1.0
Bindings:
          ncacn_np:\\RESOLUTE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: schedsvc.dll
UUID    : 0A74EF1C-41A4-4E06-83AE-DC74FB1CDD53 v1.0
Bindings:
          ncalrpc:[senssvc]
          ncalrpc:[OLEE9B886A61590C4D14A2E70C0C483]
          ncalrpc:[IUserProfile2]

Protocol: N/A
Provider: gpsvc.dll
UUID    : 2EB08E3E-639F-4FBA-97B1-14F878961076 v1.0 Group Policy RPC Interface
Bindings:
          ncalrpc:[LRPC-c0c7d2efad7b809338]

Protocol: N/A
Provider: N/A
UUID    : A500D4C6-0DD1-4543-BC0C-D5F93486EAF8 v1.0
Bindings:
          ncalrpc:[LRPC-b17255792d8ddbc8dd]
          ncalrpc:[LRPC-1f98e993e546ed33ef]
          ncalrpc:[LRPC-7aebf6781d586a4002]
          ncacn_ip_tcp:10.10.10.169[49665]
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]
          ncacn_np:\\RESOLUTE[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: N/A
Provider: nrpsrv.dll
UUID    : 30ADC50C-5CBC-46CE-9A0E-91914789E23C v1.0 NRP server endpoint
Bindings:
          ncalrpc:[LRPC-7aebf6781d586a4002]
          ncacn_ip_tcp:10.10.10.169[49665]
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]
          ncacn_np:\\RESOLUTE[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: [MS-EVEN6]: EventLog Remoting Protocol
Provider: wevtsvc.dll
UUID    : F6BEAFF7-1E19-4FBB-9F8F-B89E2018337C v1.0 Event log TCPIP
Bindings:
          ncacn_ip_tcp:10.10.10.169[49665]
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]
          ncacn_np:\\RESOLUTE[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: N/A
Provider: dhcpcsvc6.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D6 v1.0 DHCPv6 Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]
          ncacn_np:\\RESOLUTE[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: N/A
Provider: dhcpcsvc.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D5 v1.0 DHCP Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc]
          ncacn_np:\\RESOLUTE[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: N/A
Provider: N/A
UUID    : 7F1343FE-50A9-4927-A778-0C5859517BAC v1.0 DfsDs service
Bindings:
          ncacn_np:\\RESOLUTE[\PIPE\wkssvc]
          ncalrpc:[LRPC-aa3d9b0653c3996766]
          ncalrpc:[DNSResolver]

Protocol: N/A
Provider: N/A
UUID    : EB081A0D-10EE-478A-A1DD-50995283E7A8 v3.0 Witness Client Test Interface
Bindings:
          ncalrpc:[LRPC-aa3d9b0653c3996766]
          ncalrpc:[DNSResolver]

Protocol: N/A
Provider: N/A
UUID    : F2C9B409-C1C9-4100-8639-D8AB1486694A v1.0 Witness Client Upcall Server
Bindings:
          ncalrpc:[LRPC-aa3d9b0653c3996766]
          ncalrpc:[DNSResolver]

Protocol: N/A
Provider: N/A
UUID    : DF4DF73A-C52D-4E3A-8003-8437FDF8302A v0.0 WM_WindowManagerRPC\Server
Bindings:
          ncalrpc:[LRPC-2225ba370d5aba64c4]
          ncalrpc:[OLE1238E4ED0F0E7F52A9AA3931BD14]
          ncalrpc:[LRPC-11f446e9eb29e0501d]
          ncalrpc:[LRPC-fe228235aba0f8a3ab]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 2FB92682-6599-42DC-AE13-BD2CA89BD11C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-11f446e9eb29e0501d]
          ncalrpc:[LRPC-fe228235aba0f8a3ab]

Protocol: N/A
Provider: N/A
UUID    : F47433C3-3E9D-4157-AAD4-83AA1F5C2D4C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-11f446e9eb29e0501d]
          ncalrpc:[LRPC-fe228235aba0f8a3ab]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 7F9D11BF-7FB9-436B-A812-B2D50C5D4C03 v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-11f446e9eb29e0501d]
          ncalrpc:[LRPC-fe228235aba0f8a3ab]

Protocol: N/A
Provider: BFE.DLL
UUID    : DD490425-5325-4565-B774-7E27D6C09C24 v1.0 Base Firewall Engine API
Bindings:
          ncalrpc:[LRPC-fe228235aba0f8a3ab]

Protocol: [MS-FASP]: Firewall and Advanced Security Protocol
Provider: FwRemoteSvr.dll
UUID    : 6B5BDD1E-528C-422C-AF8C-A4079BE4FE48 v1.0 Remote Fw APIs
Bindings:
          ncacn_ip_tcp:10.10.10.169[49671]
          ncalrpc:[ipsec]

Protocol: N/A
Provider: efssvc.dll
UUID    : 04EEB297-CBF4-466B-8A2A-BFD6A2F10BBA v1.0 EFSK RPC Interface
Bindings:
          ncacn_np:\\RESOLUTE[\pipe\efsrpc]
          ncalrpc:[LRPC-bb109787116fe59468]

Protocol: N/A
Provider: efssvc.dll
UUID    : DF1941C5-FE89-4E79-BF10-463657ACF44D v1.0 EFS RPC Interface
Bindings:
          ncacn_np:\\RESOLUTE[\pipe\efsrpc]
          ncalrpc:[LRPC-bb109787116fe59468]

Protocol: [MS-NRPC]: Netlogon Remote Protocol
Provider: netlogon.dll
UUID    : 12345678-1234-ABCD-EF00-01234567CFFB v1.0
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.169[49677]
          ncacn_np:\\RESOLUTE[\pipe\d9ad01a0b7c9240f]
          ncacn_http:10.10.10.169[49676]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE066639720FBA1BFC04535D12CFD2]
          ncacn_ip_tcp:10.10.10.169[49667]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\RESOLUTE[\pipe\lsass]

Protocol: [MS-RAA]: Remote Authorization API Protocol
Provider: N/A
UUID    : 0B1C2170-5732-4E0E-8CD3-D9B16F3B84D7 v0.0 RemoteAccessCheck
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.169[49677]
          ncacn_np:\\RESOLUTE[\pipe\d9ad01a0b7c9240f]
          ncacn_http:10.10.10.169[49676]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE066639720FBA1BFC04535D12CFD2]
          ncacn_ip_tcp:10.10.10.169[49667]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\RESOLUTE[\pipe\lsass]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.169[49677]
          ncacn_np:\\RESOLUTE[\pipe\d9ad01a0b7c9240f]
          ncacn_http:10.10.10.169[49676]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE066639720FBA1BFC04535D12CFD2]
          ncacn_ip_tcp:10.10.10.169[49667]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\RESOLUTE[\pipe\lsass]

Protocol: [MS-SAMR]: Security Account Manager (SAM) Remote Protocol
Provider: samsrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AC v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.169[49677]
          ncacn_np:\\RESOLUTE[\pipe\d9ad01a0b7c9240f]
          ncacn_http:10.10.10.169[49676]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE066639720FBA1BFC04535D12CFD2]
          ncacn_ip_tcp:10.10.10.169[49667]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\RESOLUTE[\pipe\lsass]

Protocol: [MS-LSAT]: Local Security Authority (Translation Methods) Remote
Provider: lsasrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AB v0.0
Bindings:
          ncacn_np:\\RESOLUTE[\pipe\d9ad01a0b7c9240f]
          ncacn_http:10.10.10.169[49676]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE066639720FBA1BFC04535D12CFD2]
          ncacn_ip_tcp:10.10.10.169[49667]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\RESOLUTE[\pipe\lsass]

Protocol: [MS-DRSR]: Directory Replication Service (DRS) Remote Protocol
Provider: ntdsai.dll
UUID    : E3514235-4B06-11D1-AB04-00C04FC2DCD2 v4.0 MS NT Directory DRS Interface
Bindings:
          ncacn_np:\\RESOLUTE[\pipe\d9ad01a0b7c9240f]
          ncacn_http:10.10.10.169[49676]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE066639720FBA1BFC04535D12CFD2]
          ncacn_ip_tcp:10.10.10.169[49667]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncalrpc:[lsacap]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[securityevent]
          ncalrpc:[audit]
          ncacn_np:\\RESOLUTE[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : 1A0D010F-1C33-432C-B0F5-8CF4E8053099 v1.0 IdSegSrv service
Bindings:
          ncalrpc:[LRPC-6af9e9d82bbc1e9fca]

Protocol: N/A
Provider: srvsvc.dll
UUID    : 98716D03-89AC-44C7-BB8C-285824E51C4A v1.0 XactSrv service
Bindings:
          ncalrpc:[LRPC-6af9e9d82bbc1e9fca]

Protocol: N/A
Provider: N/A
UUID    : E38F5360-8572-473E-B696-1B46873BEEAB v1.0
Bindings:
          ncalrpc:[LRPC-12ceb51b69cee56e00]

Protocol: N/A
Provider: N/A
UUID    : 4C9DBF19-D39E-4BB9-90EE-8F7179B20283 v1.0
Bindings:
          ncalrpc:[LRPC-12ceb51b69cee56e00]

Protocol: [MS-CMPO]: MSDTC Connection Manager:
Provider: msdtcprx.dll
UUID    : 906B0CE0-C70B-1067-B317-00DD010662DA v1.0
Bindings:
          ncalrpc:[LRPC-7be841a81136df569a]
          ncalrpc:[OLE71828F335AC633D6AD38B38C2CA8]
          ncalrpc:[LRPC-1224c7260a1750294c]
          ncalrpc:[LRPC-1224c7260a1750294c]
          ncalrpc:[LRPC-1224c7260a1750294c]

Protocol: [MS-SCMR]: Service Control Manager Remote Protocol
Provider: services.exe
UUID    : 367ABB81-9844-35F1-AD32-98F038001003 v2.0
Bindings:
          ncacn_ip_tcp:10.10.10.169[49688]

Protocol: N/A
Provider: winlogon.exe
UUID    : 12E65DD8-887F-41EF-91BF-8D816C42C2E7 v1.0 Secure Desktop LRPC interface
Bindings:
          ncalrpc:[WMsgKRpc07EB61]

Protocol: [MS-FRS2]: Distributed File System Replication Protocol
Provider: dfsrmig.exe
UUID    : 897E2E5F-93F3-4376-9C9C-FD2277495C27 v1.0 Frs2 Service
Bindings:
          ncacn_ip_tcp:10.10.10.169[49919]
          ncalrpc:[OLE736D80A42B1F3ED319E8345BE8F8]

Protocol: [MS-DNSP]: Domain Name Service (DNS) Server Management
Provider: dns.exe
UUID    : 50ABC2A4-574D-40B3-9D66-EE4FD5FBA076 v5.0
Bindings:
          ncacn_ip_tcp:10.10.10.169[50024]

[*] Received 297 endpoints.


```
