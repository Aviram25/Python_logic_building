def compound_interest(principal, rate, contribution, years):
    r = rate / 100
    growth_factor = (1 + r) ** years
    final_amount = principal * growth_factor + contribution * ((growth_factor - 1) / r)
    return round(final_amount, 2)
