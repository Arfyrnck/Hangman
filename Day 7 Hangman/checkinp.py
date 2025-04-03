import random
from hangman_words import word_list
from hangman_art import HANGMANPICS,logo


lives = 0

print(logo)

choosen_word = random.choice(word_list)
print(f"The chosen word is: {choosen_word}")


placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)    


game_over = False
correct_letters = []


while not game_over:
    
    print(f"***********************************<{lives}>/6 LİVES LEFT******************************")
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""  


    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"
    
    print(display)
    
    if guess not in choosen_word:
        lives +=1
        print(f"You guessed {guess}, that's not in the words. You lose a life.")
        if lives == 6:
            game_over = True
            print(f"**************************IT WAS {choosen_word}!YOU LOSE*****************************************") 
    
    if "_" not in display:
        game_over = True
        print("*******************************YOU WİN*******************************************")
  
    
    print(HANGMANPICS[lives])