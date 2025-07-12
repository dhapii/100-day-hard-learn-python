

# indexing
text = "kithly"
print(text[0])
print(text[-2])

# slicing
print(text[3:5])
print(text[:5])
print(text[1:5])
# perbedaan indexing dan slicing adalah kalau indexing hanya berfokus pada huruf yang di panggil sedangkan slicing adalah huruf dalam range yang di panggil

# slicing dan indexing 
buah = ['apel', 'jeruk', 'nanas']
print(buah[0])
print(buah[2])
print(buah[0:])

# fungsi dan metode str penting 
nama = "kithly gabriel"
print(nama.upper())
print(nama.title())
print(nama.split())
# metode list
angka = [1, 2, 3]
angka.append(4) #tambah elemen
angka.remove(3) # hapus elemen
angka.insert(1, 99) #sisipkan 
# print(angka.append(6)) # maka hasilnya akan none karena append remove insert hanya merubah list dan tidak dapat mengembalikan nilai untuk di tampilakan di terminal 
print(angka) #ini yang benar
print(len(angka)) #panjang list

# konversi tipedata 
teks = '123'
angka = int(teks) # dari string ke int
teks2 = str(angka) #dari int ke string
print(teks2)
print(angka)

# mini projek untuk hari ini adalah pengeja kaliamt
# Masukkan kalimat: belajar python itu seru
# List kata: ['belajar', 'python', 'itu', 'seru']
# Kata pertama: belajar
# Kata terakhir: seru


kata = str(input("Masukkan kata yang ingin di eja: "))
ejaan = kata.split()
if len(ejaan) >= 1:
    print(f"Kata Pertama{ejaan[0]}")
if len(ejaan) >= 2:
    print(f"Kata Kedua {ejaan[1]}")
if len(ejaan) >= 3:
    print(f"Kata Ketiga {ejaan[2]}")
if len(ejaan) >= 4:
    print(f"Kata Keempat {ejaan[3]}")
if len(ejaan) >= 5:
    print(f"Kata Kelima {ejaan[4]}")
if len(ejaan) >= 6:
    print(f"Kata Keenam {ejaan[5]}")
if len(ejaan) >= 7:
    print(f"Kata Ketujuh {ejaan[6]}")
if len(ejaan) >= 8:
    print(f"Kata Kedelapan {ejaan[7]}")
if len(ejaan) >= 9:
    print(f"Kata Kesembilan {ejaan[8]}")
if len(ejaan) >= 10:
    print(f"Kata Kesepuluh {ejaan[9]}")
if len(ejaan) > 10: 
    print("kata Kata Terlalu panjang Untuk di eja")








