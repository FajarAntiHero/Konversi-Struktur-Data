from module import Property # Import Class Property
class Main:
    programDescription = (
        "Program ini digunakan untuk melakukan konversi bentuk data antara tipe data yang berbeda "
        "seperti MATRIX, QUEUE, STACK, LINKED LIST, dan GRAPH. Program ini menyediakan fungsi-fungsi "
        "yang menerima input dalam satu tipe data dan mengubahnya ke format yang diinginkan, "
        "serta menangani kesalahan umum yang mungkin terjadi selama proses konversi. "
        "Tujuan utama program ini adalah untuk mempermudah proses transformasi data dan memastikan "
        "kesesuaian tipe data dalam berbagai operasi pada aplikasi Python."
    )

    @classmethod
    def main(cls):
        Property.clearTerminal()
        Property.dynamicHeader("program konversi bentuk data")
        Property.writeDescription(Main.programDescription, 100)
        print(Property.singleLine)

        while True:
            confirmStartProgram = str(input("Mulai Program? [Y/N] : "))
            if confirmStartProgram == "Y" or confirmStartProgram == "Yes" or confirmStartProgram == "y":
                object = Property()
                object.main()
                break
            elif confirmStartProgram == "N" or confirmStartProgram == "No" or confirmStartProgram == "n":
                Property.dynamicSubHeader("terima kasih")
                break
            else:
                Property.dynamicSubHeader("input data salah! ulangi!")

        Property.pauseProgram(2)
        Property.clearTerminal()
        Property.dynamicHeader("program konversi bentuk data selesai!")

if __name__ == "__main__" :
    Main.main()