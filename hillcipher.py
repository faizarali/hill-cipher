# This program encrypts the alphabetic letters in a file using the Hill
# cipher where the Hill matrix can be any size from 2 x 2 up to 9 x 9.
import sys

try:
    # First command line parameter will be the "encryption key file".
    with open(sys.argv[1], 'r') as key_file:
        key = key_file.read().split()

    # Second command line parameter will be the file to be encrypted.
    with open(sys.argv[2], 'r') as plaintext_file:
        plaintext = plaintext_file.read().replace('\n', '').replace(' ', '')

    # Get the first integer from the key text file. This will determine the
    # size of our key matrix (it will be n by n dimensions).
    n = int(key[0])

except:
    print("You didn't include the correct command line arguments!")
    sys.exit(1)

print()
print()

print('Key matrix:')
print()

# Converts the rest of the key file into a 2d matrix.
key_matrix = key[1:]
key_matrix = [key_matrix[i:i+n] for i in range(0, len(key_matrix), n)]
key_matrix = [list(map(int, i)) for i in key_matrix]

# Prints the matrix to the terminal.
print('\n'.join(['  '.join([str(cell) for cell in row]) for row in key_matrix]))
print()
print()

# We only care about the alphabetic letters in our plaintext.
plaintext = ''.join(filter(str.isalpha, plaintext))

# Pad with X until plaintext is a multiple of key size.
while len(plaintext) % n != 0:
    # plaintext = plaintext + 'X'
    plaintext = ''.join([plaintext, 'X'])

# We are only dealing with lowercase letters for this program.
plaintext = plaintext.lower()

# This function will make sure our output is exactly 80 letters per row,
# except for the last row, which may possibly have fewer.
def printToConsole(text):
    count = 0
    for char in text:
        print(char, end='')
        # Put a newline when we print 80 characters.
        if (count + 1) % 80 == 0:
            print()
        count += 1
    print()

print('Plaintext:')
print()

printToConsole(plaintext)
print()
print()

print('Ciphertext:')
print()

# Making our encrypted string (aka our ciphertext).
def encrypt(plaintext):
    res = ""
    for i in range(0, len(plaintext), n):
        # res = res + encrypt_block(plaintext[i:i+n])
        res = ''.join([res, encrypt_block(plaintext[i:i+n])])
    return res

# Matrix Multiplication with the given block.
def encrypt_block(block):
    res = ['0'] * n
    for row in range(n):
        sum  = 0
        for col in range(n):
            sum += (key_matrix[row][col] * (ord(block[col]) - ord('a')))
        res[row] = chr(ord('a') + (sum % 26))
    return ''.join(res)

printToConsole(encrypt(plaintext))
