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
        step12 = int(input("Wybierz numer pola: "))
        while step12 != 2 or step12 != 4 or step12 != 6 or step12 != 7 or step12 != 8 or step12 != 9:
            if step12 == 2:
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
                print("Przegrana\n")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    break 
                else:
                    print("\nKoniec\n")
                    exit()
            elif step12 == 4:
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
                print("Przegrana\n")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    break 
                else:
                    print("\nKoniec\n")
                    exit()       
            elif step12 == 6:
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
                print("Przegrana\n")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    break 
                else:
                    print("\nKoniec\n")
                    exit() 
            elif step12 == 7:
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
                step13 = int(input("Wybierz numer pola: "))
                while step13 != 2 or step13 != 6 or step13 != 8 or step13 != 9:
                    if step13 == 2:
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
                        print("Przegrana\n")
                        grastep13 = input("Chcesz grać dalej t - tak , n -nie: ")
                        if grastep13 == "t":
                            print("\n\nNowa gra")
                            break
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif step13 == 6:
                        print("\n")
                        print("O | - | X       1 | 2 | 3")
                        print("X | X | O       4 | 5 | 6")
                        print("0 | - | -       7 | 8 | 9")
                        print("\n")
                        print("\n")
                        print("O | - | X       1 | 2 | 3")
                        print("X | X | O       4 | 5 | 6")
                        print("0 | X | -       7 | 8 | 9")
                        print("\n")
                        step14 = int(input("Wybierz numer pola: "))
                        while step14 !=2 or step14 != 9:
                            if step14 == 2:
                                print("\n")
                                print("O | - | X       1 | 2 | 3")
                                print("X | X | O       4 | 5 | 6")
                                print("O | X | -       7 | 8 | 9")
                                print("\n")
                                print("\n")
                                print("O | 0 | X       1 | 2 | 3")
                                print("X | X | O       4 | 5 | 6")
                                print("0 | X | X       7 | 8 | 9")
                                print("\n")
                                print("\nRemis\n")
                                print("Koniec gry\n")
                                exit()
                            elif step14 == 9:
                                print("\n")
                                print("O | - | X       1 | 2 | 3")
                                print("X | X | O       4 | 5 | 6")
                                print("O | X | -       7 | 8 | 9")
                                print("\n")
                                print("\n")
                                print("O | X | X       1 | 2 | 3")
                                print("X | X | O       4 | 5 | 6")
                                print("0 | X | -       7 | 8 | 9")
                                print("\n")  
                                print("Przegrana\n")
                                grastep4 = input("Chcesz grać dalej t - tak , n -nie: ")
                                if grastep4 == "t":
                                    print("\n\nNowa gra")
                                    break
                                else:
                                    print("\nKoniec\n")
                                    exit()
                            else:
                                print("Błąd") 
                                step14 = int(input("Wprowadź prawidłową wartość: ") )
                                continue
                        

                    elif step13 == 8:
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
                        print("Przegrana\n")
                        grastep13 = input("Chcesz grać dalej t - tak , n -nie: ")
                        if grastep13 == "t":
                            print("\n\nNowa gra")
                            break
                        else:
                            print("\nKoniec\n")
                            exit()
                    elif step13 == 9:
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
                        print("Przegrana\n")
                        grastep13 = input("Chcesz grać dalej t - tak , n -nie: ")
                        if grastep13 == "t":
                            print("\n\nNowa gra")
                            break
                        else:
                            print("\nKoniec\n")
                            exit()
                    else:
                        print("Błąd") 
                        step13 = int(input("Wprowadź prawidłową wartość: ") )
                        continue            
    
            elif step12 == 8:
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
                print("Przegrana\n")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    break 
                else:
                    print("\nKoniec\n")
                    exit()
            elif step12 == 9:
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
                print("Przegrana\n")
                gra = input("Chcesz grać dalej t - tak , n -nie: ")
                if gra == "t":
                    print("\nNowa gra")
                    break 
                else:
                    print("\nKoniec\n")
                    exit()
            else:
                print("Błąd") 
                step12 = int(input("Wprowadź prawidłową wartość: ") )
                continue   
    #koniec dla pola numer 1
# to do obsługa
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
    elif step1 == 5:
        print("\nBłąd")
        print("Wprowadź prawidłowa wartość. ")
        continue
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