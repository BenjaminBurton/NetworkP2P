import hashlib

class Block:
    def __init__(self, index, previous_hash, data, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.previous_hash) + str(self.data) + str(self.difficulty) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self):
        target = "0" * self.difficulty

        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return "Block: " + str(self.index) + ", Hash: " + str(self.hash) + ", Difficulty: " + str(self.difficulty)

# Example usage
block1 = Block(1, "previous_hash_1", "Data 1", 4)
block1.mine_block()
print(block1)

block2 = Block(2, block1.hash, "Data 2", 5)
block2.mine_block()
print(block2)
