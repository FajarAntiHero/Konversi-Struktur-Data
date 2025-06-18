from .property import Property as pr

class Queue:
    def __init__(self, data: list):
        self.__items: list = data

    @property
    def getDataQueue(self) -> list:
        return self.__items

    @getDataQueue.setter
    def enqueue(self, item: int):
        self.__items.append(item)  # Menambahkan item ke belakang antrian
        pr.customPrint("{:^100}".format(f"Ditambahkan [{item}] ke dalam Antrian"), 'blue')
        print(pr.singleLine)

    def is_empty(self):
        return len(self.__items) == 0

    def dequeue(self):
        if not self.is_empty():
            removed = self.__items.pop(0)  # Menghapus item dari depan antrian (FIFO)
            pr.customPrint("{:^100}".format(f"Dihapus [{removed}] dari Antrian"), 'blue')
            print(pr.singleLine)
        else:
            pr.customPrint("{:^100}".format(f"Antrian Kosong"), 'blue')
            print(pr.singleLine)

    def peek(self):
        if not self.is_empty():
            pr.customPrint("{:^100}".format(f"Data Antrian Paling Depan Adalah [{self.__items[0]}]"), 'blue')
            print(pr.singleLine)
        else:
            pr.customPrint("{:^100}".format(f"Antrian Kosong"), 'blue')
            print(pr.singleLine)

    def size(self):
        pr.customPrint("{:^100}".format(f"Panjang Antrian : {len(self.__items)}"), 'blue')
        print(pr.singleLine)

    def showData(self):
        pr.customPrint("{:^100}".format(f"Isi Antrian : {self.__items}"), 'blue')
        print(pr.singleLine)

    def main(self) -> None : 
        while True:
            pr.clearTerminal()
            pr.dynamicHeader("program konversi bentuk data")
            pr.dynamicSubHeader("Konversi menjadi Queue")
            pr.customPrint("{:<100}".format("1. Enqueue (Tambah data ke Antrian)"), 'blue')
            pr.customPrint("{:<100}".format("2. Dequeue (Hapus data teratas Antrian)"), 'blue')
            pr.customPrint("{:<100}".format("3. Peek (Lihat data depan Antrian)"), 'blue')
            pr.customPrint("{:<100}".format("4. Show (Lihat isi Antrian)"), 'blue')
            pr.customPrint("{:<100}".format("5. Size (Lihat Ukuran/Panjang Antrian)"), 'blue')
            pr.customPrint("{:<100}".format("0. Keluar Dari Program"), 'red')

            print(pr.singleLine)
            try:
                choice = str(input("Pilih operasi [1/2/3/4/5]: "))
                print(pr.singleLine)
                if choice == '1':
                    data = int(input("Masukkan data yang ingin dimasukkan ke stack: "))
                    print(pr.singleLine)
                    self.enqueue = data
                elif choice == '2':
                    self.dequeue()
                elif choice == '3':
                    self.peek()
                elif choice == '4':
                    self.showData()
                elif choice == '5':
                    self.size()
                elif choice == '0':
                    pr.customPrint("{:^100}".format("Keluar dari sub-program Queue..."), 'green')
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
