```bash
enum4linux-ng -A -d -v 10.10.10.169 2>&1
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp139/enum4linux-ng.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp139/enum4linux-ng.txt):

```
[92mENUM4LINUX - next generation (v1.3.4)[0m

 ==========================
|    Target Information    |
 ==========================
[94m[*] Target ........... 10.10.10.169[0m
[94m[*] Username ......... ''[0m
[94m[*] Random Username .. 'mcfcxgzc'[0m
[94m[*] Password ......... ''[0m
[94m[*] Timeout .......... 5 second(s)[0m

 =====================================
|    Listener Scan on 10.10.10.169    |
 =====================================
[94m[*] Checking LDAP[0m
[92m[+] LDAP is accessible on 389/tcp[0m
[94m[*] Checking LDAPS[0m
[92m[+] LDAPS is accessible on 636/tcp[0m
[94m[*] Checking SMB[0m
[92m[+] SMB is accessible on 445/tcp[0m
[94m[*] Checking SMB over NetBIOS[0m
[92m[+] SMB over NetBIOS is accessible on 139/tcp[0m

 ====================================================
|    Domain Information via LDAP for 10.10.10.169    |
 ====================================================
[94m[*] Trying LDAP[0m
[92m[+] Appears to be root/parent DC[0m
[92m[+] Long domain name is: megabank.local[0m

 ===========================================================
|    NetBIOS Names and Workgroup/Domain for 10.10.10.169    |
 ===========================================================
[V] Trying to get NetBIOS names information, running command: nmblookup -s /tmp/tmp_fv2wya7 -A 10.10.10.169
[91m[-] Could not get NetBIOS names information via 'nmblookup': timed out[0m

 =========================================
|    SMB Dialect Check on 10.10.10.169    |
 =========================================
[94m[*] Trying on 445/tcp[0m
[92m[+] Supported dialects and settings:
Supported dialects:
  SMB 1.0: true
  SMB 2.02: true
  SMB 2.1: true
  SMB 3.0: true
  SMB 3.1.1: true
Preferred dialect: SMB 3.0
SMB1 only: false
SMB signing required: true[0m

 ===========================================================
|    Domain Information via SMB session for 10.10.10.169    |
 ===========================================================
[94m[*] Enumerating via unauthenticated SMB session on 445/tcp[0m
[92m[+] Found domain information via SMB
NetBIOS computer name: RESOLUTE
NetBIOS domain name: MEGABANK
DNS domain: megabank.local
FQDN: Resolute.megabank.local
Derived membership: domain member
Derived domain: MEGABANK[0m

 =========================================
|    RPC Session Check on 10.10.10.169    |
 =========================================
[94m[*] Check for null session[0m
[V] Attempting to make session, running command: smbclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -t 5 -c help '//10.10.10.169/ipc$'
[92m[+] Server allows session using username '', password ''[0m
[94m[*] Check for random user[0m
[V] Attempting to make session, running command: smbclient -W MEGABANK -U mcfcxgzc% -s /tmp/tmp_fv2wya7 -t 5 -c help '//10.10.10.169/ipc$'
[91m[-] Could not establish random user session: STATUS_LOGON_FAILURE[0m

 ===================================================
|    Domain Information via RPC for 10.10.10.169    |
 ===================================================
[V] Attempting to get domain SID, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c lsaquery 10.10.10.169
[92m[+] Domain: MEGABANK[0m
[92m[+] Domain SID: S-1-5-21-1392959593-3013219662-3596683436[0m
[92m[+] Membership: domain member[0m

 ===============================================
|    OS Information via RPC for 10.10.10.169    |
 ===============================================
[94m[*] Enumerating via unauthenticated SMB session on 445/tcp[0m
[92m[+] Found OS information via SMB[0m
[94m[*] Enumerating via 'srvinfo'[0m
[V] Attempting to get OS info with command, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c srvinfo 10.10.10.169
[91m[-] Could not get OS info via 'srvinfo': STATUS_ACCESS_DENIED[0m
[92m[+] After merging OS information we have the following result:
OS: Windows Server 2016 Standard 14393
OS version: '10.0'
OS release: '1607'
OS build: '14393'
Native OS: Windows Server 2016 Standard 14393
Native LAN manager: Windows Server 2016 Standard 6.3
Platform id: null
Server type: null
Server type string: null[0m

 =====================================
|    Users via RPC on 10.10.10.169    |
 =====================================
[94m[*] Enumerating users via 'querydispinfo'[0m
[V] Attempting to get userlist, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c querydispinfo 10.10.10.169
[92m[+] Found 27 user(s) via 'querydispinfo'[0m
[94m[*] Enumerating users via 'enumdomusers'[0m
[V] Attempting to get userlist, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c enumdomusers 10.10.10.169
[92m[+] Found 27 user(s) via 'enumdomusers'[0m
[94m[*] Enumerating users details[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 500' 10.10.10.169
[92m[+] Found details for user 'Administrator' (RID 500)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 501' 10.10.10.169
[92m[+] Found details for user 'Guest' (RID 501)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 502' 10.10.10.169
[92m[+] Found details for user 'krbtgt' (RID 502)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 503' 10.10.10.169
[92m[+] Found details for user 'DefaultAccount' (RID 503)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 1105' 10.10.10.169
[92m[+] Found details for user 'ryan' (RID 1105)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 1111' 10.10.10.169
[92m[+] Found details for user 'marko' (RID 1111)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6601' 10.10.10.169
[92m[+] Found details for user 'sunita' (RID 6601)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6602' 10.10.10.169
[92m[+] Found details for user 'abigail' (RID 6602)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6603' 10.10.10.169
[92m[+] Found details for user 'marcus' (RID 6603)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6604' 10.10.10.169
[92m[+] Found details for user 'sally' (RID 6604)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6605' 10.10.10.169
[92m[+] Found details for user 'fred' (RID 6605)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6606' 10.10.10.169
[92m[+] Found details for user 'angela' (RID 6606)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6607' 10.10.10.169
[92m[+] Found details for user 'felicia' (RID 6607)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6608' 10.10.10.169
[92m[+] Found details for user 'gustavo' (RID 6608)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6609' 10.10.10.169
[92m[+] Found details for user 'ulf' (RID 6609)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6610' 10.10.10.169
[92m[+] Found details for user 'stevie' (RID 6610)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6611' 10.10.10.169
[92m[+] Found details for user 'claire' (RID 6611)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6612' 10.10.10.169
[92m[+] Found details for user 'paulo' (RID 6612)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6613' 10.10.10.169
[92m[+] Found details for user 'steve' (RID 6613)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6614' 10.10.10.169
[92m[+] Found details for user 'annette' (RID 6614)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6615' 10.10.10.169
[92m[+] Found details for user 'annika' (RID 6615)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6616' 10.10.10.169
[92m[+] Found details for user 'per' (RID 6616)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 6617' 10.10.10.169
[92m[+] Found details for user 'claude' (RID 6617)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 10101' 10.10.10.169
[92m[+] Found details for user 'melanie' (RID 10101)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 10102' 10.10.10.169
[92m[+] Found details for user 'zach' (RID 10102)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 10103' 10.10.10.169
[92m[+] Found details for user 'simon' (RID 10103)[0m
[V] Attempting to get detailed user info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'queryuser 10104' 10.10.10.169
[92m[+] Found details for user 'naoki' (RID 10104)[0m
[92m[+] After merging user results we have 27 user(s) total:
'10101':
  username: melanie
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Password last set Time: Sun, 26 Jan 2025 20:23:03 EST
    Password can change Time: Mon, 27 Jan 2025 20:23:03 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x2775'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'10102':
  username: zach
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Wed, 04 Dec 2019 05:39:28 EST
    Password can change Time: Thu, 05 Dec 2019 05:39:28 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x2776'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'10103':
  username: simon
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Wed, 04 Dec 2019 05:39:59 EST
    Password can change Time: Thu, 05 Dec 2019 05:39:59 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x2777'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'10104':
  username: naoki
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Wed, 04 Dec 2019 05:40:44 EST
    Password can change Time: Thu, 05 Dec 2019 05:40:44 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x2778'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'1105':
  username: ryan
  name: Ryan Bertrand
  acb: '0x00000210'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Password last set Time: Sun, 26 Jan 2025 20:22:02 EST
    Password can change Time: Mon, 27 Jan 2025 20:22:02 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x451'
    group_rid: '0x201'
    acb_info: '0x00000210'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: true
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'1111':
  username: marko
  name: Marko Novak
  acb: '0x00000210'
  description: Account created. Password set to Welcome123!
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: Account created. Password set to Welcome123!
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Fri, 27 Sep 2019 09:17:15 EDT
    Password can change Time: Sat, 28 Sep 2019 09:17:15 EDT
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x457'
    group_rid: '0x201'
    acb_info: '0x00000210'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: true
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'500':
  username: Administrator
  name: (null)
  acb: '0x00000210'
  description: Built-in account for administering the computer/domain
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: Built-in account for administering the computer/domain
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Sun, 26 Jan 2025 20:15:02 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Password last set Time: Sun, 26 Jan 2025 20:22:03 EST
    Password can change Time: Mon, 27 Jan 2025 20:22:03 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x1f4'
    group_rid: '0x201'
    acb_info: '0x00000210'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000081'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: true
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'501':
  username: Guest
  name: (null)
  acb: '0x00000215'
  description: Built-in account for guest access to the computer/domain
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: Built-in account for guest access to the computer/domain
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Wed, 31 Dec 1969 19:00:00 EST
    Password can change Time: Wed, 31 Dec 1969 19:00:00 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x1f5'
    group_rid: '0x202'
    acb_info: '0x00000215'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: true
    Password not expired: true
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'502':
  username: krbtgt
  name: (null)
  acb: '0x00000011'
  description: Key Distribution Center Service Account
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: Key Distribution Center Service Account
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Wed, 25 Sep 2019 09:29:12 EDT
    Password can change Time: Thu, 26 Sep 2019 09:29:12 EDT
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x1f6'
    group_rid: '0x201'
    acb_info: '0x00000011'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: true
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'503':
  username: DefaultAccount
  name: (null)
  acb: '0x00000215'
  description: A user account managed by the system.
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: A user account managed by the system.
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Wed, 31 Dec 1969 19:00:00 EST
    Password can change Time: Wed, 31 Dec 1969 19:00:00 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x1f7'
    group_rid: '0x201'
    acb_info: '0x00000215'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: true
    Password not expired: true
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6601':
  username: sunita
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:26:29 EST
    Password can change Time: Wed, 04 Dec 2019 16:26:29 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19c9'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6602':
  username: abigail
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:27:31 EST
    Password can change Time: Wed, 04 Dec 2019 16:27:31 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19ca'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6603':
  username: marcus
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:27:59 EST
    Password can change Time: Wed, 04 Dec 2019 16:27:59 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19cb'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6604':
  username: sally
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:28:30 EST
    Password can change Time: Wed, 04 Dec 2019 16:28:30 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19cc'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6605':
  username: fred
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:29:02 EST
    Password can change Time: Wed, 04 Dec 2019 16:29:02 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19cd'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6606':
  username: angela
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:29:43 EST
    Password can change Time: Wed, 04 Dec 2019 16:29:43 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19ce'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6607':
  username: felicia
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:30:54 EST
    Password can change Time: Wed, 04 Dec 2019 16:30:54 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19cf'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6608':
  username: gustavo
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:31:42 EST
    Password can change Time: Wed, 04 Dec 2019 16:31:42 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d0'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6609':
  username: ulf
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:32:20 EST
    Password can change Time: Wed, 04 Dec 2019 16:32:20 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d1'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6610':
  username: stevie
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:33:13 EST
    Password can change Time: Wed, 04 Dec 2019 16:33:13 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d2'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6611':
  username: claire
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:33:45 EST
    Password can change Time: Wed, 04 Dec 2019 16:33:45 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d3'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6612':
  username: paulo
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:34:47 EST
    Password can change Time: Wed, 04 Dec 2019 16:34:47 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d4'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6613':
  username: steve
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:35:25 EST
    Password can change Time: Wed, 04 Dec 2019 16:35:25 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d5'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6614':
  username: annette
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:36:56 EST
    Password can change Time: Wed, 04 Dec 2019 16:36:56 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d6'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6615':
  username: annika
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:37:24 EST
    Password can change Time: Wed, 04 Dec 2019 16:37:24 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d7'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6616':
  username: per
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:38:12 EST
    Password can change Time: Wed, 04 Dec 2019 16:38:12 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d8'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false
'6617':
  username: claude
  name: (null)
  acb: '0x00000010'
  description: (null)
  details:
    Home Drive: ''
    Dir Drive: ''
    Profile Path: ''
    Logon Script: ''
    Description: ''
    Workstations: ''
    Comment: ''
    Remote Dial: ''
    Logon Time: Wed, 31 Dec 1969 19:00:00 EST
    Logoff Time: Wed, 31 Dec 1969 19:00:00 EST
    Kickoff Time: Wed, 13 Sep 30828 22:48:05 EDT
    Password last set Time: Tue, 03 Dec 2019 16:39:56 EST
    Password can change Time: Wed, 04 Dec 2019 16:39:56 EST
    Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT
    unknown_2[0..31]: ''
    user_rid: '0x19d9'
    group_rid: '0x201'
    acb_info: '0x00000010'
    fields_present: '0x00ffffff'
    logon_divs: '168'
    bad_password_count: '0x00000000'
    logon_count: '0x00000000'
    padding1[0..7]: ''
    logon_hrs[0..21]: ''
    Account Disabled: false
    Password not expired: false
    Account locked out: false
    Password expired: false
    Interdomain trust account: false
    Workstation trust account: false
    Server trust account: false
    Trusted for delegation: false[0m

 ======================================
|    Groups via RPC on 10.10.10.169    |
 ======================================
[94m[*] Enumerating local groups[0m
[V] Attempting to get local groups, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'enumalsgroups domain' 10.10.10.169
[92m[+] Found 5 group(s) via 'enumalsgroups domain'[0m
[94m[*] Enumerating builtin groups[0m
[V] Attempting to get builtin groups, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'enumalsgroups builtin' 10.10.10.169
[92m[+] Found 29 group(s) via 'enumalsgroups builtin'[0m
[94m[*] Enumerating domain groups[0m
[V] Attempting to get domain groups, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c enumdomgroups 10.10.10.169
[92m[+] Found 16 group(s) via 'enumdomgroups'[0m
[94m[*] Enumerating group details[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 517' 10.10.10.169
[91m[-] Could not get details for local group 'Cert Publishers' (RID 517): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 553' 10.10.10.169
[91m[-] Could not get details for local group 'RAS and IAS Servers' (RID 553): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 571' 10.10.10.169
[91m[-] Could not get details for local group 'Allowed RODC Password Replication Group' (RID 571): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 572' 10.10.10.169
[91m[-] Could not get details for local group 'Denied RODC Password Replication Group' (RID 572): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 1101' 10.10.10.169
[91m[-] Could not get details for local group 'DnsAdmins' (RID 1101): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 548' 10.10.10.169
[91m[-] Could not get details for builtin group 'Account Operators' (RID 548): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 554' 10.10.10.169
[91m[-] Could not get details for builtin group 'Pre-Windows 2000 Compatible Access' (RID 554): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 557' 10.10.10.169
[91m[-] Could not get details for builtin group 'Incoming Forest Trust Builders' (RID 557): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 560' 10.10.10.169
[91m[-] Could not get details for builtin group 'Windows Authorization Access Group' (RID 560): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 561' 10.10.10.169
[91m[-] Could not get details for builtin group 'Terminal Server License Servers' (RID 561): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 544' 10.10.10.169
[91m[-] Could not get details for builtin group 'Administrators' (RID 544): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 545' 10.10.10.169
[91m[-] Could not get details for builtin group 'Users' (RID 545): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 546' 10.10.10.169
[91m[-] Could not get details for builtin group 'Guests' (RID 546): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 550' 10.10.10.169
[91m[-] Could not get details for builtin group 'Print Operators' (RID 550): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 551' 10.10.10.169
[91m[-] Could not get details for builtin group 'Backup Operators' (RID 551): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 552' 10.10.10.169
[91m[-] Could not get details for builtin group 'Replicator' (RID 552): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 555' 10.10.10.169
[91m[-] Could not get details for builtin group 'Remote Desktop Users' (RID 555): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 556' 10.10.10.169
[91m[-] Could not get details for builtin group 'Network Configuration Operators' (RID 556): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 558' 10.10.10.169
[91m[-] Could not get details for builtin group 'Performance Monitor Users' (RID 558): STATUS_NO_SUCH_GROUP[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 559' 10.10.10.169
[91m[-] Could not find details for builtin group 'Performance Log Users': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 562' 10.10.10.169
[91m[-] Could not find details for builtin group 'Distributed COM Users': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 568' 10.10.10.169
[91m[-] Could not find details for builtin group 'IIS_IUSRS': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 569' 10.10.10.169
[91m[-] Could not find details for builtin group 'Cryptographic Operators': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 573' 10.10.10.169
[91m[-] Could not find details for builtin group 'Event Log Readers': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 574' 10.10.10.169
[91m[-] Could not find details for builtin group 'Certificate Service DCOM Access': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 575' 10.10.10.169
[91m[-] Could not find details for builtin group 'RDS Remote Access Servers': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 576' 10.10.10.169
[91m[-] Could not find details for builtin group 'RDS Endpoint Servers': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 577' 10.10.10.169
[91m[-] Could not find details for builtin group 'RDS Management Servers': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 578' 10.10.10.169
[91m[-] Could not find details for builtin group 'Hyper-V Administrators': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 579' 10.10.10.169
[91m[-] Could not find details for builtin group 'Access Control Assistance Operators': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 580' 10.10.10.169
[91m[-] Could not find details for builtin group 'Remote Management Users': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 581' 10.10.10.169
[91m[-] Could not find details for builtin group 'System Managed Accounts Group': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 582' 10.10.10.169
[91m[-] Could not find details for builtin group 'Storage Replica Administrators': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 549' 10.10.10.169
[91m[-] Could not find details for builtin group 'Server Operators': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 498' 10.10.10.169
[91m[-] Could not find details for domain group 'Enterprise Read-only Domain Controllers': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 512' 10.10.10.169
[91m[-] Could not find details for domain group 'Domain Admins': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 513' 10.10.10.169
[91m[-] Could not find details for domain group 'Domain Users': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 514' 10.10.10.169
[91m[-] Could not find details for domain group 'Domain Guests': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 515' 10.10.10.169
[91m[-] Could not find details for domain group 'Domain Computers': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 516' 10.10.10.169
[91m[-] Could not find details for domain group 'Domain Controllers': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 518' 10.10.10.169
[91m[-] Could not find details for domain group 'Schema Admins': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 519' 10.10.10.169
[91m[-] Could not find details for domain group 'Enterprise Admins': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 520' 10.10.10.169
[91m[-] Could not find details for domain group 'Group Policy Creator Owners': timed out[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 521' 10.10.10.169
[92m[+] Found details for domain group 'Read-only Domain Controllers' (RID 521)[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 522' 10.10.10.169
[92m[+] Found details for domain group 'Cloneable Domain Controllers' (RID 522)[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 525' 10.10.10.169
[92m[+] Found details for domain group 'Protected Users' (RID 525)[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 526' 10.10.10.169
[92m[+] Found details for domain group 'Key Admins' (RID 526)[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 527' 10.10.10.169
[92m[+] Found details for domain group 'Enterprise Key Admins' (RID 527)[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 1102' 10.10.10.169
[92m[+] Found details for domain group 'DnsUpdateProxy' (RID 1102)[0m
[V] Attempting to get detailed group info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c 'querygroup 1103' 10.10.10.169
[92m[+] Found details for domain group 'Contractors' (RID 1103)[0m
[92m[+] After merging groups results we have 50 group(s) total:
'1101':
  groupname: DnsAdmins
  type: local
  details: null
'1102':
  groupname: DnsUpdateProxy
  type: domain
  details:
    Description: DNS clients who are permitted to perform dynamic updates on behalf of some other clients (such as DHCP servers).
    Group Attribute: '7'
    Num Members: '0'
'1103':
  groupname: Contractors
  type: domain
  details:
    Description: Contractors
    Group Attribute: '7'
    Num Members: '1'
'498':
  groupname: Enterprise Read-only Domain Controllers
  type: domain
  details: null
'512':
  groupname: Domain Admins
  type: domain
  details: null
'513':
  groupname: Domain Users
  type: domain
  details: null
'514':
  groupname: Domain Guests
  type: domain
  details: null
'515':
  groupname: Domain Computers
  type: domain
  details: null
'516':
  groupname: Domain Controllers
  type: domain
  details: null
'517':
  groupname: Cert Publishers
  type: local
  details: null
'518':
  groupname: Schema Admins
  type: domain
  details: null
'519':
  groupname: Enterprise Admins
  type: domain
  details: null
'520':
  groupname: Group Policy Creator Owners
  type: domain
  details: null
'521':
  groupname: Read-only Domain Controllers
  type: domain
  details:
    Description: Members of this group are Read-Only Domain Controllers in the domain
    Group Attribute: '7'
    Num Members: '0'
'522':
  groupname: Cloneable Domain Controllers
  type: domain
  details:
    Description: Members of this group that are domain controllers may be cloned.
    Group Attribute: '7'
    Num Members: '0'
'525':
  groupname: Protected Users
  type: domain
  details:
    Description: Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939
      for more information.
    Group Attribute: '7'
    Num Members: '0'
'526':
  groupname: Key Admins
  type: domain
  details:
    Description: Members of this group can perform administrative actions on key objects within the domain.
    Group Attribute: '7'
    Num Members: '0'
'527':
  groupname: Enterprise Key Admins
  type: domain
  details:
    Description: Members of this group can perform administrative actions on key objects within the forest.
    Group Attribute: '7'
    Num Members: '0'
'544':
  groupname: Administrators
  type: builtin
  details: null
'545':
  groupname: Users
  type: builtin
  details: null
'546':
  groupname: Guests
  type: builtin
  details: null
'548':
  groupname: Account Operators
  type: builtin
  details: null
'549':
  groupname: Server Operators
  type: builtin
  details: null
'550':
  groupname: Print Operators
  type: builtin
  details: null
'551':
  groupname: Backup Operators
  type: builtin
  details: null
'552':
  groupname: Replicator
  type: builtin
  details: null
'553':
  groupname: RAS and IAS Servers
  type: local
  details: null
'554':
  groupname: Pre-Windows 2000 Compatible Access
  type: builtin
  details: null
'555':
  groupname: Remote Desktop Users
  type: builtin
  details: null
'556':
  groupname: Network Configuration Operators
  type: builtin
  details: null
'557':
  groupname: Incoming Forest Trust Builders
  type: builtin
  details: null
'558':
  groupname: Performance Monitor Users
  type: builtin
  details: null
'559':
  groupname: Performance Log Users
  type: builtin
  details: null
'560':
  groupname: Windows Authorization Access Group
  type: builtin
  details: null
'561':
  groupname: Terminal Server License Servers
  type: builtin
  details: null
'562':
  groupname: Distributed COM Users
  type: builtin
  details: null
'568':
  groupname: IIS_IUSRS
  type: builtin
  details: null
'569':
  groupname: Cryptographic Operators
  type: builtin
  details: null
'571':
  groupname: Allowed RODC Password Replication Group
  type: local
  details: null
'572':
  groupname: Denied RODC Password Replication Group
  type: local
  details: null
'573':
  groupname: Event Log Readers
  type: builtin
  details: null
'574':
  groupname: Certificate Service DCOM Access
  type: builtin
  details: null
'575':
  groupname: RDS Remote Access Servers
  type: builtin
  details: null
'576':
  groupname: RDS Endpoint Servers
  type: builtin
  details: null
'577':
  groupname: RDS Management Servers
  type: builtin
  details: null
'578':
  groupname: Hyper-V Administrators
  type: builtin
  details: null
'579':
  groupname: Access Control Assistance Operators
  type: builtin
  details: null
'580':
  groupname: Remote Management Users
  type: builtin
  details: null
'581':
  groupname: System Managed Accounts Group
  type: builtin
  details: null
'582':
  groupname: Storage Replica Administrators
  type: builtin
  details: null[0m

 ======================================
|    Shares via RPC on 10.10.10.169    |
 ======================================
[V] Attempting to get share list using authentication, running command: smbclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -t 5 -L //10.10.10.169 -g
[94m[*] Enumerating shares[0m
[92m[+] Found 0 share(s) for user '' with password '', try a different user[0m

 =========================================
|    Policies via RPC for 10.10.10.169    |
 =========================================
[94m[*] Trying port 445/tcp[0m
[92m[+] Found policy:
Domain password information:
  Password history length: 24
  Minimum password length: 7
  Maximum password age: not set
  Password properties:
  - DOMAIN_PASSWORD_COMPLEX: false
  - DOMAIN_PASSWORD_NO_ANON_CHANGE: false
  - DOMAIN_PASSWORD_NO_CLEAR_CHANGE: false
  - DOMAIN_PASSWORD_LOCKOUT_ADMINS: false
  - DOMAIN_PASSWORD_PASSWORD_STORE_CLEARTEXT: false
  - DOMAIN_PASSWORD_REFUSE_PASSWORD_CHANGE: false
Domain lockout information:
  Lockout observation window: 30 minutes
  Lockout duration: 30 minutes
  Lockout threshold: None
Domain logoff information:
  Force logoff time: not set[0m

 =========================================
|    Printers via RPC for 10.10.10.169    |
 =========================================
[V] Attempting to get printer info, running command: rpcclient -W MEGABANK -U % -s /tmp/tmp_fv2wya7 -c enumprinters 10.10.10.169
[91m[-] Could not get printer info via 'enumprinters': STATUS_ACCESS_DENIED[0m

Completed after 187.19 seconds


```
