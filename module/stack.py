from .property import Property as pr

class Stack:
    def __init__(self, data: list):
        self.__items: list = data

    @property
    def getDataStack(self) -> list:
        return self.__items

    @getDataStack.setter
    def push(self, item):
        while True:
            try:
                self.__items.append(item)
                pr.customPrint("{:^100}".format(f"Ditambahkan {item} ke dalam data"), 'blue')
                print(pr.singleLine)
                break
            except TypeError:
                pass

    def is_empty(self):
        return len(self.__items) == 0
    
    def popData(self) -> None:
        if not self.is_empty():
            popped_item = self.__items.pop()
            self.__items == popped_item
            pr.customPrint("{:^100}".format(f"Diambil {popped_item} dari data paling atas"), 'blue')
            print(pr.singleLine)
        else:
            print("{:^100}".format("Data kosong! Tidak Ada yang bisa diambil".upper()))
            print(pr.singleLine)

    def peekTopItem(self):
        if not self.is_empty():
            pr.customPrint("{:^100}".format(f"Data Paling atas : {self.__items[-1]}"), 'blue')
            print(pr.singleLine)
        else:
            print("{:^100}".format("Data kosong! Tidak Ada data yang paling atas".upper()))
            print(pr.singleLine)

    def lengthData(self):
        pr.customPrint("{:^100}".format(f"Panjang Data : {len(self.__items)}".upper()), 'blue')
        print(pr.singleLine)

    def showData(self):
        pr.customPrint("{:^100}".format(f"Isi Stack : {self.__items}"), 'blue')
        print(pr.singleLine)

    def main(self) -> None:
        while True:
            pr.clearTerminal()
            pr.dynamicHeader("program konversi bentuk data")
            pr.dynamicSubHeader("Konversi menjadi Stack")
            pr.customPrint("{:<100}".format("1. Push (Tambah data ke stack)"), 'blue')
            pr.customPrint("{:<100}".format("2. Pop (Hapus data teratas stack)"), 'blue')
            pr.customPrint("{:<100}".format("3. Peek (Lihat data teratas stack)"), 'blue')
            pr.customPrint("{:<100}".format("4. Show (Lihat isi stack)"), 'blue')
            pr.customPrint("{:<100}".format("5. Size (Ukuran stack)"), 'blue')
            pr.customPrint("{:<100}".format("0. Keluar Dari Program"), 'red')
            
            print(pr.singleLine)
            try:
                choice = str(input("Pilih operasi [1/2/3/4/5]: "))
                print(pr.singleLine)
                if choice == '1':
                    data = int(input("Masukkan data yang ingin dimasukkan ke stack: "))
                    print(pr.singleLine)
                    self.push = data
                elif choice == '2':
                    self.popData()
                elif choice == '3':
                    self.peekTopItem()
                elif choice == '4':
                    self.showData()
                elif choice == '5':
                    self.lengthData()
                elif choice == '0':
                    pr.customPrint("{:^100}".format("Keluar dari sub-program Stack..."), 'green')
                    pr.pauseProgram(1)
                    break
                else:
                    print("{:^100}".format("Pilihan tidak valid!".upper()))
            except TypeError:
                pass

            is_continue = str(input("{:<50}".format("Lanjutkan Mengubah Data? [Y/N] : ")))
            if is_continue == "N" or is_continue == "n":
                break
            elif is_continue == "Y" or is_continue == "y":
                continue
            else:
                print("{:^100}".format("Input Data Tidak Sesuai!".upper()))
            
            
