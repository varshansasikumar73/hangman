import random
with open ("wordlist.txt") as f:
    words = f.read().splitlines()
    No_Capitals_Word_List = []
    for word in words:
        word = word.lower()
        No_Capitals_Word_List.append(word)
print(No_Capitals_Word_List)


hanger0 = r"""      
        ______
        |    |
        |    |
             |
             |
             |
        """
hanger1 = r"""      
        ______
        |    |
        |    |
        O    |
             |
             |
             |
             |
        """
hanger2 = r"""      
        ______
        |    |
        |    |
        O    |
        |    |
        |    |
             |
             |
        """
hanger3 = r"""      
        ______
        |    |
        |    |
        O    |
        |/   |
        |    |
             |
             |
        """
hanger4 = r"""      
        ______
        |    |
        |    |
        O    |
       \|/   |
        |    |
             |
             |
        """
hanger5 = r"""      
        ______
        |    |
        |    |
        O    |
       \|/   |
        |    |
       /     |
             |
        """
hanger6 = r"""      
        ______
        |    |
        |    |
        O    |
       \|/   |
        |    |
       / \   |
             |
        """
hangman_death_counter = 0
def gallows():
    if hangman_death_counter == 0:
        print(hanger0)
    if hangman_death_counter == 1:
        print(hanger1)
    elif hangman_death_counter == 2:
        print(hanger2)
    elif hangman_death_counter == 3:
        print(hanger3)
    elif hangman_death_counter == 4:
        print(hanger4)
    elif hangman_death_counter == 5:
        print(hanger5)
    elif hangman_death_counter == 6:
        print(hanger6)
        print("You lost!")

chosen = list(random.choice(No_Capitals_Word_List))
    
spaces = []
for char in chosen:
    char = "_"
    spaces.append(char)

alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
used_letters = []
winner = False
winning_line = "You got the word right!"
def DID_YOU_WIN():
    global winner
    if spaces == chosen:
        print(winning_line)
        winner = True
        return winner


def guess_letter():
    global hangman_death_counter
    while hangman_death_counter <= 5 and winner == False:
        print(f"These are all the letters you've used: {used_letters}")
        guessedLetter = input("enter a letter:")
        while guessedLetter not in alphabet:
            guessedLetter = input("guess again and use a letter pls:")
        while guessedLetter in used_letters:
            print(f"These are all the letters you've used: {used_letters}")
            guessedLetter = input("You've already used this letter, pick a different one:")
        if guessedLetter not in chosen:
            used_letters.append(guessedLetter)
            hangman_death_counter += 1
            print (f"This letter is not in the word!")
            gallows()
            print("".join(spaces))
        elif guessedLetter in chosen:
            used_letters.append(guessedLetter)
            gallows()
            for i,char in enumerate (chosen):
                if guessedLetter == char:
                    spaces[i] = guessedLetter
                    print("".join(spaces))
        DID_YOU_WIN()
            
            
                
guess_letter()




