import hashlib

class Block:
    def __init__(self, index, previous_hash, data, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.previous_hash) + str(self.data) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

def validate_block(block, previous_block):
    # Verify block index continuity
    if block.index != previous_block.index + 1:
        return False

    # Verify block integrity
    if block.previous_hash != previous_block.hash:
        return False

    # Verify block hash
    if block.hash != block.calculate_hash():
        return False

    return True

# Example usage
block1 = Block(1, "previous_hash_1", "Data 1", 1234)
block2 = Block(2, block1.hash, "Data 2", 5678)

# Validate block2 against block1
if validate_block(block2, block1):
    print("Block 2 is valid.")
else:
    print("Block 2 is not valid.")
