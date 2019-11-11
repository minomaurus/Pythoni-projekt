from lünktekst import tee_lünktekstiks
from easygui import *
def kasutajaliides(tekst):
    vastus=enterbox(msg=tee_lünktekstiks(tekst),title="siin võiks olla tekstifaili nimi vms",strip=True)
    return vastus
tekst1='Rachel kaotas Rossi ahvi ära'
#print(kasutajaliides(tekst1))