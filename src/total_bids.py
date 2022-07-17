# add bids will update the dict with keys and values
def add_bids(bids, name, amount):
    bids.update({name: amount})

# highest_bid will find the highest bid and return the person with the highest bid
def highest_bid(bid):
    winner = ''
    all_bids = list(bid.values())
    max_bid = max(all_bids)

    for keys, items in bid.items():
        if items == max_bid:
            winner = keys
        else:
            continue

    return winner
