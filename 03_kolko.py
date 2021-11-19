#variables

while True:
    print("\n")
    print("- | - | -       1 | 2 | 3")
    print("- | X | -       4 | 5 | 6")
    print("- | - | -       7 | 8 | 9")
    print("\n")
    pole = int(input("Wybierz numer pola: "))
    if  pole == 1:
        print("\n")
        print("O | - | -       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")
        print("\n")
        print("O | - | X       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")
        dalej = int(input("Wybierz numer pola: "))
        if dalej == 2:
            print("\n")
            print("O | O | X       1 | 2 | 3")
            print("- | X | -       4 | 5 | 6")
            print("- | - | -       7 | 8 | 9")
            print("\n")
            print("\n")
            print("O | O | X       1 | 2 | 3")
            print("- | X | -       4 | 5 | 6")
            print("X | - | -       7 | 8 | 9")
            print("\n")
            print("Przegrana")
            gra = input("Chcesz grać dalej t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break
        elif dalej == 4:
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("O | X | -       4 | 5 | 6")
            print("- | - | -       7 | 8 | 9")
            print("\n")
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("O | X | -       4 | 5 | 6")
            print("X | - | -       7 | 8 | 9")
            print("\n")
            print("Przegrana")
            gra = input("Chcesz grać dalej t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break            
        elif dalej == 6:
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("- | X | 0       4 | 5 | 6")
            print("- | - | -       7 | 8 | 9")
            print("\n")
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("- | X | 0       4 | 5 | 6")
            print("X | - | -       7 | 8 | 9")
            print("\n")
            print("Przegrana")
            gra = input("Chcesz grać dalej t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break  
        elif dalej == 7:
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("- | X | -       4 | 5 | 6")
            print("0 | - | -       7 | 8 | 9")
            print("\n")
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("X | X | -       4 | 5 | 6")
            print("0 | - | -       7 | 8 | 9")
            print("\n")
            print("Przegrana")
            gra = input("Chcesz grać dalej t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break  
        elif dalej == 8:
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("- | X | -       4 | 5 | 6")
            print("- | 0 | -       7 | 8 | 9")
            print("\n")
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("- | X | -       4 | 5 | 6")
            print("X | O | -       7 | 8 | 9")
            print("\n")
            print("Przegrana")
            gra = input("Chcesz grać dalej t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break  
        elif dalej == 9:
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("- | X | -       4 | 5 | 6")
            print("- | - | 0       7 | 8 | 9")
            print("\n")
            print("\n")
            print("O | - | X       1 | 2 | 3")
            print("- | X | -       4 | 5 | 6")
            print("X | - | 0       7 | 8 | 9")
            print("\n")
            print("Przegrana")
            gra = input("Chcesz grać dalej t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break  
    #koniec dla pola numer 1
    elif pole == 2:
        print("\n")
        print("- | O | -       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")
        print("\n")
        print("- | O | X       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")  
    elif pole == 3:
        print("\n")
        print("- | - | 0       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")
        print("\n")
        print("X | - | O       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")  
    elif pole == 4:
        print("\n")
        print("- | - | -       1 | 2 | 3")
        print("O | X | -       4 | 4 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")
        print("\n")
        print("- | - | X       1 | 2 | 3")
        print("O | X | -       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")  
    elif pole == 6:
        print("\n")
        print("- | - | -       1 | 2 | 3")
        print("- | X | 0       4 | 4 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")
        print("\n")
        print("- | - | X       1 | 2 | 3")
        print("- | X | O       4 | 5 | 6")
        print("- | - | -       7 | 8 | 9")
        print("\n")  
    elif pole == 7:
        print("\n")
        print("- | - | -       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("O | - | -       7 | 8 | 9")
        print("\n")
        print("\n")
        print("X | - | -       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("O | - | -       7 | 8 | 9")
        print("\n")  
    elif pole == 8:
        print("\n")
        print("- | - | -       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | O | -       7 | 8 | 9")
        print("\n")
        print("\n")
        print("- | - | X       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | O | -       7 | 8 | 9")
        print("\n")

    elif pole == 9:
        print("\n")
        print("- | - | -       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | 0       7 | 8 | 9")
        print("\n")
        print("\n")
        print("- | - | X       1 | 2 | 3")
        print("- | X | -       4 | 5 | 6")
        print("- | - | 0       7 | 8 | 9")
        print("\n")
    else:
        break