```bash
smbmap -H 172.16.185.83 -P 139 2>&1
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-share-permissions.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-share-permissions.txt):

```

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.4 | Shawn Evans - ShawnDEvans@gmail.com<mailto:ShawnDEvans@gmail.com>
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[-] Checking for open ports...                                                                                                    


[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[*] Detected 1 hosts serving SMB
[-] Authenticating...                                                                                                    


[*] Established 0 SMB connections(s) and 0 authenticated session(s)
                                                                                                    


[*] Closed 0 connections
[-] Authenticating...                                                                                                    


[!] Connection error on 172.16.185.83


```
```bash
smbmap -u null -p "" -H 172.16.185.83 -P 139 2>&1
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-share-permissions.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-share-permissions.txt):

```

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.4 | Shawn Evans - ShawnDEvans@gmail.com<mailto:ShawnDEvans@gmail.com>
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[-] Checking for open ports...                                                                                                    


[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[*] Detected 1 hosts serving SMB
[-] Authenticating...                                                                                                    


[*] Established 0 SMB connections(s) and 0 authenticated session(s)
                                                                                                    


[*] Closed 0 connections
[-] Authenticating...                                                                                                    


[!] Connection error on 172.16.185.83


```
```bash
smbmap -H 172.16.185.83 -P 139 -r 2>&1
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-list-contents.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-list-contents.txt):

```

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.4 | Shawn Evans - ShawnDEvans@gmail.com<mailto:ShawnDEvans@gmail.com>
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[-] Checking for open ports...                                                                                                    


[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[*] Detected 1 hosts serving SMB
[/] Authenticating...                                                                                                    


[-] Authenticating...                                                                                                    


[*] Established 0 SMB connections(s) and 0 authenticated session(s)
[\] Closing connections..                                                                                                    


[|] Closing connections..                                                                                                    


[/] Closing connections..                                                                                                    


[-] Closing connections..                                                                                                    


[\] Closing connections..                                                                                                    


[|] Closing connections..                                                                                                    


[/] Closing connections..                                                                                                    


[-] Closing connections..                                                                                                    


                                                                                                    


[*] Closed 0 connections
[/] Authenticating...                                                                                                    


[!] Connection error on 172.16.185.83
[\] Closing connections..

```
```bash
smbmap -u null -p "" -H 172.16.185.83 -P 139 -r 2>&1
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-list-contents.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-list-contents.txt):

```

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.4 | Shawn Evans - ShawnDEvans@gmail.com<mailto:ShawnDEvans@gmail.com>
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[-] Checking for open ports...                                                                                                    


[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[*] Detected 1 hosts serving SMB
[/] Authenticating...                                                                                                    


[-] Authenticating...                                                                                                    


[*] Established 0 SMB connections(s) and 0 authenticated session(s)
[\] Closing connections..                                                                                                    


[|] Closing connections..                                                                                                    


[/] Closing connections..                                                                                                    


[-] Closing connections..                                                                                                    


[\] Closing connections..                                                                                                    


[|] Closing connections..                                                                                                    


[/] Closing connections..                                                                                                    


[-] Closing connections..                                                                                                    


                                                                                                    


[*] Closed 0 connections
[/] Authenticating...                                                                                                    


[!] Connection error on 172.16.185.83
[\] Closing connections..

```
```bash
smbmap -H 172.16.185.83 -P 139 -x "ipconfig /all" 2>&1
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-execute-command.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-execute-command.txt):

```

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.4 | Shawn Evans - ShawnDEvans@gmail.com<mailto:ShawnDEvans@gmail.com>
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[-] Checking for open ports...                                                                                                    


[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[*] Detected 1 hosts serving SMB
[/] Authenticating...                                                                                                    


[*] Established 0 SMB connections(s) and 0 authenticated session(s)
[-] Closing connections..                                                                                                    


                                                                                                    


[*] Closed 0 connections
[/] Authenticating...                                                                                                    


[!] Connection error on 172.16.185.83


```
```bash
smbmap -u null -p "" -H 172.16.185.83 -P 139 -x "ipconfig /all" 2>&1
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-execute-command.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.83/scans/tcp139/smbmap-execute-command.txt):

```

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.4 | Shawn Evans - ShawnDEvans@gmail.com<mailto:ShawnDEvans@gmail.com>
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[/] Checking for open ports...                                                                                                    


[-] Checking for open ports...                                                                                                    


[\] Checking for open ports...                                                                                                    


[|] Checking for open ports...                                                                                                    


[*] Detected 1 hosts serving SMB
[/] Authenticating...                                                                                                    


[*] Established 0 SMB connections(s) and 0 authenticated session(s)
[-] Closing connections..                                                                                                    


                                                                                                    


[*] Closed 0 connections
[/] Authenticating...                                                                                                    


[!] Connection error on 172.16.185.83


```
