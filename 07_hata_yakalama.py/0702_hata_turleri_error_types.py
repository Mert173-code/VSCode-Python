# #syntax error
# hatfanınGunleri={
#     "1":"pazartesi",
#     "2":"salı",
#     "3":"çarsamba"
# }

#result = haftaninGunler[4]

# try:
#     a = int(input("sayi1 : "))
#     b = int(input("sayi2 : "))
#     print(a/b)
# except:
#     print("hatalı giriş")

# -------------------------------------------------
# mevsimler = [
#     "",
#     "ilkbahar",
#     "yaz",
#     "son bahar",
#     "kış",
# ]

# try:
#     favMemsim = int(input("lütfen fav. mevsimi giriniz [1-4] : "))
#     result = mevsimler[favMemsim]
#     print(result)
# except Exception as e:
#     print(e,"lütfen 1-4 arası değer girin")

#-----------------------------
# import datetime
# def degerAl():
#     global dTarihi
#     dTarihi=input("y-a-g : ")
#     cEpoch = datetime.datetime.now().timestamp()
#     dEpoch=datetime.datetime.fromisoformat(dTarihi).timestamp()
#     if dEpoch>cEpoch:
#         raise Exception("lütfen d.tarihini bugünün trhinden büyük girmeyin")

# try:
#     degerAl()
#     print(dTarihi)
# except ValueError as v:
#     print("lütfen y-a-g formatta girin")
# except Exception as ex:
#     dTarihi=datetime.datetime.now()
    # print(ex, "d.tarihi", dTarihi, "olarak set edildi")
#1980-01-06
# lütfen d.tarihini bugünün trhinden büyük girmeyin d.tarihi 2022-11-06 12:42:12.530507 olarak set edildi
# ---------------------------

# tr, karakter girilmesin, minimum 8 karakter
# def isValidPassword():
#     while True:
#         trKarakterler = ["ş", "ç", "ğ", "ü", "ö", "ı", "İ"]

#         p = input("lütfen parola politikası test et, çıkmak için [ç] : ")
#         if p in ["ç", "Ç"]:
#             break
#         try:
#             if len(p) < 8:
#                 raise Exception("uygun olmayan parola - minimum karakter politikası")

#             for i in p:
#                 if i in trKarakterler:
#                     raise Exception("uygun olmayan parola - tr karakter politikası")
#             print("parola uygun")
#         except Exception as e:
#             print(e)


# isValidPassword()


