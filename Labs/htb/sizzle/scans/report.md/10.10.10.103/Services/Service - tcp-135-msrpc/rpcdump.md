```bash
impacket-rpcdump -port 135 10.10.10.103
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp135/tcp_135_rpc_rpcdump.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp135/tcp_135_rpc_rpcdump.txt):

```
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Retrieving endpoint list from 10.10.10.103
Protocol: [MS-RSP]: Remote Shutdown Protocol
Provider: wininit.exe
UUID    : D95AFE70-A6D5-4259-822E-2C84DA1DDB0D v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.103[49664]
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\SIZZLE[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc08AF70]

Protocol: N/A
Provider: winlogon.exe
UUID    : 76F226C3-EC14-4325-8A99-6A46348418AF v1.0
Bindings:
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\SIZZLE[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc08AF70]
          ncalrpc:[WMsgKRpc08BCE1]

Protocol: N/A
Provider: N/A
UUID    : FC48CD89-98D6-4628-9839-86F7A3E4161A v1.0
Bindings:
          ncalrpc:[OLE1E7BB9743DB68582750E277469F0]
          ncalrpc:[LRPC-d77c3ed6f4294baac6]
          ncalrpc:[dabrpc]
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-4bb688238679e29534]
          ncalrpc:[LRPC-a5a37f58263b7eaeb2]
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 9B008953-F195-4BF9-BDE0-4471971E58ED v1.0
Bindings:
          ncalrpc:[LRPC-d77c3ed6f4294baac6]
          ncalrpc:[dabrpc]
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-4bb688238679e29534]
          ncalrpc:[LRPC-a5a37f58263b7eaeb2]
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : D09BDEB5-6171-4A34-BFE2-06FA82652568 v1.0
Bindings:
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-4bb688238679e29534]
          ncalrpc:[LRPC-a5a37f58263b7eaeb2]
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-a5a37f58263b7eaeb2]
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-4009d74460c9eae4e6]
          ncalrpc:[LRPC-7983c75cb7fed95f56]
          ncalrpc:[LRPC-77065b526c601a86f0]

Protocol: N/A
Provider: N/A
UUID    : 697DCDA9-3BA9-4EB2-9247-E11F1901B0D2 v1.0
Bindings:
          ncalrpc:[LRPC-4bb688238679e29534]
          ncalrpc:[LRPC-a5a37f58263b7eaeb2]
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 857FB1BE-084F-4FB5-B59C-4B2C4BE5F0CF v1.0
Bindings:
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : B8CADBAF-E84B-46B9-84F2-6F71C03F9E55 v1.0
Bindings:
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 20C40295-8DBA-48E6-AEBF-3E78EF3BB144 v1.0
Bindings:
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2513BCBE-6CD4-4348-855E-7EFB3C336DD3 v1.0
Bindings:
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 88ABCBC3-34EA-76AE-8215-767520655A23 v0.0
Bindings:
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 76C217BC-C8B4-4201-A745-373AD9032B1A v1.0
Bindings:
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 55E6B932-1979-45D6-90C5-7F6270724112 v1.0
Bindings:
          ncalrpc:[LRPC-94b00f7e604f8c3ebb]
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 4DACE966-A243-4450-AE3F-9B7BCB5315B8 v1.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 1832BCF6-CAB8-41D4-85D2-C9410764F75A v1.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : C521FACF-09A9-42C5-B155-72388595CBF0 v0.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2C7FD9CE-E706-4B40-B412-953107EF9BB0 v0.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 0D3E2735-CEA0-4ECC-A9E2-41A2D81AED4E v1.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : C605F9FB-F0A3-4E2A-A073-73560F8D9E3E v1.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 1B37CA91-76B1-4F5E-A3C7-2ABFC61F2BB0 v1.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 8BFC3BE1-6DEF-4E2D-AF74-7C47CD0ADE4A v1.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2D98A740-581D-41B9-AA0D-A88B9D5CE938 v1.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\LSM_API_service]
          ncalrpc:[LSMApi]
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: sysntfy.dll
UUID    : C9AC6DB5-82B7-4E55-AE8A-E464ED7B4277 v1.0 Impl friendly name
Bindings:
          ncalrpc:[LRPC-dc09bfcdd96f004eec]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
          ncalrpc:[samss lpc]
          ncalrpc:[SidKey Local End Point]
          ncalrpc:[protected_storage]
          ncalrpc:[lsasspirpc]
          ncalrpc:[lsapolicylookup]
          ncalrpc:[LSA_EAS_ENDPOINT]
          ncacn_np:\\SIZZLE[\pipe\lsass]
          ncalrpc:[audit]
          ncalrpc:[securityevent]
          ncalrpc:[LSARPC_ENDPOINT]
          ncalrpc:[lsacap]

Protocol: N/A
Provider: N/A
UUID    : 5824833B-3C1A-4AD2-BDFD-C31D19E23ED2 v1.0
Bindings:
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : BDAA0970-413B-4A3E-9E5D-F6DC9D7E0760 v1.0
Bindings:
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 3B338D89-6CFA-44B8-847E-531531BC9992 v1.0
Bindings:
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 8782D3B9-EBBD-4644-A3D8-E8725381919B v1.0
Bindings:
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 085B0334-E454-4D91-9B8C-4134F9E793F3 v1.0
Bindings:
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 4BEC6BB8-B5C2-4B6F-B2C1-5DA5CF92D0D9 v1.0
Bindings:
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: appidsvc.dll
UUID    : 8A7B5006-CC13-11DB-9705-005056C00008 v1.0 AppIDSvc
Bindings:
          ncalrpc:[LRPC-dec8dad58bd8109c3b]

Protocol: N/A
Provider: N/A
UUID    : A4B8D482-80CE-40D6-934D-B22A01A44FE7 v1.0 LicenseManager
Bindings:
          ncalrpc:[LicenseServiceEndpoint]

Protocol: [MS-PCQ]: Performance Counter Query Protocol
Provider: regsvc.dll
UUID    : DA5A86C5-12C2-4943-AB30-7F74A813D853 v1.0 RemoteRegistry Perflib Interface
Bindings:
          ncacn_np:\\SIZZLE[\PIPE\winreg]

Protocol: [MS-RRP]: Windows Remote Registry Protocol
Provider: regsvc.dll
UUID    : 338CD001-2244-31F1-AAAA-900038001003 v1.0 RemoteRegistry Interface
Bindings:
          ncacn_np:\\SIZZLE[\PIPE\winreg]

Protocol: N/A
Provider: N/A
UUID    : 3473DD4D-2E88-4006-9CBA-22570909DD10 v5.1 WinHttp Auto-Proxy Service
Bindings:
          ncalrpc:[OLE449218805A40D0ADD69C08C084EC]
          ncalrpc:[LRPC-d6d3f4d9690fd1d445]

Protocol: N/A
Provider: nsisvc.dll
UUID    : 7EA70BCF-48AF-4F6A-8968-6A440754D5FA v1.0 NSI server endpoint
Bindings:
          ncalrpc:[LRPC-d6d3f4d9690fd1d445]

Protocol: [MS-EVEN6]: EventLog Remoting Protocol
Provider: wevtsvc.dll
UUID    : F6BEAFF7-1E19-4FBB-9F8F-B89E2018337C v1.0 Event log TCPIP
Bindings:
          ncacn_ip_tcp:10.10.10.103[49665]
          ncacn_np:\\SIZZLE[\pipe\eventlog]
          ncalrpc:[eventlog]
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]
          ncalrpc:[LRPC-edde9aee41942fc0c9]
          ncalrpc:[LRPC-4009d74460c9eae4e6]
          ncalrpc:[LRPC-7983c75cb7fed95f56]

Protocol: N/A
Provider: dhcpcsvc6.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D6 v1.0 DHCPv6 Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]
          ncalrpc:[LRPC-edde9aee41942fc0c9]
          ncalrpc:[LRPC-4009d74460c9eae4e6]
          ncalrpc:[LRPC-7983c75cb7fed95f56]

Protocol: N/A
Provider: dhcpcsvc.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D5 v1.0 DHCP Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc]
          ncalrpc:[LRPC-edde9aee41942fc0c9]
          ncalrpc:[LRPC-4009d74460c9eae4e6]
          ncalrpc:[LRPC-7983c75cb7fed95f56]

Protocol: N/A
Provider: N/A
UUID    : A500D4C6-0DD1-4543-BC0C-D5F93486EAF8 v1.0
Bindings:
          ncalrpc:[LRPC-edde9aee41942fc0c9]
          ncalrpc:[LRPC-4009d74460c9eae4e6]
          ncalrpc:[LRPC-7983c75cb7fed95f56]

Protocol: N/A
Provider: nrpsrv.dll
UUID    : 30ADC50C-5CBC-46CE-9A0E-91914789E23C v1.0 NRP server endpoint
Bindings:
          ncalrpc:[LRPC-7983c75cb7fed95f56]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 2FB92682-6599-42DC-AE13-BD2CA89BD11C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-d84544f9e9d7ec0ce3]
          ncalrpc:[LRPC-1b7cb5eb7900f12034]
          ncalrpc:[LRPC-200343b8b72e698f70]

Protocol: N/A
Provider: N/A
UUID    : F47433C3-3E9D-4157-AAD4-83AA1F5C2D4C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-d84544f9e9d7ec0ce3]
          ncalrpc:[LRPC-1b7cb5eb7900f12034]
          ncalrpc:[LRPC-200343b8b72e698f70]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 7F9D11BF-7FB9-436B-A812-B2D50C5D4C03 v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-d84544f9e9d7ec0ce3]
          ncalrpc:[LRPC-1b7cb5eb7900f12034]
          ncalrpc:[LRPC-200343b8b72e698f70]

Protocol: N/A
Provider: BFE.DLL
UUID    : DD490425-5325-4565-B774-7E27D6C09C24 v1.0 Base Firewall Engine API
Bindings:
          ncalrpc:[LRPC-1b7cb5eb7900f12034]
          ncalrpc:[LRPC-200343b8b72e698f70]

Protocol: N/A
Provider: N/A
UUID    : DF4DF73A-C52D-4E3A-8003-8437FDF8302A v0.0 WM_WindowManagerRPC\Server
Bindings:
          ncalrpc:[LRPC-200343b8b72e698f70]

Protocol: N/A
Provider: pcasvc.dll
UUID    : 0767A036-0D22-48AA-BA69-B619480F38CB v1.0 PcaSvc
Bindings:
          ncalrpc:[LRPC-922627e27888c236af]
          ncalrpc:[OLE3B41C6266517DC17AFA768FDBF09]
          ncalrpc:[LRPC-a16892f312b270d98e]
          ncalrpc:[LRPC-77065b526c601a86f0]

Protocol: N/A
Provider: N/A
UUID    : E40F7B57-7A25-4CD3-A135-7F7D3DF9D16B v1.0 Network Connection Broker server endpoint
Bindings:
          ncalrpc:[LRPC-922627e27888c236af]
          ncalrpc:[OLE3B41C6266517DC17AFA768FDBF09]
          ncalrpc:[LRPC-a16892f312b270d98e]
          ncalrpc:[LRPC-77065b526c601a86f0]

Protocol: N/A
Provider: N/A
UUID    : 880FD55E-43B9-11E0-B1A8-CF4EDFD72085 v1.0 KAPI Service endpoint
Bindings:
          ncalrpc:[LRPC-922627e27888c236af]
          ncalrpc:[OLE3B41C6266517DC17AFA768FDBF09]
          ncalrpc:[LRPC-a16892f312b270d98e]
          ncalrpc:[LRPC-77065b526c601a86f0]

Protocol: N/A
Provider: N/A
UUID    : 5222821F-D5E2-4885-84F1-5F6185A0EC41 v1.0 Network Connection Broker server endpoint for NCB Reset module
Bindings:
          ncalrpc:[LRPC-a16892f312b270d98e]
          ncalrpc:[LRPC-77065b526c601a86f0]

Protocol: N/A
Provider: N/A
UUID    : 572E35B4-1344-4565-96A1-F5DF3BFA89BB v1.0 LiveIdSvcNotify RPC Interface
Bindings:
          ncalrpc:[liveidsvcnotify]

Protocol: N/A
Provider: N/A
UUID    : FAF2447B-B348-4FEB-8DBE-BEEE5B7F7778 v1.0 OnlineProviderCert RPC Interface
Bindings:
          ncalrpc:[LRPC-22cc121946f156cf5e]

Protocol: N/A
Provider: N/A
UUID    : CC105610-DA03-467E-BC73-5B9E2937458D v1.0 LiveIdSvc RPC Interface
Bindings:
          ncalrpc:[LRPC-22cc121946f156cf5e]

Protocol: N/A
Provider: IKEEXT.DLL
UUID    : A398E520-D59A-4BDD-AA7A-3C1E0303A511 v1.0 IKE/Authip API
Bindings:
          ncalrpc:[LRPC-fbe218716143fae988]
          ncacn_ip_tcp:10.10.10.103[49669]
          ncalrpc:[LRPC-e0e3607a3f60a7009a]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: N/A
UUID    : 0D3C7F20-1C8D-4654-A1B3-51563B298BDA v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-fbe218716143fae988]
          ncacn_ip_tcp:10.10.10.103[49669]
          ncalrpc:[LRPC-e0e3607a3f60a7009a]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: N/A
UUID    : B18FBAB6-56F8-4702-84E0-41053293A869 v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-fbe218716143fae988]
          ncacn_ip_tcp:10.10.10.103[49669]
          ncalrpc:[LRPC-e0e3607a3f60a7009a]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: N/A
UUID    : 3A9EF155-691D-4449-8D05-09AD57031823 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.103[49669]
          ncalrpc:[LRPC-e0e3607a3f60a7009a]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: schedsvc.dll
UUID    : 86D35949-83C9-4044-B424-DB363231FD0C v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.103[49669]
          ncalrpc:[LRPC-e0e3607a3f60a7009a]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: N/A
UUID    : 33D84484-3626-47EE-8C6F-E7E98B113BE1 v2.0
Bindings:
          ncalrpc:[LRPC-e0e3607a3f60a7009a]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: N/A
UUID    : C49A5A70-8A7F-4E70-BA16-1E8F1F193EF1 v1.0 Adh APIs
Bindings:
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: N/A
UUID    : C36BE077-E14B-4FE9-8ABC-E856EF4F048B v1.0 Proxy Manager client server endpoint
Bindings:
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: N/A
UUID    : 2E6035B2-E8F1-41A7-A044-656B439C4C34 v1.0 Proxy Manager provider server endpoint
Bindings:
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: iphlpsvc.dll
UUID    : 552D076A-CB29-4E44-8B6A-D15E59E2C0AF v1.0 IP Transition Configuration endpoint
Bindings:
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 378E52B0-C0A9-11CF-822D-00AA0051E40F v1.0
Bindings:
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 1FF70682-0A51-30E8-076D-740BE8CEE98B v1.0
Bindings:
          ncacn_np:\\SIZZLE[\PIPE\atsvc]
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: schedsvc.dll
UUID    : 0A74EF1C-41A4-4E06-83AE-DC74FB1CDD53 v1.0
Bindings:
          ncalrpc:[senssvc]
          ncalrpc:[DeviceSetupManager]
          ncalrpc:[IUserProfile2]
          ncalrpc:[OLE9F3A4FE0781DE66959D78306BE44]

Protocol: N/A
Provider: gpsvc.dll
UUID    : 2EB08E3E-639F-4FBA-97B1-14F878961076 v1.0 Group Policy RPC Interface
Bindings:
          ncalrpc:[LRPC-3541bc07f9d274bd37]

Protocol: N/A
Provider: N/A
UUID    : 7AEB6705-3AE6-471A-882D-F39C109EDC12 v1.0
Bindings:
          ncalrpc:[LRPC-3b673e00a81c15b641]

Protocol: N/A
Provider: N/A
UUID    : E7F76134-9EF5-4949-A2D6-3368CC0988F3 v1.0
Bindings:
          ncalrpc:[LRPC-3b673e00a81c15b641]

Protocol: N/A
Provider: N/A
UUID    : B3781086-6A54-489B-91C8-51D067172AB7 v1.0
Bindings:
          ncalrpc:[LRPC-3b673e00a81c15b641]

Protocol: N/A
Provider: N/A
UUID    : B37F900A-EAE4-4304-A2AB-12BB668C0188 v1.0
Bindings:
          ncalrpc:[LRPC-3b673e00a81c15b641]

Protocol: N/A
Provider: N/A
UUID    : ABFB6CA3-0C5E-4734-9285-0AEE72FE8D1C v1.0
Bindings:
          ncalrpc:[LRPC-3b673e00a81c15b641]

Protocol: N/A
Provider: N/A
UUID    : 7F1343FE-50A9-4927-A778-0C5859517BAC v1.0 DfsDs service
Bindings:
          ncacn_np:\\SIZZLE[\PIPE\wkssvc]
          ncalrpc:[OLE766F72C0264196E591D0645650C7]
          ncalrpc:[nlaapi]
          ncalrpc:[nlaplg]
          ncalrpc:[DNSResolver]
          ncalrpc:[keysvc]

Protocol: N/A
Provider: N/A
UUID    : EB081A0D-10EE-478A-A1DD-50995283E7A8 v3.0 Witness Client Test Interface
Bindings:
          ncalrpc:[OLE766F72C0264196E591D0645650C7]
          ncalrpc:[nlaapi]
          ncalrpc:[nlaplg]
          ncalrpc:[DNSResolver]
          ncalrpc:[keysvc]

Protocol: N/A
Provider: N/A
UUID    : F2C9B409-C1C9-4100-8639-D8AB1486694A v1.0 Witness Client Upcall Server
Bindings:
          ncalrpc:[OLE766F72C0264196E591D0645650C7]
          ncalrpc:[nlaapi]
          ncalrpc:[nlaplg]
          ncalrpc:[DNSResolver]
          ncalrpc:[keysvc]

Protocol: [MS-FASP]: Firewall and Advanced Security Protocol
Provider: FwRemoteSvr.dll
UUID    : 6B5BDD1E-528C-422C-AF8C-A4079BE4FE48 v1.0 Remote Fw APIs
Bindings:
          ncacn_ip_tcp:10.10.10.103[49673]

Protocol: N/A
Provider: N/A
UUID    : 51A227AE-825B-41F2-B4A9-1AC9557A1018 v1.0 Ngc Pop Key Service
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.103[49691]
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : 8FB74744-B2FF-4C00-BE0D-9EF9A191FE1B v1.0 Ngc Pop Key Service
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.103[49691]
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : B25A52BF-E5DD-4F4A-AEA6-8CA7272A0E86 v2.0 KeyIso
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.103[49691]
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: [MS-NRPC]: Netlogon Remote Protocol
Provider: netlogon.dll
UUID    : 12345678-1234-ABCD-EF00-01234567CFFB v1.0
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.103[49691]
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: [MS-RAA]: Remote Authorization API Protocol
Provider: N/A
UUID    : 0B1C2170-5732-4E0E-8CD3-D9B16F3B84D7 v0.0 RemoteAccessCheck
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.103[49691]
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.103[49691]
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: [MS-SAMR]: Security Account Manager (SAM) Remote Protocol
Provider: samsrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AC v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.103[49691]
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: [MS-LSAT]: Local Security Authority (Translation Methods) Remote
Provider: lsasrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AB v0.0
Bindings:
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: [MS-DRSR]: Directory Replication Service (DRS) Remote Protocol
Provider: ntdsai.dll
UUID    : E3514235-4B06-11D1-AB04-00C04FC2DCD2 v4.0 MS NT Directory DRS Interface
Bindings:
          ncacn_np:\\SIZZLE[\pipe\6060d100e0e4b2e3]
          ncacn_http:10.10.10.103[49690]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLEB64240F773B3960B8A3CE434675A]
          ncacn_ip_tcp:10.10.10.103[49666]
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
          ncacn_np:\\SIZZLE[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : D2716E94-25CB-4820-BC15-537866578562 v1.0
Bindings:
          ncalrpc:[OLEC27AE22008235E4517EBD1F4F29F]
          ncalrpc:[LRPC-425daa61d3c9170def]

Protocol: N/A
Provider: N/A
UUID    : 0C53AA2E-FB1C-49C5-BFB6-C54F8E5857CD v1.0
Bindings:
          ncalrpc:[OLEC27AE22008235E4517EBD1F4F29F]
          ncalrpc:[LRPC-425daa61d3c9170def]

Protocol: N/A
Provider: N/A
UUID    : 923C9623-DB7F-4B34-9E6D-E86580F8CA2A v1.0
Bindings:
          ncalrpc:[OLEC27AE22008235E4517EBD1F4F29F]
          ncalrpc:[LRPC-425daa61d3c9170def]

Protocol: N/A
Provider: sppsvc.exe
UUID    : 9435CC56-1D9C-4924-AC7D-B60A2C3520E1 v1.0 SPPSVC Default RPC Interface
Bindings:
          ncalrpc:[SPPCTransportEndpoint-00001]

Protocol: N/A
Provider: N/A
UUID    : 8EC21E98-B5CE-4916-A3D6-449FA428A007 v0.0
Bindings:
          ncalrpc:[OLE81D10E798029F8CEC16D8CFA55E4]
          ncalrpc:[LRPC-c1e77cc3af0b82be32]

Protocol: N/A
Provider: N/A
UUID    : 0FC77B1A-95D8-4A2E-A0C0-CFF54237462B v0.0
Bindings:
          ncalrpc:[OLE81D10E798029F8CEC16D8CFA55E4]
          ncalrpc:[LRPC-c1e77cc3af0b82be32]

Protocol: N/A
Provider: N/A
UUID    : B1EF227E-DFA5-421E-82BB-67A6A129C496 v0.0
Bindings:
          ncalrpc:[OLE81D10E798029F8CEC16D8CFA55E4]
          ncalrpc:[LRPC-c1e77cc3af0b82be32]

Protocol: [MS-ICPR]: ICertPassage Remote Protocol
Provider: certsrv.exe
UUID    : 91AE6020-9E3C-11CF-8D7C-00AA00C091BE v0.0
Bindings:
          ncalrpc:[OLEE770AEC05A8DED714A1425E28572]
          ncacn_np:\\SIZZLE[\pipe\cert]
          ncacn_ip_tcp:10.10.10.103[49714]

Protocol: [MS-DNSP]: Domain Name Service (DNS) Server Management
Provider: dns.exe
UUID    : 50ABC2A4-574D-40B3-9D66-EE4FD5FBA076 v5.0
Bindings:
          ncacn_ip_tcp:10.10.10.103[49708]

Protocol: N/A
Provider: N/A
UUID    : 64D1D045-F675-460B-8A94-570246B36DAB v1.0 CLIPSVC Default RPC Interface
Bindings:
          ncalrpc:[ClipServiceTransportEndpoint-00001]

Protocol: N/A
Provider: winlogon.exe
UUID    : 12E65DD8-887F-41EF-91BF-8D816C42C2E7 v1.0 Secure Desktop LRPC interface
Bindings:
          ncalrpc:[WMsgKRpc08BCE1]

Protocol: [MS-CMPO]: MSDTC Connection Manager:
Provider: msdtcprx.dll
UUID    : 906B0CE0-C70B-1067-B317-00DD010662DA v1.0
Bindings:
          ncalrpc:[LRPC-a8a548dd0ed2538975]
          ncalrpc:[LRPC-a8a548dd0ed2538975]
          ncalrpc:[LRPC-a8a548dd0ed2538975]
          ncalrpc:[OLE61C028F67EABA9E0D3BBCB1ED35E]
          ncalrpc:[LRPC-6bb303379f1474f974]

Protocol: [MS-SCMR]: Service Control Manager Remote Protocol
Provider: services.exe
UUID    : 367ABB81-9844-35F1-AD32-98F038001003 v2.0
Bindings:
          ncacn_ip_tcp:10.10.10.103[49696]

Protocol: N/A
Provider: N/A
UUID    : 4C9DBF19-D39E-4BB9-90EE-8F7179B20283 v1.0
Bindings:
          ncalrpc:[LRPC-76d214dc8d9060a60c]

Protocol: N/A
Provider: N/A
UUID    : E38F5360-8572-473E-B696-1B46873BEEAB v1.0
Bindings:
          ncalrpc:[LRPC-76d214dc8d9060a60c]

Protocol: [MS-RPRN]: Print System Remote Protocol
Provider: spoolsv.exe
UUID    : 12345678-1234-ABCD-EF00-0123456789AB v1.0
Bindings:
          ncalrpc:[LRPC-05a8f089583261d95e]
          ncacn_ip_tcp:10.10.10.103[49693]

Protocol: [MS-PAN]: Print System Asynchronous Notification Protocol
Provider: spoolsv.exe
UUID    : 0B6EDBFA-4A24-4FC6-8A23-942B1ECA65D1 v1.0
Bindings:
          ncalrpc:[LRPC-05a8f089583261d95e]
          ncacn_ip_tcp:10.10.10.103[49693]

Protocol: [MS-PAN]: Print System Asynchronous Notification Protocol
Provider: spoolsv.exe
UUID    : AE33069B-A2A8-46EE-A235-DDFD339BE281 v1.0
Bindings:
          ncalrpc:[LRPC-05a8f089583261d95e]
          ncacn_ip_tcp:10.10.10.103[49693]

Protocol: N/A
Provider: spoolsv.exe
UUID    : 4A452661-8290-4B36-8FBE-7F4093A94978 v1.0
Bindings:
          ncalrpc:[LRPC-05a8f089583261d95e]
          ncacn_ip_tcp:10.10.10.103[49693]

Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol
Provider: spoolsv.exe
UUID    : 76F03F96-CDFD-44FC-A22C-64950A001209 v1.0
Bindings:
          ncalrpc:[LRPC-05a8f089583261d95e]
          ncacn_ip_tcp:10.10.10.103[49693]

Protocol: N/A
Provider: srvsvc.dll
UUID    : 98716D03-89AC-44C7-BB8C-285824E51C4A v1.0 XactSrv service
Bindings:
          ncalrpc:[LRPC-dd973b6975a92092bf]

Protocol: N/A
Provider: N/A
UUID    : 1A0D010F-1C33-432C-B0F5-8CF4E8053099 v1.0 IdSegSrv service
Bindings:
          ncalrpc:[LRPC-dd973b6975a92092bf]

[*] Received 545 endpoints.


```
