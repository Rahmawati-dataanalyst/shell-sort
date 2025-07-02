import time
import random

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Fungsi untuk generate data acak
def generate_data(size):
    return random.sample(range(1, size * 10), size)

# Modifikasi data kecil & data besar
data_kecil = [10, 4, 15, 3, 1, 12, 2]
hasil = shell_sort(data_kecil)
print("Data terurut:", hasil)

data_besar = [2456, 1342, 7654, 3456, 4378, 1692]
hasil = shell_sort(data_besar)
print("Data terurut:", hasil)

# Eksekusi dan ukur durasi
def eksekusi_sorting(nama, data):
    print(f"\nMenjalankan Shell Sort untuk: {nama}")
    start_time = time.time()
    shell_sort(data)
    durasi = time.time() - start_time
    print(f"Durasi: {durasi:.6f} detik")
    return durasi

durasi_kecil = eksekusi_sorting("Data Kecil", data_kecil.copy())
durasi_besar = eksekusi_sorting("Data Besar", data_besar.copy())

# Output untuk Google Sheet
print("\nUntuk Google Sheet:")
print("Algoritma\tDurasi (kecil)\tDurasi (besar)\tNotasi Big O")
print(f"Shell Sort\t{durasi_kecil:.6f}\t{durasi_besar:.6f}\tO(n^2) average, O(n log² n) best")

# Kode ini bisa langsung kamu ubah ukuran datanya dan dicatat hasilnya untuk sheet ✨