#region string_metodlari

# ad="şakiR"
# yas=30
# pi=3.14

# yas=str(yas)

#regionupper
"""result=ad.upper()
print(result)"""
#endregion

#regionlower
"""result=ad.lower()
print(result)"""
#endregion

# result=ad.count("a")
# print(result)

"""
kotuKelimeler = ["tü", "kaka", "serseri", "kötü"]

yorum = yorum.replace("sansürlenecek", "...")
print(yorum)
"""


#replace
"""
kotuKelimeler=["tüh","kaka","serseri","kötü"] 
yorum= "geçen gün mahallemizdeki serseri markette kötü kelimeler kullanıyordu. Ama çok nazik bir serseri, tüh, kaka falan diyordu."
for i in kotuKelimeler:
    yorum=yorum.replace(i,"...")
print(yorum)
"""

# #startwith() endswith()
# url="https://www.okan.com.tr"
# result=url.startswith("www")
# result=url.endswith("com.tr")

# #strip() lstirp() rstrip()
# kurum= "   Tuzla Mesek Lisesi    "
# print(len(kurum))
# result=kurum.strip()
# result=kurum.lstrip()
# result=kurum.rstrip()
# print(result)
# print(len(result))

# #isdigit() isalpha()
# result="1"
# print(result.isdigit())


#Split ayırma icin
"""kurumAdi="İstanbul Esenyurt Üniversitesi"
result=kurumAdi.split()
#print(type(result))
print(result)
"""








