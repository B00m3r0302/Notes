```bash
hydra smtp-enum://10.10.10.77:25/vrfy -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" 2>&1
```

[/home/kali/Notes/Labs/htb/reel/scans/tcp25/tcp_25_smtp_user-enum_hydra_vrfy.txt](file:///home/kali/Notes/Labs/htb/reel/scans/tcp25/tcp_25_smtp_user-enum_hydra_vrfy.txt):

```
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-01-27 20:52:45
[DATA] max 16 tasks per 1 server, overall 16 tasks, 17 login tries (l:17/p:1), ~2 tries per task
[DATA] attacking smtp-enum://10.10.10.77:25/vrfy
[ERROR] command is disabled on the server (choose different method): 502 VRFY disallowed.
1 of 1 target completed, 0 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-01-27 20:52:46


```
```bash
hydra smtp-enum://10.10.10.77:25/expn -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" 2>&1
```

[/home/kali/Notes/Labs/htb/reel/scans/tcp25/tcp_25_smtp_user-enum_hydra_expn.txt](file:///home/kali/Notes/Labs/htb/reel/scans/tcp25/tcp_25_smtp_user-enum_hydra_expn.txt):

```
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-01-27 20:52:47
[DATA] max 16 tasks per 1 server, overall 16 tasks, 17 login tries (l:17/p:1), ~2 tries per task
[DATA] attacking smtp-enum://10.10.10.77:25/expn
1 of 1 target completed, 0 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-01-27 20:52:48


```
