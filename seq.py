a = float(input("Enter the first no. of AP:"))
d = float(input("Enter the common difference:"))
n = int(input("Enter the number of last term of Ap:"))

for i in range(n):
    term = a+i*d
    sum = n/2*(2*a+(n-1*d))
print(f"the{n}term of the AP are:{term}")
print(f"{n}the sum of AP are:{sum}")