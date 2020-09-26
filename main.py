#main.py
import sys

def errMessage():
    raise SystemExit(f"Usage: {sys.argv[0]}  (-c) <arguments>...")

def main(clas):
    opts = [opt for opt in clas if opt.startswith("-")]
    args = [arg for arg in clas if not arg.startswith("-")]

    if "-c" in opts:
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
    else:
        errMessage()

if __name__ == "__main__":
    main(sys.argv[1:])
