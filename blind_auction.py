from artt import logo
import os
# To clear the screen
def clear_terminal():
   os.system("cls" if os.name == "nt" else "clear")
print(logo)

auction = {}
# The function to find the highest bid
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding_finished = False

# Auction loop
while not bidding_finished:
  name = input("What is your name? : ")
  bid = int(input("What's your bid? : $"))
  auction[name] = bid
  questions = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if questions == "no":
    bidding_finished = True
    find_highest_bidder(auction)
  elif questions == "yes":
        clear_terminal()