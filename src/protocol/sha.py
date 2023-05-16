import hashlib

def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    return sha256.hexdigest()

# Example usage
data = "Hello, blockchain!"
hash_value = calculate_hash(data)
print(f"Data: {data}")
print(f"SHA-256 Hash: {hash_value}")
