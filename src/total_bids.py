
def highest_bid(bid):
    """This function will take a dict object and find the max value"""
    winner = ''
    all_bids = list(bid.values())
    max_bid = max(all_bids)

    for keys, items in bid.items():
        if items == max_bid:
            winner = keys
        else:
            continue

    return winner
