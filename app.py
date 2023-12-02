from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Fungsi untuk menambahkan data mahasiswa
# Fungsi untuk menambahkan data mahasiswa
def tambah_data(nama, nim, jurusan, nilai):
    with open('data_mahasiswa_ipb.txt', 'a') as file:
        file.write(f'{nama},{nim},{jurusan},{nilai}\n')
    return f"Data mahasiswa {nama} berhasil ditambahkan dengan nilai {nilai}!"

# Fungsi untuk menulis data ke file
def tulis_data():
    with open('data_mahasiswa_ipb.txt', 'r') as file:
        data = file.readlines()
        if not data:
            return "Tidak ada data mahasiswa."
        else:
            return [line.strip() for line in data]

# Fungsi untuk mengurutkan data berdasarkan NIM
def urutkan_data():
    with open('data_mahasiswa_ipb.txt', 'r') as file:
        data = file.readlines()
        if not data:
            return "Data tidak ada."
        else:
            sorted_data = sorted(data, key=lambda x: x.split(',')[1])
            return [line.strip() for line in sorted_data]

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
            return f"Data mahasiswa dengan NIM {nim} berhasil dihapus!"
        else:
            return f"Tidak ada data mahasiswa dengan NIM {nim}."

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk form submit
@app.route('/submit', methods=['POST'])
def submit():
    pilihan = request.form['pilihan']
    if pilihan == '1':
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']
        nilai = request.form['nilai']
        result = tambah_data(nama, nim, jurusan, nilai)
    elif pilihan == '2':
        result = tulis_data()
    elif pilihan == '3':
        result = urutkan_data()
    elif pilihan == '4':
        nim = request.form['nim_hapus']
        result = hapus_data(nim)
    elif pilihan == '5':
        result = "Terima kasih!"
    else:
        result = "Perintah tidak dimengerti. Silakan pilih kembali."
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
