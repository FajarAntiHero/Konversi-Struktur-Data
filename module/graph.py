from .property import Property as pr

class TreeNode:
    """Representasi sebuah node dalam Graph Tree."""
    def __init__(self, data):
        self.data = data
        self.children = [] # Daftar anak-anak node ini

    def add_child(self, child_node):
        """Menambahkan node anak ke node saat ini."""
        if not isinstance(child_node, TreeNode):
            raise ValueError("Child must be a TreeNode instance.")
        self.children.append(child_node)

    def __repr__(self, level=0):
        """Representasi string rekursif untuk node dan anak-anaknya."""
        ret = "  " * level + f"- {self.data}\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

class GraphTree:
    """Implementasi dasar Graph Tree."""
    def __init__(self, initial_data: list = None):
        self.__root = None
        self.__nodes = {} # Untuk menyimpan referensi node berdasarkan data, memudahkan pencarian

        if initial_data:
            pr.customPrint("{:^100}".format("Membangun Pohon dari Data Awal..."), 'yellow')
            pr.customPrint("{:^100}".format("Untuk Tree yang lebih kompleks, gunakan opsi menu."), 'yellow')
            pr.pauseProgram(2)
            # Kita bisa menginterpretasikan data awal sebagai hirarki sederhana
            # Misalnya, elemen pertama adalah root, sisanya adalah anak-anak level 1
            if initial_data:
                self.__root = TreeNode(initial_data[0])
                self.__nodes[initial_data[0]] = self.__root
                for item in initial_data[1:]:
                    child_node = TreeNode(item)
                    self.__root.add_child(child_node)
                    self.__nodes[item] = child_node
            
    def get_root(self):
        """Mengembalikan node akar pohon."""
        return self.__root

    def add_node_to_parent(self, parent_data, child_data):
        """Menambahkan node anak ke node induk yang sudah ada."""
        parent_node = self.__nodes.get(parent_data)
        if parent_node:
            if child_data not in self.__nodes: # Hanya tambahkan jika child_data belum ada
                child_node = TreeNode(child_data)
                parent_node.add_child(child_node)
                self.__nodes[child_data] = child_node
                pr.customPrint("{:^100}".format(f"Ditambahkan [{child_data}] sebagai anak dari [{parent_data}]"), 'blue')
            else:
                pr.customPrint("{:^100}".format(f"Data anak [{child_data}] sudah ada dalam pohon."), 'red')
        else:
            pr.customPrint("{:^100}".format(f"Induk [{parent_data}] tidak ditemukan."), 'red')
        print(pr.singleLine)

    def find_node(self, data):
        """Mencari node berdasarkan data dan mengembalikan node tersebut."""
        node = self.__nodes.get(data)
        if node:
            pr.customPrint("{:^100}".format(f"Node dengan data [{data}] ditemukan."), 'blue')
        else:
            pr.customPrint("{:^100}".format(f"Node dengan data [{data}] tidak ditemukan."), 'red')
        print(pr.singleLine)
        return node
    
    def show_tree(self):
        """Menampilkan struktur pohon secara visual."""
        if self.__root:
            pr.customPrint("{:^100}".format("Struktur Graph Tree:"), 'green')
            print(self.__root) # Memanggil __repr__ dari root node
        else:
            pr.customPrint("{:^100}".format("Pohon kosong."), 'red')
        print(pr.singleLine)

    def main(self):
        while True:
            pr.clearTerminal()
            pr.dynamicHeader("PROGRAM KONVERSI BENTUK DATA")
            pr.dynamicSubHeader("KONVERSI MENJADI GRAPH TREE")
            
            # Tampilkan pohon saat ini
            if self.__root:
                pr.customPrint("{:^100}".format("Pohon Saat Ini:"), 'cyan')
                print(self.__root)
                print(pr.singleLine)
            else:
                pr.customPrint("{:^100}".format("Pohon belum dibuat. Silakan tambahkan Root/Node."), 'yellow')
                print(pr.singleLine)

            pr.customPrint("{:<100}".format("1. Tambah Node (Root/Child)"), 'blue')
            pr.customPrint("{:<100}".format("2. Cari Node"), 'blue')
            pr.customPrint("{:<100}".format("3. Tampilkan Pohon"), 'blue')
            pr.customPrint("{:<100}".format("0. Keluar Dari Program"), 'red')
            print(pr.singleLine)

            try:
                choice = str(input("Pilih operasi [1/2/3/0]: "))
                print(pr.singleLine)

                if choice == '1':
                    if not self.__root:
                        try:
                            root_data = int(input("Masukkan data untuk Node Root (angka): "))
                            self.__root = TreeNode(root_data)
                            self.__nodes[root_data] = self.__root
                            pr.customPrint("{:^100}".format(f"Node Root [{root_data}] berhasil dibuat."), 'green')
                        except ValueError:
                            pr.customPrint("{:^100}".format("Input tidak valid! Harap masukkan angka untuk Root."), 'red')
                    else:
                        try:
                            parent_data = int(input("Masukkan data Node Induk (yang sudah ada): "))
                            child_data = int(input("Masukkan data Node Anak yang akan ditambahkan: "))
                            self.add_node_to_parent(parent_data, child_data)
                        except ValueError:
                            pr.customPrint("{:^100}".format("Input tidak valid! Harap masukkan angka."), 'red')
                    pr.pauseProgram(2)

                elif choice == '2':
                    if not self.__root:
                        pr.customPrint("{:^100}".format("Pohon kosong. Tidak ada yang bisa dicari."), 'red')
                        pr.pauseProgram(2)
                        continue
                    try:
                        search_data = int(input("Masukkan data Node yang ingin dicari: "))
                        self.find_node(search_data)
                    except ValueError:
                        pr.customPrint("{:^100}".format("Input tidak valid! Harap masukkan angka."), 'red')
                    pr.pauseProgram(2)

                elif choice == '3':
                    self.show_tree()
                    pr.pauseProgram(3) # Beri waktu untuk melihat pohon
                    
                elif choice == '0':
                    pr.customPrint("{:^100}".format("Keluar dari sub-program Graph Tree..."), 'green')
                    pr.pauseProgram(1)
                    break
                else:
                    pr.customPrint("{:^100}".format("Pilihan tidak valid!"), 'red')
                    pr.pauseProgram(2)

            except ValueError: # Catch all ValueErrors from input
                pr.customPrint("{:^100}".format("Input tidak valid! Harap masukkan angka untuk pilihan menu."), 'red')
                pr.pauseProgram(2)

            is_continue = str(input("{:<50}".format("Lanjutkan Mengubah Data? [Y/N] : ")))
            if is_continue == "N" or is_continue == "n":
                break
            elif is_continue == "Y" or is_continue == "y":
                continue
            else:
                print("{:^100}".format("Input Data Tidak Sesuai!".upper()))