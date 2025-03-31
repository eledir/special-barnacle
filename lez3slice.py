# -*- coding: utf-8 -*-

# Creiamo una lista di numeri
numeri = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Creiamo degli oggetti slice
prima_meta = slice(0, 5)       # Primi 5 elementi
numeri_pari = slice(1, None, 2)  # Numeri in posizione dispari

# Usiamo gli slice sulla lista
print("Prima metaa:", numeri[prima_meta])
print("Elementi in posizione dispari:", numeri[numeri_pari])
