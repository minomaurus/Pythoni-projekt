from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import sys
import os

# teeme faili sisu lausete listiks
fail = input("Sisestage tekstifaili nimi: ")
f = open(fail,encoding="UTF-8")
sisu = f.read()
laused = sisu.split(".")
laused.pop(-1) #võtab viimase tühja sõne välja
f.close()

#võtab igast lausest juhusliku sõna välja, asendab selle ?-ga
#tagastab sõnastiku, mille võtmed on lüngad ja elemendid lünklaused
def tee_lünktekstiks(tekst):
    lünktekst={}
    for lause in tekst:
        tekst_listina=lause.split()
        lünk=tekst_listina[randint(1,len(tekst_listina))-1]
        lünk=lünk.strip().strip(',') #eemaldab kirjavahemärgid, mis võivad lause sees olla
        lünktekst[lünk]=lause.replace(lünk,'?').strip()
    return lünktekst

def kontrolli(vastused, lüngad):
    õiged=[]
    loendur=0
    for vastus in vastused:
        vastus=vastus.get()
        if vastus==lüngad[loendur]:
            õiged.append(loendur+1)
        loendur+=1
    
    if len(õiged)==len(lüngad):
        õige()
    else:
        vale(õiged)

#loob akna, mis avaneb õigete vastuste korral ja annab mängijale valiku uuesti mängida või lahkuda
def õige():
    raam.attributes('-topmost', False)
    win = Toplevel()
    win.title(' ')
    message = "  Kõik vastused olid õiged!  "
    Label(win, text=message).pack()
    Button(win, text='Mängi uuesti', command=raam.destroy).pack()
    Button(win, text='Lahku mängust', command=lõpeta).pack() #sulgeb mängu

#loob akna, mis avaneb vähemalt ühe vale vastuse korra
#ütleb, millised vastused olid õiged ja suunab tagasi ülesande juurde
def vale(õiged):
    raam.attributes('-topmost', False)
    win = Toplevel()
    win.title(' ')
    if õiged==[]:
        message = "Kõik vastused olid valed!"
    else:
        numbrid=''
        for i in range(len(õiged)):
            numbrid+=str(õiged[i]) + "."
            if i==len(õiged)-2:
                numbrid+=" ja"
            elif i<len(õiged)-2:
                numbrid+=","
            numbrid+=" "
        message = "Vastasid õigesti " + numbrid + "küsimusele"
    Label(win, text=message).pack()
    Button(win, text='Tagasi vastama', command=win.destroy).pack()
    Button(win, text='Näita õigeid vastuseid', command=näita).pack()
def näita():
    raam.destroy()
    asendus = Tk()
    asendus.title("Ülesanne")
    asendus.attributes('-topmost', True)
    loendur=1
    for lause in laused:
        silt=ttk.Label(asendus,text=(lause.strip()+'. '))
        silt.pack(padx=5)
        loendur+=1
    alamraam=ttk.Frame(asendus)
    nupp = ttk.Button(alamraam, text="Mängi uuesti", command=asendus.destroy)
    nupp.pack(padx=5,side=LEFT)
    nupp = ttk.Button(alamraam, text="Lahku mängust", command=partial(lõpeta2,asendus))
    nupp.pack(padx=5,side=LEFT)
    alamraam.pack()
    
def lõpeta():
    global a
    a=0
    raam.destroy()
def lõpeta2(silt):
    global a
    a=0
    silt.destroy()
def lünktekst_ekraanile(raam,ülesanne):
    loendur=0
    vastused=[]
    lüngad=[]
    for lünk, lünklause in ülesanne.items():
        alamraam=ttk.Frame(raam)
        lause_osad=lünklause.split('?')
        print(lause_osad)
        silt = ttk.Label(alamraam, text=lause_osad[0])
        silt.pack(padx=5,side=LEFT)
        #silt.grid(column=0, row=loendur, padx=5, pady=5, sticky=(N, W))
        vastus = ttk.Entry(alamraam)
        vastus.pack(side=LEFT)
        #vastus.grid(column=1, row=loendur, padx=5, pady=5, sticky=(N, W))
        silt = ttk.Label(alamraam, text=(lause_osad[1]+'.'))
        silt.pack(padx=5,side=LEFT)        
        #silt.grid(column=2, row=loendur, padx=5, pady=5, sticky=(N, E))
        vastused.append(vastus)
        lüngad.append(lünk)
        loendur+=1
        alamraam.pack()
    nupp = ttk.Button(raam, text="Valmis!", command=partial(kontrolli, vastused, lüngad)) #kasutame partialit, sest nupulevajutusega funktsiooni väljakutsumiseks peab command f olema ilma argumendita
    nupp.pack(padx=5)
#genereerib uusi ülesandeid, kuni öeldakse, et lõpeta
a=1
while a:
    raam = Tk()
    raam.title("Ülesanne")
    ülesanne=tee_lünktekstiks(laused)
    lünktekst_ekraanile(raam,ülesanne)
    raam.attributes('-topmost', True)
    raam.mainloop()

