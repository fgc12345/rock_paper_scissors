import random

print("Welcome to Rock Paper Scissors!")

while True:
    print("['rock', 'paper', 'scissors']rock중 하나를 선택하세요!!")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    내가_낸것 = input()
    if 내가_낸것 in ["rock", "paper", "scissors"]:
        print("컴퓨터가 낸것은 %s!" % computer_choice)
        #무승부
        if computer_choice == 내가_낸것:
            print ('무승부!')

        #지는경우
        if computer_choice == "rock":
            if 내가_낸것 == "scissors":
                print("You lose!")
        if computer_choice == "scissors":
            if 내가_낸것 == "paper":
                print("You lose!")
        if computer_choice == "paper":
            if 내가_낸것 == "rock":
                print("You lose!")

        #이기는경우
        if computer_choice == "rock":
            if 내가_낸것 == "paper":
                print("You win!")
        if computer_choice == "scissors":
            if 내가_낸것 == "rock":
                print("You win!")
        if computer_choice == "paper":
            if 내가_낸것 == "scissors":
                print("You win!")
    else:
        print("다시 내세요!")