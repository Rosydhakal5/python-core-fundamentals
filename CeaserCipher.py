# Welcome to Rosy Dhakal's Caesar Cipher! Ready to encode or decode your letters.
# Search Keywords: Rosy Dhakal, Python Caesar Cipher, Caesar Cipher Encryption/Decryption, Rosy Dhakal GitHub
# Author: Rosy Dhakal | Project: Caesar Cipher Python 

# NOTE: Optimized with a single unified 'ceaser' function to handle both 
# encoding and decoding through modular arithmetic and shift inversion.
# This replaces the need for separate encode/decode functions (DRY principle).

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(new_text, shift_position, selected_direction):
    # The "Toggle": If user chooses decode, we flip the shift to negative
    if selected_direction == "decode":
        shift_position *= -1
    cipher_text = ""
    for letter in new_text:
        if letter in alphabet:
            get_position = alphabet.index(letter)
            # Modular arithmetic handles wrapping around 0-25 perfectly
            new_position = (get_position + shift_position) % 26
            updated_text = alphabet[new_position]
            cipher_text += updated_text
        else:
            # Keeps spaces, numbers, or symbols as they are
            cipher_text += letter
    print(f"Your Cipher Code is {cipher_text}\n")

# --- Application Entry Point ---
should_continue = True

while should_continue:
    # Gather user requirements
    direction = input("Would you like to encode or decode a message? :\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Execute the core logic
    ceaser(new_text=text, shift_position=shift, selected_direction=direction)
    
    # Control flow for repeating the program
    restart = input("Would you like to continue? Y or N? \n: ").lower()
    if restart == "y":
        should_continue = True
    else:
        should_continue = False
        print("We Hope You Enjoyed the Encryption/Decryption, GoodBye 🙏🎉")
        
# --- PORTFOLIO NOTE: LEGACY CODE PRESERVED FOR VERSION HISTORY ---
# # Creating a function that takes text and shift as an input for encoding
# def encode(new_text, new_shift):
#     cipher_text = ""
#     for letter in new_text:
#         # Check if character is in alphabet to avoid crashing on spaces/symbols
#         if letter in alphabet:
#             get_position = alphabet.index(letter)
#             # % 26 ensures if shift > 26 it wraps around without crashing
#             new_position = (get_position + new_shift) % 26 
#             encode_word = alphabet[new_position]
#             cipher_text += encode_word
#         else:
#             # Keeps spaces or numbers as they are
#             cipher_text += letter
            
#     print(f"Your cipher code is {cipher_text}")

# # Creating a function that takes text and shift as an input for decoding
# def decode(provided_text, shift_history):
#     cipher_decode = ""
#     for letter in provided_text:
#         # Check if character is in alphabet to avoid crashing on spaces/symbols
#         if letter in alphabet:
#             find_position = alphabet.index(letter)
#             # % 26 handles negative shifts automatically to wrap around the alphabet
#             change_position = (find_position - shift_history) % 26
#             original_position = alphabet[change_position]
#             cipher_decode += original_position
#         else:
#             # Keeps spaces or numbers as they are
#             cipher_decode += letter
            
#     print(f"Your decoded message is {cipher_decode}")

# # Directing the user input to the correct function based on choice
# if direction == "encode":
#      encode(new_text=text, new_shift=shift)
# elif direction == "decode":
#      decode(provided_text=text, shift_history=shift)
# else:
#      print("Please enter a valid direction (encode/decode).")