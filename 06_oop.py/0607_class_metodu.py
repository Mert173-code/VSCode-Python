from sqlite3 import adapt


class Insan:
    insanlar = []

    def __init__(self, ad, soyad) -> None:
        self.ad = ad
        self.soyad = soyad
        Insan.Ekle(self)

    @classmethod
    def Ekle(cls, insanNesnesi):
        Insan.insanlar.append(insanNesnesi)

    def BilgiVer(self):
        print("....")

i1=Insan("Ali","Kemal")