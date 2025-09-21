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
def display_choice():
    banner()
    print("____________________________________________________")
    print("| ------------- TOOL NAME : NAVE-TOOLS ------------ |")
    print("| --------------- AUTHOR : NAVE-HACK -------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"CHOICES:",b+"                                     |")
    print(b+"|",g+"1.",r+"Social media phishing tools", y+"(10)",b+"          |")
    print(b+"|",g+"2.",r+"URL hider tools",y+"            (4)",b+"           |")
    print(b+"|",g+"3.",r+"Password generator tools",y+"   (5)",b+"           |")
    print(b+"|",g+"4.",r+"Phone number osint tools",y+"   (4)",b+"           |")
    print(b+"|",g+"5.",r+"Ip changer tools",y+"           (5)",b+"           |")
    print(b+"|",g+"6.",r+"Instagram tools",y+"            (3)",b+"           |")
    print(b+"|",g+"nave.",r+"To exit",b+"                                |")
    print(b+"•••••••••••••••••••••••••••••••••••••••••••••••••")

# Get users choice
def get_user_choice():
    return input("Enter choice : ")

# start the script
def main():
        display_choice()
        choice = get_user_choice()

        if choice == '1':
          page_1()

        elif choice == '2':
          page_2()

        elif choice == '3':
          page_3()

        elif choice == '4':
          page_4()

        elif choice == "5":
         page_5()

        elif choice == "6":
         page_6()

        elif choice == "nave":
          os.system("exit")

        else:
          main()

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
    print(b+"|",g+"7.",r+"LORDPHISH",y+"      (shell)",b+"                   |")
    print(b+"|",g+"8.",r+"DARKPHISH",y+"      (python)",b+"                  |")
    print(b+"|",g+"9.",r+"T-PHISH",y+"        (shell)",b+"                   |")
    print(b+"|",g+"10.",r+"RAVANA",y+"        (shell)",b+"                   |")
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
               os.chdir("zphisher")
               os.system(" bash zphisher.sh ")

    elif choice == "2":
               os.system("clear")
               os.system("pkg install git python3 php openssh -y")
               os.system("sudo apt install git python3 php openssh-client -y")
               os.system("git clone https://github.com/KasRoudra2/MaxPhisher")
               os.system("pip3 install -r MaxPhisher/files/requirements.txt")
               os.system("pip3 install maxphisher")
               os.system("sudo pip3 install maxphisher")
               os.system("clear")
               os.chdir("MaxPhisher")
               os.system("python3 maxphisher.py")

    elif choice == "3":
               os.system("clear")
               os.system("pkg install git -y")
               os.system("sudo apt install git -y")
               os.system("git clone https://github.com/Ignitetch/AdvPhishing.git")
               os.chdir("AdvPhishing")
               os.system("bash Android-Setup.sh")
               os.system("bash Linux-Setup.sh")
               os.system("bash AdvPhishing.sh")

    elif choice == "4":
               os.system("clear")
               os.system("pkg install git golang -y")
               os.system("apt install sudo -y")
               os.system("sudo apt install git golang-go -y")
               print("\033[32m")
               os.system("git clone https://github.com/gophish/gophish.git")
               os.chdir("gophish")
               os.system("go build")
               os.system("go run gophish.go")

    elif choice == "5":
               os.system("clear")
               os.system("wget https://raw.githubusercontent.com/Raikia/FiercePhish/master/install.sh")
               os.system("chmod +x install.sh")
               os.system("clear")
               os.system("bash install.sh")

    elif choice == "6":
               os.system("clear")
               os.system("apt install git wget php unzip curl -y")
               os.system("pkg install git wget php unzip curl -y")
               os.system("git clone https://github.com/AbirHasan2005/ShellPhish.git")
               os.system("clear")
               os.chdir("ShellPhish")
               os.system("bash shellphish.sh")

    elif choice == "7":
               os.system("clear")
               os.system("sudo apt install git php openssh wget -y")
               os.system("pkg install git php openssh wget -y")
               os.system("git clone https://github.com/therealelyayo/LordPhish-1.git")
               os.chdir("LordPhish-1")
               os.system("bash lord.sh")

    elif choice == "8":
               os.system("clear")
               os.system("sudo apt install python3 curl php git openssh nodejs npm python3-tk -y")
               os.system("pkg  install python3 curl php git openssh nodejs npm python3-tk -y")
               os.system("pip3 install requests wget pyshorteners")
               os.system("git clone https://github.com/Cyber-Anonymous/Dark-Phish.git")
               os.chdir("Dark-Phish")
               os.system("python3 dark-phish.py")

    elif choice == "9":
               os.system("clear")
               os.system("sudo apt install git unzip -y")
               os.system("pkg install git unzip -y")
               os.system("git clone https://github.com/Stefin-Franklin/T-Phish.git")
               os.chdir("T-Phish")
               os.system("unzip T-Phish.zip")
               os.chdir("T-Phish")
               os.system("bash start.sh")
               os.system("bash phish.sh")

    elif choice == "10":
               os.system("clear")
               os.system("sudo apt install git -y ")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/princekrvert/Ravana.git")
               os.chdir("Ravana")
               os.system("bash ravana.sh")

    else:
          main()


# Create a URLHIDING tools page
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
          os.chdir("Facad1ng")
          os.system("pip3 install -r requirements.txt")
          os.system("clear")
          os.system("python3 facad1ng.py")

    elif choice == '2':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/IHA089/URLHider.git")
          os.chdir("URLHider")
          os.system("pip3 install -r requirements.txt")
          os.system("clear")
          os.system("python3 URLHider.py")

    elif choice == '3':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/mishakorzik/mask-url.git")
          os.system("pip3 install requests")
          os.system("clear")
          os.chdir("mask-url")
          os.system("python3 mask.py")

    elif choice == '4':
          os.system("clear")
          os.system("pkg install git -y")
          os.system("apt install git -y ")
          os.system("git clone https://github.com/rsdraju99/maskphish.git")
          os.system("clear")
          os.chdir("maskphish")
          os.system("bash maskphish.sh")

    else:
          main()

# Create a password generator tools page
def page_3():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : PASSWORD GENERATOR  TOOLS ---- |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"PASSWORD GENERATOR  TOOLS:",b+"                   |")
    print(b+"|",g+"1.",r+"Crunch",y+"                      (c)",b+"          |")
    print(b+"|",g+"2.",r+"Cupp",y+"                        (python)",b+"     |")
    print(b+"|",g+"3.",r+"W-list-gen",y+"                  (python)",b+"     |")
    print(b+"|",g+"4.",r+"Pydictor",y+"                    (python)",b+"     |")
    print(b+"|",g+"5.",r+"Psudohash",y+"                   (python)",b+"     |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == '1':
          os.system("clear")
          banner()
          print("")
          print(g)
          min = input("ENTER THE PASSWORD LENTH (min) : ")
          max = input("ENTER THE PASSWORD LENTH (max) : ")
          pas = input("ENTER THE PASSKEYWORD TO GENERATE PASSWORD : ")
          file = input("ENTER THE FILE NAME TO SAVE GENERATED PASSWORD : ")
          os.system(f"crunch {min} {max} {pas} > {file}")
          print("")
          print("")
          print(r+"YOUR PASSWORD WAS SAVED IN ",g+file)

    elif choice == '2':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/Mebus/cupp.git")
          os.system("clear")
          print("\033[31m")
          os.chdir("cupp")
          os.system("python3 cupp.py -i")

    elif choice == "3":
               os.system("clear")
               os.system("sudo apt install git -y")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/IHA089/W-list-gen.git")
               os.chdir("W-list-gen")
               os.system("python3 wlistgen.py")

    elif choice == "4":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/LandGrey/pydictor.git")
               os.chdir("pydictor")
               os.system("python3 pydictor.py")

    elif choice == "5":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/t3l3machus/psudohash.git")
               os.system("pip3 install tqdm")
               os.chdir("psudohash")
               os.system("python3 psudohash.py")

    else:
          main()

# Create a phone number osint tools page
def page_4():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : PHONE NUMBER OSINT TOOLS ----- |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"PHONE NUMBER OSINT TOOLS",b+"                     |")
    print(b+"|",g+"1.",r+"Truecallerjs",y+"      (java)",b+"                 |")
    print(b+"|",g+"2.",r+"Phoneinfoga",y+"       (python)",b+"               |")
    print(b+"|",g+"3.",r+"Owl-sint",y+"          (python)",b+"               |")
    print(b+"|",g+"4.",r+"Th3inspector",y+"      (perl)",b+"                 |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
               os.system("clear")
               os.system("sudo apt install git nodejs -y")
               os.system("pkg install git nodejs -y")
               os.system("npm install truecallerjs")
               os.system("npm install -g truecallerjs")
               os.system("git clone https://github.com/sumithemmadi/truecallerjs.git")
               os.chdir("truecallerjs")
               os.system("truecallerjs login")
               print(g)
               print("Use this tool must you be login with your phone number")
               print("You forget login run this command:")
               print("truecallerjs login ")
               print("truecallerjs -s [number]: Use this command to search for a phone number and retrieve the caller name and related information.")

    elif choice == "2":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/la-deep-web/Phoneinfoga.git")
               os.chdir("Phoneinfoga")
               os.system("pip3 install -r requirements.txt")
               os.system("python3 phoneinfoga.py -h ")

    elif choice == "3":
               os.system("clear")
               os.system("sudo apt install git python2 python3 -y")
               os.system("pkg install git python2 python3 -y")
               os.system("git clone https://github.com/IccTeam/Owl-sint.git")
               os.chdir("Owl-sint")
               os.system("bash module.sh")
               os.system("python3 owlsint.py")

    elif choice == "4":
               os.system("clear")
               os.system("sudo apt install git perl -y")
               os.system("pkg install git perl -y")
               os.system("git clone https://github.com/Moham3dRiahi/Th3inspector.git")
               os.chdir("Th3inspector")
               os.system("bash install.sh")
               os.system("perl Th3inspector.pl")

    else:
          main()

# Create a ip changer tools page
def page_5():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : IP CHANGER TOOLS ------------- |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"IP CHANGER TOOLS ",b+"                             |")
    print(b+"|",g+"1.",r+"Tor ip changer",y+"         (python)",b+"           |")
    print(b+"|",g+"2.",r+"Gr33n37-ip-changer",y+"     (shell)",b+"            |")
    print(b+"|",g+"3.",r+"Auto_Tor_IP_changer",y+"    (python)",b+"           |")
    print(b+"|",g+"4.",r+"PyTor-IP-Changer",y+"       (python)",b+"           |")
    print(b+"|",g+"5.",r+"Ip-changer",y+"             (shell)",b+"            |")
    print("••••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg  install git python3 -y")
               os.system("git clone https://github.com/isPique/Tor-IP-Changer.git")
               os.chdir("Tor-IP-Changer")
               os.system("pip3  install -r requiremkents.txt")
               os.system("python3 IP-Changer.py")

    elif choice == "2":
               os.system("clear")
               os.system("sudo apt install git -y")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/gr33n37/gr33n37-ip-changer.git")
               os.chdir("gr33n37-ip-changer")
               os.system("bash ip-changer.sh")

    elif choice == "3":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/FDX100/Auto_Tor_IP_changer.git")
               os.chdir("Auto_Tor_IP_changer")
               os.system("python3 install.py")
               os.system("python3 autoTOR.py")

    elif choice == "4":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/G0ldenRat10/PyTor-IP-Changer.git")
               os.chdir("PyTor-IP-Changer")
               os.system("pip3 install -r requirements.txt")
               os.system("python3 pytor.py")

    elif choice == "5":
               ip_changer()

    else:
          main()

# Create a instagram tools page 
def page_6():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : INSTAGRAM  TOOLS ------------- |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________")
    print(b+"|",g+"Instagram tools:",b+"                     |")
    print(b+"|",g+"1.",r+"Osint tools",y+"       (4)",b+"            |")
    print(b+"|",g+"2.",r+"Passwordcracking",y+"  (1)",b+"            |")
    print(b+"|",g+"3.",r+"Mass report",y+"       (1)",b+"            |")
    print("•••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
         insta_osint()

    elif choice == "2":
         password_cracking()

    elif choice == "3":
         insta_mass_report()

    else:
          main()

def ip_changer():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : IP-CHANGER ----- ------------- |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________")
    print(b+"|",g+"IP-CHANGER:",b+"                     |")
    print(b+"|",g+"1.",r+"INSTALL TOOL",y+"        ",b+"            |")
    print(b+"|",g+"2.",r+"RUN TOOL",y+"   ",b+"            |")
    print("•••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
         os.system("clear")
         os.system("sudo apt install curl -y")
         os.system("pkg install curl -y")
         os.system("curl -sL https://github.com/Anon4You/Ip-Changer/raw/main/installer.sh | bash")
         print("Tool installed")
         time.sleep(3)
         ip_changer()

    elif choice == "2":
         os.system("clear")
         sec = input("ENTER HOW MANY SECONDS TO CHANGE IP (min:5): ")
         banner()
         os.system(f"ip-changer -r {sec}")

    else:
          main()

# Create a osint tools page
def insta_osint():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : OSINT TOOLS ------------------ |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_____________________________________________")
    print(b+"|",g+"Osint tools:",b+"                              |")
    print(b+"|",g+"1.",r+"Ig-osint-v2",y+"                (python)",b+"   |")
    print(b+"|",g+"2.",r+"Ig-osint-tomxploit",y+"         (python)",b+"   |")
    print(b+"|",g+"3.",r+"Owl-sint",y+"                   (python)",b+"   |")
    print("••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
       os.system("clear")
       os.system("sudo apt install git python3 -y")
       os.system("pkg install git python3 -y")
       os.system("git clone https://github.com/Achik-Ahmed/IG-OSINT-V2.git")
       os.chdir("IG-OSINT-V2")
       os.system("pip3 install instaloader")
       os.system("python3 ig.py")

    elif choice == "2":
       os.system("clear")
       os.system("sudo apt install git python3 -y")
       os.system("pkg install git python3 -y")
       os.system("git clone https://github.com/t0mxplo1t/IG-OSINT.git")
       os.chdir("IG-OSINT")
       os.system("pip3 install instaloader")
       os.system("python3 ig.py")

    elif choice == "3":
       os.system("clear")
       os.system("sudo apt install git python2 python3 -y")
       os.system("pkg install git python2 python3 -y")
       os.system("git clone https://github.com/IccTeam/Owl-sint.git")
       os.chdir("Owl-sint")
       os.system("bash module.sh")
       os.system("python3 owlsint.py")

    else:
          main()

# Create a password cracking tools page
def password_cracking():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : PASSWORD CRACKING TOOLS ------ |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"Password cracking  tools:",b+"           |")
    print(b+"|",g+"1.",r+"Instainsane",y+"           (shell)",b+"   |")
    """print(b+"|",g+"2.",r+"",y+"        ()",b+"        |")"""
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
        os.system("clear")
        os.system("sudo apt install git curl tor openssl -y")
        os.system("pkg install git curl tor openssl -y")
        os.system("git clone https://github.com/umeshshinde19/instainsane.git")
        os.chdir("instainsane")
        os.system("chmod +x install.sh")
        os.system("bash install.sh")
        os.system("bash instainsane.sh")

    else:
          main()

def insta_mass_report():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : INSTA MASS REPORT TOOLS ------ |")
    print("| -------------- AUTHOR : NAVE-HACK --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"Insta mass report tools:",b+"            |")
    print(b+"|",g+"1.",r+"SMH",y+"              (python)",b+"       |") 
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
        os.system("clear")
        os.system("sudo apt install git python3 python3-pip -y")
        os.system("pkg install git python3 ")
        os.system("git clone https://github.com/rdWei/SocialMediaHackingToolkit.git")
        os.chdir("SocialMediaHackingToolkit")
        os.system("pip3 install -r requirements.txt")
        os.system("python3 cmd/main.py")

    else:
          main()


if __name__ == "__main__":
    main()
