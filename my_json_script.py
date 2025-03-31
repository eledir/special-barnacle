# -*- coding: utf-8 -*-
# Importa il modulo json integrato, che fornisce funzionalità per lavorare con dati JSON.
import json


# --- Esempio 1: Lettura di dati JSON da un file usando json.load() ---

# Supponiamo di avere un file denominato 'data.json' con il seguente contenuto:
# {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# Definiamo il percorso del file JSON.
file_path = r"C:\Users\utente\Downloads\data.json"

try:
    # Apre il file JSON
    # Il file è stato aperto in modalità lettura ('r') prima di passarlo a json.load().
    with open(file_path, 'r', encoding='utf-8') as file:  # file è un oggetto file che punta ai dati contenuti in data.json.
        
        # Legge il contenuto del file
        # json.load(file) legge tutto il contenuto del file JSON.
        # Supponiamo che il file contenga:
        # {
        #   "name": "Alice",
        #   "age": 30,
        #   "city": "New York"
        # }
        
        # Converte il JSON in un oggetto Python
        # json.load(file) converte automaticamente il contenuto JSON in un dizionario Python:
        # {
        #     "name": "Alice",
        #     "age": 30,
        #     "city": "New York"
        # }
        # Questo viene memorizzato nella variabile data_from_file.
        data_from_file = json.load(file)

    # Ora 'data_from_file' è un dizionario Python contenente i dati del file JSON.
    print("Dati letti dal file (json.load()):")
    print(data_from_file)
    print(f"Tipo di dati: {type(data_from_file)}")
    print(f"Nome: {data_from_file['name']}")
    print(f"Età: {data_from_file['age']}")
    print(f"Città: {data_from_file['city']}")

    # Il file viene chiuso automaticamente
    # Grazie al with open(...), non serve chiamare file.close().
    # Il file si chiude automaticamente dopo l'uscita dal blocco with.

except FileNotFoundError:
    # Gestiamo il caso in cui il file specificato non esista.
    print(f"Errore: File non trovato in '{file_path}'")
except json.JSONDecodeError as e:
    # Gestiamo gli errori che si verificano se il file non contiene dati JSON validi.
    print(f"Errore nella decodifica JSON dal file '{file_path}': {e}")

print("\n" + "-"*30 + "\n")

# --- Esempio 2: Lettura di dati JSON da una stringa usando json.loads() ---

# Supponiamo di avere una stringa JSON come questa:
json_string = '{"name": "Bob", "age": 25, "country": "Canada"}'

try:
    # Usiamo json.loads() per analizzare la stringa JSON.
    # json.loads() prende una stringa formattata JSON come input e restituisce l'oggetto Python corrispondente.
    data_from_string = json.loads(json_string)

    # Ora 'data_from_string' è un dizionario Python creato dalla stringa JSON.
    print("Dati letti dalla stringa (json.loads()):")
    print(data_from_string)
    print(f"Tipo di dati: {type(data_from_string)}")
    print(f"Nome: {data_from_string['name']}")
    print(f"Età: {data_from_string['age']}")
    print(f"Paese: {data_from_string['country']}")

except json.JSONDecodeError as e:
    # Gestiamo gli errori che si verificano se la stringa non è JSON valido.
    print(f"Errore nella decodifica JSON dalla stringa: {e}")

# Nota: Per eseguire con successo il primo esempio, dovresti creare manualmente il file 'data.json' 
# con il contenuto indicato nel commento all'inizio del codice.
