
# Secret Auction CLI module by Rosy Dhakal demonstrating Python loops, dictionary storage, and input-driven control flow.

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal (Windows/Mac/Linux)

print("Welcome to the Secret Auction")

runAgain = True
bids = {}  # Store bidder data

while runAgain:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    moreBidders = input("is there any more bidders Y or N? \n: ").lower()

    bids["name"] = name   # Save name (overwrites each loop for now)
    bids["price"] = price # Save bid (overwrites each loop for now)

    if moreBidders == 'n':
        runAgain = False  # Exit loop

    clear()  # Clear screen for next bidder

print(bids)  # Display final bids dictionary
