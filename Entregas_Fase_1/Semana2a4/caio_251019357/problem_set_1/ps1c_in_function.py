def part_c(initial_deposit):
    down_payment = 800000 * 0.25
    months = 36

    if initial_deposit >= down_payment - 100:
        return 0.0, 0

    max_savings = initial_deposit * (1 + 1.0 / 12) ** months
    if max_savings < down_payment - 100:
        return None, None

    low = 0.0
    high = 1.0
    steps = 0

    while True:
        rate = (low + high) / 2
        savings = initial_deposit * (1 + rate / 12) ** months

        if abs(savings - down_payment) <= 100:
            return rate, steps + 1

        if savings < down_payment:
            low = rate
        else:
            high = rate

        steps += 1