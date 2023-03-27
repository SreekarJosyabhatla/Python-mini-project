import random

"""user_choice    computer_choice

    0   0       Draw
    0   1       computer win    
    0   2       user Win
    1   0       user win
    1   1       draw 
    1   2       computer win
    2   0       computer win
    2   1       user win
    2   2       draw
"""


def winner(user_choice, computer_choice):                                 
   
   if(computer_choice == user_choice):
      return(f"Draw  {computer_choice} {user_choice}")
   
   elif(user_choice == 0  and   computer_choice == 2):
      return(f"User Win  {user_choice} {computer_choice} ")
    
   elif(user_choice > computer_choice):
      return(f"User Win  {user_choice} {computer_choice} ")
   
   elif(computer_choice > user_choice):
      return(f"Computer Win  {computer_choice} {user_choice}")
   
   elif(computer_choice == 0  and  user_choice == 2):
      return(f"Computer Win  {computer_choice} {user_choice}")

     
max_outcomes = [0, 1, 2]
user_choice = int(input("Enter 0 for rock\n1 for paper\n2 for scissor\n"))
computer_choice = random.choice(max_outcomes)
x = winner(user_choice, computer_choice)
print(x)