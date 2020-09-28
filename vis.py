#Vis
import matplotlib.pyplot as plt
import csv

def stack(filename):
    categories = {"Housing" : [],
    "Transportation" :  [],
    "Food" : [],
    "Personal" : [],
    "Savings": [],
    "Debt" : [],
    "Income" : [],
    "Month" : []}
    with open(filename, mode='r') as masterFile:
        masterReader = csv.DictReader(masterFile)

        for row in masterReader:
            categories["Housing"].append(float(row["Housing"]))
            categories["Transportation"].append(float(row["Transportation"]))
            categories["Food"].append(float(row["Food"]))
            categories["Personal"].append(float(row["Personal"]))
            categories["Savings"].append(float(row["Savings"]))
            categories["Debt"].append(float(row["Debt"]))
            categories["Income"].append(float(row["Income"]))
            categories["Month"].append(row["Month"])

    plt.plot([], [], color='m', label='Housing', linewidth=5)
    plt.plot([], [], color='c', label='Transportation', linewidth=5)
    plt.plot([], [], color='r', label='Food', linewidth=5)
    plt.plot([], [], color='k', label='Personal', linewidth=5)
    plt.plot([], [], color='y', label='Savings', linewidth=5)
    plt.plot([], [], color='b', label='Debt', linewidth=5)
    plt.plot([], [], color='g', label='Income', linewidth=5)

    plt.stackplot(categories["Month"],
    categories["Income"],
    categories["Housing"],
    categories["Transportation"],
    categories["Food"],
    categories["Personal"],
    categories["Savings"],
    categories["Debt"],
    colors=['m','c','r','k','y','b','g'])

    initiate()

def initiate():
    plt.xlabel("Month")
    plt.ylabel("Percentages")
    plt.title("Budget Trends")
    plt.legend()
    plt.show()
