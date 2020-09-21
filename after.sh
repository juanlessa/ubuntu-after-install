#!bin/bash
mkdir ~/projects
cd ~/projects

#git
sudo apt install git -y
git config --global user.email "juanvlessa@ua.pt"
git config --global user.name "juanlessa"

#programming
sudo apt install build-essential default-jdk libssl-dev exuberant-ctags ncurses-term ack-grep silversearcher-ag fontconfig imagemagick libmagickwand-dev software-properties-common git vim-gtk3 curl -y
sudo apt-get install -y libreadline-dev

# sqlite3
sudo apt install libsqlite3-dev

#libpq-dev
 sudo apt install libpq-dev

#libpcap-dev
sudo apt install libpcap-dev

#apache2
sudo apt update
sudo apt install apache2 -y

#asdf
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.7.8
echo -e '\n. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo -e '\n. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc

#ruby extention
asdf plugin-add ruby https://github.com/asdf-vm/asdf-ruby.git
asdf install ruby 2.6.6
asdf global ruby 2.6.6


#gem to use metaexploit
gem install bundler
gem install sqlite3
gem install rex-text
gem install pg
gem install pcaprub
bundle install

#python
asdf plugin-add python
asdf install python 3.8.3
asdf global python 3.8.3

#python exploit-patterns 1.0.0
pip install exploit-patterns

#python redis
pip install redis

#ifconfig
sudo apt install net-tools
#locate
sudo apt install mlocate

#tmux
sudo apt install tmux

#restricted extras
sudo apt install ubuntu-restricted-extras -y

#redis
sudo apt install redis -y

#vs code
sudo snap install code --classic

#pentest
#nmap ncat
sudo apt install -y nmap
sudo apt install -y ncat
#metaexploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall

#clone metasploit repository
cd ~/Documents
git clone https://github.com/rapid7/metasploit-framework
cd ~/projects

#ssh key
ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519 -C "juanvlessa@ua.pt"
eval "$(ssh-agent -s)" #verify ssh-agent is alright
ssh-add ~/.ssh/id_ed25519 # configure agent

#connect and save github conection
ssh -T git@github.com

#gns3
sudo add-apt-repository ppa:gns3/ppa
sudo apt update 
sudo apt install gns3-gui gns3-server

#virtualbox
sudo apt install virtualbox

#spotify
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90 2EBF997C15BDA244B6EBF5D84773BD5E130D1D45
echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt update
sudo apt install spotify-client -y

#root password
sudo passwd root

#simplescreenrecorder
sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder
sudo apt update
sudo apt install simplescreenrecorder -y

#kdenlive
sudo add-apt-repository ppa:sunab/kdenlive-release
sudo apt update
sudo apt install kdenlive
