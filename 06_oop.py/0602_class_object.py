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







