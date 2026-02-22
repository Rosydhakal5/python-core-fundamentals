# =================================================================
# PROJECT: SECRET AUCTION CLI
# AUTHOR:  ROSY DHAKAL
# PURPOSE: DEMONSTRATING PYTHON DICTIONARIES & INPUT CONTROL FLOW
# =================================================================

import os

def clear():
    """Utility to clear the terminal window based on Operating System."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Header Display ---
print("****************************************")
print("* SECRET AUCTION TERMINAL         *")
print("****************************************\n")

bids = {}
should_continue = True

# --- Data Collection Loop ---
while should_continue:
    name = input("Enter bidder name: ")
    
    # Input handling for bidding price
    try:
        price = int(input("Enter bidding price: $"))
    except ValueError:
        print("Error: Please enter a numeric value.")
        continue
    
    # Store data in dictionary
    bids[name] = price
    
    status = input("\nAre there any other players? (y/n): ").lower()
    
    if status == 'n':
        should_continue = False
    elif status == 'y':
        clear()

# --- Winner Calculation Logic ---
highest_bid = 0 
winner = ""

for bidding_name in bids:
    bid_amount = bids[bidding_name]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidding_name

# --- Final Results Output ---
clear()
print("========================================")
print("            AUCTION RESULTS             ")
print("========================================")
print(f"WINNER: {winner.upper()}")
print(f"FINAL BID: ${highest_bid}")
print("========================================\n")