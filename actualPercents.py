#actualPercents
import csv

def calcPercents(filename):
    """Calculates the actual percentages of the 5 category budget at any income"""

    budget = {"Housing" : 0,
              "Transportation" : 0,
              "Food" : 0,
              "Personal" : 0,
              "Savings" : 0,
              "Debt" : 0,
              "Income" : 0,
              "Total" : 0}
    with open(filename, mode='r') as budgetFile:
        budgetReader = csv.DictReader(budgetFile)

        for row in budgetReader:
            if row["category"] == "housing":
                budget["Housing"] += round(abs(float(row["cost"])),2)
            elif row["category"] == "transportation":
                budget["Transportation"] += round(abs(float(row["cost"])),2)
            elif row["category"] == "food":
                budget["Food"] += round(abs(float(row["cost"])),2)
            elif row["category"] == "personal":
                budget["Personal"] += round(abs(float(row["cost"])),2)
            elif row["category"] == "savings":
                budget["Savings"] += round(abs(float(row["cost"])),2)
            elif row["category"] == "debt":
                budget["Debt"] += round(abs(float(row["cost"])),2)
            elif row["category"] == "income":
                budget["Income"] += round(abs(float(row["cost"])),2)

    for key in budget:
        if key != "Total":
            budget["Total"] += budget[key]

    return budget

def budgetPercents(filename):
    """Displays 5 category budget"""
    budget = calcPercents(filename)
    income = budget["Income"]

    print("DOLLAR VALUES:")
    for key in budget:
        print(f'{key}: {budget[key]}')
    print("\n")

    budget.pop("Income")
    
    print("PERCENTAGES:")
    for key in budget:
        print(f'{key}: {budget[key] / income * 100}')

if __name__ == "__main__":
    budgetPercents()
