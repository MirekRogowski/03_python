#variables

while True:
    print("\n")
    print("- | - | -       1 | 2 | 3")
    print("- | X | -       4 | 5 | 6")
    print("- | - | -       7 | 8 | 9")
    print("\n")
    step1 = int(input("Wybierz numer pola: "))
    if  step1 == 1:
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
        step2 = int(input("Wybierz numer pola: "))
        if step2 == 2:
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
        elif step2 == 4:
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
        elif step2 == 6:
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
        elif step2 == 7:
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
            step3 = int(input("Wybierz numer pola: "))
            if step3 == 2:
                print("\n")
                print("O | O | X       1 | 2 | 3")
                print("X | X | -       4 | 5 | 6")
                print("0 | - | -       7 | 8 | 9")
                print("\n")
                print("\n")
                print("O | O | X       1 | 2 | 3")
                print("X | X | X       4 | 5 | 6")
                print("0 | - | -       7 | 8 | 9")
                print("\n")
                print("Przegrana")
                grastep3 = input("Chcesz grać dalej t - tak , n -nie ")
                if grastep3 == "t":
                    print("\nNowa gra")
                    continue
                else:
                    break  
            elif step3 == 6:
                print("\n")
                print("O | - | X       1 | 2 | 3")
                print("X | X | O       4 | 5 | 6")
                print("0 | - | -       7 | 8 | 9")
                print("\n")
                print("\n")
                print("O | - | X       1 | 2 | 3")
                print("X | X | O       4 | 5 | 6")
                print("0 | - | -       7 | 8 | 9")
                print("\n")
                print("Przegrana")
                grastep3 = input("Chcesz grać dalej t - tak , n -nie ")
                if grastep3 == "t":
                    print("\nNowa gra")
                    continue
                else:
                    break  
            elif step3 == 8:
                print("\n")
                print("O | - | X       1 | 2 | 3")
                print("X | X | -       4 | 5 | 6")
                print("0 | - | -       7 | 8 | 9")
                print("\n")
                print("\n")
                print("O | - | X       1 | 2 | 3")
                print("X | X | X       4 | 5 | 6")
                print("0 | 0 | -       7 | 8 | 9")
                print("\n")
                print("Przegrana")
                grastep3 = input("Chcesz grać dalej t - tak , n -nie ")
                if grastep3 == "t":
                    print("\nNowa gra")
                    continue
                else:
                    break  
            elif step3 == 9:
                print("\n")
                print("O | - | X       1 | 2 | 3")
                print("X | X | -       4 | 5 | 6")
                print("0 | - | O       7 | 8 | 9")
                print("\n")
                print("\n")
                print("O | - | X       1 | 2 | 3")
                print("X | X | X       4 | 5 | 6")
                print("0 | - | O       7 | 8 | 9")
                print("\n")
                print("Przegrana")
                grastep3 = input("Chcesz grać dalej t - tak , n -nie ")
                if grastep3 == "t":
                    print("\nNowa gra")
                    continue
                else:
                    break  
 
        elif step2 == 8:
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
            gra = input("Chcesz grać step2 t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break  
        elif step2 == 9:
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
            gra = input("Chcesz grać step2 t - tak , n -nie ")
            if gra == "t":
                print("Nowa gra")
                continue
            else:
                break  
    #koniec dla pola numer 1
    elif step1 == 2:
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
    elif step1 == 3:
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
    elif step1 == 4:
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
    elif step1 == 6:
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
    elif step1 == 7:
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
    elif step1 == 8:
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

    elif step1 == 9:
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