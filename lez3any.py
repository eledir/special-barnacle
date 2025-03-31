# -*- coding: utf-8 -*-
# Lista con valori misti (True e False)
valori = [0, "", None, False, 42]  

# Controlliamo se almeno un elemento è True
if any(valori):  
    print("Almeno un valore  similvero")  
else:
    print("Tutti i valori sono similfalsi")

# Lista con valori tutti similfalsi
valori = [0, "", None, False, 0.0, [], {}]  

# Controlliamo se almeno un elemento è False
if any(valori):  
    print("Almeno un valore e similvero")  
else:
    print("Tutti i valori sono similfalsi")
