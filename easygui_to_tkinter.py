from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
fail = input("Sisestage tekstifaili nimi: ")
f = open(fail)
sisu = f.read() #loeb sisu
laused = sisu.split(".") #teeb sisu lausete listiks
laused.pop(-1) #võtab viimase tühja elemendi välja
f.close()

def tee_lünktekstiks(tekst):
    lünktekst={}
    for lause in tekst:
        tekst_listina=lause.split() #teeb teksti listiks sõnadest
        lünk=tekst_listina[randint(1,len(tekst_listina))-1] #võtab juhusliku järjenumbriga sõna listist
        lünk=lünk.strip().strip(',') #eemaldab kirjavahemärgid, mis võivad lause sees olla
        lünktekst[lünk]=lause.replace(lünk,'_'*len(lünk)) #teeb lünkteksti sõnastikuks, milles võtmed on lüngad ja vastavad elemendid on lünklaused
    return lünktekst

def kontrolli(vastused, lüngad):
    õiged=''
    loendur=0
    for vastus in vastused:
        vastus=vastus.get()
        if vastus==lüngad[loendur]:
            õiged+=str(loendur)+' '
            loendur+=1
    if len(õiged)/2==len(lüngad):
        messagebox.showinfo(message="Kõik vastused olid õiged!")
    else:
        messagebox.showinfo(message="Vastasid õigesti küsimustele "+õiged)

ülesanne=tee_lünktekstiks(laused)
raam = Tk()
raam.title("Ülesanne")
loendur=0
vastused=[]
lüngad=[]
for lünk, lünklause in ülesanne.items():
    silt = ttk.Label(raam, text=lünklause)
    silt.grid(column=0, row=loendur, padx=5, pady=5, sticky=(N, W))
    vastus = ttk.Entry(raam)
    vastus.grid(column=1, row=loendur, padx=5, pady=5, sticky=(N, W, E))
    vastused.append(vastus)
    lüngad.append(lünk)
    loendur+=1
nupp = ttk.Button(raam, text="Valmis!", command=partial(kontrolli, vastused, lüngad)) #kasutame partialit, sest nupulevajutusega funktsiooni väljakutsumiseks peab command f olema ilma argumendita
nupp.grid(column=1, row=2, padx=5, pady=5, sticky=(N, S, W, E))
#print(tee_lünktekstiks(laused))
raam.mainloop()