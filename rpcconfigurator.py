import os
import configparser
import tkinter as tk
from tkinter import *
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
        lines = ['[RPC]\nClientID=000000000000000000\nDetails=none\nState=none\nLargeImageKey=none\nSmallImageKey=none\nLargeImageText=none\nSmallImageText=none']
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
        lines = ['[RPC]\nClientID=000000000000000000\nDetails=none\nState=none\nLargeImageKey=none\nSmallImageKey=none\nLargeImageText=none\nSmallImageText=none']
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
# Klucz dużego zdjęcia
try:
    largeimg = parser.get('RPC', 'LargeImageKey')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nLargeImageKey=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    largeimg = 'none'
# Klucz małego zdjęcia
try:
    smallimg = parser.get('RPC', 'SmallImageKey')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nSmallImageKey=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    smallimg = 'none'
# Tekst dużego zdjęcia
try:
    limgtext = parser.get('RPC', 'LargeImageText')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nLargeImageText=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    limgtext = 'none'
# Tekst małego zdjęcia
try:
    simgtext = parser.get('RPC', 'SmallImageText')
except configparser.NoOptionError:
    if os.name == 'posix':
        lines = ['\nSmallImageText=none']
        with open(home + '/.config/AkaneRPC/config.txt', 'a') as configFile:
            configFile.writelines(lines)
            configFile.close()
    simgtext = 'none'

# Funkcja zapisująca
def save():
    print('ZAPISYWANIE ZMIAN')
    # ClientID
    clientinfo = clientid.get()
    # Detale
    details = det.get()
    # Stan
    state = sta.get()
    # Klucz dużego zdjęcia
    largeimg = lim.get()
    # Klucz małego zdjęcia
    smallimg = sim.get()
    # Tekst dużego zdięcia
    limgtext = lit.get()
    # Tekst małego zdjęcia
    simgtext = sit.get()
    lines = ['[RPC]\nClientID='+clientinfo+'\nDetails='+details+'\nState='+state+'\nLargeImageKey='+largeimg+'\nSmallImageKey='+smallimg+'\nLargeImageText='+limgtext+'\nSmallImageText='+simgtext]
    # Sprawdzanie systemu operacyjnego (linux)
    if os.name == 'posix':
        with open(home + '/.config/AkaneRPC/config.txt', 'w') as configFile:
            configFile.writelines(lines)
            configFile.close()
    # Sptawdzanie systemu operacyjego (windows)
    if os.name == 'nt':
        with open(home + '\config.txt', 'w') as configFile:
            configFile.writelines(lines)
            configFile.close()

# Tworzenie głównego okna
main = tk.Tk()

# Ustawianie tytułu i rozmiarów
main.geometry("330x365")
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
# Klucz dużego zdjęcia
lab = Label(main, text='Klucz dużego zdjęcia')
lab.pack()
lim = Entry(main)
lim.pack()
lim.insert('end', largeimg)
# Klucz małego zdjęcia
lab = Label(main, text='Klucz małego zdjęcia')
lab.pack()
sim = Entry(main)
sim.pack()
sim.insert('end', smallimg)
# Tekst dużego zdjęcia
lab = Label(main, text='Tekst dużego zdjęcia')
lab.pack()
lit = Entry(main)
lit.pack()
lit.insert('end', limgtext)
# Tekst małego zdjęcia
lab = Label(main, text='Tekst małego zdjęcia')
lab.pack()
sit = Entry(main)
sit.pack()
sit.insert('end', simgtext)
# Rozdzielacz
lab = Label(main, text='')
lab.pack()
# Przycisk zapisujący dane
but = Button(main, text='Zapisz zmiany', command=save)
but.pack()

main.mainloop()