import os
from getpass import getpass


def install(senha, programa):
    os.system("echo '{}' | sudo -S apt install -y {}".format(senha, programa))
############################################################################################################################################

def menu():
    if len(options) % 2 == 0:
        m = len(options)//2
    else:
        m = (len(options) + 1)//2
    print("\n                       installation menu")
    print("type exit to cancel")
    for i in range(1, m+1):
        if len(options) < i+m:
            print("  {:>2} - {:25}".format(i, options[i-1]))
            break
        print("  {:>2} - {:25} {:>2} - {:25}".format(i, options[i-1], m+i, options[m+i-1]))
    res = ""
    while not(res.isnumeric()) or float(res) < 1 or float(res) > len(options):
        res = input("which do you want to install? > ")
        if res == "exit":
            exit(0)
    res = options[int(res)-1]
    return res
############################################################################################################################################


def main():
    #altentication
    senha = ""
    print("You need to enter SUDO password")
    while senha == "":
        senha = getpass()
    #programs instalation
    while True:
        #show menu and get options selected
        opt = menu()
        #validate option
        if opt == "git":
            install(senha,"git")
        elif opt == "programming liberies":
            install(senha, "build-essential")
            install(senha, "default-jdk")
            install(senha, "libssl-dev")
            install(senha, "exuberant-ctags")
            install(senha, "ncurses-term")
            install(senha, "ack-grep")
            install(senha, "silversearcher-ag")
            install(senha, "fontconfig")
            install(senha, "imagemagick")
            install(senha, "libmagickwand-dev")
            install(senha, "software-properties-common")
            install(senha, "curl")
            install(senha, "libreadline-dev")
            install(senha, "libsqlite3-dev")
            install(senha, "libpq-dev")
            install(senha, "net-tools")
            install(senha, "mlocate")
        elif opt == "vim-gtk3":
            install(senha, "vim-gtk3")
        elif opt == "tmux":
            install(senha, "tmux")
        elif opt == "apache2":
            os.system(f"echo '{senha}' | sudo -S apt update")
            install(senha, "apache2")
        elif opt == "redis":
            install(senha, "redis")
        elif opt == "python":
            install(senha, "python3")
            install(senha, "python3-pip")
            os.system("pip3 install exploit-patterns")
            os.system("pip3 install redis")
            os.system("pip3 install cryptography")
            os.system("pip3 install pykcs11")
        elif opt == "ruby":
            install(senha, "ruby-full")
        elif opt == "nodejs":
            install(senha, "nodejs")
            install(senha, "npm")
        elif opt == "keepassxc":
            install(senha, "keepassxc")
        elif opt == "metasploit":
            os.system("gem install bundler")
            os.system("gem install sqlite3")
            os.system("gem install rex-text")
            os.system("gem install pg")
            os.system("gem install pcaprub")
            os.system("bundle install")
            os.system(f"echo '{senha}'| sudo curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && \./msfinstall")
            os.system("rm -rf msfinstall")
        elif opt == "nmap":
            install(senha, "nmap")
        elif opt == "ncat":
            install(senha, "ncat")
        elif opt == "xca":
            install(senha, "xca")
        elif opt == "ubuntu-restricted-extras":
            install(senha, "ubuntu-restricted-extras")
        elif opt == "vs code":
            os.system(f"echo '{senha}' | sudo snap install code --classic")
        elif opt == "gns3":
            os.system(f"echo '{senha}' | sudo add-apt-repository ppa:gns3/ppa")
            os.system(f"echo '{senha}' | sudo apt update")
            os.system(f"echo '{senha}' | sudo apt install gns3-gui gns3-server")
        elif opt == "virtualbox":
            install(senha, "virtualbox")
        elif opt == "spotfy":
            os.system(f"echo '{senha}' | sudo -S apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90 2EBF997C15BDA244B6EBF5D84773BD5E130D1D45")
            os.system("echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list")
            os.system(f"echo '{senha}' | sudo -S apt update")
            install(senha, "spotify-client")
        elif opt == "simplescreenrecorder":
            os.system(f"echo '{senha}' | sudo -S add-apt-repository ppa:maarten-baert/simplescreenrecorder")
            os.system(f"echo '{senha}' | sudo -S apt update")
            install(senha, "simplescreenrecorder")
        elif opt == "kdenlive":
            os.system(f"echo '{senha}' | sudo -S add-apt-repository ppa:sunab/kdenlive-release")
            os.system(f"echo '{senha}' | sudo -S apt update")
            install(senha, "kdenlive")
############################################################################################################################################

#add insominia
options = ["git", "programming liberies", "vim-gtk3", "tmux", "apache2", "redis", "python", "ruby", "nodejs", "keepassxc","metasploit", "nmap","ncat", "xca", "ubuntu-restricted-extras", "vs code", "spotfy", "simplescreenrecorder", "kdenlive"]
main()
