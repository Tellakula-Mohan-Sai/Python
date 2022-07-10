from drawings import stages,ascii_banner
def hangman():
    from wonderwords import RandomWord
    r = RandomWord().word()
    answer = list()
    for i in range(len(r)):
        answer.append("-")
    end_of_game = False
    lives = 6
    while not end_of_game and lives:
        guess = input("Guess a letter:")
        guess = guess.lower()
        for i in range(len(r)):
            if(r[i]==guess):
                answer[i]=guess
        if guess not in r:
            lives -= 1
            print(stages[lives])
        else:
            print(f"{''.join(answer)}")
            if "-" not in answer:
                end_of_game = True
                print("You Win!!")
    if lives == 0:
        print("Wrong guess. You are hanged!!!\n")
        print("The word was:",r)

if __name__=="__main__":
    print(ascii_banner)
    choice = True
    while choice:
        hangman()
        choice = input("Do you still want to play the game(Y or n):")
        if choice == "n":
            choice = False
        elif choice == "Y" or choice =="y":
            choice = True
        else:
            print("Wrong Input... Exiting the game")
            choice  = False
