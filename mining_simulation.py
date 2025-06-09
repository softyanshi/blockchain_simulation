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

    def mine_block(self, difficulty):
        print(f"\nMining block with difficulty {difficulty}...")
        start = time.time()
        target = '0' * difficulty
        attempts = 0
        while self.hash[:difficulty] != target:
            self.nonce += 1
            attempts += 1
            self.hash = self.calculate_hash()
        end = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce attempts: {attempts}")
        print(f"Time taken: {end - start:.4f} seconds")

block = Block(0, time.ctime(), "Some data", "0")
block.mine_block(4)  # e.g., hash must start with '0000'
