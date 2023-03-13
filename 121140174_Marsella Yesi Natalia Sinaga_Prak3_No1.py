import random

class Kotak:
    def __init__(self):
        self.isi = 'bom' if random.random() < 0.25 else 'bukan bom'
        self.status = 'belum dibuka'
    
    def tampilkan(self):
        if self.status == 'belum dibuka':
            return '?'
        elif self.isi == 'bom':
            return 'x'
        else:
            return 'o'
    
    def buka_kotak(self):
        self.status = 'sudah'
        
dimensi = int(input("Masukkan dimensi area: "))
hitung = 0
area = []
for i in range(dimensi):
    row = []
    for j in range(dimensi):
        row.append(Kotak())
    area.append(row)

bom = sum(k.isi == 'bom' for row in area for k in row)
for row in area:
        print(' '.join(k.tampilkan() for k in row))
while True: