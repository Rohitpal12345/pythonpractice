import random

tools=["rock","scissors","paper"]

while True:
    player_choice=input("enter your choice rock,scissors,paper:").lower()
    
    if player_choice =="exit":
        print("Thanks playing")
        break
    if player_choice not in tools:
        print("Your choice is invalid!")
        continue

    # take computer choice 
    computer_choice=random.choice(tools)
    print(f"computer choice is: {computer_choice}")

    if player_choice==computer_choice:
        print(f"Both choice is same Its a tile{player_choice}")

    elif player_choice=='rock':
        if computer_choice=='scissors':
            print("rock beats scissors ':You Win:")
        else:
            print("paper covered rock so 'you lose'")

    elif player_choice=="scissors":
        if computer_choice=="paper":
            print("scissors cut paper so 'You win' ")
        else:
            print("rock beats scissors so you lose")

    elif player_choice=="paper":
        if computer_choice=="rock":
            print("paper beats rock so 'you win'")
        else:
            print("scissors cut paper so you lose")
    
      
     
    
    pass