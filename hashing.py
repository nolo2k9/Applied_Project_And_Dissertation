import hashlib
import json

"""
This will return a sha-256 hash of all the given arguements.
Implements imported sha-256 function from hashlib.
Turns our data into a byte string using utf-8.
By using the sorted() method, we prevent errors involving identical data giving
different results if the data becomes unsorted or jumbled.
"""
def crypto_hash(*args):
    # parse data args to a string using a lambda function
    stringified_args = sorted(map(lambda data: json.dumps(data), args))

    print(f'stringified_args: {stringified_args}')

    #join our args into a string
    joined_data = ''.join(stringified_args)

    print(f'joined_data: {joined_data}')

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest() # hash function

"""
Main method for testing expected results
"""
def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}") # the order is different but the data is the same, expected output should be the same


# this checks if we're directly running the file, and if so just run the main method.
if __name__ == '__main__':
    main()