#export
from pathlib import Path
import csv
import actualPercents as ae

def export(filename):
    """Exports a months ledger into a master file tracking trends"""
    month = filename.split()[1].split('.')[0]
    budget = ae.calcPercents(filename)
    income = budget["Income"]
    budget.pop("Income")
    percentages = {}

    for key in budget:
        percentages[key] = (budget[key] / income) * 100
    percentages["Income"] = income
    percentages["Month"] = month
    file = "Master Ledger.csv"
    fieldnames = ["Housing",
    "Transportation",
    "Food",
    "Personal",
    "Savings",
    "Debt",
    "Total",
    "Income",
    "Month"]

    if Path(filename).is_file():
        if Path(file).is_file():
            with open(file, mode='a') as exFile:
                exWriter = csv.DictWriter(exFile, fieldnames=fieldnames)
                exWriter.writerow(percentages)
        else:
            with open(file, mode='w') as exFile:
                exWriter = csv.DictWriter(exFile, fieldnames=fieldnames)
                exWriter.writeheader()
                exWriter.writerow(percentages)

if __name__ == "__main__":
    export()
