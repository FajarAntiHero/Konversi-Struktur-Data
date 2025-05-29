class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f'Pushed: {item}')

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f'Popped: {popped_item}')
            return popped_item
        else:
            print('Stack is empty!')

    def peek(self):
        if not self.is_empty():
            print(f'Top item: {self.items[-1]}')
            return self.items[-1]
        else:
            print('Stack is empty!')

    def size(self):
        return len(self.items)

    def display(self):
        print('Stack:', self.items)

def menu():
    print("\nStack Operations Menu")
    print("1. Push (Tambah data ke stack)")
    print("2. Pop (Hapus data teratas stack)")
    print("3. Peek (Lihat data teratas stack)")
    print("4. Lihat isi stack")
    print("5. Ukuran stack")
    print("6. Keluar")

def main():
    stack = Stack()
    while True:
        menu()
        choice = input("Pilih operasi (1-6): ")
        
        if choice == '1':
            data = input("Masukkan data yang ingin dimasukkan ke stack: ")
            stack.push(data)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print(f'Ukuran stack: {stack.size()}')
        elif choice == '6':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()
