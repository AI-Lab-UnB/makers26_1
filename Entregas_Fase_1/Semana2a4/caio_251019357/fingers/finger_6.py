n = 108

low = 0.0
high = 1000
steps = 0

while True:
    rate = (low + high) / 2

    if abs(savings - down_payment) <= 100:
        return rate, steps + 1

    if savings < down_payment:
        low = rate
    else:
        high = rate

    steps += 1