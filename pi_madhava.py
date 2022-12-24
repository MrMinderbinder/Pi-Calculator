import decimal
import time

digits = input("Enter number of digits: ")
overhead = 11

decimal.getcontext().prec = int(digits) + overhead

start = time.time()
total = 10 ** (int(digits) + overhead - 1)
term = total
k = 0

while term:
    term = term // (-6 * k - 9) * (2 * k + 1)
    total += term
    k += 1

pi = str(decimal.Decimal(12).sqrt() * total)
end = time.time()

print(pi[0] + "." + pi[1:-overhead])
print("Computation time: ", end - start, "s", sep = "")
