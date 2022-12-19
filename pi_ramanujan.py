import decimal
import time

digits_selection = input("Enter number of digits: ")
print("1. Print on screen", "\n", "2. Output to file", sep = "")
output_selection = input("Enter selection: ")
        
start = time.time()

digits_selection = int(digits_selection)
overhead = int(round(digits_selection * 0.00001 + 10, 0))
digits = 10 ** (digits_selection + overhead)
decimal.getcontext().prec = digits_selection + overhead + 1
decimal.getcontext().Emin = -9999999

k = 1
term = digits
a = term
b = 0

while term: 
    term = term * (4 * k - 1) * (2 * k - 1) * (4 * k - 3) // (k ** 3 * 3073907232)
    a += term
    b += term * k
    k += 1

pi = 9801 / (decimal.Decimal(2).sqrt() * (2206 * a + 52780 * b))
end = time.time()
pi = str(pi)[:digits_selection + 1]

if output_selection == "1":
    print(pi)
elif output_selection == "2":
    filename = str(digits_selection) + " digits of π.txt"
    file = open(filename, "w")
    file.write(pi)
    file.close()

print("Computation time: ", end - start, "s", sep = "")
