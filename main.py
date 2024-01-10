rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

play = True
# users choice
while play == True: 

  users_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors \n"))
  
  if users_choice == 0:
    print(rock)
  elif users_choice == 1:
    print(paper)
  elif users_choice == 2:
    print(scissors)
  
  # generate computers choice
  print("computer's choice")
  comp_choice = random.randint(0, 2)
  
  if comp_choice == 0:
    print(rock)
  elif comp_choice == 1:
    print(paper)
  elif comp_choice == 2:
    print(scissors)
  
  if comp_choice == 2 and users_choice == 0 :
    print("You win!")
  elif comp_choice == 0 and users_choice == 2:
    print("You lost :(")
  elif comp_choice > users_choice:
    print("You lost :(")
  elif comp_choice < users_choice:
    print("You won!")
  elif comp_choice == users_choice:
    print("Tie!")

  play_again = input("Do you want to play again? Type 'yes' for yes and 'no' for no \n")

  if play_again == "no":
    play = False

echo "# rock-paper-scissors" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/chelsearwang/rock-paper-scissors.git
git push -u origin main