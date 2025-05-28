class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Menambahkan item ke belakang antrian
        print(f"'{item}' berhasil ditambahkan ke antrian.")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)  # Menghapus item dari depan antrian (FIFO)
            print(f"'{removed}' telah dihapus dari antrian.")
            return removed
        else:
            print("Antrian kosong, tidak ada data untuk dihapus.")

    def peek(self):
        if not self.is_empty():
            print(f"Data di depan antrian adalah: '{self.items[0]}'")
            return self.items[0]
        else:
            print("Antrian kosong.")

    def size(self):
        print(f"Ukuran antrian saat ini: {len(self.items)}")
        return len(self.items)

def main():
    queue = Queue()

    while True:
        print("\nMenu Queue (FIFO):")
        print("1. Tambah data ke antrian (enqueue)")
        print("2. Hapus data dari antrian (dequeue)")
        print("3. Lihat data depan antrian (peek)")
        print("4. Lihat ukuran antrian")
        print("5. Keluar")

        choice = input("Masukkan pilihan Anda (1-5): ")

        if choice == '1':
            data = input("Masukkan data yang ingin dimasukkan ke antrian: ")
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            queue.size()
        elif choice == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
main()