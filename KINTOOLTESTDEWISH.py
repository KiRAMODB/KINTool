import nmap
import os

sc = nmap

print(""" _   _ _ _   _ _____             _   
( ) ( )_) ) ( )_   _)           (_ ) 
| |/ /| |  \| | | |    _     _   | | 
|   ( | |     | | |  / _ \ / _ \ | | 
| |\ \| | | \ | | | ( (_) ) (_) )| | 
(_) (_)_)_) (_) (_)  \___/ \___/(___)
                                     
                                     """)


def main():
    n = input("1 - Network Scanner\n2 - Exploit\n\nPlease enter a number :")

    if n == '1':
        nmap()

    if n == '2':
        os.system('msfconsole')
    
    else :
        print("Please choose a number between 1 and 2")

def nmap():
    print("|------------------------------------------------------------|")
    print("|               Welcome To The Network Scanner               |")
    print("|------------------------------------------------------------|")
    ip = input("\nPlease Put The IP Adress Here :")
    sc.scan(ip, '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

if __name__ == '__main__':
    main()