import random
options = ("rock", "paper", "scissor")
user_score = 0
computer_score = 0
for i in range(5):
    print(f"\nRound {i+1}")
    user_choice = input("Enter rock, paper or scissor: ").lower()
    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)
    if user_choice not in options:
        print("Invalid choice")
        continue
    if user_choice == computer_choice:
        print("Tie")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You Win")
        user_score += 1
    else:
        print("Computer Wins")
        computer_score += 1
print("\nFinal Score")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("You are the Final Winner!")
elif computer_score > user_score:
    print("Computer is the Final Winner!")
else:
    print("Match Draw!")
    
