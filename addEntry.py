from pathlib import Path
import csv

def add(entry, filename):
    if Path(fileman).is_file():
        with open(filename, mode='w') as budgetFile:
            fieldnames = ['name', 'age', 'gender']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': 'Jack Smith', 'age': 40, 'gender': 'Male'})
    else:
        with open(filename, mode='a') as budgetFile:
	fieldnames = ['name', 'age', 'gender']
	writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
	writer.writerow({'name': 'Jack Smith', 'age': 40, 'gender': 'Male'})
        
if __name__ == "__main__":

with open('C:/Users/nickh/Desktop/example.csv', mode='a') as csvFile:
	fieldnames = ['name', 'age', 'gender']
	writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'name': 'Jack Smith', 'age': 40, 'gender': 'Male'})
	writer.writerow({'name': 'Mandy Smith', 'age': 35, 'gender': 'Female'})
