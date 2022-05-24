#copy folders and files
import os
import time
from colorama import init, Fore, Back, Style

def mainmenu():
    #ascii art print
    print (Fore.GREEN + """

    
                                               
    |                               /          
 ___| ___  ___       ___  ___  ___    ___  ___ 
|   )|   )|         |    |   )|   )| |___)|   )
|__/ |__/ |__       |__  |__/ |__/ | |__  |    
                              |                


    """ + Fore.RESET)
    time.sleep(2)
    os.system("cls")
    print ("""
    1. Copy Documents folder to Desktop
    2. Exit
    """)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        time.sleep(2)
        print ("Copying...")
        time.sleep(1)
        print(Fore.CYAN + "This may take a while..." + Fore.RESET)
        time.sleep(2)
        find_user()
        copy_docs()
        time.sleep(5)
        print("Quitting...")
    if choice == 2:
        time.sleep(2)
        exit()
    if choice > 2:
        print ("Invalid choice")
        time.sleep(2)
        mainmenu()
    





#find user name of this computer
def find_user():
    user = os.getlogin()
    return user

#copy Documents folder to this folder
def copy_docs():
    user = find_user()
    path = "C:\\Users\\" + user + "\\Documents"
    #copy
    os.system("xcopy " + path + " " + "C:\\Users\\" + user + "\\Desktop\\Documents /E /H /C /I")
    #show folder size
    size = os.path.getsize("C:\\Users\\" + user + "\\Desktop\\Documents")
    print (Fore.GREEN + "The size of the folder is: " + str(size) + " bytes" + Fore.RESET)

mainmenu()