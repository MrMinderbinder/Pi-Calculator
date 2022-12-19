import decimal
import time

digits_selection = input("Enter number of digits: ")

decimal.getcontext().prec = int(digits_selection) + 11

start = time.time()

total = 10 ** (int(digits_selection) + 10)
term = total
k = 0

while term: 
    term = term // (-6 * k - 9) * (2 * k + 1)
    total += term
    k += 1

pi = str(decimal.Decimal(12).sqrt() * total)
end = time.time()

print(pi[0] + "." + pi[1:-11])
print("Computation time: ", end - start, "s", sep = "")
