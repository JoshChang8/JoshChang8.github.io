#Class for Hangman game
class hangman:
    def __init__(self,word,location_list):
        self.word = word
        self.location_list = location_list

    def word_to_blanks(self,word):  # converts the word to blanks
        to_guess = ""
        for letter in self.word:
            to_guess = to_guess + "-"
        return to_guess
    
    def letter_location(self,word,guess,location_list): #identifies the location of guessed letters in the word
        self.location_list = []
        word_list = list(self.word)
        location = 0
        for letter in word_list:
            if letter == guess:
                self.location_list.append(location)
            location += 1
        return self.location_list
    
    def fill_in_blanks(self,guess,location_list,to_guess):
        to_guess_list = list(to_guess)
        for i in self.location_list:
            to_guess_list[i] = guess
        to_guess = ''.join(to_guess_list)
        return to_guess
