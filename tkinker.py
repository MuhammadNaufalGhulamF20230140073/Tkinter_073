import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi
def prediksi_prodi():
    try:
        # Validasi setiap input untuk memastikan tipe integer dan berada di antara 0 dan 100
        for entry in input_entries:
            nilai = int(entry.get())  # Mengubah menjadi integer
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus antara 0 dan 100")
        
        # Jika semua nilai valid, tampilkan hasil prediksi
        hasil_label.config(text="Prodi yang diprediksi: Teknologi Informasi")
    
    except ValueError as e:
        # Tampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("Error", f"Input tidak valid: {e}")
        hasil_label.config(text="")  # Hapus teks hasil jika terjadi kesalahan

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550")

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.pack(pady=10)

# Membuat frame untuk input nilai mata pelajaran
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Membuat 10 input nilai mata pelajaran
input_labels = []
input_entries = []

for i in range(10):
    label = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12))
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
    entry.grid(row=i, column=1, padx=5, pady=5)
    input_labels.append(label)
    input_entries.append(entry)

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", font=("Arial", 12, "bold"), command=prediksi_prodi)
prediksi_button.pack(pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic"))
hasil_label.pack(pady=10)

# Menjalankan loop utama aplikasi
root.mainloop()
