class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getnext()
        return count

    def show(self):
        current = self.head
        print("Head ->", end=" ")
        while current is not None:
            print(current.getdata(), end=" -> ")
            current = current.getnext()
        print("None")

    def search(self):
        current = self.head
        s = input("Masukkan data yang akan dicari: ")
        found = False
        while current is not None:
            if current.getdata() == s:
                found = True
                break
            current = current.getnext()
        if found:
            print("Data ditemukan!")
        else:
            print("Data tidak ditemukan!")

    def remove(self):
        current = self.head
        s = input("Masukkan data yang akan dihapus: ")
        found = False
        previous = None
        while current is not None:
            if current.getdata() == s:
                found = True
                break
            previous = current
            current = current.getnext()

        if found:
            if previous is None:
                self.head = current.getnext()
            else:
                previous.setnext(current.getnext())
            print("Data sudah dihapus")
        else:
            print("Data yang akan dihapus tidak ditemukan!")

    def ganjil(self, item):
        ol = OrderedList()
        for i in range(len(item)):
            if int(item[i]) % 2 != 0:
                ol.add(str(item[i]))
        return ol

    def genap(self, item):
        ol = OrderedList()
        for i in range(len(item)):
            if int(item[i]) % 2 == 0:
                ol.add(str(item[i]))
        return ol

    def sort(self, item):
        for i in range(len(item) - 1, 0, -1):
            for j in range(i):
                if int(item[j]) > int(item[j+1]):
                    item[j], item[j+1] = item[j+1], item[j]
        return item

    def tambahlist(self, item):
        pl = OrderedList()
        for i in range(len(item)):
            pl.add(str(item[i]))
        return pl


# =============================
# MAIN PROGRAM
# =============================

ol = OrderedList()

while True:
    tam = input("Masukkan data: ")
    ol.add(tam)
    lagi = input("Apakah Anda mau memasukkan data lagi? [Y/T]: ")
    if lagi.upper() != 'Y':
        break

print("\nData dalam linked list:")
ol.show()
print(f"Panjang datanya adalah: {ol.size()}")

# Contoh data tambahan
ls = [
    '111001', '110001', '1110002', '1110003', '1110004',
    '1110005', '1110006', '1110007', '1110008', '1110009'
]

# Pemisahan ganjil/genap
ganjil = ol.ganjil(ls)
genap = ol.genap(ls)

# Gabungkan list
merge = ganjil
current = genap.head
while current is not None:
    merge.add(current.getdata())
    current = current.getnext()

print("\nData setelah digabung:")
merge.show()

# Urutkan data
sorted_list = ol.sort(ls)
print("\nData setelah disortir:")
print(sorted_list)

# Tambahkan list hasil sort ke linked list baru
sorted_linked = ol.tambahlist(sorted_list)
print("\nLinked list dari data yang disortir:")
sorted_linked.show()
