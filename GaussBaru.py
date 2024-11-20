import numpy as np

# Matriks augmented
n = int(input("Masukkan ukuran matriks (n x n): "))
#membuat matriks kosong berukuran (n, n+1) yang terisi dengan angka 0.0.
a = np.zeros((n, n+1), dtype=float) 
print("Masukkan elemen matriks dan konstanta (dengan spasi antar elemen):")
for i in range(n):
    row = input(f"Baris {i+1}: ").split()
    # .split() memisahkan nilai menjadi list of strings berdasarkan 
    # spasi di setiap elemen

    # mengonversi setiap elemen string di baris menjadi angka float
    a[i] = [float(num) for num in row]

x = np.zeros(n, dtype=float)

# Fungsi untuk eliminasi maju (forward elimination)
def fs(a, n):
    for k in range(n - 1):  # Perulangan untuk elemen pivot
        for i in range(k + 1, n):
            p = a[i][k] / a[k][k]  # Faktor eliminasi
            for j in range(k, n + 1):
                a[i][j] -= p * a[k][j]  # Mengurangi baris
    print("")
    print("Matriks segitiga atasnya adalah : \n",a)
    return a

# Fungsi untuk substitusi mundur (backward substitution)
def bs(a, x, n):
    #menghitung solusi untuk variabel terakhir
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1] 

    for k in range(n - 2, -1, -1):
        s = 0
        for i in range(k + 1, n):
            #menghitung jumlah dari hasil perkalian antar koef variabel
            s += a[k][i] * x[i]
        #menghitung nilai variabel x[k] dalam proses back subsitution
        x[k] = (a[k][n] - s) / a[k][k]
    return x

# Fungsi utama untuk metode eliminasi Gauss
def gauss(a, x, n):
    a = fs(a, n) # memanggil forward elimination
    x = bs(a, x, n) #memanggil back subsitution
    return x


print("")
print("Matriks SPLnya adalah : \n",a)
solusi = gauss(a, x, n)

# Menampilkan solusi akhir
print("")
print("Solusi SPL tersebut adalah : \n")
for i in range(n):
  print("x_",i+1,"=",solusi[i])
