import hashlib 

"""
This will return a sha-256 hash of a given data
Implements imported sha-256 function from hashlib
"""
def crypto_hash(data):
    return hashlib.sha256(data) # hash function

"""
Main method for testing expected results
"""
def main():
    print(f"crypto_hash('test'): {crypto_hash('test')}")


# this checks if we're directly running the file, and if so just run the main method.
if __name__ == '__main__':
    main()