import turtle

class Graph:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.t.pensize(2)
        self.screen = turtle.Screen()
        self.screen.title("Graf Persegi Panjang dengan Diagonal (e5)")

        # Koordinat simpul secara manual untuk meniru bentuk gambar
        self.positions = {
            'A': (-150, 100),
            'B': (-150, -100),
            'C': (150, -100),
            'D': (150, 100)
        }

        # Daftar edge dan label
        self.edges = [
            ('A', 'B', 'e1'),
            ('B', 'C', 'e2'),
            ('A', 'D', 'e3'),
            ('C', 'D', 'e4'),
            ('B', 'D', 'e5')  # diagonal
        ]

    def gambar_edge(self, node1, node2, label):
        x1, y1 = self.positions[node1]
        x2, y2 = self.positions[node2]

        # Gambar garis
        self.t.penup()
        self.t.goto(x1, y1)
        self.t.pendown()
        self.t.goto(x2, y2)

        # Hitung posisi tengah untuk label edge
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        # Geser label sedikit agar tidak menabrak garis
        offset = 10 if label != "e5" else -15
        self.t.penup()
        self.t.goto(mid_x, mid_y + offset)
        self.t.write(label, align="center", font=("Arial", 10, "normal"))

    def gambar_node(self, label, pos):
        x, y = pos
        self.t.penup()
        self.t.goto(x, y - 10)
        self.t.pendown()
        self.t.fillcolor("lightblue")
        self.t.begin_fill()
        self.t.circle(15)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(x, y + 5)
        self.t.write(label, align="center", font=("Arial", 12, "bold"))

    def gambar_graph(self):
        # Gambar semua edge
        for node1, node2, label in self.edges:
            self.gambar_edge(node1, node2, label)

        # Gambar semua simpul
        for label, pos in self.positions.items():
            self.gambar_node(label, pos)

        self.screen.exitonclick()

# Program utama
if __name__ == "__main__":
    g = Graph()
    g.gambar_graph()







