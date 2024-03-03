from random import choice
count = 0
user_wins = 0
computer_wins = 0
cc = ["Paper","Rock","Scissor"]
print("Welcome to our paper, rock and scissor game")
round1 = int(input("Enter how many rounds you wanted to  play : "))
for i in range(1,round1 + 1):
    print("Round : ", i)
    print("Paper")
    print("Rock")
    print("Scissor")
    user_input = input("Chose : ")
    computer_input = choice(cc)
    print("Computer choice : ", computer_input)
    print("User choice : ",  user_input)
    if user_input == computer_input:
        print("Match tied")
        count = count + 1
        # user_wins = user_wins + 1
        # computer_wins =  computer_wins + 1
    elif user_input == 'Paper'.lower() and computer_input == 'rock'.lower():
        print("User wins")
        user_wins = user_wins + 1
        count += 1
    elif user_input == 'rock'.lower() and computer_input == 'Scissor'.lower():
        print("User wins")
        user_wins = user_wins + 1
        count = count + 1
    elif user_input == 'scissor'.lower() and computer_input == 'Paper'.lower():
        print("User wins")
        user_wins = user_wins + 1
        count = count + 1
    else:
        print("Computer wins")
        computer_wins = computer_wins + 1
        count = count + 1
print("Total games played : ", count)
print("User win : ", user_wins)
print("Computer wins : ", computer_wins)