"""
This class's function is for converting our hex data into a binary format.
The idea is that it solves the problem of the hash function generating hash values that are too easy for the CPU to solve.
i.e. a powerful CPU might mine blocks too fast.
"""

# Dictionary of hex keys
# to convert hex to its equivalent binary
HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

"""
Our conversion method
"""
def hex_to_binary(hex_string):
    binary_string = '' # result

    # loop through dictionary and find relevant character
    # then add it to binary_string
    for character in hex_string:
        binary_string += HEX_TO_BINARY_CONVERSION_TABLE[character]

    return binary_string

"""
Testing with output
"""
def main():
    number = 555
    hex_number = hex(number) # 'hex' returns the hex of our int
    print(f'hex_number: {hex_number}')

if __name__ == '__main__':
    main()