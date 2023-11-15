# akses list:
## programnya
````python
# Buat sebuah list sebanyak 5 elemen dengan nilai bebas
my_list = [10, 20, 30, 40, 50]
# Tampilkan elemen ke 3
print(my_list[2])
# Ambil nilai elemen ke 2 sampai elemen ke 4
print(my_list[1:4])
# Ambil elemen terakhir
print(my_list[-1])
````
## Outputnya
![Alt text](latihan1.png)


## ubah elemen list:
### programnya
````python
# Ubah elemen ke 4 dengan nilai lainnya
my_list[3] = 45
# Ubah elemen ke 4 sampai dengan elemen terakhir
my_list[3:] = [45, 55]
````

## Tambah elemen list:
````python
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
A = my_list[:2]
B = A.copy()
# Tambah list B dengan nilai string
B.append("sixty")
# Tambah list B dengan 3 nilai
B.extend([70, 80, 90])
````
## Gabungkan list B dengan list A
````python
combined_list = A + B
print(combined_list)
````
### Outputnya
![Alt text](output.png)


# Praktikum 5
## programnya
````python
from prettytable import PrettyTable

def calculate_nilai_akhir(tugas, uts, uas):
    return 0.3 * tugas + 0.35 * uts + 0.35 * uas

# Membuat objek PrettyTable
table = PrettyTable()
table.field_names = ["No", "Nama", "Nim", "Tugas", "UTS", "UAS", "Nilai Akhir"]

# Buat list kosong untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    # Meminta input data mahasiswa
    nama = input("Masukkan Nama Mahasiswa (stop untuk mengakhiri): ")
    
    # Check apakah pengguna ingin mengakhiri input
    if nama.lower() == 'stop':
        break
    nim = float(input("Masukan Nim: "))
    tugas = float(input("Masukkan Nilai Tugas (0-100): "))
    uts = float(input("Masukkan Nilai UTS (0-100): "))
    uas = float(input("Masukkan Nilai UAS (0-100): "))

    # Menghitung nilai akhir
    nilai_akhir = calculate_nilai_akhir(tugas, uts, uas)

    # Menambahkan data ke dalam list
    data_mahasiswa.append({
        'No': len(data_mahasiswa) + 1,
        'Nama': nama,
        'Nim': nim,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })

# Mengisi tabel dengan data
for data in data_mahasiswa:
    table.add_row([data['No'], data['Nama'], data['Nim'], data['Tugas'], data['UTS'], data['UAS'], data['Nilai Akhir']])

# Menampilkan tabel
print(table)
````

## Outputnya
![Alt text](praktikum.png)

# Flowchart
![Alt text](flowchart.png)