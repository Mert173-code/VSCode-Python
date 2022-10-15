# liste=[i for i in range(1,9) if i>=3]
# print(liste)


# haftaninGunleri = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
# # ["Haftanın 1. Günü Pazartesi", "Haftanın 2. Günü Salı", "Haftanın 3. Günü Çarşamba" ...]


# haftaninGunleri = ["","Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

# listem = [f"Haftanın {i}. günü {haftaninGunleri[i]}" for i in range(1, 8)]
# print(listem)



"""
fav. mevsim, çıkmak için -1 : yaz
fav. mevsim, çıkmak için -1 : sonbahar
fav. mevsim, çıkmak için -1 : yaz
daha önce eklediniz
fav. mevsim, çıkmak için -1 : ilkbahar
fav. mevsim, çıkmak için -1 : -1
favori mevsimlerimiz yaz, sonbahar, ilkbahar
"""

"""
mevsimler=[]
while True:
    mevsim=input("fav. mevsim, çıkmak için -1 :")
    if mevsim=="-1":
        break
    if mevsim in mevsimler :
        print("daha once eklediniz")  
        continue

    mevsimler.append(mevsim)
print(f"Favori mevsimleriniz {mevsimler}")
"""

"""
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
#1,2,3,4,5,6,7,8
tekilListe=list.copy()
for i in list2:
    if i not in tekilListe:
        tekilListe.append(i)
print(tekilListe)        

"""


"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
#1,2,3,4,5,6,7,8
# tekilListe = list1.copy()
# for i in list2:
#     if i not in tekilListe:
#         tekilListe.append(i)
# print(tekilListe)




list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
ortakElemanlar = []
for i in list1:
    if i in list2:
        ortakElemanlar.append(i)
print(ortakElemanlar)

"""















