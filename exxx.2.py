import os

# Dizionario vuoto per memorizzare username e password
credenziali = {}

# Richiesta input utente
username = input("Inserisci il tuo username: ")
password = input("Inserisci la tua password: ")

# Salvataggio nel dizionario
credenziali[username] = password

# Percorso del file da controllare
file_path = r"C:\Users\utente\Desktop\credenziali.txt"


# Verifica se il file esiste
dice_esiste = os.path.exists(file_path)

if dice_esiste:
    print(f"Il file '{file_path}' esiste.")
else:
    print(f"Il file '{file_path}' non esiste. Creazione del file...")
    with open(file_path, "w") as file:
        for user, pwd in credenziali.items():
            file.write(f"{user}:{pwd}\n")
    print(f"File '{file_path}' creato con successo.")

# Verifica lettura del file
with open(file_path, "r") as file:
    print("Contenuto del file salvato:")
    print(file.read())
