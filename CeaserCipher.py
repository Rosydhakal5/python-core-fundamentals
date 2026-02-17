#Welcome to Rosy Dhakal's Caesar Cipher! Ready to encode your letters.
# Search Keywords: Rosy Dhakal, Python Caesar Cipher, Caesar Cipher Encryption, Rosy Dhakal GitHub
# Author: Rosy Dhakal | Project: Caesar Cipher Python Tool 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Creating a function that takes text and shift as an input 
def encode(new_text, new_shift):
    cipher_text = ""
    for letter in new_text:
        # Check if character is in alphabet to avoid crashing on spaces/symbols
        if letter in alphabet:
            get_position = alphabet.index(letter)
            # % 26 ensures if shift > 26 it wraps around without crashing
            new_position = (get_position + new_shift) % 26 
            encode_word = alphabet[new_position]
            cipher_text += encode_word
        else:
            # Keeps spaces or numbers as they are
            cipher_text += letter
            
    print(f"Your cipher code is {cipher_text}")

# Calling the function using keyword arguments
encode(new_text=text, new_shift=shift)