import pypresence as rpc
import time
import configparser
import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import pypresence
import psutil

# Funkcja do bezpiecznego wyłączania programu
def exitprogram():
    os._exit(0)

# Funkcja do otwierania okna błędu, kiedy nie ma pliku konfiguracyjnego
def errwin():
    main = tk.Tk()
    main.title('BŁĄD')
    lab = Label(main, text='Brak Pliku Konfiguracyjnego!')
    lab.pack(padx=10,pady=15)
    but = Button(main, text='OK', command=exitprogram)
    but.pack()
    main.protocol("WM_DELETE_WINDOW", exitprogram)
    main.mainloop()

# Inicjowanie parsera
parser = configparser.ConfigParser()

# Sprawdzanie systemu operacyjnego (linux)
if os.name == 'posix':
    home = (os.path.expanduser('~'))
    if not os.path.exists(home + '/.config/AkaneRPC/config.txt'):
        errwin()
    parser.read(home + '/.config/AkaneRPC/config.txt')

# Sprawdzanie systemu operacyjnego (windows)
if os.name == 'nt':
    home = 'C:\AkaneRPC'
    if not os.path.exists(home + '\config.txt'):
        errwin()
    parser.read(home + '\config.txt')

# Zbieranie informacji z pliku konfiguracji
try:
    clientinfo = parser.get('RPC', 'ClientID')
    details = parser.get('RPC', 'Details')
    state = parser.get('RPC', 'State')
    largeimg = parser.get('RPC', 'LargeImageKey')
    smallimg = parser.get('RPC', 'SmallImageKey')
    limgtext = parser.get('RPC', 'LargeImageText')
    simgtext = parser.get('RPC', 'SmallImageText')
    showCPU = parser.get('RPC', 'showCPU')
    showRAM = parser.get('RPC', 'showRAM')
    showElapsed = parser.get('RPC', 'showElapsed')

# W razie gdy zbieranie informacji z pliku konfiguracji wyrzuci błąd pokazywanie okna błędu
except:
    main = tk.Tk()
    main.title('BŁĄD')
    lab = Label(main, text='Błąd pliku konfiguracyjnego!')
    lab.pack(padx=10,pady=15)
    but = Button(main, text='OK', command=exitprogram)
    but.pack()
    main.protocol("WM_DELETE_WINDOW", exitprogram)
    main.mainloop()
# Ustawianie identyfikatora klienta
rpresence = rpc.Presence(clientinfo)

# Funkcja do połączenia z discordem
def connect(start):
    try:
        start = time.time()
        rpresence.connect()
        return start
# Jeśli discord nie jest otwarty wykonujemy ponowną próbę połączenia po 15 sekundach
    except(pypresence.exceptions.InvalidPipe):
        print("INVALIDPIPEERROR")
        time.sleep(15)
        connect(start)
        return start
# Jeśli użytkownik wprowadził zły identyfikator klienta pokazujemy okno błędu
    except(pypresence.exceptions.InvalidID):
        main = tk.Tk()
        main.title('BŁĄD')
        lab = Label(main, text='Zły identyfikator klienta')
        lab.pack(padx=10,pady=15)
        but = Button(main, text='OK', command=exitprogram)
        but.pack()
        main.protocol("WM_DELETE_WINDOW", exitprogram)
        main.mainloop()

# Aktualizowanie statusu
def update(start):
    if showElapsed == 'True':
        try:
            if showCPU == 'True' and showRAM == 'True':
                cpu = str(psutil.cpu_percent(5))
                ram = str(psutil.virtual_memory()[2])
                print(rpresence.update(state=state + " " + ram + "%", details=details + " " + cpu + "%", large_image=largeimg, small_image=smallimg, large_text=limgtext, small_text=simgtext, start=int(start)))
            if showCPU == 'True' and showRAM == 'False':
                cpu = str(psutil.cpu_percent(5))
                print(rpresence.update(state=state, details=details + " " + cpu + "%", large_image=largeimg, small_image=smallimg, large_text=limgtext, small_text=simgtext, start=int(start)))
            if showCPU == 'False' and showRAM == 'True':
                ram = str(psutil.virtual_memory()[2])
                print(rpresence.update(state=state + " " + ram + "%", details=details, large_image=largeimg, small_image=smallimg, large_text=limgtext, small_text=simgtext, start=int(start)))
            if showCPU == 'False' and showRAM == 'False':
                print(rpresence.update(state=state, details=details, large_image=largeimg, small_image=smallimg, large_text=limgtext, small_text=simgtext, start=int(start)))

    # Błędy dotyczące:
        except(pypresence.exceptions.ServerError):
            # Długości detali będącej mniejszą niż 2 litery
            if details.len() < 2:
                main = tk.Tk()
                main.title('BŁĄD')
                lab = Label(main, text='Detale mają mniej niż 2 litery!')
                lab.pack(padx=10,pady=15)
                but = Button(main, text='OK', command=exitprogram)
                but.pack()
                main.protocol("WM_DELETE_WINDOW", exitprogram)
                main.mainloop()
            # Długości stanu będącej mniejszą niż 2 litery
            elif state.len() < 2:
                main = tk.Tk()
                main.title('BŁĄD')
                lab = Label(main, text='Stan ma mniej niż 2 litery!')
                lab.pack(padx=10, pady=15)
                but = Button(main, text='OK', command=exitprogram)
                but.pack()
                main.protocol("WM_DELETE_WINDOW", exitprogram)
                main.mainloop()
            # Braku internetu
            else:
                main = tk.Tk()
                main.title('BŁĄD')
                lab = Label(main, text='Błąd sieci! Sprawdź czy masz dostęp do internetu.')
                lab.pack(padx=10, pady=15)
                but = Button(main, text='OK', command=exitprogram)
                but.pack()
                main.protocol("WM_DELETE_WINDOW", exitprogram)
                main.mainloop()
    # Jeśli discord zostaje zamknięty podczas działania programu próbujemy ponownie się połączyć
        except(AssertionError):
            print('ASSERTIONERROR')
            connect(start)
    else:
        try:
            if showCPU == 'True' and showRAM == 'True':
                cpu = str(psutil.cpu_percent(5))
                ram = str(psutil.virtual_memory()[2])
                print(rpresence.update(state=state + " " + ram + "%", details=details + " " + cpu + "%",
                                       large_image=largeimg, small_image=smallimg, large_text=limgtext,
                                       small_text=simgtext))
            if showCPU == 'True' and showRAM == 'False':
                cpu = str(psutil.cpu_percent(5))
                print(rpresence.update(state=state, details=details + " " + cpu + "%", large_image=largeimg,
                                       small_image=smallimg, large_text=limgtext, small_text=simgtext))
            if showCPU == 'False' and showRAM == 'True':
                ram = str(psutil.virtual_memory()[2])
                print(rpresence.update(state=state + " " + ram + "%", details=details, large_image=largeimg,
                                       small_image=smallimg, large_text=limgtext, small_text=simgtext))
            if showCPU == 'False' and showRAM == 'False':
                print(rpresence.update(state=state, details=details, large_image=largeimg, small_image=smallimg,
                                       large_text=limgtext, small_text=simgtext))

        # Błędy dotyczące:
        except(pypresence.exceptions.ServerError):
            # Długości detali będącej mniejszą niż 2 litery
            if details.len() < 2:
                main = tk.Tk()
                main.title('BŁĄD')
                lab = Label(main, text='Detale mają mniej niż 2 litery!')
                lab.pack(padx=10, pady=15)
                but = Button(main, text='OK', command=exitprogram)
                but.pack()
                main.protocol("WM_DELETE_WINDOW", exitprogram)
                main.mainloop()
            # Długości stanu będącej mniejszą niż 2 litery
            elif state.len() < 2:
                main = tk.Tk()
                main.title('BŁĄD')
                lab = Label(main, text='Stan ma mniej niż 2 litery!')
                lab.pack(padx=10, pady=15)
                but = Button(main, text='OK', command=exitprogram)
                but.pack()
                main.protocol("WM_DELETE_WINDOW", exitprogram)
                main.mainloop()
            # Braku internetu
            else:
                main = tk.Tk()
                main.title('BŁĄD')
                lab = Label(main, text='Błąd sieci! Sprawdź czy masz dostęp do internetu.')
                lab.pack(padx=10, pady=15)
                but = Button(main, text='OK', command=exitprogram)
                but.pack()
                main.protocol("WM_DELETE_WINDOW", exitprogram)
                main.mainloop()
        # Jeśli discord zostaje zamknięty podczas działania programu próbujemy ponownie się połączyć
        except(AssertionError):
            print('ASSERTIONERROR')
            connect()


# Inicjowanie połączenia
start = time.time()
start = connect(start)

# Pętla, która umożliwia aktualizowanie statusu co 10 sekund, aktualnie trochę bezużyteczna, ale
# może się przydać do nowych funkcji.
while True:
    try:
        update(start=start)
    except(pypresence.exceptions.InvalidID):
        print('DISCORDCLOSEDERROR')
        rpresence.close()
        rpresence = rpc.Presence(clientinfo)
        start = time.time()
    time.sleep(5)