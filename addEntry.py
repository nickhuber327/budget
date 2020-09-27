from pathlib import Path
import csv

def add(filename, date, item, category, cost):
    if category != "income":
        cost *= -1
        
    if Path(filename).is_file():
        with open(filename, mode='r') as budgetFile:
            budgetReader = csv.DictReader(budgetFile)
            sum = cost
            for row in budgetReader:
                sum += float(row["cost"])

        with open(filename, mode='a') as budgetFile:
            fieldnames = ['date',
            'item',
            'category',
            'cost',
            'sum']
            writer = csv.DictWriter(budgetFile, fieldnames=fieldnames)
            writer.writerow({'date': date,
            'item': item,
            'category': category,
            'cost': cost,
            'sum': sum})
    else:
        with open(filename, mode='w') as budgetFile:
            fieldnames = ['date',
            'item',
            'category',
            'cost',
            'sum']
            writer = csv.DictWriter(budgetFile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'date': date,
            'item': item,
            'category': category,
            'cost': cost,
            'sum' : 0})

if __name__ == "__main__":
    add()
