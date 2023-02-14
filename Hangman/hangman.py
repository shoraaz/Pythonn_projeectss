import random
from hangman_wordlist import word_list
from hangman_pic import logo

selected_word = random.choice(word_list)
game_ends = False
lives = 6
print(logo)

# Creating blank spaces
spaces = []
for _ in range(len(selected_word)):
    spaces += "_"

while not game_ends:
    guess = input("Guess a letter: ").lower()
    if guess in spaces:
        print(f"BRAVO! You have already guessed {guess}")
    # Checking guessed letter
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == guess:
            spaces[position] = letter
    if guess not in selected_word:

        print(f"You guessed {guess}, that's not in the word.A LIFE LOST.")
        lives -= 1
        if lives == 0:
            game_ends = True
            print("ALL LIVES LOST.You lose.")
    print(f"{' '.join(spaces)}")


    if "_" not in spaces:
        game_ends = True
        print("You win.")

    from hangman_pic import stages

    print(stages[lives])
print(f"Actual word was {selected_word}")