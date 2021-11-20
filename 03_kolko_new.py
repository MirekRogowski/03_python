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
        while True:
            p12 = input("Wybierz pole: ")
            if p12 == "2":
                p2 = "O"
                p7 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9) 
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "4":
                p4 = "O"
                p7 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9) 
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "6":
                p6 = "O"
                p7 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9) 
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "7":
                p7 = "O"
                p4 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                while True:
                    p123 = input("Wybierz pole: ")
                    if p123 == "2":
                        p2 = "O"
                        p6 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p123 == "6":
                        p6 = "O"
                        p8 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        p1234 = input("Wybierz pole: ")
                        while True:
                            if p1234 == "2":
                                p2 = "O"
                                p9 = "X"
                                print(p1+p2+p3)
                                print(p4+p5+p6)
                                print(p7+p8+p9)
                                print("\nRemis\n")
                                exit()
                            elif p1234 == "9":
                                p9 = "O"
                                p2 = "X"
                                print(p1+p2+p3)
                                print(p4+p5+p6)
                                print(p7+p8+p9)
                                print("\nPrzegrana")
                                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                                if gra == "t":
                                    print("\nNowa gra")
                                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                                    p5 = "X"
                                    print(p1+p2+p3)
                                    print(p4+p5+p6)
                                    print(p7+p8+p9)
                                    break           
                                else:
                                    print("\nKoniec\n")
                                    exit()
                            else:
                                print("\nBłąd")
                                print("Wprowadź prawidłową wartość. \n") 
                    elif p123 == "8":
                        p8 = "O"
                        p6 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p123 == "9":
                        p9 = "O"
                        p6 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break           
                        else:
                            print("\nKoniec\n")
                            exit()
                    else:
                        print("\nBłąd")
                        print("Wprowadź prawidłową wartość. \n")
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)                
                        continue
                break         
            elif p12 == "8":
                p8 = "O"
                p7 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9) 
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "9":
                p6 = "O"
                p7 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9) 
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            else:
                print("\nBłąd")
                print("12 Wprowadź prawidłową wartość. \n")
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)                
                continue
    elif p == "2":
        p2 = "O"
        p1 = "X"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
        while True:
            p12 = input("Wybierz pole: ")
            if p12 == "3":
                p3 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "4":
                p4 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "6":
                p6 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "7":
                p7 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "8":
                p8 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p12 == "9":
                p9 = "O"
                p7 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                while True:
                    p123 = input("Wybierz pole: ")
                    if p123 == "3":
                        p3 = "O"
                        p4 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p123 == "4":
                        p4 = "O"
                        p3 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p123 == "6":
                        p6 = "O"
                        p3 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p123 == "8":
                        p8 = "O"
                        p3 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    else:
                        print("\nBłąd")
                        print("Wprowadź prawidłową wartość. \n")
                        continue
                break
            else:
                print("\nBłąd")
                print("Wprowadź prawidłową wartość. \n")
                continue

    elif p == "4":
        p4 = "O"
        p1 = "X"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
        while True:
            p14 = input("Wybierz pole: ")
            if p14 == "2":
                p2 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p14 == "3":
                p3 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p14 == "6":
                p6 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p14 == "7":
                p7 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p14 == "8":
                p8 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p14 == "9":
                p9 = "O"
                p3 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                while True:
                    p143 = input("Wybierz pole: ")
                    if p143 == "2":
                        p2= "O"
                        p7 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p143 == "6":
                        p6 = "O"
                        p7 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p143 == "7":
                        p7 = "O"
                        p2 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p143 == "8":
                        p8 = "O"
                        p7 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    else:
                        print("\nBłąd")
                        print("Wprowadź prawidłową wartość. \n")
                        continue
                break
            else:
                print("\nBłąd")
                print("Wprowadź prawidłową wartość. \n")
                continue


    elif p == "8":
        p8 = "O"
        p1 = "X"
        print(p1+p2+p3)
        print(p4+p5+p6)
        print(p7+p8+p9)
        while True:
            p18 = input("Wybierz pole: ")
            if p18 == "2":
                p2 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p18 == "3":
                p3 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p18 == "4":
                p4 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p18 == "6":
                p6 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p18 == "7":
                p6 = "O"
                p9 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                print("\nPrzegrana")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                    p5 = "X"
                    print(p1+p2+p3)
                    print(p4+p5+p6)
                    print(p7+p8+p9)
                    break            
                else:
                    print("\nKoniec\n")
                    exit()
            elif p18 == "9":
                p9 = "O"
                p7 = "X"
                print(p1+p2+p3)
                print(p4+p5+p6)
                print(p7+p8+p9)
                while True:
                    p183 = input("Wybierz pole: ")
                    if p183 == "2":
                        p2 = "O"
                        p4 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p183 == "3":
                        p3 = "O"
                        p4 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p183 == "4":
                        p4 = "O"
                        p3 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif p183 == "6":
                        p6 = "O"
                        p3 = "X"
                        print(p1+p2+p3)
                        print(p4+p5+p6)
                        print(p7+p8+p9)
                        print("\nPrzegrana")
                        gra = input("Chcesz grać dalej t - tak , n -nie: ")
                        if gra == "t":
                            print("\nNowa gra")
                            p1 = p2 = p3 = p4 = p6 = p7 = p8 = p9 = "-"
                            p5 = "X"
                            print(p1+p2+p3)
                            print(p4+p5+p6)
                            print(p7+p8+p9)
                            break            
                        else:
                            print("\nKoniec\n")
                            exit()
                    else:
                        print("\nBłąd")
                        print("Wprowadź prawidłową wartość. \n")
                        continue
                break
            else:
                print("\nBłąd")
                print("183 Wprowadź prawidłową wartość. \n")
                continue
    # elif p == "9":
    #     p1 = "X"
    #     p9 = "O"
    #     print(p1+p2+p3)
    #     print(p4+p5+p6)
    #     print(p7+p8+p9)
    else:
        print("\nBłąd")
        print("-test Wprowadź prawidłową wartość. \n")
        continue

