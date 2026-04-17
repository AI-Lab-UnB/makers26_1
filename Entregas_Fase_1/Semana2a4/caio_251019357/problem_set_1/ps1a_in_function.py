def part_a(yearly_salary, portion_saved, cost_of_dream_home):
    down_payment = cost_of_dream_home * 0.25
    current_savings = 0.0
    monthly_deposit = yearly_salary / 12 * portion_saved
    months = 0

    while current_savings < down_payment:
        current_savings = current_savings * (1 + 0.05 / 12) + monthly_deposit
        months += 1

    return months