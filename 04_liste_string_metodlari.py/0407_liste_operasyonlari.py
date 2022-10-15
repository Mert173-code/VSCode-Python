# listem=[1,2,3,4,5]
# listem[2]=listem[3] #listem =[1,2,4,4,5]
# listem[3]=listem[2]
# print(listem)

# yukardaki arasındaki fark

# listem = [1, 2, 3, 4, 5]
# temp=listem[2]
# listem[2] = listem[3]
# listem[3] = listem[2]
# print(listem)


# slice çalımaları
"""kurum ="ecodation"
result=kurum
result=kurum[2]
result=kurum[3]
result=kurum[-3]
result=kurum[0:3]
print(result)

"""

"""
# listem = [1, 2, 3, 4, 5]
# listem[2], listem[3] = listem[3], listem[2]
# print(listem)

#slice çalışmalarımız
kurum = "ecodation"
result = kurum
result = kurum[2]
result = kurum[3]
result = kurum[-3]
result = kurum[:]
result = kurum[0:3]
result = kurum[-1]
result = kurum[1:4]
result = kurum[-1:]
result = kurum[1:]
result = kurum[:3] # liste 3 den başla "ecodation"
result = kurum[-3:-1] # liste 3 den başla "ecodation"
result = kurum[1:5:2] # liste 3 den başla "ecodation"
result = kurum[::1]
result = kurum[::-1]
# listem = [1, 2, 3, 4, 5]
# result = listem[::-1]
# result = listem[-3:-1]

# print(result)



"""


# internet sitesi dogruluk testi
"""
site = input("lütfen internet sitesini giriniz : ")
if site[-3:]!="com" or site[:3]!="www":
    print("hatalı adres")
else:
    print(f"internet adresiniz {site}")
"""


# tek satırla kesme
"""
aciklama = "Word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar. Örneğin, birbiriyle uyumlu bir kapak sayfası, başlık ve kenar çubuğu ekleyebilirsiniz. Ekle'ye tıklayın ve ardından farklı galerilerden eklemek istediğiniz öğeleri seçin."
if len(aciklama) > 30:
    aciklama = aciklama[:30]
print(f"{aciklama}...")
"""


# iki basamaklı sayıyı mente donusturen program
"""
orn 95
doksan bes
"""
# while True:
#     birler = ["","bir","iki","üç","dört","beş","alt","yedi","sekiz","dokuz"]
#     onlar =  ["","on","yirmi","otuz","kırk","elli","atmış","yetmiş","seksen","doksan"]
#     sayi=int(input("Lütfen sayi giriniz: "))

#     s=str(sayi)

#     print(onlar[int(s[0])],birler[int(s[1])])
#print(f"{onlar[sayi//10]} {birler[sayi%10]}  )    hoca yöntemi

"""
isim=str(input("Lütfen isminizi giriniz :\t"))
print(f"adınız {isim}")
"""
# favoriFilm = []
# while True:
#         x = int(input("Lütfen seçimizi yapınız: "))
#         if x == 4:
#             break
#         elif x == 1:
#                 film = input("Eklenecek Film Adı Girin : ")
#                 favoriFilm.append(film)
#         elif x == 2:
#                 film = input("Cıkarılcak film adı giriniz: ")
#                 favoriFilm.remove(film)
#         elif x == 3:
#                 for i in range(0, len(favoriFilm)):
#                     print(f"{i+1}. filmin adı {favoriFilm[i] } ")
#         else:
#                 print("Hatalı seçim")



















