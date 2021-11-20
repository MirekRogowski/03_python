p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
p5 = "X"
print(p1+p2+p3)
print(p4+p5+p6)
print(p7+p8+p9)
while True:
    p = input("Wybierz pole: ")
    if p == "1":
        p1 = "O"
        p3 = "X"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
        
    elif p == "2":
        p1 = "X"
        p2 = "O"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
    elif p == "3":
        p1 = "X"
        p3 = "O"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
    elif p == "4":
        p1 = "X"
        p4 = "O"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
    elif p == "6":
        p1 = "X"
        p6 = "O"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
    elif p == "7":
        p1 = "X"
        p7 = "O"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
    elif p == "8":
        p1 = "X"
        p8 = "0"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
    elif p == "9":
        p1 = "X"
        p9 = "O"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
    else:
        print("\nBłąd")
        print("Wprowadź prawidłową wartość. \n")
        continue

