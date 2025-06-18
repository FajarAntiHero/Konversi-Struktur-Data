import numpy as np
import os
from .property import Property as pr

class Matrix:
    def __init__(self, initial_data: list = None):
        # Inisialisasi atribut instans
        self.__data = []
        if initial_data:
            # Jika ada data awal, coba ubah ke numpy array 1D
            try:
                self.__data = np.array(initial_data, dtype=float)
            except ValueError:
                pr.customPrint("{:^100}".format("Data awal tidak valid untuk Matrix. Menggunakan Matrix kosong."), 'red')
                self.__data = np.array([], dtype=float)
            
        self.__matrixA = None
        self.__matrixB = None
        self.__matrixResult = None
        self.__matrixOperation = ""
        self.__hasMatrix = False # Untuk melacak apakah matriks sudah diinput
        self.__combinedMatrix = False # Untuk melacak apakah hasil operasi sudah ada

    def _initiateMatrix(self, matrix_name: str):
        """Meminta input dimensi dan elemen untuk sebuah matriks."""
        pr.clearTerminal()
        pr.dynamicSubHeader(f"Input Matrix {matrix_name}")
        
        while True:
            try:
                rows = int(input(f"{matrix_name} - Masukkan jumlah baris: "))
                cols = int(input(f"{matrix_name} - Masukkan jumlah kolom: "))
                if rows <= 0 or cols <= 0:
                    pr.customPrint("{:^100}".format("Baris dan kolom harus lebih dari 0!"), 'red')
                    pr.pauseProgram(2)
                    continue
                break
            except ValueError:
                pr.customPrint("{:^100}".format("Input tidak valid! Harap masukkan angka."), 'red')
                pr.pauseProgram(2)
        
        matrix_elements = []
        for i in range(rows):
            row_elements = []
            for j in range(cols):
                while True:
                    try:
                        val = float(input(f"{matrix_name} Baris:[{i+1}] Kolom:[{j+1}] : "))
                        row_elements.append(val)
                        break
                    except ValueError:
                        pr.customPrint("{:^100}".format("Input tidak valid! Harap masukkan angka."), 'red')
            matrix_elements.append(row_elements)
        
        return np.array(matrix_elements, dtype=float)

    def _showMatrixMenu(self):
        """Menampilkan menu operasi matriks."""
        pr.customPrint("{:<100}".format("1. Input 2 Matrix Baru"), 'blue')
        pr.customPrint("{:<100}".format("2. Operasi Elemen-per-Elemen (+, -, *, /)"), 'blue')
        pr.customPrint("{:<100}".format("3. Perkalian Matriks (Dot Product)"), 'blue')
        pr.customPrint("{:<100}".format("4. Hapus Semua Matrix"), 'blue')
        pr.customPrint("{:<100}".format("0. Keluar Dari Program"), 'red')
        print(pr.singleLine)
        
        while True:
            try:
                choice = int(input("Pilih operasi: "))
                return choice
            except ValueError:
                pr.customPrint("{:^100}".format("Pilihan tidak valid! Harap masukkan angka."), 'red')
                pr.pauseProgram(1)
                pr.clearTerminal()
                pr.dynamicHeader("program konversi bentuk data")
                pr.dynamicSubHeader("Konversi menjadi Matrix")
                self._showMatrixMenu() # Tampilkan menu lagi setelah error

    def main(self):
        # Tampilkan data awal dari Controller jika ada
        if self.__data.size > 0:
            pr.clearTerminal()
            pr.dynamicHeader("program konversi bentuk data")
            pr.dynamicSubHeader("Data Awal Dikonversi ke Matrix 1D")
            pr.customPrint(f"{'Data Awal (Matrix 1D):':<100}", 'cyan')
            print(self.__data)
            print(pr.singleLine)
            pr.pauseProgram(3)

        while True:
            pr.clearTerminal()
            pr.dynamicHeader("program konversi bentuk data")
            pr.dynamicSubHeader("Konversi menjadi Matrix")
            
            # Tampilkan matriks yang sedang aktif jika ada
            if self.__hasMatrix:
                pr.customPrint(f"{'Matrix A:':<100}", 'cyan')
                print(self.__matrixA)
                print(pr.singleLine)
                pr.customPrint(f"{'Matrix B:':<100}", 'cyan')
                print(self.__matrixB)
                print(pr.singleLine)
            if self.__combinedMatrix:
                pr.customPrint(f"{'Hasil ' + self.__matrixOperation + ':':<100}", 'cyan')
                print(self.__matrixResult)
                print(pr.singleLine)

            choice = self._showMatrixMenu()

            if choice == 1:
                self.__matrixA = self._initiateMatrix("Matrix A")
                self.__matrixB = self._initiateMatrix("Matrix B")
                self.__hasMatrix = True
                self.__combinedMatrix = False # Reset hasil operasi sebelumnya
            elif choice == 2:
                if not self.__hasMatrix:
                    pr.customPrint("{:^100}".format("Silakan input matriks terlebih dahulu."), 'red')
                    pr.pauseProgram(2)
                    continue
                
                if self.__matrixA.shape != self.__matrixB.shape:
                    pr.customPrint("{:^100}".format("Dimensi matriks tidak cocok untuk operasi elemen-per-elemen."), 'red')
                    pr.pauseProgram(2)
                    continue

                pr.clearTerminal()
                pr.dynamicSubHeader("Pilih Operasi Elemen-per-Elemen")
                op = input("Operasi (+, -, *, /): ")
                print(pr.singleLine)

                try:
                    if op == '+':
                        self.__matrixResult = self.__matrixA + self.__matrixB
                        self.__matrixOperation = "Penjumlahan"
                    elif op == '-':
                        self.__matrixResult = self.__matrixA - self.__matrixB
                        self.__matrixOperation = "Pengurangan"
                    elif op == '*':
                        self.__matrixResult = self.__matrixA * self.__matrixB
                        self.__matrixOperation = "Perkalian Elemen"
                    elif op == '/':
                        self.__matrixResult = self.__matrixA / self.__matrixB
                        self.__matrixOperation = "Pembagian Elemen"
                    else:
                        pr.customPrint("{:^100}".format("Operasi tidak valid."), 'red')
                        pr.pauseProgram(2)
                        continue
                    self.__combinedMatrix = True
                except Exception as e:
                    pr.customPrint(f"{'Terjadi kesalahan saat operasi: ' + str(e):^100}", 'red')
                    pr.pauseProgram(3)

            elif choice == 3:
                if not self.__hasMatrix:
                    pr.customPrint("{:^100}".format("Silakan input matriks terlebih dahulu."), 'red')
                    pr.pauseProgram(2)
                    continue

                if self.__matrixA.shape[1] != self.__matrixB.shape[0]:
                    pr.customPrint("{:^100}".format("Dimensi tidak cocok untuk dot product:"), 'red')
                    pr.customPrint("{:^100}".format(f"Kolom Matrix A ({self.__matrixA.shape[1]}) harus sama dengan baris Matrix B ({self.__matrixB.shape[0]})"), 'red')
                    pr.pauseProgram(3)
                    continue

                try:
                    self.__matrixResult = self.__matrixA @ self.__matrixB
                    self.__matrixOperation = "Perkalian Matriks (Dot Product)"
                    self.__combinedMatrix = True
                except Exception as e:
                    pr.customPrint(f"{'Terjadi kesalahan saat perkalian matriks: ' + str(e):^100}", 'red')
                    pr.pauseProgram(3)

            elif choice == 4:
                if not self.__hasMatrix:
                    pr.customPrint("{:^100}".format("Belum ada matriks yang bisa dihapus."), 'red')
                else:
                    konfirmasi = input("Yakin ingin menghapus semua matrix? (y/n): ").lower()
                    if konfirmasi == 'y':
                        self.__hasMatrix = False
                        self.__combinedMatrix = False
                        self.__matrixA = None
                        self.__matrixB = None
                        self.__matrixResult = None
                        self.__matrixOperation = ""
                        pr.customPrint("{:^100}".format("Matrix berhasil dihapus."), 'blue')
                    else:
                        pr.customPrint("{:^100}".format("Penghapusan dibatalkan."), 'blue')
                pr.pauseProgram(2)

            elif choice == 0:
                pr.customPrint("{:^100}".format("Keluar dari sub-program Matrix..."), 'green')
                pr.pauseProgram(1)
                break
            else:
                pr.customPrint("{:^100}".format("Pilihan tidak valid!"), 'red')
                pr.pauseProgram(2)
            
            is_continue = str(input("{:<50}".format("Lanjutkan Mengubah Data? [Y/N] : ")))
            if is_continue == "N" or is_continue == "n":
                break
            elif is_continue == "Y" or is_continue == "y":
                continue
            else:
                print("{:^100}".format("Input Data Tidak Sesuai!".upper()))