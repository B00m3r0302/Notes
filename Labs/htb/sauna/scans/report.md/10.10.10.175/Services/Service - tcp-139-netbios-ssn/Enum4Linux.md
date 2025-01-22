```bash
enum4linux-ng -A -d -v 10.10.10.175 2>&1
```

[/home/kali/Notes/Labs/htb/sauna/scans/tcp139/enum4linux-ng.txt](file:///home/kali/Notes/Labs/htb/sauna/scans/tcp139/enum4linux-ng.txt):

```
[92mENUM4LINUX - next generation (v1.3.4)[0m

 ==========================
|    Target Information    |
 ==========================
[94m[*] Target ........... 10.10.10.175[0m
[94m[*] Username ......... ''[0m
[94m[*] Random Username .. 'uaucigoh'[0m
[94m[*] Password ......... ''[0m
[94m[*] Timeout .......... 5 second(s)[0m

 =====================================
|    Listener Scan on 10.10.10.175    |
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
|    Domain Information via LDAP for 10.10.10.175    |
 ====================================================
[94m[*] Trying LDAP[0m
[92m[+] Appears to be root/parent DC[0m
[92m[+] Long domain name is: EGOTISTICAL-BANK.LOCAL[0m

 ===========================================================
|    NetBIOS Names and Workgroup/Domain for 10.10.10.175    |
 ===========================================================
[V] Trying to get NetBIOS names information, running command: nmblookup -s /tmp/tmp59m7pv0c -A 10.10.10.175
[91m[-] Could not get NetBIOS names information via 'nmblookup': timed out[0m

 =========================================
|    SMB Dialect Check on 10.10.10.175    |
 =========================================
[94m[*] Trying on 445/tcp[0m
[92m[+] Supported dialects and settings:
Supported dialects:
  SMB 1.0: false
  SMB 2.02: true
  SMB 2.1: true
  SMB 3.0: true
  SMB 3.1.1: true
Preferred dialect: SMB 3.0
SMB1 only: false
SMB signing required: true[0m

 ===========================================================
|    Domain Information via SMB session for 10.10.10.175    |
 ===========================================================
[94m[*] Enumerating via unauthenticated SMB session on 445/tcp[0m
[92m[+] Found domain information via SMB
NetBIOS computer name: SAUNA
NetBIOS domain name: EGOTISTICALBANK
DNS domain: EGOTISTICAL-BANK.LOCAL
FQDN: SAUNA.EGOTISTICAL-BANK.LOCAL
Derived membership: domain member
Derived domain: EGOTISTICALBANK[0m

 =========================================
|    RPC Session Check on 10.10.10.175    |
 =========================================
[94m[*] Check for null session[0m
[V] Attempting to make session, running command: smbclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -t 5 -c help '//10.10.10.175/ipc$'
[92m[+] Server allows session using username '', password ''[0m
[94m[*] Check for random user[0m
[V] Attempting to make session, running command: smbclient -W EGOTISTICALBANK -U uaucigoh% -s /tmp/tmp59m7pv0c -t 5 -c help '//10.10.10.175/ipc$'
[91m[-] Could not establish random user session: STATUS_LOGON_FAILURE[0m

 ===================================================
|    Domain Information via RPC for 10.10.10.175    |
 ===================================================
[V] Attempting to get domain SID, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c lsaquery 10.10.10.175
[92m[+] Domain: EGOTISTICALBANK[0m
[92m[+] Domain SID: S-1-5-21-2966785786-3096785034-1186376766[0m
[92m[+] Membership: domain member[0m

 ===============================================
|    OS Information via RPC for 10.10.10.175    |
 ===============================================
[94m[*] Enumerating via unauthenticated SMB session on 445/tcp[0m
[92m[+] Found OS information via SMB[0m
[94m[*] Enumerating via 'srvinfo'[0m
[V] Attempting to get OS info with command, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c srvinfo 10.10.10.175
[91m[-] Could not get OS info via 'srvinfo': STATUS_ACCESS_DENIED[0m
[92m[+] After merging OS information we have the following result:
OS: Windows 10, Windows Server 2019, Windows Server 2016
OS version: '10.0'
OS release: '1809'
OS build: '17763'
Native OS: not supported
Native LAN manager: not supported
Platform id: null
Server type: null
Server type string: null[0m

 =====================================
|    Users via RPC on 10.10.10.175    |
 =====================================
[94m[*] Enumerating users via 'querydispinfo'[0m
[V] Attempting to get userlist, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c querydispinfo 10.10.10.175
[91m[-] Could not find users via 'querydispinfo': STATUS_ACCESS_DENIED[0m
[94m[*] Enumerating users via 'enumdomusers'[0m
[V] Attempting to get userlist, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c enumdomusers 10.10.10.175
[91m[-] Could not find users via 'enumdomusers': STATUS_ACCESS_DENIED[0m

 ======================================
|    Groups via RPC on 10.10.10.175    |
 ======================================
[94m[*] Enumerating local groups[0m
[V] Attempting to get local groups, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c 'enumalsgroups domain' 10.10.10.175
[91m[-] Could not get groups via 'enumalsgroups domain': STATUS_ACCESS_DENIED[0m
[94m[*] Enumerating builtin groups[0m
[V] Attempting to get builtin groups, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c 'enumalsgroups builtin' 10.10.10.175
[91m[-] Could not get groups via 'enumalsgroups builtin': STATUS_ACCESS_DENIED[0m
[94m[*] Enumerating domain groups[0m
[V] Attempting to get domain groups, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c enumdomgroups 10.10.10.175
[91m[-] Could not get groups via 'enumdomgroups': STATUS_ACCESS_DENIED[0m

 ======================================
|    Shares via RPC on 10.10.10.175    |
 ======================================
[V] Attempting to get share list using authentication, running command: smbclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -t 5 -L //10.10.10.175 -g
[94m[*] Enumerating shares[0m
[92m[+] Found 0 share(s) for user '' with password '', try a different user[0m

 =========================================
|    Policies via RPC for 10.10.10.175    |
 =========================================
[94m[*] Trying port 445/tcp[0m
[91m[-] SMB connection error on port 445/tcp: STATUS_ACCESS_DENIED[0m
[94m[*] Trying port 139/tcp[0m
[91m[-] SMB connection error on port 139/tcp: session failed[0m

 =========================================
|    Printers via RPC for 10.10.10.175    |
 =========================================
[V] Attempting to get printer info, running command: rpcclient -W EGOTISTICALBANK -U % -s /tmp/tmp59m7pv0c -c enumprinters 10.10.10.175
[91m[-] Could not get printer info via 'enumprinters': STATUS_ACCESS_DENIED[0m

Completed after 13.74 seconds


```
