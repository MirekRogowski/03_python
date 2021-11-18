import os
from random import setstate
width, height =os.get_terminal_size()
width = width - 1

count_elements = 0
count_kg_packages = 0
count_packages = 0
max_weight_package = 20
min_weight_package = 20
current_weight_package = 0
#weight_package = 0
number_min_weight_package = 0

max_elements = int(input("Ile elementów chcesz spakować: "))
print("0 kończy program w dowolnej ")

while count_elements < max_elements:
    element_weight = int(input("Podaj wagę elementu dodanego do paczki "))
    if element_weight ==  "0" or element_weight < 1 or element_weight > 10:
        break
    if current_weight_package + element_weight <= max_weight_package: #check weight package  
        current_weight_package += element_weight
        print(f'Bieżąca waga paczki {current_weight_package}kg')
 
    else:
        weight_package = current_weight_package #count weight package
        count_kg_packages += weight_package  #count weight packages
        count_packages +=1  #count package
        #min weight package
        if min_weight_package >= current_weight_package:
            min_weight_package = current_weight_package
            number_min_weight_package = count_packages
        current_weight_package = element_weight
        print('*'*width)
        print(f"Paczka numer {count_packages} o wadze {weight_package} została wysłana")
        print(f"Do następnej paczki dodano {current_weight_package} kilogramów")
        print('*'*width)
    
    count_elements +=1  #liczy elementy
    if count_elements == max_elements:
        count_packages +=1 
        if min_weight_package >= current_weight_package:
            min_weight_package = current_weight_package
            number_min_weight_package = count_packages
        count_kg_packages += current_weight_package
        print('*'*width)
        print(f"Paczka numer {count_packages} o wadze {current_weight_package} została wysłana")
        print(f"To była ostania paczka")
        print('*'*width)
print(f"Liczba wysłanych paczek : {count_packages}")
print(f"Waga wszytkich paczek: {count_kg_packages} ")
print(f"Suma pustych kilogramów: {count_packages * max_weight_package - count_kg_packages}")
print(f"Paczka numer {number_min_weight_package} ma najwięcej pustych kilogramów - {max_weight_package - min_weight_package} kg") 
print('*'*width)
      

