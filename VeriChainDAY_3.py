import hashlib
import time
import tkinter as tk
from tkinter import ttk

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_block(index, previous_block, data):
    timestamp = time.time()
    previous_hash = previous_block.hash
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash)

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def add_block(self, data):
        index = len(self.chain)
        previous_block = self.chain[-1]
        new_block = create_block(index, previous_block, data)
        self.chain.append(new_block)

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the previous block is correct
            if current_block.previous_hash != previous_block.hash:
                return False

            # Check if the current block's hash is correct
            if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

        return True

def print_blockchain(chain):
    for block in chain:
        print("Index:", block.index)
        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Hash:", block.hash)
        print("Previous Hash:", block.previous_hash)
        print("-" * 30)

class VeriChainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VeriChain")

        self.blockchain = Blockchain()

        self.menu_frame = ttk.Frame(root, padding="10")
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        self.add_block_button = ttk.Button(self.menu_frame, text="Add Block", command=self.add_block)
        self.add_block_button.grid(row=0, column=0, padx=5, pady=5)

        self.view_blockchain_button = ttk.Button(self.menu_frame, text="View Blockchain", command=self.view_blockchain)
        self.view_blockchain_button.grid(row=0, column=1, padx=5, pady=5)

        self.verify_blockchain_button = ttk.Button(self.menu_frame, text="Verify Blockchain", command=self.verify_blockchain)
        self.verify_blockchain_button.grid(row=0, column=2, padx=5, pady=5)

    def add_block(self):
        data = tk.simpledialog.askstring("Add Block", "Enter transaction data:")
        if data is not None:
            self.blockchain.add_block(data)
            tk.messagebox.showinfo("Success", "Block added successfully!")

    def view_blockchain(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("VeriChain Blockchain")

        blockchain_text = tk.Text(view_window, wrap="none")
        blockchain_text.insert("1.0", self.format_blockchain())
        blockchain_text.pack(expand=True, fill="both")

    def verify_blockchain(self):
        if self.blockchain.verify_chain():
            tk.messagebox.showinfo("Verification", "Blockchain is valid.")
        else:
            tk.messagebox.showwarning("Verification", "Blockchain is not valid.")

    def format_blockchain(self):
        result = ""
        for block in self.blockchain.chain:
            result += f"Index: {block.index}\n"
            result += f"Timestamp: {block.timestamp}\n"
            result += f"Data: {block.data}\n"
            result += f"Hash: {block.hash}\n"
            result += f"Previous Hash: {block.previous_hash}\n"
            result += "-" * 30 + "\n"
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = VeriChainApp(root)
    root.mainloop()
