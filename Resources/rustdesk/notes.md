#RustDesk
##Installation
1. sudo apt install -y rustc cargo xrdp xfce4 xfce4-goodies
2. sudo adduser -m -d /home/kalirdp kalirdp
3. set the password
4. for each user using rdp
```bash
echo "startxfce4" > ~/.xsession
```
5. download the latest version of the rustdesk .deb from https://github.com/rustdesk/rustdesk/releases/tag/1.3.7
6. git clone --recurse-submodules https://github.com/rustdesk/rustdesk.git
7. cd rustdesk
8. run the following to build the binary
```bash
cargo build --release
```
9. cd to target/release
10. run the following to get the binaries into /usr/bin
```bash
sudo cp hbbr /usr/bin
```
```bash
sudo cp hbbs /usr/bin
```
11. create the service files that go in /etc/systemd/system/ just copy them from Notes/Resources/rustdesk/service-files to that directory 
12. Run the following to start the services on boot 
```bash
sudo systemctl enable rustdesk-hbbr.service
```
```bash
sudo systemctl enable rustdesk-hbbs.service
```
13. Complete

