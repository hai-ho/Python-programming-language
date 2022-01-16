# viết phương trình bậc nhất một ẩn: ax + b = 0 (a#0)

a = int(input("a = "))
b = int(input("b = "))
if(a == 0):
    if(b == 0):
        print("PT vô số nghiệm")
    else:
        print("PT vô nghiệm")
else:
    if (a != 0):
        print("PT có nghiệm x = ", -b / a)