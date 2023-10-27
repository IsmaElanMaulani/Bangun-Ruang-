import math

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

def diagonal_ruang(panjang, lebar, tinggi):
    return math.sqrt(panjang**2 + lebar**2 + tinggi**2)

def keliling_balok(panjang, lebar, tinggi):
    return 4 * (panjang + lebar + tinggi)

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# Input dari pengguna
panjang = float(input("Masukkan Panjang Balok: "))
lebar = float(input("Masukkan Lebar Balok: "))
tinggi = float(input("Masukkan Tinggi Balok: "))

# Hitung dan cetak hasil
print(f"Luas Permukaan Balok: {luas_permukaan_balok(panjang, lebar, tinggi)}")
print(f"Diagonal Ruang: {diagonal_ruang(panjang, lebar, tinggi)}")
print(f"Keliling Balok: {keliling_balok(panjang, lebar, tinggi)}")
print(f"Volume Balok: {volume_balok(panjang, lebar, tinggi)}")
