import tkinter as tk
import random

def generate_card():
    card = {}
    ranges = {'B': (1, 15), 'I': (16, 30), 'N': (31, 45), 'G': (46, 60), 'O': (61, 75)}
    for col, (start, end) in ranges.items():
        card[col] = random.sample(range(start, end + 1), 5)
    card['N'][2] = 'Free'
    return card

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingo Card')
        self.selected = set()
        self.card = generate_card()
        self.create_widgets()

    def create_widgets(self):
        for row in range(5):
            for col, letter in enumerate("Bingo"):
                number = self.card[letter][row]
                cell = tk.Button(self.root, text=str(number), width=5, height=2, command=lambda r=row, c=col: self.select_number(r, c))
                cell.grid(row=row, column=col)

    def select_number(self, row, col):
        pass

    def check_bingo(self):
        pass

root = tk.TK()
app = BingoApp(root)
root.mainloop()