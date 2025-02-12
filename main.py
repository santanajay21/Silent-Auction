# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

# create a function to modularize the code and compare your bids 
def comparing_bids(bidding_dictionary):
    winner = ""
    highest_bid = 0 
    #max bid
    for bidder in bidding_dictionary:
        # this is how we get the value in a dictionary when looping through it
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


#  create a dictionary to store the bids
bids = {}

continue_bidding = True
# while loop to keep asking for bids
while continue_bidding:
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bids[name] = price
    any_more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if any_more_bids == "no":
        continue_bidding = False
        comparing_bids(bids)
    elif any_more_bids == "yes":
        continue_bidding = True
        print("\n" * 100)
    else:
        print("Invalid input. Please try again.")
        continue_bidding = False
        comparing_bids(bids)