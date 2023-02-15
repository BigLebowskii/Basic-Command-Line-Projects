

from replit import clear
from art import logo
import random


restart = True
while restart:
  
  

  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

  def win_loss_draw():
    if user_score > 21:
      print("You went over. You lose 😭")
    elif comp_score > 21:
      print("Opponent went over. You win 😁")
    elif user_score > comp_score:
      print("You win 😃")
    elif comp_score > user_score:
      print("You lose 😤")
    else:
      print("It's a draw 😑")
  
      
  def comp_score_check(comp_hand,comp_score):
    while comp_score < 17:
      comp_hand.append(deal_card())
      comp_score = calculator_score(comp_hand)
      return comp_score

      
  def calculator_score(score):
    for i in range(len(score)-1):
      if score[i] == 11 and score[i+1] == 10:
        return 0
      elif score[i] == 11 and sum(score) > 21:
        score[i].remove()
        score[i].append(1)
    return sum(score)

    

  user_hand = []
  comp_hand = []
  user_hand.append(deal_card())
  user_hand.append(deal_card())
  comp_hand.append(deal_card())
  comp_hand.append(deal_card())
  
  user_score = calculator_score(user_hand)
  comp_score = calculator_score(comp_hand)
  
  start = input("Do you want to play a game of blackjack? ").lower()
  clear()
  if start == 'yes':
    print(logo)
    print(f"Your Cards: {user_hand}, and current score: {user_score}")
    print(f"Computer's cards: [{comp_hand[0]},_]")
    if calculator_score(user_hand) == 0:
      print("YOu won")
    elif calculator_score(comp_hand) == 0:
      print("You lost")
    else:
      while user_score <= 21:
        option = input("Do you want to 'Hit' or 'Stand?'").lower()
        clear()
        if option == 'hit':
          user_hand.append(deal_card())
          user_score = calculator_score(user_hand)
          print(f"Your Cards: {user_hand}, and current score: {user_score}")
          print(f"Computer's cards: [{comp_hand[0]},_]")
        elif option == "stand":
          comp_score_check(comp_hand,comp_score)
        print(f"Your Cards: {user_hand},and current score: {user_score}")
        print(f"Computer's cards: {comp_hand}, current score: {comp_score}")
        win_loss_draw()
        break
else:
  clear()
  restart = False
  
  
  















