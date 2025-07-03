print("Selamat datang di Program konversi Suhu kithly")
print("1.Celcius")
print("2.Farenheit")
print("3.Reamur")
print("4.Kelvin")
while True:
    suhu_awal = input("Masukkan Data Suhu Yang Anda Punya(1/2/3/4): ")
    suhu_konversi = input("Masukkan Suhu tujuan konversi anda(1/2/3/4): ")
    if suhu_konversi not in ['1', '2', '3', '4'] or suhu_awal not in['1', '2', '3', '4']:
        print("ADA KESALAHAN PADA INPUT DATA SUHU!!!")
        exit()
    suhu_awal = int(suhu_awal)
    suhu_konversi = int(suhu_konversi)
    try:
        jumlahsuhu = float(input("Masukkan suhu yang mau di konversi: "))
    except ValueError:
        print("Itu Bukan Angka suhu yang benar coba lagi !!!")
        exit()

    # fungsi konversi 
    def ke_celcius(asal, nilai):
        if asal == 1:
            return nilai
        elif asal == 2:
            return (nilai - 32) *5 /9
        elif asal == 3:
            return nilai * 5 / 4
        elif asal == 4:
            return nilai - 273.15
        # fungsi dari celcius ke satuan tujuan 
    def dari_celcius(tujuan, nilaiC):
        if tujuan == 1:
            return nilaiC
        elif tujuan == 2:
            return (nilaiC *9 /5) + 32
        elif tujuan == 3:
            return nilaiC * 4 / 5
        elif tujuan == 4:
            return nilaiC + 273.15

    # proses konversi 
    nilaiC = ke_celcius(suhu_awal, jumlahsuhu)
    hasil_Akhir = dari_celcius(suhu_konversi, nilaiC)

    label = ["Celcius", "Fahrenheit", "Reamur", "Kelvin"]

    # Output hasil
    print(f"\nHasil konversi suhu {suhu_awal}: {hasil_Akhir:.2f} {label[suhu_konversi - 1]}")
    keluar = input("Ingin Melanjutkan Perhitungan(y/n): ")
    if keluar.lower != 'n':
        break