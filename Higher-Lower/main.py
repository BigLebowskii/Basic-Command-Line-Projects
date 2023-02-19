import random
from replit import clear
from art import logo, vs
from game_data import data

print(logo)
restart = True
score = 0
account_b = random.choice(data)

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_descr}, from {account_country}."
  
def check_answer(guess, a_followers, b_followers):
  """Returns whether if the user got the option right"""
  if a_followers > b_followers:
    return guess == 'A'
  else:
    return guess == 'B'
    
while restart:
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data) 
    
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  
  option = input("Who has more followers? Type 'A' or 'B': ").upper()

  followers_A = account_a['follower_count']
  followers_B = account_b['follower_count']

  clear()
  print(logo)
  
  is_correct = check_answer(option,followers_A,followers_B)

  if is_correct:
    score += 1
    print(f"You're right!   Current Score: {score}")

  else:
    print(f"You're wrong!  Final Score: {score}")
    restart = False
    