#!/bin/bash

#instalacion de programas en pacman
sudo pacman -Syu
sudo pacman -Sy qtile lightdm-gtk-greeter lightdm-gtk-greeter-settings thunar alacritty pamixer rofi rofi-power-menu brave base-devel picom networkmanager network-manager-applet feh nitrogen volumeicon cbatticon ttf-dejavu ttf-liberation noto-fonts pulseaudio pavucontrol brightnessctl arandr ntfs-3g libnotify notification-daemon xorg-xinit python3 python-pip ranger lxappearance lightdm-webkit2-greeter geeqie vlc git code htop neovim wine winetricks virtualbox blueman kdeconnect xf86-video-vmware wpa_supplicant wget curl alsa cmatrix cmake dhcpcd dhcp discord flatpak grub jmtpfs lightdm-webkit-theme-aether zip unzip unrar 
#habilitar internet
sudo systemcyl enable NetworkManager.service

#instalacion de yay
cd /home/idk
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

#instalacion de programas en yay
yay -Syu
yay -S obs-studio-browser

#instalacion de snapd
cd /home/idk
git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install spotify

