import csv
import os

# CONSTANTS
FULL_PATH = os.path.dirname(os.path.realpath(__file__))
TAXES = [0, 10000, 10009, 10010, 12000, 56789, 1234567]

def read_brackets() -> list[tuple[any, float]]:
    l = []
    with open(os.path.join(FULL_PATH, 'brackets.csv'), newline='') as csv_file:
        next(csv_file)  # skip header
        csv_reader = csv.reader(csv_file)
        b_count = 0
        for r in csv_reader:
            if not r[0].isdigit():
                l.append((None, float(r[1]), b_count))
                b_count += 1
            else:
                l.append( (int(r[0]), float(r[1]), b_count))
                b_count += 1
    return l
    # ex return: 
    #   [(10000, 0.0, 0), (30000, 0.1, 1), (100000, 0.25, 2), (None, 40.0, 3)]

BRACKETS = read_brackets()

# 
def tax(income: int) -> int:
    owe = 0
    # Find which upper tax bracket we belong to and pay taxes above it
    # ex: tax(12000)
    #   we are in the 10000 bracket
    #   pay owed tax over the 10000 bracket
    our_bracket = BRACKETS[0]
    for i in range(len(BRACKETS) - 2, -1, -1):
        up_cap = BRACKETS[i][0]  
        if income > up_cap:
            our_bracket = BRACKETS[i]
            owe += (income - our_bracket[0]) * BRACKETS[i+1][1]
            break
    # Pay all other taxes if possible
    # should be maximum amount taxable for all others now
    for i in range(our_bracket[2], 0, -1):
        owe += (BRACKETS[i][0] - BRACKETS[i-1][0]) * BRACKETS[i][1]
    return owe

def main():
    for t in TAXES:
        print('tax(%i) => %i ' % (t, tax(t)))

if __name__ == "__main__":
    main()