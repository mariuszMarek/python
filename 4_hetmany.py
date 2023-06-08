import itertools
import doctest
import string

class CzteryHetmany():
    wysokosc_planszy  = [i for i in range (0,18)]
    szerokosc_planszy = [j for j in range (0,9)]
    znaki_alfabetu = {indeks+1: znak for indeks,znak in enumerate(list(string.ascii_lowercase))}

    def __init__(self, hetmany):
        self.hetmany  = hetmany.split()
        
    def ile_pod_szachem(self):        
        pass

    def ile_poza_szachem(self):
        pass

    def które_pod_szachem(self):
        pass

    def które_poza_szachem(self):
        pass

    def przestaw_hetmana(self, kod_przestawienia):
        pass
    def czy_pozycja_hetman(self):
        # return True
        pass
    def czy_szach(self):
        # return True
        pass
    def print_znak_planszy(self,wiersz = 0,kolumna = 0):
        znak = ""
        
        if kolumna == 0:                    znak = f"{int(wiersz/2)} " if wiersz %2 == 0 and wiersz != 0 else "  "            
        elif wiersz % 2 == 1:               znak = "---"                    
        elif wiersz == 0 and kolumna > 0:   znak = f" {self.znaki_alfabetu[kolumna]} "
        elif self.czy_pozycja_hetman():     znak = self.znak_hetmana 
        elif self.czy_szach():              znak = self.znak_szach
        else: znak = "   "
        
        if kolumna != 8 and kolumna > 0: znak += "+" if znak == "---" else "|"
            
        return znak
    
    def pokaż_szachownicę(self, hetman='H', szach=' '):
        self.znak_hetmana = f" {hetman} "
        self.znak_szach   = f" {szach} "
        for poz_y in reversed(self.wysokosc_planszy):
            for poz_x in self.szerokosc_planszy:

                znak = self.print_znak_planszy(poz_y, poz_x)

                print(znak, end="")
            print()

test = CzteryHetmany("a1 c7 e3 g5")
test.pokaż_szachownicę()