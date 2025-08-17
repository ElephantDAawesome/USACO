import random
#rock beats scissor
#scissor beats paper
#paper beats rock
num = random.randint(0,2)
bool = True

while bool:
    options = ['rock', 'scissor', 'paper']
    answer = options[num]
    guess = str(input("Choose rock, paper, or scissor: ")).lower()


    if guess == answer:
        print("You guys chose the same thing bruh")
    elif (answer=='rock' and guess=='scissor') or (answer=='scissor' and guess=='paper') or (answer=='paper' and guess=='rock'):
        print("You lost: the option you chose lost. Womp womp")
        try_again = str(input("Would you like to continue: ")).lower()
        if try_again == 'yes':
            bool=True
        else:
            bool = False
            
    elif (guess=='rock' and answer=='scissor') or (guess=='scissor' and answer=='paper') or (guess=='paper' and answer=='rock'):
        print("You won: the option you chose won.")
        bool = False
        try_again = str(input("Would you like to continue: ")).lower()
        if try_again == 'yes':
            bool=True
        else:
            bool = False
    else:
        print("Your answer wasn't even legible. Try again.")


