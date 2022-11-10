# class Super:
#     def __init__(self,ad) -> None:
#         self.ad=ad

#     def __str__(self) -> str:
#         return f"benim adım {self.ad}"


# class Sub(Super):
#     def __init__(self, ad,soyad) -> None:
#         super().__init__(ad)
#         self.soyad=soyad


# subObj=Sub("Aziz","Bektaş")


# ---------------------
class Dede:
    def __init__(self, ad, soyad) -> None:
        self.ad = ad
        self.soyad = soyad
    
    @property
    def ad(self):
        """The ad property."""
        return self._ad
    @ad.setter
    def ad(self, value):
        self._ad = value

    @property
    def soyad(self):
        """The soyad property."""
        return self._soyad
    @soyad.setter
    def soyad(self, value):
        self._soyad = value
class Baba(Dede):
    def __init__(self, ad, soyad, meslegi) -> None:
        super().__init__(ad, soyad)
        self.meslegi = meslegi

class Evlat(Baba):
    def __init__(self, ad, soyad, meslegi, isOgrenci) -> None:
        super().__init__(ad, soyad, meslegi)
        self.isOgrenci = isOgrenci
d = Dede("Osman", "Dede")
b = Baba("şakir", "kayadan", "Memur")
e = Evlat("ali", "kemal", "öğrenci", True)
# ali'nin babası şakir, şakir'in de babası Osman
# print(issubclass(Memur, Insan))
print(f"{e.ad}'nin {b.__class__.__name__} {b.ad}, {b.ad}'inde {d.__class__.__name__} {d.ad}")
