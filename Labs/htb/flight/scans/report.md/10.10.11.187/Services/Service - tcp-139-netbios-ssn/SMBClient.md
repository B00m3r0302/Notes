```bash
smbclient -L //10.10.11.187 -N -I 10.10.11.187 2>&1
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp139/smbclient.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp139/smbclient.txt):

```
do_connect: Connection to 10.10.11.187 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available


```
