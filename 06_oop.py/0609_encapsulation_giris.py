
# import datetime


# class Ogrenci:
#     def __init__(self, ad, soyad, tc, sinif, okul, dTarihi) -> None:
#         self.ad = ad
#         self.soyad = soyad
#         self.tc = tc
#         self.setSinif(sinif)
#         self.setOkul(okul)
#         self.setDTarihi(dTarihi)

#     def setDTarihi(self, arg):
#         if arg <= datetime.datetime.now().year:
#             self.__dTarihi = arg
#         else:
#             self.__dTarihi =datetime.datetime.now().year

#     def getDTarihi(self):
#         return self.__dTarihi



# def setOkul(self, arg):
#         if arg == "siber güvenlik lisesi":
#             self.__okul = arg
#         else:
#             self.__okul = -1

#     def getOkul(self):
#         return self.__okul

#     def setSinif(self, arg):
#         if 8 < arg < 13:
#             self.__sinif = arg
#         else:
#             self.__sinif = -1

#     def getSinif(self):
#         return self.__sinif

#     def __str__(self) -> str:
#         if self.getOkul() == -1:
#             return "siber güvenlik lisesi dışından okul kabul edilemez"
#         if self.getSinif() == -1:
#             return "üzgünüm!!! sınıf seviyesi [9-12] dışında olamaz"
#         return f"{self.ad} {self.soyad} {self.tc} {self.__sinif} {self.__okul} {self.__dTarihi}"


# o = Ogrenci("Ali", "Kemal", 12345, 11, "siber güvenlik lisesi", 2023)
# # o.sinif="4-B" bu bir hata, private attribute e böyle erişemezsin, setter fonk. ile erişebilirsin
# # o.setSinif(10)
# # o.setOkul("pendik ito")
# # o.getSinif()
# print(o)




#----------------------------------------

# class Employe:

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not str(value).isalpha():
#             self._name = "hatalı ad"
#         else:
#             self._name = value
#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, value):
#         self._salary = value

#     def __str__(self):
#         # hatalı giriş yaptınız yazınız....
#         return f"{self.name} adlı kişinin maaşı = {self.salary}"

# e = Employe()
# e.name = "ramazan1"
# e.salary = 30000
# print(e)


# #---------------------------------------

# @property
#     def departman(self):
#         return self._departman

#     @departman.setter
#     def departman(self, value):
#         self._departman = value

#     def __str__(self):
#         # hatalı giriş yaptınız yazınız....
#         return f"{self.name} adlı kişi {self.departman} departmanındadır. maaşı = {self.salary}"



# e = Employe()
# e.name = input("lütfen adınızı giriniz: ")
# e.salary = int(input("Maaş bilgisini giriniz: "))
# e.departman = input(f"{e.name} adlı çalışanın departmanı giriniz: ")
# print(e)











