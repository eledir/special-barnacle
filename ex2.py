import json  # Importa il modulo json per lavorare con file JSON
import os    # Importa il modulo os per interagire con il sistema operativo

# Inizializza un dizionario vuoto per memorizzare gli utenti e le loro password
db = {}

# Funzione per mascherare la password
def mask(password):
    if len(password) < 2:
        return password
    else:
        return password[0] + ('*' * (len(password) - 2)) + password[-1]

# Funzione per caricare il database da un file
def load_db(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

# Funzione per salvare il database in un file
def save_db(filename):
    with open(filename, 'w') as f:
        json.dump(db, f)

# Funzione per eliminare il file del database
def delete_db(filename):
    if os.path.exists(filename):
        os.remove(filename)  # Rimuove il file
        print(f"Database '{filename}' eliminato con successo.")
        global db  # Rende il dizionario db accessibile globalmente
        db.clear()  # Svuota il dizionario db
    else:
        print(f"Errore: il file '{filename}' non esiste.")

# Carica il database all'avvio del programma
db = load_db('database.json')

# Ciclo infinito per ricevere comandi dall'utente
while True:
    cmd = input('comando: ')

    if cmd == 'chiudi':
        save_db('database.json')  # Salva il database prima di chiudere
        exit()
    
    if cmd == 'aggiungi':
        user = input('  username: ')
        pwd = input('  password: ')
        if user not in db:
            db[user] = pwd
            save_db('database.json')  # Salva il database dopo l'aggiunta
        else:
            print("Errore: l'utente è già presente!")
    
    if cmd == 'mostra':
        n = len(db)  # Calcola il numero di utenti nel database
        print('numero di utenti:', n)
        for user in db:
            print('utente:', user, 'password:', mask(db[user]))
    
    if cmd == 'elimina':
        user = input('  username da eliminare: ')
        if user in db:
            del db[user]
            save_db('database.json')  # Salva il database dopo l'eliminazione
            print(f"Utente '{user}' eliminato con successo.")
        else:
            print("Errore: l'utente non esiste!")
    
    if cmd == 'modifica':
        user = input('  username da modificare: ')
        if user in db:
            new_pwd = input('  nuova password: ')
            db[user] = new_pwd
            save_db('database.json')  # Salva il database dopo la modifica
            print(f"Password per l'utente '{user}' modificata con successo.")
        else:
            print("Errore: l'utente non esiste!")

    # Se il comando è 'cancella_db', elimina il file del database
    if cmd == 'cancella_db':
        delete_db('database.json')  # Chiama la funzione per eliminare il database

# Stampa il contenuto del database (non verrà mai raggiunto a causa del ciclo infinito)
print('database:', db)

