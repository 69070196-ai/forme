""" ProgressiveTax """
def main():
    """ ภาษีก้าวหน้า """
    income = int(input())
    over_tax = 0

    if abs(income - 150000) <= 150000 < income <= 300000:
        over_tax = abs(income - 150000)*0.05
    elif 300000 < income <= 500000 and abs(income - 300000)<=200000:
        over_tax = 7500 + (abs(income - 300000)*0.10)
    elif 500000 < income <= 750000 and abs(income - 500000)<=250000:
        over_tax = 27500 + (abs(income - 500000)*0.15)
    elif 750000 < income <= 1000000 and abs(income - 750000)<=250000:
        over_tax = 65000 + (abs(income - 750000)*0.2)
    elif abs(income - 1000000) <= 1000000 < income <= 2000000:
        over_tax = 115000 + (abs(income - 1000000)*0.25)
    elif abs(income - 2000000) <= 2000000 < income <= 4000000:
        over_tax = 365000 + (abs(income - 2000000)*0.3)
    elif income > 4000000:
        over_tax = 965000 + (abs(income - 4000000)*0.35)

    print(int(over_tax) if over_tax else 0)
main()
