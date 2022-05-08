
"""
semua sintaks dasar bahasa pemograman terdiri dari :
1. sekuensial: langkah berurutan
2. percabangan: langkah melompat jika kondisi terpenuhi
3. perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
#sequential

print('Ibu berkata, "pergi ke toko" ')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab "Beli satu botol susu, dan jika ada telor beli 6"')
print('maka budi berangkat ke toko')
print('Dan mulai berbelanja')

# percabangan
Jumlah_Botol_susu = 173
jumlah_telur = 5
print(f"Jumlah botol susu {Jumlah_Botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if Jumlah_Botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uang nya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("menyampaikan hasilnya kepada ibu")