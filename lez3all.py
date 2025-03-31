# -*- coding: utf-8 -*-
# Lista con solo valori veri
valori = [1, "Hello", [3, 4], True]  

# Controlliamo se tutti gli elementi sono True
if all(valori):  
    print("Tutti i valori sono similveri")  
else:
    print("Almeno un valore  similfalso")




# Lista con solo valori falsi
valori = [0, "", None, False, 0.0, [], {}]  
# Controlliamo se tutti gli elementi sono False
if all(valori):  
    print("Tutti i valori sono similveri")  
else:
    print("Almeno un valore  similfalso")
