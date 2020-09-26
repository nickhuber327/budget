#recommendedPercents

def budgetPercents(income):
    """Calculates the recommended perecentages of the 5 category budget at any income"""
    income = float(income)
    percents = [.35, .15, .25, .1, .15]
    categories = [
        "Housing",
        "Transportation",
        "Other living expenses",
        "Savings",
        "Debt payoff",
        "Total"]
    budget = {}
    count = 0

    for i in percents:
        budget[categories[count]] = percents[count] * income
        count += 1

    budget[categories[count]] = income
        
    for key in budget:
        print(key, ': ', budget[key])

if __name__ == "__main__":
    budgetPercents(sys.argv[1])
