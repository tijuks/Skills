import hashlib

def hash_data(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

# Example:
# hash_val = hash_data(b"important database record")