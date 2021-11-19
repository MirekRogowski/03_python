count = 0
x = int(input("Podaj wartosć: "))
while 1 <= x < 100:
    while x != 1:
        if not x %2:
            x = x/2
        else:
            x = 3 * x + 1
        count +=1
        print(f"Dla numeracji nr {count}, wartość ciągu - {int(x)} ")
    check = input("\nCzy chesz kontynouować t - tak,  n - nie: ")
    if check== "t":
        x = int(input("Podaj wartosć: "))
        continue
    else:
        break
print("\nKoniec\n ")
exit()

