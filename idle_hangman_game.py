from idle_class import hangman
import random

def display_instructions() : #Instructions of the Hangman Game
    print("Welcome to Hangman!\n")
    print("Objective of the Game")
    print("The objective of Hangman is to guess letters to find out the unknown word that is given from the topic that you select.")
    print("In order to win the game, you must guess all the correct letters of the unknown word before you run out of attempts (6 attempts)!\n")
    print("How to Play")
    print("Select one of the four categories displayed and an unknown word will be selected within that category for you to guess.")
    print("Guess a letter of the word, if the unknown word contains the letter you guessed, the letters in that word will be revealed and you will not lose a guess attempt.")
    print("If the unknown word does not contain the letter you guessed, a limb will be added to hangman.")
    print("If you have guessed all the right letters of the word, you have won the game!")
    print("If you have used all of your 6 guesses, you have lost the game.")

def man(wrong_guesses):         #Takes number of incorrect guesses to generate the hangman
  if wrong_guesses == 0:
    hang = "_______\n |    |     \n |\n |\n |\n |\n |\n_|_____"
  elif wrong_guesses == 1:
    hang = "_______\n |    |     \n |   (_)\n |\n |\n |\n |\n_|_____"
  elif wrong_guesses == 2:
    hang = "_______\n |    |     \n |   (_)\n |    |\n |    |\n |\n |\n_|_____"
  elif wrong_guesses == 3:
    hang = "_______\n |    |     \n |   (_)\n |   \|\n |    |\n |\n |\n_|_____"
  elif wrong_guesses == 4:
    hang = "_______\n |    |     \n |   (_)\n |   \|/\n |    |\n |\n |\n_|_____"
  elif wrong_guesses == 5:
    hang = "_______\n |    |     \n |   (_)\n |   \|/\n |    |\n |   /\n |\n_|_____"
  elif wrong_guesses == 6:
    hang = "_______\n |    |     \n |   (_)\n |   \|/\n |    |\n |   / \ \n |\n_|_____\n Game Over!"

  return (hang)



def choose_topic():
  while True:
    topic = input("\nPlease enter the topic that you would like. The available topics are: 'Capital Cities', 'Major Tech Companies', 'Desserts', 'Colours' \t")
    word = ""
    if topic.lower() == "capital cities":
      word = random.choice(open('capital_cities.txt').read().split()).strip()
      return word
    elif topic.lower() == "major tech companies":
      word = random.choice(open('major_tech_companies.txt').read().split()).strip()
      return word
    elif topic.lower() == "desserts":
      word = random.choice(open('desserts.txt').read().split()).strip()
      return word
    elif topic.lower() == "colours":
      word = random.choice(open('colours.txt').read().split()).strip()
      return word
    else:
      print("That is not a valid topic.")

    


def main():
    play = True
    display_instructions()
    while play:   
        word = choose_topic()
        location_list = []
        to_guess = ""
        player = hangman(word,location_list)
        wrong_guesses = 0
        wins = 0
        to_guess = str(player.word_to_blanks(word))
        print(to_guess)
        while (wrong_guesses < 6):
            guess = input(str("Enter a letter to guess: \t"))
            player.letter_location(word,guess,location_list)
            if player.location_list == []:
                wrong_guesses += 1
                print(man(wrong_guesses))
            print(player.fill_in_blanks(guess,location_list,to_guess))
            to_guess = player.fill_in_blanks(guess,location_list,to_guess)
            if to_guess == player.word:
                wins += 1
                print('You won! So far you have ', wins, " wins.") 
                break
        play_again = input("Type 'n' if you would like to exit the game. Press any other key to continue. \t")
        if play_again == "n":
            play = False
            break
        else:
            play = True
          
main()
