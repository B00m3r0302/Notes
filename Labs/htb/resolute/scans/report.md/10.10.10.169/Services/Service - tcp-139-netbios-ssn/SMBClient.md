```bash
smbclient -L //10.10.10.169 -N -I 10.10.10.169 2>&1
```

[/home/kali/Notes/Labs/htb/resolute/scans/tcp139/smbclient.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/tcp139/smbclient.txt):

```
do_connect: Connection to 10.10.10.169 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available


```
