it is essential to start and enable the Secure Shell (SSH) service. This is a primary, low bandwidth method of connecting to the device. Additionally, through an SSH connection we are then able execute offensive operations as well as add/remove remote access services or modify existing services. Most RADs are comprised of some sort of low compute device with a Linux operating system such as a raspberry pi running Debian. SSH is not started by default, so we first need to start the service then we need to enable it to ensure that the service starts every time that the RAD is powered on which ensures we have at least one way to connect to the RAD from our local machine.

- Starting the service and making it run at boot
```bash
sudo systemctl start ssh
```
```bash
sudo systemctl enable ssh
```
After we have enabled the service, we should check to make sure that the service is “Active” and “Enabled.” This means that the service is currently running and will be started by default anytime the device is turned on.
- Checking the status of the service
```bash
sudo systemctl status ssh
```

