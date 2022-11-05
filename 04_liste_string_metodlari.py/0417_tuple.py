#Koleksiyonlar (tuples_tiyuples)
"""
--list
--tuple
--dictionarty
"""

#myTuples=("kırmızı","beyaz","sarı",mor)
#myTuples="kırmızı","beyaz","sarı",mor
#myTuples="kırmızı","beyaz","sarı",mor,155,400,200
#myTuples="kırmızı","beyaz","sarı",mor,155,400,200,"mor"
# myTuples[1]="white"
# print(myTuples)

# print(myTuples[1])

# for i in myTuples:
#     print(i)

"""
myTuples="kırmızı","beyaz","sarı","mor"
myList=[]
for i in myTuples:
    myList.append(i)
print(myList)    
myList[1]="white"
print(myList)
"""
#web scrabing parse
"""
print(myList[0][3])
"""


#--------------#
"""
isimListesi=("ali","murat","ayşe","mehmet","murat")
x=input("aradıgınız eleman:")
print(f"aradıgınız öğrenci isminden {isimListesi.count(x)} adet vardır")
"""
"""
sKodlari=(1001,1004,1007,1006)
x=input("aradıgınız stok kodu:")
if x.isdigit():
    x=int(x)
    if x not in sKodlari:
        print(f"aradıgınız {x} kodlu stok mecut degil")
    else:
        print(f"aradıgınız {x} kodlu stok {sKodlari.index(x)}.stokludur.")   
else:
    print("lütfen sayisal bir değer giriniz")
"""
#index listenin neresinde oldugu

#dictionry:
#apı
#jsen(xml)

"""
pDiliOzellikleri={
    "programlamaDili":"python",
    "seviye":"yüksek",
    "interpreter": True,
    "version": "3.10"
}
print(pDiliOzellikleri)
print(type(pDiliOzellikleri))
print(pDiliOzellikleri)
""""""
for key, value in pDiliOzellikleri.items():
print(key,value)
print(key)
print(value)
"""
"""
del pDilliOzellikleri["version"]
print(pDiliOzellikleri)
pDiliOzellikleri.clear()

"""
"""
for key value in pDiliOzellikleri.items():
    if key =="seviye":
        print(value)
"""


"""
pDilliOzellikleri = {
    "programlamaDili": "python",
    "seviye": "yüksek",
    "interpreter": True,
    "version": "3.10"
}
myList = list(pDilliOzellikleri.keys())
myList.sort()
for i in myList:
    print(i, pDilliOzellikleri[i])

"""

#---------------------------#

"""
sirket = {
    "departman": {
        "yazılım": ["ali", "mehmet"],
        "muhasebe": ["inci", "elif"],
    },
    "calisanSayisi": 100,
    "ceo": "Ali Kemal",
    "telefonlar": {
        "istanbul": "021265656",
        "ankara": "031245656"
    },
    "sirketArabalari": ["i20", "renault megan", "ford focus"],
     "sirketArabalari":{
        "i20":True,
        "renault magan":False,
        "ford focus":True
     }
}    
print(sirket["ceo"])
print(sirket["calisanSayisi"])
print(sirket["telefonlar"]["ankara"])    #liste ve diconrty olması onemli
print(sirket["sirketArabalari"][0])         
print(sirket["departman"]["muhasebe"][1])




print(sirket["sirketArabalari2"].values())
for key, value in sirket["sirketArabalari2"].items():
    if value==False:
        print(f"otoparktaki araba {key}")
        cvp=input(f"otoparkataki araba{key} almak ister misin 1/0: ")
        if cvp=="1":
            sirket["sirketArabalari2"][key]=True
print(sirket["sirketArabalari2"])

"""
#---------------------------#


# ad = "ramazan şen"
# adSoyadList = ad.split()
# print(adSoyadList[0])
# print(adSoyadList[1])
# dSamples = {
#     adSoyadList[0]: adSoyadList[1]
# }
# print(dSamples)

# yukarıdaki bilgi
# print(sirket["sirketArabalari2"].values())
# for key, value in sirket["sirketArabalari2"].items():
#     if value==False:
#         print(f"otoparktaki araba {key}")










