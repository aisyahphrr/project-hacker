# Fungsi untuk menambahkan data mahasiswa
def tambah_data(nama, nim, jurusan):
    with open('data_mahasiswa_ipb.txt', 'a') as file:
        file.write(f'{nama},{nim},{jurusan}\n')
    print(f"Data mahasiswa {nama} berhasil ditambahkan!")

# Fungsi untuk menulis data ke file
def tulis_data():
    with open('data_mahasiswa_ipb.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print("Tidak ada data mahasiswa.")
        else:
            print("Data Mahasiswa:")
            for idx, line in enumerate(data, start=1):
                print(f"{idx}. {line.strip()}")

# Fungsi untuk mengurutkan data berdasarkan NIM
def urutkan_data():
    with open('data_mahasiswa_ipb.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print("Data tidak ada.")
        else:
            sorted_data = sorted(data, key=lambda x: x.split(',')[1])
            print("Data Mahasiswa sesuai urutan (Berdasarkan NIM):")
            for idx, line in enumerate(sorted_data, start=1):
                print(f"{idx}. {line.strip()}")

# Fungsi untuk menghapus data mahasiswa
def hapus_data(nim):
    with open('data_mahasiswa_ipb.txt', 'r') as file:
        lines = file.readlines()
    with open('data_mahasiswa_ipb.txt', 'w') as file:
        deleted = False
        for line in lines:
            if not line.split(',')[1] == nim:
                file.write(line)
            else:
                deleted = True
        if deleted:
            print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus!")
        else:
            print(f"Tidak ada data mahasiswa dengan NIM {nim}.")

# Menu utama
while True:
    print("\n===== Aplikasi Pendaftaran Mahasiswa Baru IPB Angkatan 61 =====")
    print("1. Tambah Data Mahasiswa Baru IPB Angkatan 61")
    print("2. Tampilkan Data Mahasiswa Baru IPB Angkatan 61")
    print("3. Urutkan Data Mahasiswa Baru IPB Angkatan 61 (Berdasarkan NIM)")
    print("4. Hapus Data Mahasiswa Baru IPB Angkatan 61")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    
    if pilihan == '1':
        nama = input("Masukkan nama mahasiswa Baru IPB Angkatan 61: ")
        nim = input("Masukkan NIM mahasiswa Baru IPB Angkatan 61: ")
        jurusan = input("Masukkan jurusan mahasiswa Baru IPB Angkatan 61: ")
        tambah_data(nama, nim, jurusan)
    elif pilihan == '2':
        tulis_data()
    elif pilihan == '3':
        urutkan_data()
    elif pilihan == '4':
        nim = input("Masukkan NIM mahasiswa Baru IPB Angkatan 61 yang ingin dihapus: ")
        hapus_data(nim)
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Perintah tidak dimengerti. Silakan pilih kembali.")
