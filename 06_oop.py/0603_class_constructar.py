# region class_constructor_sız
# class Insan:
#     insanSayisi = 0

#     def __init__(self):
#         self.ad = ""
#         self.soyad = ""
#         self.ozellik = []
#         Insan.insanSayisi += 1


# i1 = Insan()
# i1.ad = "Aziz"
# i1.soyad = "Bektaş"
# i1.ozellik.append("tembel")
# print(i1.ad, i1.soyad, i1.ozellik)
# #---------------
# i2 = Insan()
# i2.ad = "İlke"
# i2.soyad = "Bektaş"
# i2.ozellik.append("yaramaz")
# print(i2.ad, i2.soyad, i2.ozellik)
# print(Insan.insanSayisi)
# endregion






# region class_constructor_lı
# class Insan:
#     insanSayisi = 0

#     def __init__(self, ad, soyad, ozellik):
#         self.ad = ad
#         self.soyad =soyad
#         self.ozellik = ozellik
#         Insan.insanSayisi += 1


# i1 = Insan("Aziz","Bektaş",["çalışkan", "oop aşığı"])
# i2 = Insan("İlke","Bektaş", ["yaramaz", "2yaş sendromlu"])
# print(i1.ad, i1.soyad, i1.ozellik)
# print(i2.ad, i2.soyad, i2.ozellik)
# print(Insan.insanSayisi)
# endregion

#-------------------------------------------------------------#
#  region ornek5

# class Memur:
#     def __init__(self,ad,soyad,derece,kademe) -> None:
#         self.ad=ad
#         self.soyad=soyad
#         self.derece=derece
#         self.kademe=kademe
        
#     def Yazdir(self):
#         print(f"{self.ad} {self.soyad} {self.derece} {self.kademe}")      

# m=Memur("mert","lale",1,4)
# m.Yazdir()
#  endregion ornek5


# class Araba:
#     def __init__(self,ad,fiyat,km,motor) -> None:
#         self.ad=ad
#         self.fiyat=fiyat
#         self.km=km
#         self.motor=motor

#     def Yazdir(self):
#         print(f"{self.ad} {self.fiyat} {self.km} {self.motor}")

# l=Araba("Lada Samara", 45000, 180000, 1.5 )
# l.Yazdir()
#------------------------------------------#

# class ElbiseModel:
#     def __init__(self, renk, boy, fiyat, odemeSekli ) :
#         self.renk = renk
#         self.boy = boy
#         self.fiyat = fiyat
#         self.odemeSekli = odemeSekli

#     def Yazdir(self):
#         print(f"{self.renk} {self.boy} {self.fiyat} {self.odemeSekli}")

# urun1 = ElbiseModel("Pembe", "Mini", 300, "Havale")
# urun2 = ElbiseModel("Siyah", "Uzun", 500, "Taksitli")

# urun1.Yazdir()
# urun2.Yazdir()

# urunler=[
#     urunler1,
#     urunler2
# ]
# toplamFiyat=0
# for i in urunler:
#     toplamFiyat += i.fiyat
# print(toplamFiyat)

#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#


# import datetime
# class Araba:
#     def __init__(self, marka, model, motor, yil, renk="TANIMSIZ") -> None:
#         self.marka=marka
#         self.model =model
#         self.motor=motor
#         self.yil = yil
#         self.renk = renk
#         self.yas =  datetime.datetime.now().year - int(self.yil)

#     def Show(self):
#         print(f"{self.marka} {self.model} {self.motor} {self.yas} {self.renk}")

# a = Araba("Hyndai", "i20", "1.2", 2016)
# a.Show()










