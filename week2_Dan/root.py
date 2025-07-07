
a5 = float(input())
a4 = float(input())
a3 = float(input())
a2 = float(input())
a1 = float(input())
a0 = float(input())

def f(x):
    return a5*x**5 + a4*x**4 + a3*x**3 + a2*x**2 + a1*x + a0

# endpoint values
left = -100
right = 100

# tolerance
tol = 0.000000001

# bisection method
while abs(right-left) > tol:
    mid = (left+right)/2
    f_right = f(right)
    f_mid = f(mid)
    # kontrola zmamenka
    if f_right * f_mid <= 0:
        left = mid
    else:
        right = mid

root = (left + right) / 2.0
print("{0:.8f}".format(root))

