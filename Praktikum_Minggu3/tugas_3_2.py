import random

class OrangTua:
    def __init__(self, alel):
        self.alel = alel

class Ayah(OrangTua):
    pass

class Ibu(OrangTua):
    pass

class Anak:
    def __init__(self, ayah: Ayah, ibu: Ibu):
        self.ayah_alel = random.choice(ayah.alel)
        self.ibu_alel = random.choice(ibu.alel)
        self.golongan_darah = self.tentukan_golongan_darah()

    def tentukan_golongan_darah(self):
        alel = self.ayah_alel + self.ibu_alel
        if 'A' in alel and 'B' in alel:
            return 'AB'
        elif alel == 'AO' or alel == 'OA' or alel == 'AA':
            return 'A'
        elif alel == 'BO' or alel == 'OB' or alel == 'BB':
            return 'B'
        elif alel == 'OO':
            return 'O'
        else:
            return 'Tidak valid'

ayah = Ayah(['A', 'O'])
ibu = Ibu(['B', 'O'])

anak = Anak(ayah, ibu)
print(f"Alel ayah: {anak.ayah_alel}, Alel ibu: {anak.ibu_alel}")
print(f"Golongan darah anak: {anak.golongan_darah}")
