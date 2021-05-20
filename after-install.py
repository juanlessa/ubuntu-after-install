import os
from getpass import getpass


def install(password: str, programa: str):
    """ if your install is like "sudo apt install ProgramName you only need to
     call this function, install(password, ProgramName)

    Args:
        password (str): sudo password ("password is a variable, then you only need to call)
        programa (str): program name to install
    """
    os.system("echo '{}' | sudo -S apt install -y {}".format(password, programa))
############################################################################################################################################


def menu(options):
    """ function to print menu
    """
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
        print("  {:>2} - {:25} {:>2} - {:25}".format(i,
              options[i-1], m+i, options[m+i-1]))
    res = ""
    while not(res.isnumeric()) or float(res) < 1 or float(res) > len(options):
        res = input("which do you want to install? > ")
        if res == "exit":
            exit(0)
    res = options[int(res)-1]
    return res
############################################################################################################################################


def main():
    # authentication
    password = ""
    print("You need to enter SUDO password")
    while password == "":
        password = getpass()
    # programs installation
    while True:
        # show menu and get options selected
        opt = menu(options)
        # validate option
        if opt == "git":
            install(password, "git")
        elif opt == "programming liberies":
            install(password, "build-essential")
            install(password, "default-jdk")
            install(password, "libssl-dev")
            install(password, "exuberant-ctags")
            install(password, "ncurses-term")
            install(password, "ack-grep")
            install(password, "silversearcher-ag")
            install(password, "fontconfig")
            install(password, "imagemagick")
            install(password, "libmagickwand-dev")
            install(password, "software-properties-common")
            install(password, "curl")
            install(password, "libreadline-dev")
            install(password, "libsqlite3-dev")
            install(password, "libpq-dev")
            install(password, "net-tools")
            install(password, "mlocate")
        elif opt == "vim-gtk3":
            install(password, "vim-gtk3")
        elif opt == "tmux":
            install(password, "tmux")
        elif opt == "apache2":
            os.system(f"echo '{password}' | sudo -S apt update")
            install(password, "apache2")
        elif opt == "redis":
            install(password, "redis")
        elif opt == "python":
            install(password, "python3")
            install(password, "python3-pip")
            os.system("pip3 install exploit-patterns")
            os.system("pip3 install redis")
            os.system("pip3 install cryptography")
            os.system("pip3 install pykcs11")
        elif opt == "ruby":
            install(password, "ruby-full")
        elif opt == "nodejs":
            install(password, "nodejs")
            install(password, "npm")
        elif opt == "keepassxc":
            install(password, "keepassxc")
        elif opt == "metasploit":
            os.system(f"echo '{password}' | sudo -S gem install bundler")
            os.system(f"echo '{password}' | sudo -S gem install sqlite3")
            os.system(f"echo '{password}' | sudo -S gem install rex-text")
            os.system(f"echo '{password}' | sudo -S gem install pg")
            os.system(f"echo '{password}' | sudo -S gem install pcaprub")
            os.system("bundle install")
            os.system(f"echo '{password}'| sudo curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && \./msfinstall")
            os.system("rm -rf msfinstall")
        elif opt == "nmap":
            install(password, "nmap")
        elif opt == "ncat":
            install(password, "ncat")
        elif opt == "xca":
            install(password, "xca")
        elif opt == "ubuntu-restricted-extras":
            install(password, "ubuntu-restricted-extras")
        elif opt == "vs code":
            os.system(f"echo '{password}' | sudo snap install code --classic")
        elif opt == "gns3":
            os.system(
                f"echo '{password}' | sudo add-apt-repository ppa:gns3/ppa")
            os.system(f"echo '{password}' | sudo apt update")
            os.system(
                f"echo '{password}' | sudo apt install gns3-gui gns3-server")
        elif opt == "virtualbox":
            install(password, "virtualbox")
        elif opt == "spotfy":
            os.system(f"echo '{password}' | sudo -S apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90 2EBF997C15BDA244B6EBF5D84773BD5E130D1D45")
            os.system(
                "echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list")
            os.system(f"echo '{password}' | sudo -S apt update")
            install(password, "spotify-client")
        elif opt == "simplescreenrecorder":
            os.system(
                f"echo '{password}' | sudo -S add-apt-repository ppa:maarten-baert/simplescreenrecorder")
            os.system(f"echo '{password}' | sudo -S apt update")
            install(password, "simplescreenrecorder")
        elif opt == "kdenlive":
            os.system(
                f"echo '{password}' | sudo -S add-apt-repository ppa:sunab/kdenlive-release")
            os.system(f"echo '{password}' | sudo -S apt update")
            install(password, "kdenlive")
############################################################################################################################################


# add insominia
# add yarn
# zsh
# add ohmyzhec
# add docker and add permissions tu run without sudo
# add dbeaver
# add flatremix and qogir themes
# add fira code hack and jetbrains font
# add notes application
# add tulix and config tilix shortcuts (ctrl+alt+T: tilix --> open tilix,
#                                       F9: tilix --quake --> tilix quake)
# config tilix splits crtl+alt+R split right, ctrl+alt+E split down

options = ["git", "programming liberies", "vim-gtk3", "tmux", "apache2",
           "redis", "python", "ruby", "nodejs", "keepassxc", "metasploit",
           "nmap", "ncat", "xca", "ubuntu-restricted-extras", "vs code",
           "spotfy", "simplescreenrecorder", "kdenlive"]

main()
