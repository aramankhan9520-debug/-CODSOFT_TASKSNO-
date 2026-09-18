import random

print("===== ROCK PAPER SCISSORS GAME =====")

user_score = 0
computer_score = 0

while True:
    # User Input
    user = input("\nChoose rock, paper, or scissors: ").lower()

    # Check valid input
    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer Selection
    computer = random.choice(["rock", "paper", "scissors"])

    # Display choices
    print("You chose:", user)
    print("Computer chose:", computer)

    # Game Logic
    if user == computer:
        print("Result: It's a TIE!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("Result: You WIN!")
        user_score += 1

    else:
        print("Result: You LOSE!")
        computer_score += 1

    # Score
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    # Play Again
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        break

print("\n===== GAME OVER =====")
print("Final Your Score:", user_score)
print("Final Computer Score:", computer_score)
print("Thanks for playing!")