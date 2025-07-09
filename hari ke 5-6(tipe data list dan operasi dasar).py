# # for i in range(5):
# #     print(i)
# # buah = ["apel", "mangga", "jeruk"]
# # for item in buah:
# #     print(item)
# # yang atas ini dah paham lah ya wkwkw 
# # x = 0 
# # while x < 6: #loop akan terus berjalan sampai angka 6
# #     print(x)
# #     x -= 1
# # # kenapa kode di atas ngeloop tanpa henti karena jika terus menerus di kurangi satu maka tidak akan mencapai angka 6 sesuai program
# for huruf in 'kithly':
#     if huruf == 'h':
#         continue #karena ada continue maka dia akan menskip huruf yang di tulis di atas seperti program
#     print(huruf)


# while True:
#     nama = input("Masukkan nama Barang(atau ketik selesai): ")
#     if nama.lower() == 'selesai':
#         break

#     harga = input("Masukkan Harga Barang:Rp. ")
#     harga = harga.replace(".", "")
#     try:
#         harga_sistem = float(harga)
#     except ValueError:
#         print("Masukkan Harga yang Valid")
#         continue
#     print(f"Barang '{nama}' ditambahkan dengan harga Rp{harga_sistem:,.0f}")
# mini projek untuk hari ini adalah kasih dengan 5 jenis barang serta ada tabel harga,berat dan memiliki primary key untuk pemanggilan barang 
barang_dict = {
    1: {"nama":"Ayam Goreng", "harga": 25000, "berat": 1000},
    2: {"nama":"Bebek Bakar", "harga": 45000, "berat": 1500},
    3: {"nama":"Ikan Asap", "harga": 27000, "berat": 2000},
    4: {"nama":"Sapi Panggang", "harga": 35000, "berat": 1300},
    5: {"nama":"Telur Barendo", "harga": 30000, "berat": 1200}
}

total_harga = 0
total_berat = 0
daftar_belanja = []

while True:
    print("\nDaftar Barang: ")
    for kode, info in barang_dict.items():
        print(f"{kode}. {info['nama']} - Rp{info['harga']:,} / {info['berat']} gram")

    try:
        kode_input = int(input("\nMasukkan Kode Barang(atau 0 untuk selesai): "))
        if kode_input == 0:
            break

        if kode_input not in barang_dict:
            print("kode tidak di temukan, Coba kembali")
            continue
        jumlah = int(input(f"Masukkan jumlah unit {barang_dict[kode_input]['nama']}: "))
        barang = barang_dict[kode_input]

        subtotal = barang['harga'] * jumlah
        subberat = barang['berat'] * jumlah

        total_harga += subtotal
        total_berat += subberat

        daftar_belanja.append({
            "nama": barang['nama'],
            "jumlah": jumlah,
            "harga": barang['harga'],
            "subtotal": subtotal,
            "subberat": subberat
        })

        print(f"✅ {jumlah} x {barang['nama']} ditambahkan. Subtotal: Rp{subtotal:,}, Berat: {subberat}g")
    except ValueError:
        print("Input Tidak Valid Coba Lagi")

print("\n🧾 Struk Belanja:")
print("Nama\tJumlah\tHarga\t\tSubtotal\tBerat")
for item in daftar_belanja:
    print(f"{item['nama']}\t{item['jumlah']}x\tRp{item['harga']:,}\tRp{item['subtotal']:,}\t{item['subberat']}g")

print(f"\nTotal Harga: Rp{total_harga:,}")
print(f"Total Berat: {total_berat} gram\nTerimakasih Sudah berbelanja")



