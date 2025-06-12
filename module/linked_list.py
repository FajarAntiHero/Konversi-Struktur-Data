from .property import Property as pr

class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getdata(self):
        return self.__data

    def getnext(self):
        return self.__next

    def setdata(self, newdata):
        self.__data = newdata

    def setnext(self, newnext):
        self.__next = newnext


class LinkedList:
    def __init__(self, data = 0):
        self.__head = None
        self.__data = data

    def isEmpty(self):
        return self.__head is None

    def add(self, item):
        temp: Node = Node(item)
        temp.setnext(self.__head)
        self.__head = temp
        pr.customPrint("{:^100}".format(f"Data [{item}] telah ditambahkan ke Linked List"), 'blue')
        print(pr.singleLine)

    def size(self):
        current = self.__head
        count = 0
        while current is not None:
            count += 1
            current = current.getnext()
        pr.customPrint("{:^100}".format(f"Panjang Data pada Linked List : {count}"), 'blue')
        print(pr.singleLine)

    def show(self):
        current = self.__head
        pr.customPrint("Head", "blue", end="")
        pr.customPrint(" -> ", "green", end="")
        while current is not None:
            pr.customPrint(current.getdata(), "blue", end="")
            pr.customPrint(" -> ", "green", end="")
            current = current.getnext()
        pr.customPrint("None", "blue")
        print(pr.singleLine)

    def search(self, data):
        current = self.__head
        found = False
        while current is not None:
            if current.getdata() == data:
                found = True
                break
            current = current.getnext()
        if found:
            pr.customPrint("{:^100}".format(f"Data Ditemukan!"), 'blue')
            print(pr.singleLine)
        else:
            pr.customPrint("{:^100}".format(f"Data Tidak Ditemukan!"), 'blue')
            print(pr.singleLine)

    def remove(self, data):
        current = self.__head
        found = False
        previous = None
        while current is not None:
            if current.getdata() == data:
                found = True
                break
            previous = current
            current = current.getnext()

        if found:
            if previous is None:
                self.__head = current.getnext()
            else:
                previous.setnext(current.getnext())
            pr.customPrint("{:^100}".format(f"Data [{data}] sudah dihapus"), 'blue')
            print(pr.singleLine)
        else:
            pr.customPrint("{:^100}".format(f"Data Tidak Ditemukan!"), 'blue')
            print(pr.singleLine)
    
    # def sort(self, item):
    #     for i in range(len(item) - 1, 0, -1):
    #         for j in range(i):
    #             if int(item[j]) > int(item[j+1]):
    #                 item[j], item[j+1] = item[j+1], item[j]
    #     return item

    # def ganjil(self, item):
    #     ol = LinkedList()
    #     for i in range(len(item)):
    #         if int(item[i]) % 2 != 0:
    #             ol.add(str(item[i]))
    #     return ol

    # def genap(self, item):
    #     ol = LinkedList()
    #     for i in range(len(item)):
    #         if int(item[i]) % 2 == 0:
    #             ol.add(str(item[i]))
    #     return ol


    # def tambahlist(self, item):
    #     pl = LinkedList()
    #     for i in range(len(item)):
    #         pl.add(str(item[i]))
    #     return pl
    
    def main(self):
        if len(self.__data) > 1:
            for iterator in self.__data:
                self.add(iterator)

        while True:            
            pr.clearTerminal()
            pr.dynamicHeader("program konversi bentuk data")
            pr.dynamicSubHeader("Konversi menjadi Linked List")
            pr.customPrint("{:<100}".format("1. Add (Tambah data ke Linked List)"), 'blue')
            pr.customPrint("{:<100}".format("2. Search (Cari Data Pada Linked List)"), 'blue')
            # pr.customPrint("{:<100}".format("3. Sort (Urutkan Data Linked List)"), 'blue')
            pr.customPrint("{:<100}".format("3. Remove (Hapus Data Pada Linked List)"), 'blue')
            pr.customPrint("{:<100}".format("4. Show (Lihat Ukuran Linked List)"), 'blue')
            pr.customPrint("{:<100}".format("5. Size (Lihat Panjang Data Linked List)"), 'blue')

            print(pr.singleLine)

            try:
                choice = str(input("Pilih operasi [1/2/3/4/5]: "))
                print(pr.singleLine)
                if choice == '1':
                    data: int = int(input("Masukkan data yang ingin dimasukkan ke Linked List: "))
                    print(pr.singleLine)
                    self.add(data)
                elif choice == '2':
                    data: int = int(input("Masukkan data yang ingin dicari: "))
                    print(pr.singleLine)
                    self.search(data)
                # elif choice == '3':
                #     self.sort()
                elif choice == '3':
                    data: int = int(input("Masukkan data yang ingin dihapus: "))
                    print(pr.singleLine)
                    self.remove(data)
                elif choice == '4':
                    self.show()
                elif choice == '5':
                    self.size()
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
