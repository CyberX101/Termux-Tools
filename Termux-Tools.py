#@CyberTrojan
#@O7ZXZ
#@LearnTermux0
#python modules 
import time , os , datetime , pyfiglet
##############
#color 
red = '\033[31m'
green = '\033[32m'
#Termux-Helper
def Termux_Helper():
    os.system('clear')
    now = datetime.datetime.now()
    #Logo
    Linux = pyfiglet.figlet_format("Termux")
    print(red + Linux)
    print(f'''
          {red}Termux-helper-Tool
    {red}Telegram : {green}@CyberSpyWare
    {red}Programmer : {green}@CyberTrojan 
    {red}GitHub : {green}CyberX101

      ({now})
    ''')
    time.sleep(1)
    print(f'''
    {green}1 - install Metasploit 
    {red}2 - install Nmap 
    {green}3 - install Hydra
    {red}4 - install Sqlmap 
    {green}5 - install Red_Hawk
    {red}6 - install IPGeoLocation 
    {green}7 - install Cupp
    {red}8 - install Routresploit 
    {green}9 - install Kali Nethunter 
    {green}10 - install Hammer 
    {red}11 - install Slowloris
    {green}12 - install MHDDoS
    {red}13 - install CyX-Scanner-Sql
    {green}14 - install CyX-Scanner-Xss
    {red}15 - Instagram Bruteforcer 
    {green}16 - install Ubuntu
    {red}17 - install Osintgram
    {green}18 - install CyX-Uploader 
    {red}19 - install Zphisher
    {green}20 - install Admin-Panel-Finder
    {red}21 - install Facebook-Brute-force-Tool
    {green}22 - install TM-Scanner 
    {red}23 - install wifi-Scanner-Tool
    {green}24 - install sherlock 
    {red}25 - install DarkScrape
    {green}00 - Exit  
    ''')
Cyber = True 
while Cyber:
    Termux_Helper()
    Termux = input(f'{green}[#] {red}Select Number : ')
    if Termux == '1':
        time.sleep(1)
        print(f'{green}[+] {red}Installing MetaSploit ...')
        time.sleep(2)
        os.system('pkg install -y wget')
        os.system('cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh')
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Metaslpoit Installed Successfully")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '2':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Nmap ...')
        time.sleep(2)
        os.system('cd /data/data/com.termux/files/home')
        os.system('pkg update -y ')
        os.system('pkg install -y nmap')
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Nmap installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back To Menu (y/n) : ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '3':
        time.sleep(1)
        print(f"{green}[+] {red}Installing Hydra ...")
        time.sleep(2)
        os.system('cd /data/data/com.termux/files/home')
        os.system('pkg update -y ')
        os.system('pkg install -y hydra')
        os.system('cd /data/data/com.termux/files/home')
        print(f"{red}-"*60)
        print(f"{green}[+] {red}hydra installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '4':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Sqlmap ....')
        time.sleep(2)
        os.system('cd /data/data/com.termux/files/home')
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install python2')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}Sqlmap installed successfully ')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu ? (y/n) : ')
        if menu == 'y':
            Termux_Helper()
        else:
            break 
    elif Termux == '5':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Red_Hawk ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install -y php')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}Red_Hawk installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu ? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '6':
        time.sleep(1)
        print(f'{green}[+] {red}Installing IPGeoLocation ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install -y python')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git')
        os.system('cd /data/data/com.termux/files/home && cd IPGeoLocation')
        os.system('pip install -r requirements.txt')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}IPGeoLocation installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '7':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Cupp ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install -y python')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}Cupp installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '8':
        time.sleep(1)
        print(f'{green}[+] {red}Installing RouterSploit ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install -y python2')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git')
        os.system('cd /data/data/com.termux/files/home && cd routersploit')
        os.system('pip install -r requirements.txt')
        os.system('pip install -r requirements-dev.txt')
        os.system('pip install -r requests')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}routersploit installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '9':
        time.sleep(1)
        print(f'{green}[+] {red}Installing KaliNethunter ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git')
        os.system('cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}Nethunter installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '10':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Hammer ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git ')
        os.system('pkg install -y python3')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/cyweb/hammer')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}Hammerinstalled successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '11':
        time.sleep(1)
        print(f'{green}[+] {red}Installing SlowLoris ....')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git ')
        os.system('pkg install -y python3')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/gkbrk/slowloris')
        os.system('"cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}SlowLoris installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '12':
        time.sleep(1)
        print(f'{green}[+] {red}Installing MHDDoS ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install -y python3')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/MatrixTM/MHDDoS')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}MHDDoS installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '13':
        time.sleep(1)
        print(f'{green}[+] {red}Installing CyX-Scanner-Sql ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install -y python3')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/CyberX101/CyX-Scanner-Sql')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}CyX-Scanner-Sql installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '14':
        time.sleep(1)
        print(f'{green}[+] {red}Installing CyX-Scanner-Xss ...')
        time.sleep(2)
        os.system('pkg update -y')
        os.system('pkg install -y git')
        os.system('pkg install -y python3')
        os.system('cd /data/data/com.termux/files/home && git clone https://github.com/CyberX101/CyX-Scanner-Xss')
        os.system('cd /data/data/com.termux/files/home')
        print(f'{red}-'*60)
        print(f'{green}[+] {red}CyX-Scanner-Xss installed successfully ')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '15':
        time.sleep(1)
        print(f'{green}[+] {red}Installing InstaHack ...')
        time.sleep(2)
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print(f'{red}-'*60)
        print(f'{green}[+] {red}InstaHack installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back To menu? (y/n): ')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '16':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Ubuntu ...')
        time.sleep(2)
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print(f'{red}-'*60)
        print(f'{green}[+] {red}Ubuntu installed successfully ')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}back to Menu? (y/n): ')
        if menu == "y":
            Termux_Helper()
        else:
            break
    elif Termux == '17':
        time.sleep(1)
        print(f'{green}[+] {red}Installing osintgram ...')
        time.sleep(2)
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print(f'{red}-'*60)
        print(f'{green}[+] {red}osintgram installed successfully')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n): ')
        if menu == "y":
            Termux_Helper()
        else:
            break
    elif Termux  == "18":
        time.sleep(1)
        print(f'{green}[+] {red}Installing CyX-Uploader ...')
        time.sleep(2)
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/CyberX101/CyX-Uploader")
        os.system("cd /data/data/com.termux/files/home")
        print(f'{red}-'*60)
        print(f'{green}[+] {red}CyX-Uploader installed successfully ')
        print(f'{red}-'*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n): ')
        if menu == "y":
            Termux_Helper()
        else:
            break
    elif Termux == '19':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Zphisher ...')
        time.sleep(2)
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/htr-tech/zphisher")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Zphisher installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n): ')
        if menu == "y":
            Termux_Helper()
        else:
            break
    elif Termux == '20':
        time.sleep(1)
        print(f'{green}[+] {red}Inatalling Admin-Panel-Finder ...')
        time.sleep(2)
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/C4ssif3r/admin-panel-finder")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Admin-Panel-Finder installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n):')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '21':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Facebook-Brute-force-Tool ...')
        time.sleep(2)
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/IAmBlackHacker/Facebook-BruteForce")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Facebook-Brute-Force installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n):')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '22':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Tm-Scanner ...')
        time.sleep(2)
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/TechnicalMujeeb/TM-scanner")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Tm-Scanner installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n):')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '23':
        time.sleep(1)
        print(f'{green}[+] {red}Installing Wifi-Scanner-Tool ...')
        time.sleep(2)
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/s3bap3/Wifi-scanner")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Wifi-Scanner-Tool installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n):')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '24':
        print(f'{green}[+] {red}Installing Sherlock ...')
        time.sleep(2)
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sherlock-project/sherlock")
        os.system("cd /data/data/com.termux/files/home && cd sherlock")
        os.system("pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}Sherlock installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n):')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '25':
        print(f'{green}[+] {red}Installing DarkScrape ....')
        time.sleep(2)
        os.system("pkg install -y git")
        os.system("pkg install -y python3")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/itsmehacker/DarkScrape")
        os.system("cd /data/data/com.termux/files/home && cd DarkScrape")
        os.system("pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[+] {red}DarkScrape installed successfully ")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back to Menu? (y/n):')
        if menu == 'y':
            Termux_Helper()
        else:
            break
    elif Termux == '00':
        break



