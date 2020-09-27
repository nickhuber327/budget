#main.py
import sys

help = """Budget Tool Help
-c <income> recommended percentages
-v <income> <filename> actual percentages based off of spending from csv file
-i <month/year> <term> <interest rate> <principal> interest calculator"""

def errMessage():
    raise SystemExit(f"Usage: {sys.argv[0]}  (-c) <arguments>...")

def main(clas):
    opts = [opt for opt in clas if opt.startswith("-")]
    args = [arg for arg in clas if not arg.startswith("-")]
    if "-h" in opts:
        print(help)
    elif "-c" in opts:
        import recommendedPercents as rp
        try:
            rp.budgetPercents(float(args[0]))
        except IndexError:
            errMessage()
    elif "-v" in opts:
        import actualPercents as ap
        try:
            ap.budgetPercents(int(args[0]), args[1])
        except IndexError:
            errMessage()
    elif "-i" in opts:
        import interestCalc as ic
        try:
            ic.calc(args[0], int(args[1]), int(args[2]), float(args[3]))
        except IndexError:
            errMessage()
    elif "-a" in opts:
        import addEntry as ae
        try:
            ae.add(args[0], args[1], args[2], args[3], float(args[4]))
        except IndexError:
            errMessage()
    else:
        print(help)

if __name__ == "__main__":
    main(sys.argv[1:])
