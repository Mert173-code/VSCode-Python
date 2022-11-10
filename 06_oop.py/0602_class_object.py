# a = 1
# print(type(a))

# class A1:
#     pass

# class A2():
#     pass

# class A3(object):
#     pass


#------------------------------#

#class, attribute , object

 #region ornek
# class Insan:
#     ad= ""
#     soyad= ""   #----->attribute

# i1=Insan()   #------> object
#endregion

#region ornek2
# class Araba:
#     model= "Hundai"
#     sene = "2010"
#     renk = "sarı"

# a = Araba()
#endregion

#region ornek3
# class Ogrenci:
#     adSoyad = ""
#     not1 = 0
#     not2 = 0
#     #initial


# o = Ogrenci()
# o.adSoyad = "Ali Kemal"
# o.not1 = 70
# o.not2 = 80
# ortalama = (o.not1 + o.not2)/2
# print(f"{o.adSoyad} isimli öğrencinin dönem notu {ortalama}")
#endregion

# class Insan:
#     ad=""
#     soyad=""
#     def __init__(self):
#         self.ozellik =[]


# i1 = Insan()
# i1.ad="ahmet"
# i1.soyad="calıskan"
# i1.ozellik.append("Uzun")

# i2 = Insan()
# i2.ad="ahmet"
# i2.soyad="calıskan"
# i2.ozellik.append("kısa")

# print()

#--------------------------------------------#
"""
class Insan:
    def __init__(self):
        self.ad=""
        self.soyad=""
        self.ozellik=[]
        

i1=Insan()
i1.ad="ali"
i1.soyad="kemal"
i1.ozellik.append("tembel")
print(i1.ad , i1.soyad ,i1.ozellik)

"""


# region sorun
# class Insan:
#     ad = ""
#     soyad = ""
#     ozellik = []


# i1 = Insan()
# i1.ad = "Ali"
# i1.soyad = "Kemal"
# i1.ozellik.append("Tembel")
# i1.ozellik.append("Uzun")
# # -----------------------
# i2 = Insan()
# i2.ad = "Mustafa"
# i2.ozellik.append("Çalışkan")
# # -----------------------
# i3 = Insan()

# print(i1.ad, i1.soyad, i1.ozellik)
# print(i2.ad, i2.soyad, i2.ozellik)
# print(i3.ad, i3.soyad, i2.ozellik)
# endregion
"""
a = 99
class Insan:
    ad = ""
    soyad = ""
    def __init__(self):
        self.ozellik = []


i1 = Insan()
i1.ad = "Ali"
i1.soyad = "Kemal"
i1.ozellik.append("Tembel")
i1.ozellik.append("Uzun")
# -----------------------
i2 = Insan()
i2.ad = "Mustafa"
i2.ozellik.append("Çalışkan")
# -----------------------
i3 = Insan()
print(i1.ad, i1.soyad, i1.ozellik)
print(i2.ad, i2.soyad, i2.ozellik)
print(i3.ad, i3.soyad, i3.ozellik)

"""

#-----------------------------





# class tiptir, user-defined tiptir
# Araba, Insan, Firma...


"""
class A1:
    pass
class A2():
    pass
class A3(object):
    pass
"""


from cgi import print_form


class Banka:
    bankaAdi = ""
    sahibi = ""
    subeSayisi = 1500


a = 10
# <class int>


class Insan:
    ad = ""
    soyad = ""


a = 19
"""i1 = Insan()
i1.ad = "Ali"
i1.soyad = "Kemal"
# print(i1)
# print(i1.ad, i1.soyad)
i2 = Insan()
i2.ad = "Mustafa"
i3 = Insan()
i3"""

"""print(i1.ad, i1.soyad)
print(i2.ad, i2.soyad)
print(i3.ad, i3.soyad)
"""


"""
Bisiklet Class
Attribute Ekle
Object Türet
Ekrana Print
Lütfen
"""


"""
class Bisiklet:
    marka = ""
    jant = 0
    renk = ""
    katlanirMi = True
b1 = Bisiklet()
b1.marka = "salcano"
b1.jant = 26
b1.renk = "sarı siyah"
b1.katlanirMi = False
if b1.katlanirMi:
    print(b1.marka, b1.jant, b1.renk, "Katlanabilir")
else:
    print(b1.marka, b1.jant, b1.renk, "Katlanamaz")
"""


"""class Ogrenci:
    adSoyad = ""
    not1 = 0
    not2 = 0
o1 = Ogrenci()
o1.adSoyad = input("ad soyad : ")
o1.not1 = int(input("not 1 : "))
o1.not2 = int(input("not 1 : "))
ort = (o1.not1 + o1.not2)/2
# ali kemal isimli öğrencinin not ortalaması ...
print(f"{o1.adSoyad} isimli öğrencinin not ortalaması {ort}")
"""

class Okul:
    kurumKodu = 0
    mudur = ""
    il = ""
    ilce = ""


o = Okul()
o.kurumKodu = 1001
o.mudur = "Ali Kemal"
o.ilce = "Tuzla"
o.il = "İstanbul"
print(f"Okulumuz {o.kurumKodu} kurum kodu ile {o.il} ili {o.ilce} ilçesinde faaliyet göstermektedir. Ben okul müdürü {o.mudur}")

