#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import sys

__version__ = '0.31'


if int(sys.version[:1]) < 3:
    def input(prompt=''):
        return raw_input(str(prompt))


def out(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()


def reline():
    sys.stdout.write('\r')
    sys.stdout.flush()


out('Checking os type...')
time.sleep(1)
reline()
sys.stdout.write(str('Checking os type... ') + os.name + '\n')
sys.stdout.flush()
time.sleep(1)
check = False

if os.name == 'posix':
    out('Checking package structure...')
    if os.path.isfile('./sumtool') or os.path.isfile('./sumtool.py'):
        if os.path.isfile('./sumtool.py'):
            os.rename('./sumtool.py', './sumtool')
        time.sleep(1)
        reline()
        out('Checking package structure... OK\n')
        time.sleep(1)
    else:
        time.sleep(1)
        reline()
        out('Checking package structure... Done\n')
        time.sleep(1)
        print("Can't find \033[4msumtool\033[0m file in current dir.\n"
              'The package is either damaged or already installed.')
        exit()

    out('Starting posix install...')
    time.sleep(1)
    reline()
    out('Starting posix install... OK\n')
    time.sleep(1)
    print('\nWhere to install?\n')
    print('1). /usr/local/bin')
    print('2). /usr/bin')
    print('3). /bin')
    print('4). Exit\n')
    x = input('Choice: ')
    if x == '1':
        time.sleep(1)
        out('Installing to /usr/local/bin/...')
        os.system('chmod +x sumtool')
        try:
            os.rename('./sumtool', '/usr/local/bin/sumtool')
            time.sleep(1)
            reline()
            out('Installing to /usr/local/bin/... OK\n')
            check = True
        except BaseException:
            time.sleep(1)
            reline()
            out('Installing to /usr/local/bin/... Error\n')
            time.sleep(1)
            x = input('Try with sudo? (Y/n)')
            if x == 'n' or x == 'N' or x == 'No' or x == 'no':
                exit()
            time.sleep(1)
            print('Retrying with sudo...')
            os.system('sudo mv ./sumtool /usr/local/bin/')
            if not os.path.isfile('/usr/local/bin/sumtool'):
                print('\n-------------------\ninstallation failed\n-------------------\n')
                exit()
    elif x == '2':
        time.sleep(1)
        out('Installing to /usr/bin/...')
        os.system('chmod +x sumtool')
        try:
            os.rename('./sumtool', '/usr/bin/sumtool')
            time.sleep(1)
            reline()
            out('Installing to /usr/bin/... OK\n')
            check = True
        except BaseException:
            time.sleep(1)
            reline()
            out('Installing to /usr/bin/... Error\n')
            time.sleep(1)
            x = input('Try with sudo? (Y/n)')
            if x == 'n' or x == 'N' or x == 'No' or x == 'no':
                exit()
            time.sleep(1)
            print('Retrying with sudo...')
            os.system('sudo mv ./sumtool /usr/bin/')
            if not os.path.isfile('/usr/bin/sumtool'):
                print('\n-------------------\ninstallation failed\n-------------------\n')
                exit()
    elif x == '3':
        time.sleep(1)
        out('Installing to /bin/...')
        os.system('chmod +x sumtool')
        try:
            os.rename('./sumtool', '/bin/sumtool')
            time.sleep(1)
            reline()
            out('Installing to /bin/... OK\n')
            check = True
        except BaseException:
            time.sleep(1)
            reline()
            out('Installing to /bin/... Error\n')
            time.sleep(1)
            x = input('Try with sudo? (Y/n)')
            if x == 'n' or x == 'N' or x == 'No' or x == 'no':
                exit()
            time.sleep(1)
            print('Retrying with sudo...')
            os.system('sudo mv ./sumtool /bin/')
            if not os.path.isfile('/bin/sumtool'):
                print('\n-------------------\ninstallation failed\n-------------------\n')
                exit()
    else:
        if x != '4':
            print('Unknown option.')
        exit()


elif os.name == 'nt':
    if not os.path.isdir('C:\Program Files\sumtool'):
        try:
            os.mkdir('C:\Program Files\sumtool')
        except:
            if not os.path.isfile('.\install.cmd'):
                buf = '@echo off\ncd /d %~dp0\npython install.py'
                f = open('install.cmd', 'w')
                f.write(buf)
                f.close()
            print('You need admin rights for installation!\nYou can try running install.cmd as admin.')
            input('\nPress <ENTER> to exit.')
            exit()
    elif os.path.isdir('C:\Program Files\sumtool'):
        try:
            os.rename('C:\Program Files\sumtool', 'C:\Program Files\sumtool')
        except:
            if not os.path.isfile('.\install.cmd'):
                buf = '@echo off\ncd /d %~dp0\npython install.py'
                f = open('install.cmd', 'w')
                f.write(buf)
                f.close()
            print('You need admin rights for installation!\nYou can try running install.cmd as admin.')
            input('\nPress <ENTER> to exit.')
            exit()
    out('Checking package structure...')
    
    if os.path.isfile('.\sumtool') or os.path.isfile('.\sumtool.py'):
        if os.path.isfile('.\sumtool.py'):
            os.rename('.\sumtool.py', '.\sumtool')
        time.sleep(1)
        reline()
        out('Checking package structure... OK\n')
        time.sleep(1)
    else:
        time.sleep(1)
        reline()
        out('Checking package structure... Done\n')
        time.sleep(1)
        print("Can't find sumtool file in current dir.\n"
              'The package is either damaged or already installed.')
        input('\nPress <ENTER> to exit.')
        exit()

    out('Starting nt install...')

    time.sleep(1)
    reline()
    out('Starting nt install... OK\n')

    out('Handling dependencies...')

    buf = '@echo off\npython "C:\Program Files\sumtool\sumtool" %*'
    f = open('sumtool.cmd', 'w')
    f.write(buf)
    f.close()

    time.sleep(1)
    reline()
    out('Handling dependencies... OK\n')

    time.sleep(1)
    out('Installing to C:\Program Files\sumtool')

    if not os.path.isdir('C:\Program Files\sumtool'):
        os.mkdir('C:\Program Files\sumtool')
    if os.path.isfile('C:\Program Files\sumtool\sumtool'):
        os.remove('C:\Program Files\sumtool\sumtool')
    if os.path.isfile('C:\Program Files\sumtool\sumtool.cmd'):
        os.remove('C:\Program Files\sumtool\sumtool.cmd')
    os.rename('.\sumtool', 'C:\Program Files\sumtool\sumtool')
    os.rename('.\sumtool.cmd', 'C:\Program Files\sumtool\sumtool.cmd')

    time.sleep(1)
    reline()
    out('Installing to C:\Program Files\sumtool... OK\n')
    check = True
    time.sleep(1)
    print('Running PATH configuration to finish setup...\n')
    time.sleep(2)
    print('Where to add?\n')
    print('1). Add to user PATH')
    print('2). Add to system Path')
    print('3). Both previous options')
    print('4). Exit\n')
    x = input('Choice: ')
    if x == '1':
        time.sleep(1)
        print('Adding to user PATH...')
        os.system('SETX PATH "%PATH%;C:\Program Files\sumtool"')
    elif x == '2':
        time.sleep(1)
        print('Adding to system Path...')
        os.system('SETX PATH /M "%PATH%;C:\Program Files\sumtool"')
    elif x == '3':
        time.sleep(1)
        out('Adding to both paths...')
        os.system('SETX PATH "%PATH%;C:\Program Files\sumtool"')
        os.system('SETX PATH /M "%PATH%;C:\Program Files\sumtool"')
    else:
        if x != '4':
            print('Unknown option.')
        exit()
    time.sleep(1)
if check:
    print('\n------------------------------\nsumtool successfully installed\n------------------------------\n')
else:
    print('\n-------------------\ninstallation failed\n-------------------\n')
time.sleep(2)
