#Soal 1: Perbedaan Data Structure
#Jawab Pertanyaan di bawah ini:
#Jelaskan perbedaan dari List, Tuple, Set dan Dictionary!
#JAWABAN DI BAWAH!!
#List = menggunakan kurung siku, Tuple = Menggunakan Tutup kurung biasa
#Set = tidakberurutan, tidak dapat diubah*, dantidak diindeks 
#Dictionary = dapat diubah dan tidak Izinkan duplikat.

#Soal 2: Akses List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
#a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
# lengkapi disini dengan slicing list
#Expected Output :
#[ '13b', 'aa1', 1.32, 22.1 ]

a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print(a [1 : 5])

#Soal 3: Akses Nested List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
#a = [[5, 9, 8],[0, 0, 6]]
# lengkapi disini dengan subsetting list
#Expected Output :
#[0, 6]

a = [[5, 9, 8],[0, 0, 6]]
a[1].remove(0)
print(a [1])

#Soal 4: List Manipulation
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
#a = [[5, 9, 8],[0, 0, 6]]
# lengkapi disini change list value
#print(a)
#Expected Output :
#[ [5, 9, 10], [11, 0, 6] ]

a = [[5, 9, 8],[0, 0, 6]]
a[0][2] = 10 
a[1][0] = 11
print(a)

#Soal 5: Delete Element List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
#areas = ["hallway", 11.25, "kitchen", 18.0,
       # "chill zone", 20.0, "bedroom", 10.75,
        # "bathroom", 10.50, "poolhouse", 24.5,
         #"garage", 15.45]
# Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code
#print(areas)
#Expected Output:
# ['hallway',11.25, 
# 'kitchen', 18.0, 
# 'chill zone', 20.0,
# 'bedroom',10.75,
# 'poolhouse',24.5,
# 'garage',15.45]
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
        "bathroom", 10.50, "poolhouse", 24.5,
        "garage", 15.45
        ]
del areas[8:10]
print(areas)

# Soal 6: List Comprehension
#Gunakan metode **list comprehension** untuk mencari anggota dari S yang habis di bagi 2, kemudian assign hasilnya dalam bentuk list ke dalam variabel T.
#S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#T = 
#print(T)
#Expected Output:
#[0, 4, 16, 36, 64]
#Dictionary

S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
T = S[0::2] 
print(T)

#Soal 8: Menambahkan key-value baru ke Dictionary
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
#europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# tambahkan key itali ke objek dictionary dengan value roma
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe.update({"italy":"roma"})
print(europe)

#Soal 9: Boolean Comparison
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'and'
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'or'
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'not'
print((9 > 7) and (2 < 4))	
print((8 == 8) or (6 != 6))	
print(not(3 <= 1))	

#Soal 10: If-Else Statement
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
#Bualah sebuah if-else statement yang dimana akan mem-print 'High' 
#jika grade adalah 'A' dan price lebih dari 100000, kemudian mem-print
#'Medium' jika grade adalah 'A' dan price lebih dari 50000 dan memprint 'low'
#jika grade adalah 'A' dan price lebih kecil dan sama dengan 50000.		

a = 60000
if a > 100000 :
        print("High")
elif a > 50000 :
        print("Medium")
elif a < 50000 :
        print("low")