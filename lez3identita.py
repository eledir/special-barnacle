# -*- coding: utf-8 -*-


# Creiamo due liste con lo stesso contenuto
a = [1, 2, 3]
b = [1, 2, 3]

# Creiamo una variabile che punta alla stessa lista di 'a'
c = a  

# Controlliamo l'identità degli oggetti
print("a == b:", a == b)      # Confronto del valore (True, perché hanno lo stesso contenuto)
print("a is b:", a is b)      # Confronto dell'identità (False, perché sono due oggetti diversi)
print("a is c:", a is c)      # True, perché c è un riferimento alla stessa lista di a
print("b is not c:", b is not c)  # True, perché b è un oggetto separato

# Verifica con valori immutabili
x = 10
y = 10

print("x is y:", x is y)  # True, perché Python ottimizza gli interi piccoli e riutilizza la stessa memoria


# Variabile con valore None
valore = None

# Controllo corretto dell'identità con None
if valore is None:
    print("La variabile e None")
else:
    print("La variabile ha un valore")