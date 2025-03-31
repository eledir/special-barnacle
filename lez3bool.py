# -*- coding: utf-8 -*-
# Lista di valori da testare con bool()
valori = [0, "", None, [], {}, "Python", 3.14, [1, 2, 3]]

# Stampiamo il valore booleano di ciascun elemento → Alt + 26 (tastierino numerico)
for v in valori:
    print(f"bool({v}) → {bool(v)}")