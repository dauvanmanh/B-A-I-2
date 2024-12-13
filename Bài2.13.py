import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2 - 4*a*c

if delta > 0:
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt: {root1} và {root2}")
elif delta == 0:
    root = -b / (2*a)
    print(f"Phương trình có nghiệm kép: {root}")
else:
    print("Phương trình vô nghiệm")
