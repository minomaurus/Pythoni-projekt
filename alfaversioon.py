from random import randint
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
from easygui import *
def kasutajaliides(tekst):
    ülesanne=tee_lünktekstiks(tekst)
    for lünk, lünklause in ülesanne.items(): 
        vastus=enterbox(msg=lünklause,title="Ülesanne",strip=True)
        if vastus==lünk:
            msgbox("Õige vastus!")
        else:
            msgbox("Vale vastus!")
    return vastus
#print(tee_lünktekstiks(laused))
kasutajaliides(laused)