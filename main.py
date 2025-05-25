from module import matrix


def main():
    while True:
        print("=== Main Program ===")
        print("1. Jalankan Matrix Tool")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        match pilihan:
            case "1":
                matrix._runMatrixProgram()
            case "0":
                print("Keluar dari program utama...")
                break
            case _:
                print("Pilihan tidak valid!")
                input("Tekan Enter...")

if __name__ == "__main__":
    main()
