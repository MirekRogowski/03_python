count = 0
print("\nPrawidłowa wartość od 1 do 100")
x = int(input("\nPodaj wartosć: "))
while 1 <= x <= 100:
    if x == 1:
        print("\nCiąg ma 1 element \n")
        exit()
    else:
        while x != 1:
            if not x % 2:
                x = x/2
            else:
                x = 3 * x + 1
            count +=1
 #           print(f"Dla numeracji nr {count}, wartość ciągu wynosi: {int(x)} ")
        print(f"Ciąg ma {count} elementów")
        check = input("\n(t)ak -nowa iteracja, (k)oniec ")
        if check == "t":
            x = int(input("\nPodaj wartosć: "))
            count = 0
            continue
        exit()
print("Koniec\n ")
exit()

