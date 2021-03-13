import math
import time
print("+++++++++++++++++")
print("\tQuadratic Formulae Calculator")
print("+++++++++++++++++")
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
c = int(input("Enter value c: "))

root_part = (b**2 - 4*a*c) ** 0.5
ans1 = (-b + root_part)/(2*a)

ans2 = (-b - root_part)/(2*a)
print("Calculating...")

print("Answer is: ",round(ans1,3),"or: ",round(ans2,3))
