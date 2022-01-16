# viết phương trình bậc nhất một ẩn: ax + b = 0 (a#0)
import math
def GH(a,b):
    if(a == 0):
        if(b == 0):
            print("PT vô số nghiệm")
        else:
            print("PT vô nghiệm")
    if(a != 0):
        print("PT có nghiệm x = ", -b / a)
a = float(input("a = "))
b = float(input("b = "))
GH(a,b)