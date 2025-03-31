# Le liste sono iterabili
mia_lista = [1, 2, 3]
for elemento in mia_lista:
    print(elemento)

# I dizionari sono iterabili sulle loro chiavi (per default)
mio_dizionario = {"a": 1, "b": 2}
for chiave in mio_dizionario:
    print(chiave)

# Le stringhe sono iterabili sui loro caratteri
mia_stringa = "ciao"
for carattere in mia_stringa:
    print(carattere)

# I file aperti sono iterabili sulle loro righe
with open("mio_file.txt", "w") as f:
    f.write("Riga 1\n")
    f.write("Riga 2\n")

with open("mio_file.txt", "r") as f:
    for riga in f:
        print(riga.strip())

# Utilizzo esplicito di iter() e next() (dietro le quinte del ciclo for)
iteratore_lista = iter(mia_lista)
print(next(iteratore_lista)) # Stampa 1
print(next(iteratore_lista)) # Stampa 2
# ... e così via, fino a StopIteration