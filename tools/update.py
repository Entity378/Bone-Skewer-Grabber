import os
from time import sleep
from zipfile import ZipFile

import requests

VERSION = '1.0.2'

def check_update():
    code = requests.get('https://raw.githubusercontent.com/Entity378/Bone-Skewer-Grabber/main/tools/update.py').text
    if "VERSION = '1.0.2'" in code:
        print('This version is up to date!')
        print('Exiting...')
        sleep(2)
        exit()
    else:
        print('''
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                  Your version of Bone Skewer Grabber is outdated!''')
        choice = input('\nWould you like to update? (y/n): ')
        if choice.lower() == 'y':
            new_version_source = requests.get('https://github.com/Entity378/Bone-Skewer-Grabber/archive/refs/heads/main.zip')
            with open("Bone-Skewer-Grabber-main.zip", 'wb')as zipfile:
                zipfile.write(new_version_source.content)
            with ZipFile("Bone-Skewer-Grabber-main.zip", 'r') as filezip:
                filezip.extractall(path=os.path.join(os.path.expanduser("~"), "Desktop"))
            os.remove("Bone-Skewer-Grabber-main.zip")
            print('The new version is now on your desktop.\nUpdate Complete!')
            print("Exiting...")
            sleep(5)
        if choice.lower() == 'n':
            print('Exiting...')
            sleep(2)
            exit()


if __name__ == '__main__':
    check_update()
