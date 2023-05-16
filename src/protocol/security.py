import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

def calculate_hash(index, previous_hash, timestamp, data, nonce):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(nonce)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block", 0), 0)

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    nonce = mine_block(previous_block, data)
    hash = calculate_hash(index, previous_block.hash, timestamp, data, nonce)
    return Block(index, previous_block.hash, timestamp, data, hash, nonce)

def mine_block(previous_block, data):
    target_difficulty = 4  # Adjust the difficulty as needed

    # Prepare the initial value for the nonce
    nonce = 0

    # Find a nonce value that results in a hash with the required number of leading zeros
    while True:
        hash = calculate_hash(previous_block.index + 1, previous_block.hash, time.time(), data, nonce)
        if hash.startswith("0" * target_difficulty):
            return nonce
        nonce += 1

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Number of blocks to add
num_blocks_to_add = 5

# Generate and add new blocks to the blockchain
for i in range(num_blocks_to_add):
    new_block_data = f"Block #{i+1}"
    new_block = create_new_block(previous_block, new_block_data)
    blockchain.append(new_block)
    previous_block = new_block

# Print the blockchain
for block in blockchain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Nonce: {block.nonce}")
    print("")
