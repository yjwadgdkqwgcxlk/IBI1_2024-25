# Variables for comparison
a = 15
b = 75
c = a + b  # 90
d = 90
e = 5
f = d + e  # 95

# Comparing c and f, f should be greater than c
if c < f:
    print("Driving is faster than walking")
elif c > f:
    print("Walking is faster than driving")
else:
    print("Both are equally fast")

# Boolean logic part with truth table
# Truth table for W = X and Y:
# X    Y    W
# 0    0    0
# 0    1    0
# 1    0    0
# 1    1    1

X = True
Y = False
W = X and Y
print("W is", W)

