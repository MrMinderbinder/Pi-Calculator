import time

def arctan(x, digits):        
    numerator = digits * x
    denominator = 1 + x ** 2
    term = numerator // denominator
    total = term    
    two_n = 2

    while term:
        term = term // (denominator * (two_n + 1)) * two_n
        total += term
        two_n += 2

    return total

digits_selection = input("Enter number of digits: ")

print("1. Machin's Formula")
print("2. Gauss's Formula ")

formula_selection = input("Enter selection: ")

print("1. Print on screen", "\n", "2. Output to file", sep = "")
output_selection = input("Enter selection: ")

start = time.time()

digits = 10 ** (int(digits_selection) + 10)

if formula_selection == "1":
    pi = 16 * arctan(5, digits) - 4 * arctan(239, digits)
elif formula_selection == "2":
    pi = 48 * arctan(18, digits) + 32 * arctan(57, digits) - 20 * arctan(239, digits)

end = time.time()

pi = "3." + str(pi)[1:-11]

if output_selection == "1":
    print(pi)
elif output_selection == "2":
    filename = digits_selection + " digits of π.txt"
    file = open(filename, "w")
    file.write(pi)
    file.close()

print("Computation time: ", end - start, "s", sep = "")
