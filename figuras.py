class Kubs:

    #metode, kas inicializē objektu
    def __init__(self, malas_garums, krasa):
        if malas_garums <=10 and malas_garums >= 2:
            self.malas_garums = malas_garums
        else:
            print("Malas garums neatbilsts nosacījumiem.")
            self.malas_garums=2
        self.krasa = krasa

    #metode, kas aprēķina tilpumu
    def aprekinat_tilpumu(self):
        tilpums = self.malas_garums**3
        return tilpums

    #metode, kas nodzēš objektu
    def __del__(self):
        print("Objekts ir likvidēts! Tā krāsa bija ", self.krasa, ".")
        
#objekti
kubg = Kubs(10, "zaļa")
kubr = Kubs(1, "sarkana")

print("Kuba g krāsa ir ",kubg.krasa, " un  tā tilpums ir ", kubg.aprekinat_tilpumu(), " cm3.")
print("Kuba s garums ir ",kubr.malas_garums, " cm.")

#objekta dzēšana
del kubr

#pārbauda vai kubr eksistē
try:
    print(kubr.malas_garums)
except:
    print("Objekts neeksistē!")

print("Kuba g malas garums ir ",kubg.malas_garums," cm.")

#klases bloks, kas manto no klases kubs
class Bloks(Kubs):
    def __init__(self, malas_garums, krasa, skaits, forma):
        super().__init__(malas_garums,krasa)
        if skaits>=1 and skaits<=4:
            self.__skaits=skaits
        else:
            print("Neatbilstoša kuba skaita vērtība!")
        self.__skaits = skaits
        self.nosaukums = str(krasa)+str(self.__skaits)
        self.forma = forma
        formas_vertibas = [11,12,13,14,22]

        if forma not in formas_vertibas:
            self.derigums=0
            print("Forma neatbilst nosacījumiem!")
        else:
            self.derigums=1
    
    def tilpums(self):
        kuba_tilpums=self.malas_garums**3
        bloka_tilpums= kuba_tilpums*self.__skaits
        return bloka_tilpums

    def mainit_formu(self, jauna_forma):
        formas_vertibas = [11,12,13,14,22]

        if jauna_forma not in formas_vertibas:
            self.derigums=0
            print("Forma neatbilst nosacījumiem!")
        else:
            self.derigums=1

#objektu veidošana
orange3 = Bloks(5, "oranža", 3, 13)
print("Formas o nummurs ir",orange3.nosaukums, ", tā tilpums ir", orange3.tilpums(), " cm3.")


blue5 = Bloks(7, "zila", 5, 23)
print(blue5.nosaukums, blue5.derigums)
blue5.mainit_formu(12)
print("Formas b nummurs ir",blue5.nosaukums, ", tā tilpums ir", blue5.tilpums(), " cm3.")
