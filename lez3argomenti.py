# -*- coding: utf-8 -*-
# # dichiaro variabile d
d = "Hello " \
"puo essere cambiata"
print(d)
d = "Visto che cambio!"
print(d)
#controllo se d è True o False
if d:
    print("d è similvero")
else:
    print("d è similfalso") 
'''
d è False in contesti booleani come: '
'd = '0' , d = '0.00'
'd =  [] lista vuota'
'd = 'None'
'd = 'False'  ... ora variamo d'
'''
d = '12.00'
if d:
    print("d è similvero")
else:
    print("d è similfalso") 
#argomenti.py
def calcola_stipendio(nome, stipendio_lordo, tasse=23, bonus=0):
    stipendio_netto = stipendio_lordo - (stipendio_lordo * tasse / 100) + bonus
    print(f"{nome} ha un netto di: {stipendio_netto}€")
    return stipendio_netto
#argomenti posizionali
calcola_stipendio("Gia", 1000)

#argomenti posizionali + keyword
calcola_stipendio("Luca",2000, tasse=25)

#keyword per modificare tutti i parametri 
calcola_stipendio(nome="Anna", stipendio_lordo=2500, tasse=  24, bonus=100) 

