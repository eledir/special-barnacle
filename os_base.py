# Importa il modulo os per interagire con il file system
import os  

# Richiedi all'utente di inserire il percorso base tramite input
base_dir = input("Inserisci percorso base: ")  

# Combina il percorso base con la cartella "templates" usando os.path.join
# per garantire compatibilità cross-OS (Windows/Linux/Mac)
templates_dir = os.path.join(base_dir, "templates")  

# Verifica se la directory templates esiste già
if not os.path.exists(templates_dir):  
    # Crea ricorsivamente tutta la struttura di cartelle necessaria
    os.makedirs(templates_dir)  
    # Stampa il percorso assoluto normalizzato della nuova cartella
    print(f"Cartella creata: {os.path.abspath(templates_dir)}")  
else:
    # Se la cartella esiste già, stampa il percorso corrente
    print(f"Esistente: {templates_dir}")  

