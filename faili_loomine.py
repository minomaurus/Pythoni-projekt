fail= input("Sisestage tekstifaili nimi: ")
from random import randint
f= open(fail)
sisu= f.read() #loeb sisu
lause= sisu.split(".") #teeb sisu lausete listiks
lause.pop(-1)
f.close()
def tee_lünktekstiks(tekst):
    tekst_listina=tekst.split() #teeb teksti listiks sõnadest
    lünk=tekst_listina[randint(1,len(tekst_listina))-1] #võtab juhusliku järjenumbriga sõna listist
    lünk=lünk.strip().strip(',') #eemaldab kirjavahemärgid, mis võivad lause sees olla
    lünktekst=tekst.replace(lünk,'_'*len(lünk))
    return lünktekst
l= open("lünktekst.txt", "w")
for i in lause:
    laused= str(i)
    l.write(tee_lünktekstiks(laused)+".")
l.close()