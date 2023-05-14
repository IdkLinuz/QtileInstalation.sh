#!/bin/bash
mv QtileInstalation.sh QtileInstalation

#instalacion de programas en pacman
sudo pacman -Syu
sudo pacman -Sy qtile lightdm-gtk-greeter lightdm-gtk-greeter-settings thunar alacritty pamixer rofi rofi-power-menu brave base-devel picom networkmanager network-manager-applet feh nitrogen volumeicon cbatticon ttf-dejavu ttf-liberation noto-fonts pulseaudio pavucontrol brightnessctl arandr ntfs-3g libnotify notification-daemon xorg-xinit python3 python-pip ranger lxappearance lightdm-webkit2-greeter geeqie vlc git code htop neovim wine winetricks virtualbox blueman kdeconnect xf86-video-vmware wpa_supplicant wget curl alsa cmatrix cmake dhcpcd dhcp discord flatpak grub jmtpfs lightdm-webkit-theme-aether zip unzip unrar virtualbox-host-dkms linux-lts-headers virtualbox-guest-iso flameshot
#habilitar internet
sudo systemctl enable NetworkManager.service
sudo systemctl start NetworkManager.service
#instalacion de yay
cd /home/idk
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

#instalacion de programas en yay
yay -Syu
yay -S obs-studio-browser
yay -S nerd-fonts-git
#instalacion de snapd
cd
git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install spotify
sudo snap install whatsapp-for-linux

#Configurar lightdm
cd ~/QtileInstalation
cp lightdm.conf /etc/lightdm/lightdm.conf
cp lightdm-webkit2-greeter.conf /etc/lightdm/lightdm-webkit2-greeter.conf

#Instalacion del qtile
cd ~/QtileInstalation
cp config.py ~/.config/qtile/config.py
cp autostart.sh ~/.config/qtile/autostart.sh

#Instalacion tema gtk
cd
https://github.com/dracula/alacritty/archive/master.zip
unzip alacritty-master.zip

#Instalar virtualbox
cd ~/QtileInstalation
sudo modprobe vboxdrv
cp virtualbox.conf /etc/modules-load.d/virtualbox.conf
sudo gpasswd -a $USER vboxusers

#Configurar rofi
git clone https://github.com/adi1090x/rofi.git
cd rofi
chmod +x setup.sh
bash setup.sh
cd ~/QtileInstalation
cp MisColores.rasi ~/.config/rofi/colors
cp launcher.sh ~/.config/rofi/launchers/type-3/launcher.sh
cp powermenu.sh ~/.config/rofi/powermenu/type-3/powermenu.sh

#Configurar alacritty
cd ~/QtileInstalation
cp alacritty.yml ~/.config/alacritty/alacritty.yml

#Instalar grub
cd
git clone https://github.com/Teraskull/bigsur-grub2-theme

cd bigsur-grub2-theme

./install.sh
