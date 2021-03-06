import os
import configparser
import tkinter as tk
from tkinter.ttk import *

# Sprawdzanie systemu operacyjnego (linux)
if os.name == 'posix':
    print('NAZWA SYSTEMU: POSIX')
    # Ustawianie lokalizacji 'home' (np. /home/akane)
    home = (os.path.expanduser('~'))
    # Sprawdzanie czy istnieje folder dla pliku konfiguracyjnego
    if not os.path.exists(home + '/.config/AkaneRPC'):
        print('BRAK FOLDERU KONFIGURACJI! (~/.config/AkaneRPC)')
        print('TWORZENIE FOLDERU ~/.config/AkaneRPC')
        os.makedirs(home + '/.config/AkaneRPC')
    # Sprawdzanie czy plik konfiguracyjny istnieje
    if not os.path.exists(home + '/.config/AkaneRPC/config.txt'):
        print('PLIK KONFIGURACYJNY NIE ISTNIEJE!')
        lines = ['[RPC]\nClientID=000000000000000000\nDetails=none\nState=none\nLargeImageKey=none\nSmallImageKey=none\nLargeImageText=none\nSmallImageText=none\nshowCPU=False\nshowRAM=False']
        with open(home + '/.config/AkaneRPC/config.txt', 'w') as configFile:
            print('TWORZENIE PLIKU KONFIGURACYJNEGO')
            configFile.writelines(lines)
            configFile.close()
    # Inicjowanie parsera
    parser = configparser.ConfigParser()
    parser.read(home + '/.config/AkaneRPC/config.txt')

# Sprawdzanie systemu operacyjnego (windows)
elif os.name == 'nt':
    print('NAZWA SYSTEMU: NT')
    # Ustawianie lokalizacji 'home' (C:\AkaneRPC)
    home = "C:\AkaneRPC"
    # Sprawdzanie czy folder konfiguracji istnieje
    if not os.path.exists(home):
        print("Brak folderu konfiguracji! (C:\AkaneRPC)")
        print("Tworzenie folderu konfiguracji...")
        os.mkdir(home)
    # Sprawdzanie czy plik konfiguracji istnieje
    if not os.path.exists(home + "\config.txt"):
        print("Brak pliku konfiguracyjnego! (C:\AkaneRPC\config.txt)")
        print("Tworzenie pliku konfiguracyjnego...")
        lines = ['[RPC]\nClientID=000000000000000000\nDetails=none\nState=none\nLargeImageKey=none\nSmallImageKey=none\nLargeImageText=none\nSmallImageText=none\nshowCPU=False\nshowRAM=False']
        with open(home + "\config.txt", "w") as configFile:
            configFile.writelines(lines)
            configFile.close()
    # Inicjowanie parsera
    parser = configparser.ConfigParser()
    parser.read(home + "\config.txt")

# Zbieranie informacji z pliku konfiguracyjnego
# ClientID
clientinfo = parser.get('RPC', 'ClientID')
# Detale
details = parser.get('RPC', 'Details')
# Stan
state = parser.get('RPC', 'State')
# Klucz du??ego zdj??cia
try:
    largeimg = parser.get('RPC', 'LargeImageKey')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nLargeImageKey=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    largeimg = 'none'
# Klucz ma??ego zdj??cia
try:
    smallimg = parser.get('RPC', 'SmallImageKey')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nSmallImageKey=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    smallimg = 'none'
# Tekst du??ego zdj??cia
try:
    limgtext = parser.get('RPC', 'LargeImageText')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nLargeImageText=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    limgtext = 'none'
# Tekst ma??ego zdj??cia
try:
    simgtext = parser.get('RPC', 'SmallImageText')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nSmallImageText=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    simgtext = 'none'
# Pokazywanie procentu procesora
try:
    showCPU = parser.get('RPC', 'showCPU')
except configparser.NoOptionError:
    if os.name == 'nt':
        lines = ['\nshowCPU=False']
        with open(home + '\config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    showCPU = 'False'
try:
    showElapsed = parser.get('RPC', 'showElapsed')
except configparser.NoOptionError:
    if os.name == 'nt':
        lines = ['\nshowElapsed=False']
        with open(home + '\config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    showElapsed = 'False'
# Pokazywanie procentu ramu
try:
    showRAM = parser.get('RPC', 'showRAM')
except configparser.NoOptionError:
    if os.name == 'nt':
        lines = ['\nshowRAM=False']
        with open(home + '\config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    showRAM = 'False'

# Funkcja zapisuj??ca
def save():
    print('ZAPISYWANIE ZMIAN')
    # ClientID
    clientinfo = clientid.get()
    # Detale
    details = det.get()
    # Stan
    state = sta.get()
    # Klucz du??ego zdj??cia
    largeimg = lim.get()
    # Klucz ma??ego zdj??cia
    smallimg = sim.get()
    # Tekst du??ego zdi??cia
    limgtext = lit.get()
    # Tekst ma??ego zdj??cia
    simgtext = sit.get()
    # Poka?? procent procesora
    showCPUt2 = f'{showCPUt.get()}'
    # Poka?? procent RAMu
    showRAMt2 = f'{showRAMt.get()}'
    showElapsedt2 = f'{showElapsedt.get()}'
    # Przygotuj informacje do zapisu
    lines = ['[RPC]\nClientID='+clientinfo+'\nDetails='+details+'\nState='+state+'\nLargeImageKey='+largeimg+'\nSmallImageKey='+smallimg+'\nLargeImageText='+limgtext+'\nSmallImageText='+simgtext+'\nshowCPU='+showCPUt2+'\nshowRAM='+showRAMt2+'\nshowElapsed='+showElapsedt2]
    # Sprawdzanie systemu operacyjnego (linux)
    if os.name == 'posix':
        # Zapisz
        with open(home + '/.config/AkaneRPC/config.txt', 'w') as configFile:
            configFile.writelines(lines)
            configFile.close()
    # Sptawdzanie systemu operacyjego (windows)
    if os.name == 'nt':
        # Zapisz
        with open(home + '\config.txt', 'w') as configFile:
            configFile.writelines(lines)
            configFile.close()

# Tworzenie g????wnego okna
main = tk.Tk()

# Ustawianie tytu??u i rozmiar??w
main.geometry("330x420")
main.title("Konfigurator AkaneRPC")

# Rozdzielacz
lab = Label(main, text='')
lab.pack()
# ClientID
lab = Label(main, text='Identyfikator Klienta')
lab.pack()
clientid = Entry(main)
clientid.pack()
clientid.insert('end', clientinfo)
# Detale
lab = Label(main, text='Detale (Pierwsza linia)')
lab.pack()
det = Entry(main)
det.pack()
det.insert('end', details)
# Stan
lab = Label(main, text='Stan (Druga linia)')
lab.pack()
sta = Entry(main)
sta.pack()
sta.insert('end', state)
# Klucz du??ego zdj??cia
lab = Label(main, text='Klucz du??ego zdj??cia')
lab.pack()
lim = Entry(main)
lim.pack()
lim.insert('end', largeimg)
# Klucz ma??ego zdj??cia
lab = Label(main, text='Klucz ma??ego zdj??cia')
lab.pack()
sim = Entry(main)
sim.pack()
sim.insert('end', smallimg)
# Tekst du??ego zdj??cia
lab = Label(main, text='Tekst du??ego zdj??cia')
lab.pack()
lit = Entry(main)
lit.pack()
lit.insert('end', limgtext)
# Tekst ma??ego zdj??cia
lab = Label(main, text='Tekst ma??ego zdj??cia')
lab.pack()
sit = Entry(main)
sit.pack()
sit.insert('end', simgtext)
# Poka?? procent procesora
showCPUt = tk.StringVar(value=showCPU)
cpucheck = Checkbutton(main, text='Poka?? procent procesora', variable=showCPUt, onvalue='True', offvalue='False')
cpucheck.pack()
# Poka?? procent RAMu
showRAMt = tk.StringVar(value=showRAM)
ramcheck = Checkbutton(main, text='Poka?? procent RAMu', variable=showRAMt, onvalue='True', offvalue='False')
ramcheck.pack()
showElapsedt = tk.StringVar(value=showElapsed)
elapsedcheck = Checkbutton(main, text='Poka?? czas sp??dzony od uruchomienia discorda', variable=showElapsedt, onvalue='True', offvalue='False')
elapsedcheck.pack()
# Rozdzielacz
lab = Label(main, text='')
lab.pack()
# Przycisk zapisuj??cy dane
but = Button(main, text='Zapisz zmiany', command=save)
but.pack()

main.mainloop()