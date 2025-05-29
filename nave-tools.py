# Importing necessary modules
import os
import time

# colours setup
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'

# Create a banner
def banner():
 os.system("clear")
 print("\033[32m")
 print(" _    _  ____  _     _____      _     ____  ____  _  __")
 print("/ \  / |/  _ \/ \ |\/  __/     / \ /|/  _ \/   _\/ |/ /")
 print("| |\ | || / \|| | //|  \ _____ | |_||| / \||  /  | |_/")
 print("| | \| || |-||| \// |  /_\____\| | ||| |-|||  \__| | |")
 print("\_/  \_|\_/ \|\__/  \____\     \_/ \|\_/ \|\____/\_|\_)")

# Create and display a choices
def display_choices():
    banner()
    print("____________________________________________________")
    print("| ------------- TOOL NAME : NAVE-TOOLS ------------ |")
    print("| --------------- AUTHOR : NAVE-HACK -------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"CHOICES:",b+"                                     |")
    print(b+"|",g+"1.",r+"Social media phishing tools", y+"(6)",b+"           |")
    print(b+"|",g+"2.",r+"URL hider tools",y+"            (4)",b+"           |")
    print(b+"|",g+"nave.",r+"To exit",b+"                                |")
    print(b+"•••••••••••••••••••••••••••••••••••••••••••••••••")

# Get users choice
def get_user_choice():
    return input("Enter choice : ")

# start the script
def main():
        display_choices()
        choice = get_user_choice()

        if choice == '1':
          page_1()

        elif choice == '2':
          page_2()

        elif choice == "nave":
          os.system("exit")

        else:
          os.system("python3 nave-tools.py")

# Create a phishing tools choice page
def page_1():
    banner()
    print("____________________________________________________")
    print("| ------------- TOOL NAME : PHISHING TOOLS -------- |")
    print("| ----------------- AUTHOR : NAVE-HACK ------------ |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"PHISHING TOOLS:",b+"                              |")
    print(b+"|",g+"1.",r+"ZPHISHER",y+"       (shell)",b+"                   |")
    print(b+"|",g+"2.",r+"MAXPHISHER",y+"     (python)",b+"                  |")
    print(b+"|",g+"3.",r+"ADVPHISHING",y+"    (shell)",b+"                   |")
    print(b+"|",g+"4.",r+"GOPHISH",y+"        (golang)",b+"                  |")
    print(b+"|",g+"5.",r+"FIERCEPHISH",y+"    (php)",b+"                     |")
    print(b+"|",g+"6.",r+"SHELLPHISH",y+"     (shell)",b+"                   |")
    print(b+"•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
               os.system("clear")
               os.system(" pkg install git -y")
               os.system(" sudo apt install git -y")
               os.system(" git clone --depth=1 https://github.com/htr-tech/zphisher.git")
               os.system("clear")
               os.system(" bash zphisher/zphisher.sh ")

    elif choice == "2":
               os.system("clear")
               os.system("pkg install git python3 php openssh -y")
               os.system("sudo apt install git python3 php openssh-client -y")
               os.system("git clone https://github.com/KasRoudra2/MaxPhisher")
               os.system("pip3 install -r MaxPhisher/files/requirements.txt")
               os.system("pip3 install maxphisher")
               os.system("sudo pip3 install maxphisher")
               os.system("clear")
               os.system("python3 MaxPhisher/maxphisher.py")

    elif choice == "3":
               os.system("clear")
               os.system("pkg install git -y")
               os.system("sudo apt install git -y")
               os.system("git clone https://github.com/Ignitetch/AdvPhishing.git")
               os.system("bash AdvPhishing/Android-Setup.sh")
               os.system("bash AdvPhishing/Linux-Setup.sh")
               os.system("clear")
               os.system("bash AdvPhishing/AdvPhishing.sh")

    elif choice == "4":
               os.system("clear")
               os.system("pkg install git golang -y")
               os.system("apt install sudo -y")
               os.system("sudo apt install git golang-go -y")
               print("\033[32m")
               os.system("git clone https://github.com/gophish/gophish.git")
               print("")
               print("")
               print("")
               print("\033[31m")
               print("This script was not automatacally run")
               print("To run this script commands given below")
               print("commands:")
               print("")
               print("""cd gophish
go build
go run gophish.go""")

    elif choice == "5":
               os.system("clear")
               os.system("wget https://raw.githubusercontent.com/Raikia/FiercePhish/master/install.sh")
               os.system("chmod +x install.sh")
               os.system("bash install.sh")

    elif choice == "6":
               os.system("clear")
               os.system("apt install git wget php unzip curl -y")
               os.system("pkg install git wget php unzip curl -y")
               os.system("git clone https://github.com/AbirHasan2005/ShellPhish.git")
               os.system("bash ShellPhish/shellphish.sh")

#Create a URLHIDING tools page
def page_2():
    banner()
    print("____________________________________________________")
    print("| ------------- TOOL NAME : URLHIDING TOOLS ------- |")
    print("| ----------------- AUTHOR : NAVE-HACK ------------ |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"URLHIDING TOOLS:",b+"                             |")
    print(b+"|",g+"1.",r+"Facad1ng",y+"      (python)",b+"                   |")
    print(b+"|",g+"2.",r+"URLhider",y+"      (python)",b+"                   |")
    print(b+"|",g+"3.",r+"Mask-url",y+"      (python)",b+"                   |")
    print(b+"|",g+"4.",r+"Maskphish",y+"     (shell)",b+"                    |")
    print(b+"•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == '1':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/spyboy-productions/Facad1ng.git")
          os.system("pip3 install -r Facad1ng/requirements.txt")
          os.system("python3 Facad1ng/facad1ng.py")

    elif choice == '2':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/IHA089/URLHider.git")
          os.system("pip3 install -r URLHider/requirements.txt")
          os.system("python3 URLHider/URLHider.py")

    elif choice == '3':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/mishakorzik/mask-url.git")
          os.system("pip3 install requests")
          os.system("python3 mask-url/mask.py")

    elif choice == '4':
          os.system("clear")
          os.system("pkg install git -y")
          os.system("apt install git -y ")
          os.system("git clone https://github.com/rsdraju99/maskphish.git")
          os.system("bash maskphish/maskphish.sh")

    else:
          os.system("python3 nave-tools.py")
if __name__ == "__main__":
    main()

