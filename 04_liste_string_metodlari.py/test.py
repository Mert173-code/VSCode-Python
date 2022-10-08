#ödev:
"""
rakamlar=[6,2,7,3,5]
çiktı:
["Altı","İki","Yedi","Üç","Beş" ]
"""

"""
rakamlar=[8,7,6]
for i in rakamlar:
    if i==1:
        print("BİR",end=" ")
    elif i==2:
        print("İKİ",end=" ")
    elif i==3:
        print("ÜÇ",end=" ")
    elif i==4:
        print("DORT",end=" ")
    elif i==5:
        print("BEŞ",end=" ")
    elif i==6:
        print("ALTI",end=" ")
    elif i==7:
        print("YEDİ",end=" ")
    elif i==8:
        print("SEKİZ",end=" ")
    elif i==9:
        print("DOKUZ",end=" ")
"""



"""
    - Youtube izlenme oranı son ek ekleme ile ilgili örneği yapınız.
    - izlenme 18000         → 18 B
    - izlenme 1800000       → 1.8 Mn
    - izlenme 1800000000    → 1.8 Ml
"""
"""
izlenme=18000
if 1000<=izlenme<=999999:
    print(f"{izlenme//1000} B")
elif 1000000 <=izlenme <=999999999:
    print(f"{(izlenme//1000)/1000} Mn")    
"""

from itertools import count
from unittest import result


# ogrenci_listesi=["mehmet","ahmet"]
# print(ogrenci_listesi)
# gelmeyenlerListesi=ogrenci_listesi.copy()
# print(type(ogrenci_listesi))
# print(type(gelmeyenlerListesi))
# print(gelmeyenlerListesi)
"""
result=ogrenci_listesi.count("furkan")
print(result)
saymak icin kullanılan
"""
"""
searchItem="irem"
result=ogrenci_listesi.count(searchItem)
print(f"aradiğiniz ögrenci {result }adet bulundu")

→methodlar parantez icinde yazılır

"""

"""
sayiListesi=[3,6,7,8,9,3]
items=["ahmet","sena",True ,3<9,5>10]
print(items.count(True))
"""

"""
for i in ogrenciListesi:
    if i == "furkan":
        result = ogrenciListesi.count(i)
        print(f" aradığınız {i} elemanından {result} adet bulundu")
        break
"""


"""notListesi=[30,50,60,70,99]
notListesi.sort()
#notListesi.sort()#küçükten→büyüğe
notListesi.sort(reverse=True)
"""

"""
#Sırlama algoritmesi
notListesi = [30, 50, 60, 70, 99]
# notListesi.sort() # küçükten → büyüğe
# notListesi.sort(reverse=True) # büyükten → büyüğe
# notListesi.sort(reverse=False) # küçükten → büyüğe
notListesi.reverse() # büyükten → büyüğe
print(notListesi)
"""

"""
#Nerde oldugunu bulur
notListesi=[30,50,60,70,99]
result=notListesi.index(50)
print(result)
"""

#global talent

#extend SSS→FAQ
a=[3,5,8,1,2,7]
b=[2,6,8]
lenA,lenB=len(a),len(b)
diff=abs(lenA-lenB)
print(diff)
if lenA<lenB:
    a.extend([0]*diff)
else:
    b.extend([0]*diff)    
print(a)
print(b)





















