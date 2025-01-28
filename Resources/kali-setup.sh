#!/bin/bash

# Alyssa Feagans 6/2024

home="/home/kali" # UPDATE ME TO USER'S HOME DIRECTORY!

# Install Oh-My-Zsh
# ------------------------------------------------------------------------------------------------
#sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install spaceship prompt
echo "echo $ZSH_VERSION #> 5.8.1\n"
echo "echo -e "\xee\x82\xa0" #> \n"
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

# Adding variables to ~/.zshrc
echo 'alias lsa="ls -la"' >> ~/.zshrc
echo 'alias vol3="python3 /opt/volatility3/vol.py"' >> ~/.zshrc
echo 'alias shellsource="source ~/.zshrc"' >> /.zshrc
source ~/.zshrc
# Get Default shell
# -------------------------------------------------------------------------------------------------
default_shell=$(echo $SHELL)

if [[ $default_shell == *"zsh"* ]]; then
    echo "Default shell is zsh.."
    shell_config="$home/.zshrc"
else
    echo "Assuming default shell is bash or shell.."
    shell_config="$home/.bashrc"
fi

# Install & clean packages
# -------------------------------------------------------------------------------------------------
sudo apt update -y && sudo apt upgrade -y
sudo apt autoremove -y
sudo apt autoclean 

sudo apt install -y neovim enum4linux-ng libreoffice-common fcrackzip freerdp3-x11 havoc cmake libssl-dev awscli docker.io docx2txt eyewitness feroxbuster flameshot golang gowitness impacket-scripts pack seclists sshuttle zaproxy can-utils powercat powershell powershell-empire powersploit crackmapexec netexec evil-winrm python3-can jq python3 python3-pip curl dnsrecon enum4linux gobuster nbtscan nikto nmap onesixtyone oscanner redis-tools smbclient smbmap snmp sslscan sipvicious tnscmd10g rustup whatweb wkhtmltopdf python3-venv autorecon obsidian code-oss thonny 

# Install Project Discovery
# https://blog.projectdiscovery.io/getting-started-with-projectdiscovery-in-linux-and-windows/
# -------------------------------------------------------------------------------------------------
echo "Installing Project Discovery ...\n"
# Assumes golang is installed, TODO add a check here

# Add GOPATH to shell config
go_path=$(go env | grep GOPATH | cut -d "'" -f 2)
echo "export PATH='$PATH:$go_path/bin'" >> $shell_config
source $shell_config

go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest

# Prepare tools and wordlists
# -------------------------------------------------------------------------------------------------

# Upgrading pip
echo "Upgrading pip\n"
python3 -m pip install --upgrade pip

# Git clone repos
# -------------------------------------------------------------------------------------------------
echo "Cloning github repos ...\n"

# Basic Blob Finder 
sudo git clone https://github.com/joswr1ght/basicblobfinder.git /opt/basicblobfinder

# SUDO KILLER
sudo git clone https://github.com/TH3xACE/SUDO_KILLER.git /opt/SUDO_KILLER

# Rubeus
sudo git clone https://github.com/GhostPack/Rubeus.git /opt/Rubeus

# Hudson's Notes
sudo git clone https://github.com/B00m3er0302/Notes.git /home/kali/Notes

# GCPBucketBrute
echo "Installing GCPBucketBrute ...\n"
sudo git clone https://github.com/RhinoSecurityLabs/GCPBucketBrute.git /opt/GCPBucketBrute
python3 -m pip install -r /opt/GCPBucketBrute/requirements.txt

# Install Zerotier
# -------------------------------------------------------------------------------------------------
echo "Installing Zerotier ...\n"
cd ~/Downloads
curl -s https://install.zerotier.com | sudo bash


# Pip Install
# -------------------------------------------------------------------------------------------------
echo "Installing python packages with pip ...\n"
python3 -m pip install updog


# Install Wordlists
# -------------------------------------------------------------------------------------------------
echo "Installing wordlist files ...\n"
cd /usr/share/wordlists

# Create a new file with weak seasonal passwords
sudo curl -L "https://weakpasswords.net/" > seasonal-pw.txt
# Delete last line in file (author tag)
sudo sed -i '$d' seasonal-pw.txt
# Remove white lines
sudo sed -i '/^$/d' seasonal-pw.txt

# Hashcat Rules
cd /usr/share/hashcat/rules
sudo git clone https://github.com/stealthsploit/OneRuleToRuleThemStill.git

# Enabling SSH and Apache server
# ------------------------------------------------------------------------------------------------
echo "Starting SSH & Apache2 server\n"
sudo systemctl start ssh
sudo systemctl start apache2
sudo systemctl enable ssh
sudo systemctl enable apache2

# Copy files to SSH server
# ------------------------------------------------------------------------------------------------
echo "Pulling and copying files to the apache2 server\n"

echo "Done :)\n"
echo "Rebooting...\n"
sudo reboot

