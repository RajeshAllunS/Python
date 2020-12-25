
# from art import logo
from game_data import data
# from art import vs
import art
import replit
import random

score = 0
print(art.logo)

def compare(first,second):
  if first > second:
    return 'A'
  else:
    return 'B'

first = random.choice(data)
first_count = first['follower_count']

guess = True
while guess:
  print(f"Compare A: {first['name']}, {first['description']}, from {first['country']}")
  second = random.choice(data)
  second_count = second['follower_count']
  while first == second:
    second = random.choice(data)
    second_count = second['follower_count']
  print(art.vs)
  print(f"Against B: {second['name']}, {second['description']}, from {second['country']}")
  more_follower = input("Who has more followers? Type 'A' or 'B': ")
  if compare(first_count,second_count) == more_follower:
    replit.clear()
    score += 1
    print(art.logo)
    print(f"You're right! Current score {score}.")
    first = second
  else:
    replit.clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final Score: {score}.")
    guess = False


