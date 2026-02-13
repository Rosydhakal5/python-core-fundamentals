import random

# List of hangman stages from empty to full (Index 0 = start, 6 = complete hangman)
stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

# Initial empty gallows before any wrong guesses
initial = '''
  +---+
      |
      |
      |
      |
      |
=========
'''

# List of possible words for the game
word_list = [
    "nepal", "india", "china", "japan", "brazil", "canada", "egypt", "france", 
    "spain", "italy", "peru", "mexico", "chile", "ghana", "kenya", "fiji", 
    "cuba", "oman", "iran", "iraq", "mali", "chad", "laos", "togo", "jordan",
    "qatar", "yemen", "sudan", "libya", "benin", "gabon", "haiti", "malta",
    "thailand", "vietnam", "germany", "greece", "norway", "sweden", "poland",
    "turkey", "russia", "korea", "austria", "belgium", "denmark", "finland",
    "ireland", "hungary", "iceland", "algeria", "morocco", "nigeria", "uganda",
    "zambia", "angola", "bolivia", "ecuador", "guyana", "uruguay", "panama",
    "belize", "jamaica", "bahamas", "monaco", "cyprus", "georgia", "armenia",
    "israel", "kuwait", "lebanon", "bhutan", "myanmar", "taiwan", "brunei",
    "namibia", "senegal", "tunisia", "eritrea", "liberia", "romania", "serbia",
    "albania", "croatia", "estonia", "latvia", "ukraine", "belarus", "andorra",
    "portugal", "bulgaria", "slovakia", "slovenia", "paraguay", "suriname",
    "colombia", "venezuela", "pakistan", "mongolia", "australia"
]

# Randomly select a word for this round
selected_word = random.choice(word_list)
length = len(selected_word)

# Create a display list with underscores for each letter
display = []
for _ in range(length):
 display += "_"
print(display)

# Show the initial empty gallows
print(initial)

# Initialize the number of wrong guesses
lives = 0

# List to keep track of letters the user has already guessed
userInput = []

# Game loop runs until the game ends
end_of_game = False
while not end_of_game:
    # Ask user for a letter and convert to lowercase
    guess = input("\nenter a letter\n ").lower()
    
    # Check if guessed letter is in the selected word and reveal it
    for i in range(0, length):
        if guess == selected_word[i]:
            display[i] = guess
    
    # Check if player has guessed all letters (win condition)
    if "_" not in display:  
        print("You win")
        end_of_game = True
    
    # If guess is wrong, show the next hangman stage
    if not guess in selected_word:
        new_life = stages[lives]
        print(new_life)
        lives += 1  # Increment wrong guess counter
        
    # Game over if player reaches 7 wrong guesses
    if lives == 7:
        print(f"Game Over, word was {selected_word}")
        end_of_game = True
        
    # Check if the letter was already guessed
    if guess in userInput:
        print("You already Guessed it")
        continue  # Skip rest of loop for repeated guesses
    userInput.append(guess)  # Add guess to list
    
    # Show current progress and all guesses
    print(display)
    print(f"your guess was {userInput}")
