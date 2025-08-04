def game(user_choice,computer_choice):
    if(user_choice=="Rock" and computer_choice=="Paper"):
        print(f"user choice is {user_choice}")
        print(f"computer choice is {computer_choice}")
        print(f"The winner is computer as it chooses {computer_choice}")
    elif(user_choice=="Rock" and computer_choice=="Scissors"):
        print(f"user choice is {user_choice}")
        print(f"computer choice is {computer_choice}")
        print(f"The winner is user as he chooses {user_choice}")
    elif(user_choice=="Paper" and computer_choice=="Rock"):
        print(f"user choice is {user_choice}")
        print(f"computer choice is {computer_choice}")
        print(f"The winner is user as he chooses {user_choice}")
    elif(user_choice=="Paper" and computer_choice=="Scissors"):
        print(f"user choice is {user_choice}")
        print(f"computer choice is {computer_choice}")
        print(f"The winner is computer as it chooses {computer_choice}")
    elif(user_choice=="Scissors" and computer_choice=="Rock"):
        print(f"user choice is {user_choice}")
        print(f"computer choice is {computer_choice}")
        print(f"The winner is computer as it chooses {computer_choice}")
    elif(user_choice=="Scissors" and computer_choice=="Paper"):
        print(f"user choice is {user_choice}")
        print(f"computer choice is {computer_choice}")
        print(f"The winner is user as he chooses {user_choice}")
    elif(user_choice == computer_choice):
        print(f"user choice is {user_choice}")
        print(f"computer choice is {computer_choice}")
        print("It is a Draw")
import random
print("1.Rock\n2.Paper\n3.Scissors")
user_choice=input("Enter Your Choice as Rock, Paper, Scissors: ")
l=["Rock","Paper","Scissors"]
computer_choice= random.choice(l)
print(computer_choice)
game(user_choice , computer_choice)
print("Do you want to play again give Yes or No")
user_interest=input("Give Your Interest:")
if(user_interest == "Yes"):
    import random
    print("1.Rock\n2.Paper\n3.Scissors")
    user_choice=input("Enter Your Choice as Rock, Paper, Scissors: ")
    l=["Rock","Paper","Scissors"]
    computer_choice= random.choice(l)
    print(computer_choice)
    game(user_choice , computer_choice)
else:
    print("Ok It's Your Wish")









