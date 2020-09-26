#main.py
import sys
import recommendedPercents as rp
import actualPercents as ap
import addEntry as ae

def errMessage():
    raise SystemExit(f"Usage: {sys.argv[0]}  (-c) <arguments>...")

def main(clas):
    opts = [opt for opt in clas if opt.startswith("-")]
    args = [arg for arg in clas if not arg.startswith("-")]

    if "-c" in opts:
        try:
            rp.budgetPercents(args[0])
        except IndexError:
            errMessage()
    elif "-v" in opts:
        try:
            ap.budgetPercents(args[0], args[1])
        except IndexError:
            errMessage()
    elif "-a" in opts:
        try:
            ae.add(args[0:])
        except IndexError:
            errMessage()
    else:
        errMessage()

if __name__ == "__main__":
    main(sys.argv[1:])
