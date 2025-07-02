print("Selamat datang di kithly kalkulator")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
while True:
    operasi = input(str("Pilih Operasi(1/2/3/4): "))
    if operasi not in ['1', '2', '3', '4']:
        print("Pilih Angka Yang Benar")
        continue
    try:
        angka1 = float(input("Masukkan Angka Pertama: "))
        angka2 = float(input("Masukkan Angka Ke Dua: "))
    except ValueError:
        print("Itu Bukan Angka Ganteng")
        continue

    if operasi == '1':
        hasil = angka1 + angka2
        print(f"Hasil Dari penjumlahan tersebut adalah {hasil}")
    elif operasi == '2':
        hasil = angka1 - angka2
        print(f"Hasil Dari Pengurangan Tersebut Adalah {hasil}")
    elif operasi == '3':
        hasil = angka1 * angka2
        print("Hasil Dari Perkalian Tersebut Adalah {hasil}")
    elif operasi == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
            print("Hasil Dari Pembagian Tersebut Adalah {hasil}")
        else:
            print("Tidak Bisa Membagi dengan nol")
    else:
        print("Operasi tidak sesuai silahkan pilih dari 1-4")
    keluar = input("Ingin melanjutkan menghitung(y/n): ")
    if keluar.lower() != 'y':
        break






