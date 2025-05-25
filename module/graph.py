import turtle
import math

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes              # List of node labels, e.g. ['A', 'B', 'C', 'D']
        self.edges = edges              # List of tuple edges, e.g. [('A', 'B'), ('A', 'C')]
        self.node_pos = {}             # Posisi node di layar
        self.radius = 200              # Radius lingkaran tata letak
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.t.pensize(2)
        self.screen = turtle.Screen()
        self.screen.title("Visualisasi Graph (Teori Graf)")

    def atur_posisi_node(self):
        # Menempatkan node secara melingkar
        sudut_total = 360
        sudut_per_node = sudut_total / len(self.nodes)
        for i, node in enumerate(self.nodes):
            sudut = math.radians(sudut_per_node * i)
            x = self.radius * math.cos(sudut)
            y = self.radius * math.sin(sudut)
            self.node_pos[node] = (x, y)

    def gambar_edges(self):
        for node1, node2 in self.edges:
            x1, y1 = self.node_pos[node1]
            x2, y2 = self.node_pos[node2]
            self.t.penup()
            self.t.goto(x1, y1)
            self.t.pendown()
            self.t.goto(x2, y2)

    def gambar_nodes(self):
        for node, (x, y) in self.node_pos.items():
            self.t.penup()
            self.t.goto(x, y - 10)  # supaya lingkaran pas di tengah
            self.t.pendown()
            self.t.fillcolor("lightblue")
            self.t.begin_fill()
            self.t.circle(20)
            self.t.end_fill()
            self.t.penup()
            self.t.goto(x, y + 5)
            self.t.write(node, align="center", font=("Arial", 12, "bold"))

    def gambar_graph(self):
        self.atur_posisi_node()
        self.gambar_edges()
        self.gambar_nodes()
        self.screen.exitonclick()

# Program utama
if __name__ == "__main__":
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
    
    g = Graph(nodes, edges)
    g.gambar_graph()











