from random import randint
import re
def tee_lünktekstiks(tekst):
    tekst_listina=tekst.split() #teeb teksti listiks sõnadest
    lünk=tekst_listina[randint(1,len(tekst_listina))-1] #võtab juhusliku järjenumbriga sõna listist
    lünk=lünk.strip().strip(',') #eemaldab kirjavahemärgid, mis võivad lause sees olla
    lünktekst=tekst.replace(lünk,'_'*len(lünk))
    return lünktekst
tekst1 = 'Joey ei tea, mida tähendab rafineeritud'
print(tee_lünktekstiks(tekst1))