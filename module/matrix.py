import numpy as np
import os

class MatrixHandler:
    def __init__(self):
        self._matrixMain()

    def _matrixMain(self):
        def clear_terminal():
            os.system('cls' if os.name == 'nt' else 'clear')

        def input_matrix(nama=""):
            x = int(input("Masukkan panjang Matriks (baris): "))
            y = int(input("Masukkan lebar Matriks (kolom): "))
            if not nama:
                nama = input("Masukkan nama Matriks: ")
            data = []
            for i in range(x):
                baris = []
                for j in range(y):
                    val = float(input(f"{nama} Baris:[{i+1}] Kolom:[{j+1}] : "))
                    baris.append(val)
                data.append(baris)
            return np.array(data), nama

        def show_menu():
            print("=== Menu Matriks ===")
            print("1. Input 2 Matriks")
            print("2. Operasikan Matriks (elemen-per-elemen)")
            print("3. Perkalian Matriks (dot product)")
            print("4. Hapus Matriks")
            print("0. Keluar")
            try:
                return int(input("Pilih menu: "))
            except ValueError:
                return -1

        matrixA = matrixB = result = None
        namaA = namaB = opName = ""
        has_matrix = combined = False

        while True:
            clear_terminal()
            if has_matrix:
                print(f"Matriks {namaA}:\n{matrixA}\n")
                print(f"Matriks {namaB}:\n{matrixB}\n")
            if combined:
                print(f"Hasil {opName}:\n{result}\n")

            menu = show_menu()

            if menu == 1:
                clear_terminal()
                matrixA, namaA = input_matrix()
                clear_terminal()
                matrixB, namaB = input_matrix()
                has_matrix = True
                combined = False

            elif menu == 2:
                if not has_matrix:
                    print("Silakan input matriks terlebih dahulu.")
                elif matrixA.shape != matrixB.shape:
                    print("Dimensi matriks tidak cocok untuk operasi elemen-per-elemen.")
                else:
                    op = input("Pilih operasi (+ - * /): ")
                    try:
                        if op == '+':
                            result = matrixA + matrixB
                            opName = "Penjumlahan"
                        elif op == '-':
                            result = matrixA - matrixB
                            opName = "Pengurangan"
                        elif op == '*':
                            result = matrixA * matrixB
                            opName = "Perkalian"
                        elif op == '/':
                            if np.any(matrixB == 0):
                                raise ZeroDivisionError("Pembagian dengan nol.")
                            result = matrixA / matrixB
                            opName = "Pembagian"
                        else:
                            print("Operasi tidak valid.")
                            input("Tekan Enter untuk kembali...")
                            continue
                        combined = True
                    except Exception as e:
                        print("Terjadi kesalahan saat operasi:", e)
                input("Tekan Enter untuk kembali...")

            elif menu == 3:
                if not has_matrix:
                    print("Silakan input matriks terlebih dahulu.")
                elif matrixA.shape[1] != matrixB.shape[0]:
                    print(f"Dimensi tidak cocok untuk dot product:\nKolom {namaA} harus sama dengan baris {namaB}")
                else:
                    try:
                        result = matrixA @ matrixB
                        opName = "Perkalian Matriks (Dot Product)"
                        combined = True
                    except Exception as e:
                        print("Terjadi kesalahan saat perkalian matriks:", e)
                input("Tekan Enter untuk kembali...")

            elif menu == 4:
                if not has_matrix:
                    print("Belum ada matriks yang bisa dihapus.")
                else:
                    if input("Yakin ingin menghapus semua matriks? (y/n): ").lower() == 'y':
                        matrixA = matrixB = result = None
                        namaA = namaB = opName = ""
                        has_matrix = combined = False
                        print("Matriks berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                input("Tekan Enter untuk kembali...")

            elif menu == 0:
                print("Keluar dari sub-program matrix...")
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk lanjut...")