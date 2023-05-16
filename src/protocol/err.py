import hashlib
import time

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

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

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

# Function to validate the integrity of the blockchain
def validate_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]

        # Check if the block index is correct
        if current_block.index != previous_block.index + 1:
            raise Exception(f"Invalid block index for block #{current_block.index}")

        # Check if the previous hash is correct
        if current_block.previous_hash != previous_block.hash:
            raise Exception(f"Invalid previous hash for block #{current_block.index}")

        # Check if the block's hash is correct
        hash = calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data)
        if current_block.hash != hash:
            raise Exception(f"Invalid hash for block #{current_block.index}")

    print("Blockchain is valid.")

# Validate the blockchain
try:
    validate_blockchain(blockchain)
except Exception as e:
    print("Blockchain is invalid.")
    print(e)
