```bash
impacket-rpcdump -port 593 10.10.10.192
```

[/home/kali/Notes/Labs/htb/blackfield/scans/tcp593/tcp_593_rpc_rpcdump.txt](file:///home/kali/Notes/Labs/htb/blackfield/scans/tcp593/tcp_593_rpc_rpcdump.txt):

```
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies

[*] Retrieving endpoint list from 10.10.10.192
Protocol: [MS-RSP]: Remote Shutdown Protocol
Provider: wininit.exe
UUID    : D95AFE70-A6D5-4259-822E-2C84DA1DDB0D v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49664]
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\DC01[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc088AF0]

Protocol: N/A
Provider: winlogon.exe
UUID    : 76F226C3-EC14-4325-8A99-6A46348418AF v1.0
Bindings:
          ncalrpc:[WindowsShutdown]
          ncacn_np:\\DC01[\PIPE\InitShutdown]
          ncalrpc:[WMsgKRpc088AF0]
          ncalrpc:[WMsgKRpc089BF1]

Protocol: N/A
Provider: N/A
UUID    : FC48CD89-98D6-4628-9839-86F7A3E4161A v1.0
Bindings:
          ncalrpc:[dabrpc]
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-83fcbd44e667598fa6]
          ncalrpc:[LRPC-f2061adb01c2c8d130]
          ncalrpc:[LRPC-4ec6c71c47b089d857]
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : D09BDEB5-6171-4A34-BFE2-06FA82652568 v1.0
Bindings:
          ncalrpc:[csebpub]
          ncalrpc:[LRPC-83fcbd44e667598fa6]
          ncalrpc:[LRPC-f2061adb01c2c8d130]
          ncalrpc:[LRPC-4ec6c71c47b089d857]
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-f2061adb01c2c8d130]
          ncalrpc:[LRPC-4ec6c71c47b089d857]
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-4ec6c71c47b089d857]
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]
          ncalrpc:[LRPC-007245f09aed99b9e7]
          ncalrpc:[LRPC-35576d498bba455f62]

Protocol: N/A
Provider: N/A
UUID    : 697DCDA9-3BA9-4EB2-9247-E11F1901B0D2 v1.0
Bindings:
          ncalrpc:[LRPC-83fcbd44e667598fa6]
          ncalrpc:[LRPC-f2061adb01c2c8d130]
          ncalrpc:[LRPC-4ec6c71c47b089d857]
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 9B008953-F195-4BF9-BDE0-4471971E58ED v1.0
Bindings:
          ncalrpc:[LRPC-f2061adb01c2c8d130]
          ncalrpc:[LRPC-4ec6c71c47b089d857]
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : DD59071B-3215-4C59-8481-972EDADC0F6A v1.0
Bindings:
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
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 76C217BC-C8B4-4201-A745-373AD9032B1A v1.0
Bindings:
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 55E6B932-1979-45D6-90C5-7F6270724112 v1.0
Bindings:
          ncalrpc:[LRPC-196fc959eff59cd8c2]
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 857FB1BE-084F-4FB5-B59C-4B2C4BE5F0CF v1.0
Bindings:
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : B8CADBAF-E84B-46B9-84F2-6F71C03F9E55 v1.0
Bindings:
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 20C40295-8DBA-48E6-AEBF-3E78EF3BB144 v1.0
Bindings:
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2513BCBE-6CD4-4348-855E-7EFB3C336DD3 v1.0
Bindings:
          ncalrpc:[LRPC-28101ad4b6bda9a925]
          ncalrpc:[OLEFAC5C8E7AF5A8E72D1827BCA7D80]
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 0D3E2735-CEA0-4ECC-A9E2-41A2D81AED4E v1.0
Bindings:
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : C605F9FB-F0A3-4E2A-A073-73560F8D9E3E v1.0
Bindings:
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 1B37CA91-76B1-4F5E-A3C7-2ABFC61F2BB0 v1.0
Bindings:
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 8BFC3BE1-6DEF-4E2D-AF74-7C47CD0ADE4A v1.0
Bindings:
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
          ncalrpc:[actkernel]
          ncalrpc:[umpo]

Protocol: N/A
Provider: N/A
UUID    : 2D98A740-581D-41B9-AA0D-A88B9D5CE938 v1.0
Bindings:
          ncalrpc:[LRPC-2b5f86ce6b83612f4b]
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
          ncalrpc:[LRPC-7880a9121a91cf77fc]
          ncalrpc:[IUserProfile2]
          ncalrpc:[LRPC-3cb3254a3b59fa2ee6]
          ncalrpc:[LRPC-9438d5c2aff92a2c5e]
          ncalrpc:[senssvc]
          ncalrpc:[LRPC-375d81b68cd71eaa57]
          ncalrpc:[OLE57C33E4C439CF7578090EC2D5C02]
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : 64D1D045-F675-460B-8A94-570246B36DAB v1.0 CLIPSVC Default RPC Interface
Bindings:
          ncalrpc:[ClipServiceTransportEndpoint-00001]

Protocol: N/A
Provider: nrpsrv.dll
UUID    : 30ADC50C-5CBC-46CE-9A0E-91914789E23C v1.0 NRP server endpoint
Bindings:
          ncalrpc:[LRPC-0b33f7ead2ce46fb5c]

Protocol: N/A
Provider: nsisvc.dll
UUID    : 7EA70BCF-48AF-4F6A-8968-6A440754D5FA v1.0 NSI server endpoint
Bindings:
          ncalrpc:[LRPC-118c36d430fe9b75f5]

Protocol: N/A
Provider: N/A
UUID    : E40F7B57-7A25-4CD3-A135-7F7D3DF9D16B v1.0 Network Connection Broker server endpoint
Bindings:
          ncalrpc:[LRPC-f904bc2b013c061a00]
          ncalrpc:[OLE02EF3661A552756D93EA855457B1]
          ncalrpc:[LRPC-eeffbdd491050488cd]
          ncalrpc:[LRPC-007245f09aed99b9e7]

Protocol: N/A
Provider: N/A
UUID    : 880FD55E-43B9-11E0-B1A8-CF4EDFD72085 v1.0 KAPI Service endpoint
Bindings:
          ncalrpc:[LRPC-f904bc2b013c061a00]
          ncalrpc:[OLE02EF3661A552756D93EA855457B1]
          ncalrpc:[LRPC-eeffbdd491050488cd]
          ncalrpc:[LRPC-007245f09aed99b9e7]

Protocol: N/A
Provider: N/A
UUID    : 5222821F-D5E2-4885-84F1-5F6185A0EC41 v1.0 Network Connection Broker server endpoint for NCB Reset module
Bindings:
          ncalrpc:[LRPC-eeffbdd491050488cd]
          ncalrpc:[LRPC-007245f09aed99b9e7]

Protocol: N/A
Provider: N/A
UUID    : A500D4C6-0DD1-4543-BC0C-D5F93486EAF8 v1.0
Bindings:
          ncalrpc:[LRPC-dbfca93d6b70ffb183]
          ncalrpc:[LRPC-35576d498bba455f62]

Protocol: [MS-EVEN6]: EventLog Remoting Protocol
Provider: wevtsvc.dll
UUID    : F6BEAFF7-1E19-4FBB-9F8F-B89E2018337C v1.0 Event log TCPIP
Bindings:
          ncacn_ip_tcp:10.10.10.192[49665]
          ncacn_np:\\DC01[\pipe\eventlog]
          ncalrpc:[eventlog]

Protocol: N/A
Provider: dhcpcsvc6.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D6 v1.0 DHCPv6 Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc6]
          ncalrpc:[dhcpcsvc]

Protocol: N/A
Provider: dhcpcsvc.dll
UUID    : 3C4728C5-F0AB-448B-BDA1-6CE01EB0A6D5 v1.0 DHCP Client LRPC Endpoint
Bindings:
          ncalrpc:[dhcpcsvc]

Protocol: N/A
Provider: N/A
UUID    : DF4DF73A-C52D-4E3A-8003-8437FDF8302A v0.0 WM_WindowManagerRPC\Server
Bindings:
          ncalrpc:[LRPC-70699f2f4b878a55bb]

Protocol: N/A
Provider: gpsvc.dll
UUID    : 2EB08E3E-639F-4FBA-97B1-14F878961076 v1.0 Group Policy RPC Interface
Bindings:
          ncalrpc:[LRPC-e1ebc39fff68e451ff]

Protocol: N/A
Provider: N/A
UUID    : 3A9EF155-691D-4449-8D05-09AD57031823 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49666]
          ncalrpc:[LRPC-4ddd0e214f5457e084]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\DC01[\PIPE\atsvc]
          ncalrpc:[LRPC-8d857eb13ff6b75f4a]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: schedsvc.dll
UUID    : 86D35949-83C9-4044-B424-DB363231FD0C v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49666]
          ncalrpc:[LRPC-4ddd0e214f5457e084]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\DC01[\PIPE\atsvc]
          ncalrpc:[LRPC-8d857eb13ff6b75f4a]

Protocol: N/A
Provider: N/A
UUID    : 33D84484-3626-47EE-8C6F-E7E98B113BE1 v2.0
Bindings:
          ncalrpc:[LRPC-4ddd0e214f5457e084]
          ncalrpc:[ubpmtaskhostchannel]
          ncacn_np:\\DC01[\PIPE\atsvc]
          ncalrpc:[LRPC-8d857eb13ff6b75f4a]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 378E52B0-C0A9-11CF-822D-00AA0051E40F v1.0
Bindings:
          ncacn_np:\\DC01[\PIPE\atsvc]
          ncalrpc:[LRPC-8d857eb13ff6b75f4a]

Protocol: [MS-TSCH]: Task Scheduler Service Remoting Protocol
Provider: taskcomp.dll
UUID    : 1FF70682-0A51-30E8-076D-740BE8CEE98B v1.0
Bindings:
          ncacn_np:\\DC01[\PIPE\atsvc]
          ncalrpc:[LRPC-8d857eb13ff6b75f4a]

Protocol: N/A
Provider: schedsvc.dll
UUID    : 0A74EF1C-41A4-4E06-83AE-DC74FB1CDD53 v1.0
Bindings:
          ncalrpc:[LRPC-8d857eb13ff6b75f4a]

Protocol: N/A
Provider: N/A
UUID    : 7F1343FE-50A9-4927-A778-0C5859517BAC v1.0 DfsDs service
Bindings:
          ncacn_np:\\DC01[\PIPE\wkssvc]
          ncalrpc:[LRPC-aecf02c2d84afed182]

Protocol: N/A
Provider: N/A
UUID    : EB081A0D-10EE-478A-A1DD-50995283E7A8 v3.0 Witness Client Test Interface
Bindings:
          ncalrpc:[LRPC-aecf02c2d84afed182]

Protocol: N/A
Provider: N/A
UUID    : F2C9B409-C1C9-4100-8639-D8AB1486694A v1.0 Witness Client Upcall Server
Bindings:
          ncalrpc:[LRPC-aecf02c2d84afed182]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 2FB92682-6599-42DC-AE13-BD2CA89BD11C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-b687aa43e8c380083f]
          ncalrpc:[LRPC-0d21eed34cb5901a30]
          ncalrpc:[LRPC-9887b916e9bf76ae72]
          ncalrpc:[LRPC-19828fb3c222a8f2c4]

Protocol: N/A
Provider: N/A
UUID    : F47433C3-3E9D-4157-AAD4-83AA1F5C2D4C v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-0d21eed34cb5901a30]
          ncalrpc:[LRPC-9887b916e9bf76ae72]
          ncalrpc:[LRPC-19828fb3c222a8f2c4]

Protocol: N/A
Provider: MPSSVC.dll
UUID    : 7F9D11BF-7FB9-436B-A812-B2D50C5D4C03 v1.0 Fw APIs
Bindings:
          ncalrpc:[LRPC-9887b916e9bf76ae72]
          ncalrpc:[LRPC-19828fb3c222a8f2c4]

Protocol: N/A
Provider: BFE.DLL
UUID    : DD490425-5325-4565-B774-7E27D6C09C24 v1.0 Base Firewall Engine API
Bindings:
          ncalrpc:[LRPC-19828fb3c222a8f2c4]

Protocol: N/A
Provider: N/A
UUID    : 3473DD4D-2E88-4006-9CBA-22570909DD10 v5.1 WinHttp Auto-Proxy Service
Bindings:
          ncalrpc:[fc63c1fc-39fb-4498-8fc8-7ffc9ac5e08a]
          ncalrpc:[LRPC-29235b04cf842f5b1d]

Protocol: N/A
Provider: certprop.dll
UUID    : 30B044A5-A225-43F0-B3A4-E060DF91F9C1 v1.0
Bindings:
          ncalrpc:[LRPC-950c26fe881694c003]

Protocol: N/A
Provider: N/A
UUID    : 29770A8F-829B-4158-90A2-78CD488501F7 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49667]
          ncacn_np:\\DC01[\pipe\SessEnvPublicRpc]
          ncalrpc:[SessEnvPrivateRpc]
          ncalrpc:[LRPC-375d81b68cd71eaa57]

Protocol: N/A
Provider: N/A
UUID    : 572E35B4-1344-4565-96A1-F5DF3BFA89BB v1.0 LiveIdSvcNotify RPC Interface
Bindings:
          ncalrpc:[liveidsvcnotify]

Protocol: N/A
Provider: N/A
UUID    : FAF2447B-B348-4FEB-8DBE-BEEE5B7F7778 v1.0 OnlineProviderCert RPC Interface
Bindings:
          ncalrpc:[LRPC-b11885515ac8a98b61]

Protocol: N/A
Provider: N/A
UUID    : CC105610-DA03-467E-BC73-5B9E2937458D v1.0 LiveIdSvc RPC Interface
Bindings:
          ncalrpc:[LRPC-b11885515ac8a98b61]

Protocol: N/A
Provider: N/A
UUID    : C2D1B5DD-FA81-4460-9DD6-E7658B85454B v1.0
Bindings:
          ncalrpc:[LRPC-653ef2069057720293]
          ncalrpc:[OLE015522BA1550E4BE6428E31675E2]

Protocol: N/A
Provider: N/A
UUID    : F44E62AF-DAB1-44C2-8013-049A9DE417D6 v1.0
Bindings:
          ncalrpc:[LRPC-653ef2069057720293]
          ncalrpc:[OLE015522BA1550E4BE6428E31675E2]

Protocol: N/A
Provider: N/A
UUID    : 7AEB6705-3AE6-471A-882D-F39C109EDC12 v1.0
Bindings:
          ncalrpc:[LRPC-653ef2069057720293]
          ncalrpc:[OLE015522BA1550E4BE6428E31675E2]

Protocol: N/A
Provider: N/A
UUID    : E7F76134-9EF5-4949-A2D6-3368CC0988F3 v1.0
Bindings:
          ncalrpc:[LRPC-653ef2069057720293]
          ncalrpc:[OLE015522BA1550E4BE6428E31675E2]

Protocol: N/A
Provider: N/A
UUID    : B37F900A-EAE4-4304-A2AB-12BB668C0188 v1.0
Bindings:
          ncalrpc:[LRPC-653ef2069057720293]
          ncalrpc:[OLE015522BA1550E4BE6428E31675E2]

Protocol: N/A
Provider: N/A
UUID    : ABFB6CA3-0C5E-4734-9285-0AEE72FE8D1C v1.0
Bindings:
          ncalrpc:[LRPC-653ef2069057720293]
          ncalrpc:[OLE015522BA1550E4BE6428E31675E2]

Protocol: [MS-NRPC]: Netlogon Remote Protocol
Provider: netlogon.dll
UUID    : 12345678-1234-ABCD-EF00-01234567CFFB v1.0
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.192[49675]
          ncacn_np:\\DC01[\pipe\0e866ab3cfffb103]
          ncacn_http:10.10.10.192[49674]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE57C33E4C439CF7578090EC2D5C02]
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: [MS-RAA]: Remote Authorization API Protocol
Provider: N/A
UUID    : 0B1C2170-5732-4E0E-8CD3-D9B16F3B84D7 v0.0 RemoteAccessCheck
Bindings:
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.192[49675]
          ncacn_np:\\DC01[\pipe\0e866ab3cfffb103]
          ncacn_http:10.10.10.192[49674]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE57C33E4C439CF7578090EC2D5C02]
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]
          ncalrpc:[NETLOGON_LRPC]
          ncacn_ip_tcp:10.10.10.192[49675]
          ncacn_np:\\DC01[\pipe\0e866ab3cfffb103]
          ncacn_http:10.10.10.192[49674]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE57C33E4C439CF7578090EC2D5C02]
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: [MS-SAMR]: Security Account Manager (SAM) Remote Protocol
Provider: samsrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AC v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49675]
          ncacn_np:\\DC01[\pipe\0e866ab3cfffb103]
          ncacn_http:10.10.10.192[49674]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE57C33E4C439CF7578090EC2D5C02]
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: [MS-LSAT]: Local Security Authority (Translation Methods) Remote
Provider: lsasrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AB v0.0
Bindings:
          ncacn_np:\\DC01[\pipe\0e866ab3cfffb103]
          ncacn_http:10.10.10.192[49674]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE57C33E4C439CF7578090EC2D5C02]
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: [MS-DRSR]: Directory Replication Service (DRS) Remote Protocol
Provider: ntdsai.dll
UUID    : E3514235-4B06-11D1-AB04-00C04FC2DCD2 v4.0 MS NT Directory DRS Interface
Bindings:
          ncacn_np:\\DC01[\pipe\0e866ab3cfffb103]
          ncacn_http:10.10.10.192[49674]
          ncalrpc:[NTDS_LPC]
          ncalrpc:[OLE57C33E4C439CF7578090EC2D5C02]
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : 51A227AE-825B-41F2-B4A9-1AC9557A1018 v1.0 Ngc Pop Key Service
Bindings:
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : 8FB74744-B2FF-4C00-BE0D-9EF9A191FE1B v1.0 Ngc Pop Key Service
Bindings:
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : B25A52BF-E5DD-4F4A-AEA6-8CA7272A0E86 v2.0 KeyIso
Bindings:
          ncacn_ip_tcp:10.10.10.192[49668]
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
          ncacn_np:\\DC01[\pipe\lsass]

Protocol: N/A
Provider: N/A
UUID    : C49A5A70-8A7F-4E70-BA16-1E8F1F193EF1 v1.0 Adh APIs
Bindings:
          ncalrpc:[OLE9F164020D96CE6719AC0EFE30B60]
          ncalrpc:[TeredoControl]
          ncalrpc:[TeredoDiagnostics]
          ncalrpc:[LRPC-4156ffb62d22714298]

Protocol: N/A
Provider: N/A
UUID    : C36BE077-E14B-4FE9-8ABC-E856EF4F048B v1.0 Proxy Manager client server endpoint
Bindings:
          ncalrpc:[TeredoControl]
          ncalrpc:[TeredoDiagnostics]
          ncalrpc:[LRPC-4156ffb62d22714298]

Protocol: N/A
Provider: N/A
UUID    : 2E6035B2-E8F1-41A7-A044-656B439C4C34 v1.0 Proxy Manager provider server endpoint
Bindings:
          ncalrpc:[TeredoControl]
          ncalrpc:[TeredoDiagnostics]
          ncalrpc:[LRPC-4156ffb62d22714298]

Protocol: N/A
Provider: iphlpsvc.dll
UUID    : 552D076A-CB29-4E44-8B6A-D15E59E2C0AF v1.0 IP Transition Configuration endpoint
Bindings:
          ncalrpc:[LRPC-4156ffb62d22714298]

Protocol: N/A
Provider: N/A
UUID    : 0D3C7F20-1C8D-4654-A1B3-51563B298BDA v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-98f943abb3fb5573bd]
          ncalrpc:[OLE521A7B91965804E0E343E24C3A56]

Protocol: N/A
Provider: N/A
UUID    : B18FBAB6-56F8-4702-84E0-41053293A869 v1.0 UserMgrCli
Bindings:
          ncalrpc:[LRPC-98f943abb3fb5573bd]
          ncalrpc:[OLE521A7B91965804E0E343E24C3A56]

Protocol: N/A
Provider: N/A
UUID    : A4B8D482-80CE-40D6-934D-B22A01A44FE7 v1.0 LicenseManager
Bindings:
          ncalrpc:[LicenseServiceEndpoint]

Protocol: N/A
Provider: N/A
UUID    : 1A0D010F-1C33-432C-B0F5-8CF4E8053099 v1.0 IdSegSrv service
Bindings:
          ncalrpc:[LRPC-5d5fdeeb3994c763eb]

Protocol: N/A
Provider: srvsvc.dll
UUID    : 98716D03-89AC-44C7-BB8C-285824E51C4A v1.0 XactSrv service
Bindings:
          ncalrpc:[LRPC-5d5fdeeb3994c763eb]

Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol
Provider: spoolsv.exe
UUID    : 76F03F96-CDFD-44FC-A22C-64950A001209 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49677]
          ncalrpc:[LRPC-27d3f8f62f64af6880]

Protocol: N/A
Provider: spoolsv.exe
UUID    : 4A452661-8290-4B36-8FBE-7F4093A94978 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49677]
          ncalrpc:[LRPC-27d3f8f62f64af6880]

Protocol: [MS-PAN]: Print System Asynchronous Notification Protocol
Provider: spoolsv.exe
UUID    : AE33069B-A2A8-46EE-A235-DDFD339BE281 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49677]
          ncalrpc:[LRPC-27d3f8f62f64af6880]

Protocol: [MS-PAN]: Print System Asynchronous Notification Protocol
Provider: spoolsv.exe
UUID    : 0B6EDBFA-4A24-4FC6-8A23-942B1ECA65D1 v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49677]
          ncalrpc:[LRPC-27d3f8f62f64af6880]

Protocol: [MS-RPRN]: Print System Remote Protocol
Provider: spoolsv.exe
UUID    : 12345678-1234-ABCD-EF00-0123456789AB v1.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49677]
          ncalrpc:[LRPC-27d3f8f62f64af6880]

Protocol: [MS-PCQ]: Performance Counter Query Protocol
Provider: regsvc.dll
UUID    : DA5A86C5-12C2-4943-AB30-7F74A813D853 v1.0 RemoteRegistry Perflib Interface
Bindings:
          ncacn_np:\\DC01[\PIPE\winreg]

Protocol: [MS-RRP]: Windows Remote Registry Protocol
Provider: regsvc.dll
UUID    : 338CD001-2244-31F1-AAAA-900038001003 v1.0 RemoteRegistry Interface
Bindings:
          ncacn_np:\\DC01[\PIPE\winreg]

Protocol: N/A
Provider: sysmain.dll
UUID    : B58AA02E-2884-4E97-8176-4EE06D794184 v1.0
Bindings:
          ncalrpc:[LRPC-d9c021616318826e2e]

Protocol: N/A
Provider: IKEEXT.DLL
UUID    : A398E520-D59A-4BDD-AA7A-3C1E0303A511 v1.0 IKE/Authip API
Bindings:
          ncalrpc:[LRPC-2b4e6e15646f30863b]

Protocol: N/A
Provider: N/A
UUID    : 98CD761E-E77D-41C8-A3C0-0FB756D90EC2 v1.0
Bindings:
          ncalrpc:[LRPC-e2103542396bc3ae95]

Protocol: N/A
Provider: N/A
UUID    : D22895EF-AFF4-42C5-A5B2-B14466D34AB4 v1.0
Bindings:
          ncalrpc:[LRPC-e2103542396bc3ae95]

Protocol: N/A
Provider: N/A
UUID    : E38F5360-8572-473E-B696-1B46873BEEAB v1.0
Bindings:
          ncalrpc:[LRPC-e2103542396bc3ae95]

Protocol: N/A
Provider: N/A
UUID    : 95095EC8-32EA-4EB0-A3E2-041F97B36168 v1.0
Bindings:
          ncalrpc:[LRPC-e2103542396bc3ae95]

Protocol: N/A
Provider: N/A
UUID    : FD8BE72B-A9CD-4B2C-A9CA-4DED242FBE4D v1.0
Bindings:
          ncalrpc:[LRPC-e2103542396bc3ae95]

Protocol: N/A
Provider: N/A
UUID    : 4C9DBF19-D39E-4BB9-90EE-8F7179B20283 v1.0
Bindings:
          ncalrpc:[LRPC-e2103542396bc3ae95]

Protocol: [MS-CMPO]: MSDTC Connection Manager:
Provider: msdtcprx.dll
UUID    : 906B0CE0-C70B-1067-B317-00DD010662DA v1.0
Bindings:
          ncalrpc:[LRPC-6e3d0e7ad89fae5354]
          ncalrpc:[OLE4D9421472A7D518258A07643B369]
          ncalrpc:[LRPC-a5a3db9f193462af87]
          ncalrpc:[LRPC-a5a3db9f193462af87]
          ncalrpc:[LRPC-a5a3db9f193462af87]

Protocol: N/A
Provider: N/A
UUID    : 2F5F6521-CB55-1059-B446-00DF0BCE31DB v1.0 Unimodem LRPC Endpoint
Bindings:
          ncalrpc:[unimdmsvc]
          ncalrpc:[tapsrvlpc]
          ncacn_np:\\DC01[\pipe\tapsrv]

Protocol: N/A
Provider: N/A
UUID    : 650A7E26-EAB8-5533-CE43-9C1DFCE11511 v1.0 Vpn APIs
Bindings:
          ncalrpc:[LRPC-60d1a5e4652cc4fa1b]
          ncalrpc:[VpnikeRpc]
          ncalrpc:[RasmanLrpc]
          ncacn_np:\\DC01[\PIPE\ROUTER]

Protocol: [MS-SCMR]: Service Control Manager Remote Protocol
Provider: services.exe
UUID    : 367ABB81-9844-35F1-AD32-98F038001003 v2.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49686]

Protocol: N/A
Provider: winlogon.exe
UUID    : 12E65DD8-887F-41EF-91BF-8D816C42C2E7 v1.0 Secure Desktop LRPC interface
Bindings:
          ncalrpc:[WMsgKRpc089BF1]

Protocol: [MS-DNSP]: Domain Name Service (DNS) Server Management
Provider: dns.exe
UUID    : 50ABC2A4-574D-40B3-9D66-EE4FD5FBA076 v5.0
Bindings:
          ncacn_ip_tcp:10.10.10.192[49689]

Protocol: [MS-FRS2]: Distributed File System Replication Protocol
Provider: dfsrmig.exe
UUID    : 897E2E5F-93F3-4376-9C9C-FD2277495C27 v1.0 Frs2 Service
Bindings:
          ncacn_ip_tcp:10.10.10.192[49702]
          ncalrpc:[OLE74C515EF7E22D1D795D354C58786]

Protocol: N/A
Provider: N/A
UUID    : FF9FD3C4-742E-45E0-91DD-2F5BC632A1DF v1.0 appxsvc
Bindings:
          ncalrpc:[LRPC-80dbcc9c36a8f7fec2]

Protocol: N/A
Provider: N/A
UUID    : AE2DC901-312D-41DF-8B79-E835E63DB874 v1.0 appxsvc
Bindings:
          ncalrpc:[LRPC-80dbcc9c36a8f7fec2]

Protocol: N/A
Provider: N/A
UUID    : B1EF227E-DFA5-421E-82BB-67A6A129C496 v0.0
Bindings:
          ncalrpc:[LRPC-ab213fa20cd48bb2d5]
          ncalrpc:[OLE93A0BD8126C34C92DCCC38414728]

Protocol: N/A
Provider: N/A
UUID    : 0FC77B1A-95D8-4A2E-A0C0-CFF54237462B v0.0
Bindings:
          ncalrpc:[LRPC-ab213fa20cd48bb2d5]
          ncalrpc:[OLE93A0BD8126C34C92DCCC38414728]

Protocol: N/A
Provider: N/A
UUID    : 8EC21E98-B5CE-4916-A3D6-449FA428A007 v0.0
Bindings:
          ncalrpc:[LRPC-ab213fa20cd48bb2d5]
          ncalrpc:[OLE93A0BD8126C34C92DCCC38414728]

[*] Received 436 endpoints.


```
