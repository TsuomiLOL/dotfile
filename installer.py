import os
import time

os.system("sudo pacman -Syyuu archlinux-keyring")
os.system("sudo pacman -S neovim xed")

#yay
print("---------- Yay ----------")
yayinstall = input("Install yay? y/n: ")
if yayinstall == "y":
    os.system("sudo pacman -S git")
    os.system("cd /opt")
    os.system("sudo git clone https://aur.archlinux.org/yay-git.git")
    os.system("sudo chown -R tsuomi:tsuomi ./yay-git")
    os.system("cd yay-git")
    os.system("makepkg -si")
    os.system("cd ~")
else:
    pass

#paru
print("---------- Paru ----------")
os.system("sudo pacman -S --needed base-devel")
os.system("git clone https://aur.archlinux.org/paru.git")
os.system("cd paru")
os.system("makepkg -si")
os.system("cd ~")

#doas
print("---------- Doas ----------")
os.system("git clone https://aur.archlinux.org/doas.git")
os.system("cd doas")
os.system("makepkg -si")
os.system("cd /etc/")
print("""\n\n\n\n\nWrite in doas.conf:

permit :wheel

25 seconds...""")
time.sleep(25)
os.system("sudo nvim doas.conf")
os.system("cd ~")

#time
print("---------- Time ----------")
os.system("sudo ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime")
os.system("localectl set-locale LANG=en_US.UTF-8")

#login screen
#print("---------- Login Screen ----------")
#os.system("sudo pacman -S sddm")
#os.system("systemctl enable sddm")

#application
print("---------- Application ----------")
os.system("yay -S i3-gaps dmenu polybar alacritty plasma noto-fonts-emoji noto-fonts noto-fonts-cjk noto-fonts-extra picom pavucontrol ttf-nerd-fonts-symbols-mono net-tools fuse htop radeontop p7zip heroic-games-launcher-bin torbrowser-launcher wireshark-qt noisetorch-bin dunst rofi openvpn rclone mpv firefox-developer-edition libva-utils libva-mesa-driver mesa-vdpau yt-dlp nautilus thunar wine-staging proton-ge-custom-bin doas virtualbox gvfs thunar-volman scrcpy papirus-icon-theme stacer-bin bottom lxappearance latte-dock libappindicator-gtk3 spectacle zsh grapejuice pfetch")

#zsh
print("---------- Zsh ----------")
os.system('sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"')
os.system("sudo git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")

#swap
print("---------- Swap ----------")
os.system("cd ~")
os.system("sudo dd if=/dev/zero of=/swapfile bs=1G count=10")
os.system("sudo chmod 600 /swapfile")
os.system("sudo mkswap /swapfile")
os.system("sudo swapon /swapfile")
print("""\n\n\n\n\nWrite in fstab:

/swapfile none swap	defaults 0 0

25 seconds...""")
time.sleep(25)
os.system("sudo nvim /etc/fstab")

#roblox
print("---------- Roblox ----------")
a = input("Install Roblox? y/n: ")
if a == "y":
    os.system("git clone --depth=1 https://github.com/Frogging-Family/wine-tkg-git.git")
    os.system("cd wine-tkg-git/")
    os.system("curl https://raw.githubusercontent.com/e666666/robloxWineBuildGuide/main/roblox-wine-staging-v2.2.patch --output roblox-wine-staging-v2.2.patch")
    os.system("git apply roblox-wine-staging-v2.2.patch --allow-empty")
    os.system("cd wine-tkg-git")
    os.system("makepkg -si")
    os.system("wget https://pastebin.com/raw/5SeVb005 -O /tmp/grapejuice-wine-tkg.py")
    os.system("python3 /tmp/grapejuice-wine-tkg.py")
else:
    pass

print("\n\n\n\n\n\n\n\n\nRun: pip3 install jedi")
