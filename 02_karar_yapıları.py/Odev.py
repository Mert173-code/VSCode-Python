
# region ODEV-1
"""
a=int(input("Bir sayi giririniz \t :"))
if a>0 :
    print(f"sayının karesi {a*a}")

elif a<0:
    print(f"sayinin karekökü {a*(0.5)}")   

else :
    print("sayı 0 dır")      """
# endregion


# region ODEV-2
"""
fiyat1 , fiyat2 = int(input("1.fiyati giriniz  \t :")) , int(input("2.fiyati girinz \t :"))
if fiyat1<0 :
    print("Doğru bir fiyat giriniz")

elif fiyat2<0 :
     print("Doğru bir fiyat giriniz")

elif fiyat1+fiyat2>200:
    a = (fiyat2*25)/100
    print(f" -> Ürünlerin fiyatı {fiyat1} , {fiyat2} TL'dir. İkinci ürüne {a} lik indirim yapılmıstır Borcunuz : {fiyat1+a} .")    
  """
# endregion

# region ODEV-3
"""
a = int(input("a değeri giriniz :"))
b = int(input("b değeri giriniz :"))
c = int(input("c değeri giriniz :"))

delta = b*b - 4*a*c

if  delta>0 :
    print(f"iki kök vardır : {-b+(delta*0.5)/2*a} , {-b-(delta*0.5)/2*a}")

elif delta==0:
    print(f"iki kök {-b/a*2}")
else :
    print("kök yoktur")    
    """
# endregion