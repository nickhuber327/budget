#Vis
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

import csv

def graph(filename="ledgers/master.csv"):
    fig = plt.figure()
    ax = plt.subplot2grid((1,1), (0,0))
    categories = {"Housing" : [],
    "Transportation" :  [],
    "Food" : [],
    "Personal" : [],
    "Savings": [],
    "Debt" : [],
    "Income" : [],
    "Month" : []}

    colors = ['m', 'c', 'r', 'k', 'y', 'b', 'g']

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

    ax.plot_date(categories["Month"], categories["Housing"], '-', label="Housing")
    """
    plt.plot([], [], color=colors[0], label='Housing', linewidth=5)
    plt.plot([], [], color=colors[1], label='Transportation', linewidth=5)
    plt.plot([], [], color=colors[2], label='Food', linewidth=5)
    plt.plot([], [], color=colors[3], label='Personal', linewidth=5)
    plt.plot([], [], color=colors[4], label='Savings', linewidth=5)
    plt.plot([], [], color=colors[5], label='Debt', linewidth=5)
    plt.plot([], [], color=colors[6], label='Income', linewidth=5)
    """
    """
    plt.stackplot(categories["Month"],
    categories["Income"],
    categories["Housing"],
    categories["Transportation"],
    categories["Food"],
    categories["Personal"],
    categories["Savings"],
    categories["Debt"],
    colors=colors)
    """
    plt.xlabel("Month")
    plt.ylabel("Percentages")
    plt.title("Budget Trends")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    graph()
