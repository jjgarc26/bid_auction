from total_bids import add_bids,highest_bid

print("Welcome to bidding")
# Empty variable to hold all bidders and continue the while loop
bids = {}
continue_bid = True
while continue_bid:
    print(bids)
    name = input("What is your name?: ")
    bid = int(input("How much are you bidding?: $"))
    more_bids = input("Are there anymore bidders?: ")
    add_bids(bids, name, bid)

    if more_bids == "yes":
        continue
    else:
        continue_bid = False
print(f"The winner is {highest_bid(bids)}")


