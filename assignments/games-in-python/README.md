
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, and conditionals. You will practice handling user input, tracking game state, and controlling game flow from start to finish.

## 📝 Tasks

### 🛠️	Create the Core Hangman Loop

#### Description
Set up the main game loop for Hangman. Randomly choose a word from a predefined list, accept one-letter guesses from the player, and update the displayed progress after each guess.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display the current word progress using underscores (for example: `_ _ _ _`).
- Accept and process one letter guess per turn.
- Reveal correctly guessed letters in all matching positions.


### 🛠️	Track Attempts and End Conditions

#### Description
Add logic for incorrect guesses and game completion. The game should end with a clear win or lose message depending on whether the player guesses the word before attempts run out.

#### Requirements
Completed program should:

- Track remaining incorrect guesses and reduce the count only for wrong letters.
- Prevent invalid or repeated input from breaking the game flow.
- End with a win message when the full word is guessed.
- End with a lose message when attempts are exhausted, and show the correct word.
