import math
import sys

if len(sys.argv) != 4:
    print("please supply 3 arguments for a, b and c")
    exit() 

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    print("not a quadratic equation")
    exit()

## compute discriminant
d = b*b - 4*a*c

if d > 0 :
    rd = math.sqrt(d)
    x1 = (-b + rd)/(2*a)
    x2 = (-b - rd)/(2*a)
    print(x1,x2)
elif d < 0:
    rd = math.sqrt(-d)
    x1 = complex(-b/(2*a),rd/(2*a))
    x2 = complex(-b/(2*a), -rd/(2*a))
    print(x1,x2)
elif d == 0:
    x = -b/(2*a)
    print(x) 
