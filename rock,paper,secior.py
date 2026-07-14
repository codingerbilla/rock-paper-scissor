import random
options = ("rock","paper","scissor")
user_choice = input("What is you choose? (rock,paper,scissor): \n ").lower()
computer_choice = random.choice(options)
print(f"computer_choice : {computer_choice}")
if user_choice not in options:
    print("invalid choice")
elif computer_choice == user_choice:
    print("tie")
elif( (user_choice == "rock" and computer_choice == "scissor") or
    (user_choice == "paper" and computer_choice == "rock") or 
    (user_choice == "scissor" and computer_choice == "paper")):
    print("you win")
else:
    print("you lose")
    
