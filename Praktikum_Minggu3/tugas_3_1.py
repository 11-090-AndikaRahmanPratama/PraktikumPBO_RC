import math

class Kalkulator:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, bilangan):
        return Kalkulator(self.nilai + bilangan.nilai)

    def __sub__(self, bilangan):
        return Kalkulator(self.nilai - bilangan.nilai)

    def __mul__(self, bilangan):
        return Kalkulator(self.nilai * bilangan.nilai)

    def __truediv__(self, bilangan):
        if bilangan.nilai == 0:
            raise ValueError("Tidak bisa membagi dengan bilangan 0.")
        return Kalkulator(self.nilai / bilangan.nilai)

    def __pow__(self, bilangan):
        return Kalkulator(self.nilai ** bilangan.nilai)

    def logaritma(self):
        if self.nilai <= 0:
            raise ValueError("Harus positif.")
        return math.log(self.nilai)

    def __str__(self):
        return f"{self.nilai}"

kalkulator1 = Kalkulator(8)
kalkulator2 = Kalkulator(4)

print(f"{kalkulator1.nilai} + {kalkulator2.nilai} = {kalkulator1 + kalkulator2}")
print(f"{kalkulator1.nilai} - {kalkulator2.nilai} = {kalkulator1 - kalkulator2}")
print(f"{kalkulator1.nilai} * {kalkulator2.nilai} = {kalkulator1 * kalkulator2}")
print(f"{kalkulator1.nilai} / {kalkulator2.nilai} = {kalkulator1 / kalkulator2}")
print(f"{kalkulator1.nilai} ** {kalkulator2.nilai} = {kalkulator1 ** kalkulator2}")
print(f"log({kalkulator1.nilai}) = {kalkulator1.logaritma()}")
