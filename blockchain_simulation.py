import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Create genesis block
genesis_block = Block(0, time.ctime(), "Genesis Block", "0")

# Create second block
block1 = Block(1, time.ctime(), "Block 1 Data", genesis_block.hash)

# Create third block
block2 = Block(2, time.ctime(), "Block 2 Data", block1.hash)

# Chain
blockchain = [genesis_block, block1, block2]

# Display chain
for block in blockchain:
    print(f"Index: {block.index}\nData: {block.data}\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\n")

# Tamper with block1 data
print("--- Tampering Block 1 ---")
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()

# Display chain again
for block in blockchain:
    print(f"Index: {block.index}\nData: {block.data}\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\n")
