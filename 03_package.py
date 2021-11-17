import os
from random import setstate
width, height =os.get_terminal_size()
width = width - 1

count_packages = 0
count_kg_packages = 0
max_weight_package = 20
min_weight_package = 20
current_weight_package = 0
#weight_package = 0
number_min_weight_package = 0

max_packages = int(input("Ile paczek chcesz wysłać: "))
print("0 kończy program w dowolnej ")

while count_packages < max_packages:
    element_weight_package = int(input("Podaj wagę pojedyńczej pozycji w pacze: "))
    if element_weight_package ==  "0" or element_weight_package < 1 or element_weight_package > 10:
        break
    if current_weight_package + element_weight_package <= max_weight_package:
        current_weight_package += element_weight_package
        print(f'Bieżąca waga paczki {current_weight_package}kg')
    else:
        weight_package = current_weight_package
        count_kg_packages += weight_package
        count_packages +=1
        if min_weight_package >= current_weight_package:
            min_weight_package = current_weight_package
            number_min_weight_package = count_packages
        current_weight_package = element_weight_package
        print('*'*width)
        print(f"Paczka numer {count_packages} o wadze {weight_package} została wysłana")
        print('*'*width)
        print(f"Do następnej paczki waży {current_weight_package} kilogramów")
        print('*'*width)

print(f"Liczba wysłanych paczek : {count_packages}")
print(f"Waga wszytkich paczek: {count_kg_packages} ")
print(f"Suma pustych kilogramów: {count_packages * max_weight_package - count_kg_packages}")
print(f"Paczka numer {number_min_weight_package} ma najwięcej pustych kilogramów - {max_weight_package - min_weight_package} kg") 


print('Goodbye !')        