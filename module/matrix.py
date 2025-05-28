# Module's Imports
import numpy as np
import os

# Module's Classes
class Matrix:
    def __init__(self, x: int = 0, y: int = 0, namaMatrix: str = ""):
        self.x = x
        self.y = y
        self.n = namaMatrix
        self.data = None

    def _initiateMatrix(self):
        if self.x == 0 or self.y == 0:
            self.x = int(input("Masukkan panjang Matrix (baris): "))
            self.y = int(input("Masukkan lebar Matrix (kolom): "))
        if not self.n:
            self.n = input("Masukkan nama Matrix: ")

        isiMatrix = []
        for i in range(self.x):
            baris = []
            for j in range(self.y):
                val = float(input(f"{self.n} Baris:[{i+1}] Kolom:[{j+1}] : "))
                baris.append(val)
            isiMatrix.append(baris)

        self.data = np.array(isiMatrix)
        return self.data

# Module's Functions
def _clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def _showMenu():
    print("=== Menu Matrix ===")
    print("1. Input 2 Matrix")
    print("2. Operasikan Matrix (elemen-per-elemen)")
    print("3. Perkalian Matriks (dot product)")
    print("4. Hapus Matrix")
    print("0. Keluar")
    try:
        return int(input("Pilih menu: "))
    except ValueError:
        return -1

def _runMatrixProgram():
    global hasMatrix, combinedMatrix
    global MVarA, MVarB, matrixA, matrixB, matrixResult, matrixOperation

    _clearTerminal()

    hasMatrix = False
    combinedMatrix = False
    MVarA = None
    MVarB = None
    matrixA = None
    matrixB = None
    matrixResult = None
    matrixOperation = ""

    while True:
        _clearTerminal()
        if hasMatrix:
            print(f"Matriks {MVarA.n}:\n{matrixA}\n")
            print(f"Matriks {MVarB.n}:\n{matrixB}\n")
        if combinedMatrix:
            print(f"Hasil {matrixOperation}:\n{matrixResult}\n")

        menuPointer = _showMenu()

        match menuPointer:
            case 1:
                _clearTerminal()
                MVarA = Matrix()
                matrixA = MVarA._initiateMatrix()
                _clearTerminal()
                MVarB = Matrix()
                matrixB = MVarB._initiateMatrix()
                hasMatrix = True
                combinedMatrix = False
            case 2:
                if not hasMatrix:
                    print("Silakan input matrix terlebih dahulu.")
                    input("Tekan Enter untuk kembali...")
                    continue

                if matrixA.shape != matrixB.shape:
                    print("Dimensi matriks tidak cocok untuk operasi elemen-per-elemen.")
                    input("Tekan Enter untuk kembali...")
                    continue

                print("\nPilih operasi: +  -  *  /")
                op = input("Operasi: ")

                try:
                    if op == '+':
                        matrixResult = matrixA + matrixB
                        matrixOperation = "Penjumlahan"
                    elif op == '-':
                        matrixResult = matrixA - matrixB
                        matrixOperation = "Pengurangan"
                    elif op == '*':
                        matrixResult = matrixA * matrixB
                        matrixOperation = "Perkalian"
                    elif op == '/':
                        matrixResult = matrixA / matrixB
                        matrixOperation = "Pembagian"
                    else:
                        print("Operasi tidak valid.")
                        input("Tekan Enter untuk kembali...")
                        continue
                    combinedMatrix = True
                except Exception as e:
                    print("Terjadi kesalahan saat operasi:", e)
                    input("Tekan Enter untuk kembali...")

            case 3:
                if not hasMatrix:
                    print("Silakan input matrix terlebih dahulu.")
                    input("Tekan Enter untuk kembali...")
                    continue

                if matrixA.shape[1] != matrixB.shape[0]:
                    print(f"Dimensi tidak cocok untuk dot product:")
                    print(f"Kolom {MVarA.n} harus sama dengan baris {MVarB.n}")
                    input("Tekan Enter untuk kembali...")
                    continue

                try:
                    matrixResult = matrixA @ matrixB
                    matrixOperation = "Perkalian Matriks (Dot Product)"
                    combinedMatrix = True
                except Exception as e:
                    print("Terjadi kesalahan saat perkalian matriks:", e)
                    input("Tekan Enter untuk kembali...")

            case 4:
                if not hasMatrix:
                    print("Belum ada matriks yang bisa dihapus.")
                else:
                    konfirmasi = input("Yakin ingin menghapus semua matrix? (y/n): ").lower()
                    if konfirmasi == 'y':
                        hasMatrix = False
                        combinedMatrix = False
                        MVarA = None
                        MVarB = None
                        matrixA = None
                        matrixB = None
                        matrixResult = None
                        matrixOperation = ""
                        print("Matrix berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                input("Tekan Enter untuk kembali...")

            case 0:
                print("Keluar dari sub-program matrix...")
                break

            case _:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk lanjut...")

