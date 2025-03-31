mio_dizionario = {"nome": "Alice", "eta": 30}
print(mio_dizionario["nome"]) # Accesso tramite chiave
print(len(mio_dizionario))    # Ottenere il numero di elementi
print("eta" in mio_dizionario) # Verifica se una chiave esiste
print(mio_dizionario.keys())   # Ottenere una vista sulle chiavi
print(mio_dizionario.values()) # Ottenere una vista sui valori
print(mio_dizionario.items())  # Ottenere una vista sulle coppie (chiave, valore)
print(mio_dizionario.get("citta", "Sconosciuta")) # Ottenere un valore con un valore predefinito