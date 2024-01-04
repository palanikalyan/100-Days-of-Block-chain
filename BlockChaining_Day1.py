import hashlib
import time
import json
from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, ttk, END, Frame

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = f"{index}{previous_hash}{timestamp}{data}"
    return hashlib.sha256(value.encode()).hexdigest()

class BlockchainApp:
    def __init__(self, master):
        self.master = master
        master.title("Blockchain")
        master.geometry("500x400")

        self.blocks = []
        self.current_data = ""

        self.label = Label(master, text="Blockchain", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.entry_label = Label(master, text="Data:", font=("Helvetica", 12))
        self.entry_label.pack()

        self.entry = Entry(master, width=50, font=("Helvetica", 12))
        self.entry.pack()

        self.add_block_button = Button(master, text="Add Block", command=self.add_block, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.add_block_button.pack(pady=10)

        self.view_blockchain_button = Button(master, text="View Blockchain", command=self.view_blockchain, font=("Helvetica", 12), bg="#2196F3", fg="white")
        self.view_blockchain_button.pack(pady=10)

        self.frame = Frame(master)
        self.frame.pack()

        self.text = Text(self.frame, height=10, width=50, wrap="word", font=("Helvetica", 10))
        self.text.pack(side="left")

        self.scrollbar = Scrollbar(self.frame, command=self.text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=self.scrollbar.set)

    def add_block(self):
        index = len(self.blocks)
        previous_hash = self.blocks[-1].hash if self.blocks else "0"
        timestamp = time.time()
        data = self.entry.get()
        current_hash = calculate_hash(index, previous_hash, timestamp, data)

        new_block = Block(index, previous_hash, timestamp, data, current_hash)
        self.blocks.append(new_block)

        self.current_data = ""
        self.entry.delete(0, END)

    def view_blockchain(self):
        self.text.delete(1.0, END)
        for block in self.blocks:
            block_info = f"Index: {block.index}\nPrevious Hash: {block.previous_hash}\nTimestamp: {block.timestamp}\nData: {block.data}\nHash: {block.hash}\n\n"
            self.text.insert(END, block_info)

if __name__ == "__main__":
    root = Tk()
    app = BlockchainApp(root)
    root.mainloop()
