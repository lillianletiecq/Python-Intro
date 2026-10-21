# Program: Competancy5_Game.py
# Programmer: Lillian Letiecq
# Email: lletiecq@student.cnm.edu
# Purpose: to play hangman with the computer, where the computer chooses a word that is hard to guess 

import random 

class Rules:
    def __init__(self):
        self.word_list = ["Hymn", "Lynx", "Myth", "Sphynx", "Rhythm", "Sync", "Flysch", "Ghylls", "Sylphs", "Syzygy", "Crypt", "Glyph", "Ghylls", "Myrrh", "Nymph", "Slyly", "Wryly", "Tryst", "Fly", "Gym", "Quiz", "Fizz", "Buzz", "Jinx", "Fuzz", "Jink", "Haze", "Hajj", "Vex", "Fox", "Apex", "Affix", "Annex", "Axel", "Coccyx", "Lax", "Junk", "Jazz", "Razz", "Buzzing", "Zit", "Zine", "Zap", "Zinc", "Dizzy", "Jiff", "Zigzag", "Sylphs", "Syzygy", "Crypt", "Glyph", "Myrrh", "Nymph", "Slyly", "Wryly", "Tryst", "Fly", "Gym", "Quiz", "Fizz", "Buzz", "Jinx", "Fuzz", "Jink", "Haze", "Hajj", "Vex", "Fox", "Apex", "Affix", "Annex", "Axel", "Coccyx", "Lax", "Junk", "Jazz", "Razz", "Buzzing", "Zit", "Zine", "Zap","Hymn", "Syzygy", "Crypt", 
                "Glyph", "Myrrh", "Nymph", "Slyly", "Wryly", "Tryst", "Fly", "Nymph", "Slyly", "Wryly", "Tryst", "Fly", "Gym", "Quiz", "Fizz", "Buzz", "Jinx", "Fuzz", "Jink", "Haze", "Hajj", "Vex", "Fox", "Apex", "Affix", "Annex", "Axel", "Coccyx", "Lax", "Junk", "Jazz", "Razz", "Buzzing", "Zit", "Zine", "Zap", "Zinc", "Dizzy", "Jiff", "Zigzag", "Quest", "Quaff", "Qualm", "Query", "Quietude", "Quip", "Diphthong", "Diphtheria", "Ophthalmologist", "Ytterbium", "Myth", "Byte", "Oocyte", "Acolyte", "Flytrap", "Anytime", "Umph", "Phoo", "Phial", "Morph", "Aphid", "Biblioklept", "Nauseant", "Addend", "Agelast", "Peristeronic", "Hibernal", "Subnivean", "Sitzmark", "Primaveral", "Solivagant", "Filipendulous", "Jentacular",
                "Catillate", "Bellycheer", "Avidulous", "Retrogradation", "Spinous", "Illaudable", "Grimoire", "Fantod", "Dyspathy", "Orgulous", "Dilapidator", "Crimpy", "Jubilarian", "Flibbertigibbet", "Mollycoddle", "Dingus", "Doohickey", "Ballyhoo", "Fuddy-duddy", "Sozzled", "Bumfuzzled", "Foppish", "Brouhaha", "Gobbledygook", "Jackanapes", "Ragamuffin", "Cattywampus", "Slumgullion", "Hullabaloo", "Ill-willie", "Hogwash", "Unperson", "Taradiddle", "Lollygag", "Flummoxed", "Skedaddle", "Hocus-pocus", "Bamboozle", "Kerfuffle", "Collywobbles", "Hornswoggle", "Poppycock", "Rigmarole", "Fiddle-faddle", "Higgledy-piggledy", "Mumbo-jumbo", "Nincompoop", "Razzmatazz", "Shenanigans", "Tomfoolery", "Widdershins", "Highfalutin"]
            
        self.word = self.computer_choose_word(self.word_list)
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        self.user_input = ""

    def computer_choose_word(self, word_list):
        return random.choice(word_list)
    
    def greeting(self, word):
        print("Welcome to Hangman! The computer has chosen a word. Try to guess it one letter at a time.")
        print("The word has", len(word), "letters.")
        print("You have 6 incorrect guesses before you lose. Good luck!")
        print("Input your guess as a single letter. If you want to guess the entire word, type 'guess'.")

    def user_guess_letter(self):
        return input("Please enter your guess: ").lower()

    def user_guess_word(self):
        return input("Please enter your guess for the entire word: ").lower()

    def display_word_progress(self, word, guessed_letters):
        display = [letter if letter.lower() in guessed_letters else "_" for letter in word]
        print("Current word progress:", " ".join(display))

    def chances_remaining(self):
        remaining = self.max_incorrect_guesses - self.incorrect_guesses
        print(f"You have {remaining} incorrect guesses remaining.")

    def is_word_solved(self):
        return all(letter.lower() in self.guessed_letters for letter in self.word)


    def word_correct(self):
        if self.user_guess_word().strip() == self.word.lower():
            print(f"Congratulations! You correctly guessed the word: {self.word}!")
            return True
        else:
            print("Sorry, that is not the correct word.")
            self.incorrect_guesses += 1
            return False

    def letter_correct(self, letter):
        if letter in self.word.lower():
            print(f"Good guess! '{letter}' is in the word.")
        else:
            print(f"Sorry, '{letter}' is not in the word.")
            self.incorrect_guesses += 1
        self.guessed_letters.append(letter)

    def mechanics(self):
        while self.incorrect_guesses < self.max_incorrect_guesses:
            self.display_word_progress(self.word, self.guessed_letters)
            self.chances_remaining()

            user_input = self.user_guess_letter().strip()
            if user_input == "guess":
                if self.word_correct():
                    return
                continue

            if len(user_input) != 1 or not user_input.isalpha():
                print("Please enter a single letter, or type 'guess' to guess the whole word.")
                continue

            user_input = user_input.lower()
            if user_input in self.guessed_letters:
                print(f"You already guessed '{user_input}'. Try another letter.")
                continue

            self.letter_correct(user_input)
            if self.is_word_solved():
                print(f"Congratulations! You uncovered all letters! The word was: {self.word}!")
                return
        print(f"Game over! You've run out of guesses. The word was: {self.word}")


def play_game():
    game = Rules()
    game.greeting(game.word)
    game.mechanics()

def main():
     while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again in ("no", "n"):
            print("Thank you for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    main()