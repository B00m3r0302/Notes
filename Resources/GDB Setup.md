Pwndbg: https://github.com/pwndbg/pwndbg

Peda: https://github.com/longld/peda

GEF: https://github.com/hugsy/gef

# Setup
## PwnDBG
- From /home/USER
```bash
git clone https://github.com/pwndbg/pwndbg
```
```bash
cd pwndbg
```
```bash
./setup.sh
```
```bash
mv pwndbg ~/pwndbg-src
```
```bash
echo "source ~/pwndbg-src/gdbinit.py" > ~/.gdbinit_pwndbg
```
## PEDA
- From /home/user
```bash
git clone https://github.com/longld/peda.git ~/peda
```
## GEF
```bash
wget -O ~/.gdbinit-gef.py https://raw.githubusercontent.com/hugsy/gef/refs/heads/main/gef.py
```
## .gdbinit file
```bash
sudo vim ~/.gdbinit
```
- Add the following contents
```ini
define init-peda
source ~/peda/peda.py
end
document init-peda
Initializes the PEDA (Python Exploit Development Assistant for GDB) framework
end

define init-pwndbg
source ~/.gdbinit_pwndbg
end
document init-pwndbg
Initializes PwnDBG
end

define init-gef
source ~/.gdbinit-gef.py
end
document init-gef
Initializes GEF (GDB Enhanced Features)
end
```
## Create executables
###  gdb-peda
```bash
sudo vim /usr/bin/gdb-peda
```
- Add the following contents
```bash
#!/bin/sh
exec gdb -q -ex init-peda "$@"
```
### gdb-pwndbg
```bash
sudo vim /usr/bin/gdb-pwndbg
```
- Add the following contents
```bash
#!/bin/sh
exec gdb -q -ex init-pwndbg "$@"
```
### gdb-gef
```bash
sudo vim /usr/bin/gdb-gef
```
- Add the following contents
```bash
#!/bin/sh
exec gdb -q -ex init-gef "$@"
```
## Make them executable
```bash 
sudo chmod +x /usr/bin/gdb-*
```
# Usage
## gdb-peda
```bash
gdb-peda
```
## gdb-pwndbg
```bash
gdb-pwndbg
```
## gdb-gef
```bash
gdb-gef
```
