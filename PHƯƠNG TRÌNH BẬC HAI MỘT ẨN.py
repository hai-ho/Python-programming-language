# viết phương trình bậc hai một ẩn: ax + by + c = 0 (a#0)
import math
def GH(a,b,c):
    if(a == 0):
        if(b == 0):
            if(c == 0):
                print("PT vô số nghiệm")
            else:
                print("PT vô nghiệm")
        else:
            if(c == 0):
                print("PT có một nghiệm x = 0")
            else:
                print("PT có nghiệm x = ", -c / b)
    else:
        delta = b * b - 4 * a * c
        if(delta > 0):
            print("nghiệm x1 = ",((-b + math.sqrt(delta)) / (2 * a)))
            print("nghiệm x2 = ",((-b - math.sqrt(delta)) / (2 * a)))
        elif (delta == 0):
            print("PT có nghiệm kép X1 = X2 = ", -b / (2 * a))
        else:
            print("PT vô nghiệm")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
GH(a,b,c)