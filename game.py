import random

options = ["rock", "paper", "scissors"]

print("--- Welcome to Rock, Paper, Scissors! ---")

while True:
    user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing! Goodbye.")
        break
        
    if user_choice not in options:
        print("Invalid choice. Try again!")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine Winner
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
