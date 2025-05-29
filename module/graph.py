class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_simpul(self, simpul):
        if simpul not in self.graph:
            self.graph[simpul] = []

    def tambah_sisi(self, dari, ke):
        self.tambah_simpul(dari)
        self.tambah_simpul(ke)
        if ke not in self.graph[dari]:
            self.graph[dari].append(ke)
        if dari not in self.graph[ke]:
            self.graph[ke].append(dari)   # Jika graf tidak berarah

    def buat_dari_list(self, data_list):
        for pasangan in data_list:
            if len(pasangan) == 2:
                self.tambah_sisi(pasangan[0], pasangan[1])

    def tampilkan_graph(self):
        for simpul, tetangga in self.graph.items():
            print(f"{simpul} -> {tetangga}")

# Program utama
if __name__ == "__main__":
    # Data relasi dalam bentuk list
    data = [
        ['A', 'B'],
        ['A', 'C'],
        ['B', 'D'],
        ['C', 'D'],
        ['D', 'E']
    ]

    g = Graph()
    g.buat_dari_list(data)
    print("Graf dari list data:")
    g.tampilkan_graph()







