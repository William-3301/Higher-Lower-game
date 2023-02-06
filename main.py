from random import randint
from art import logo
from game_data import data

print(logo)
print("\n")
score = 0

game_cont = True

while game_cont:
  final_n = len(data) - 1
  choose_1 = randint(0,final_n)
  choose_2 = choose_1
  
  while choose_2 == choose_1:
    choose_2 = randint(0,final_n)
  
  print(data[choose_1]["name"], "a" , data[choose_1]["description"], "from", data[choose_1]["country"] )
  
  print("\n")
  
  print(data[choose_2]["name"], "a" , data[choose_2]["description"], "from", data[choose_2]["country"] )
  
  user_choice = input("Who has more followers?").lower()
  
  if user_choice == data[choose_1]["name"].lower():
    if data[choose_1]["follower_count"] > data[choose_2]["follower_count"]:
      score += 1
      print("You win! Your score is:", score)
    else:
      print("You lose! Your score is:",score)
      game_cont = False
  
  else:
    
    if data[choose_1]["follower_count"] < data[choose_2]["follower_count"]:
      score += 1
      print("You win! Your score is:", score)
    else:
      print("You lose! Your score is:",score)
      game_cont = False
      
  print("\n")
  
