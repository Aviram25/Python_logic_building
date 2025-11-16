def max_satisfaction(expectations, cards):
    # Sort both lists so we match smallest expectation with smallest usable card
    expectations.sort()
    cards.sort()

    i = j = 0       # i → expectation pointer, j → card pointer
    count = 0

    # Walk through both lists
    while i < len(expectations) and j < len(cards):

        # If the current card meets the current expectation,
        # we satisfy this teammate and move to the next person + next card
        if cards[j] >= expectations[i]:
            count += 1
            i += 1
            j += 1
        
        # If the card is too small, discard it and try the next card
        else:
            j += 1

    # Total satisfied teammates
    return count
