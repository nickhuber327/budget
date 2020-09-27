#export
from pathlib import Path
import csv
import actualPercents as ae

def export(income, month, filename):
    """Exports a months ledger into a master file tracking trends"""
    budget = ae.calcPercents(income, filename)
    percentages = {}
    for key in budget:
        percentages[key] = (budget[key] / income) * 100
    percentages["Month"] = month
    file = "Master Ledger.csv"
    fieldnames = ["Housing",
    "Transportation",
    "Food",
    "Personal",
    "Savings",
    "Debt",
    "Total",
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
