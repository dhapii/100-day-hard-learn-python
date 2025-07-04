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


while True:
    nama = input("Masukkan nama Barang(atau ketik selesai): ")
    if nama.lower() == 'selesai':
        break

    harga = input("Masukkan Harga Barang:Rp. ")
    harga = harga.replace(".", "")
    try:
        harga_sistem = float(harga)
    except ValueError:
        print("Masukkan Harga yang Valid")
        continue
    print(f"Barang '{nama}' ditambahkan dengan harga Rp{harga_sistem:,.0f}")