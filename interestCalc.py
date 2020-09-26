#interestCalc
def month(t, p, r):
    r_dec = r / 100
    m = t / 12
    return p * (1 + (r_dec * m))

def year(t, p, r):
    r_dec = r / 100
    return p * (1 + r_dec * t)

def calc(period, t, p, r):
    if period == "month":
        month(t, p, r)
    elif period == "year":
        year(t, p, r)

if __name__ == "__main__":
    calc()
