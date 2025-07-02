import time

def shell_sort_durasi(arr):
    n = len(arr)
    gap = n // 2

    start_time = time.time () #memulai menghitung waktu

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp        
        gap //= 2

        end_time = time.time()
        duration = end_time - start_time
        return duration


data = [25, 3, 75, 12, 8, 60, 1]
print("Sebelum diurutkan:", data)
durasi = shell_sort_durasi(data)
print("Setelah diurutkan:", data)
print(f"Waktu eksekusi: {durasi:.6f} detik")


