# Importa il modulo per interagire con il file system
import os  

# Richiede all'utente il percorso base principale
percorso_base = input("Inserisci la directory principale: ")  

# Costruisce un percorso complesso con 3 sottodirectory annidate
percorso_completo = os.path.join(percorso_base, "progetto", "docs", "reports")  

try:
    # Crea ricorsivamente tutte le directory mancanti
    # exist_ok=True: evita errori se la directory esiste già
    os.makedirs(percorso_completo, exist_ok=True)  
    
    # Verifica e stampa il percorso creato
    if os.path.exists(percorso_completo):
        print(f"Struttura creata: {os.path.abspath(percorso_completo)}")
        
except PermissionError as pe:
    # Gestione errori di permesso
    print(f"Errore permessi: {str(pe)}")
    
except FileExistsError as fee:
    # Caso particolare per sistemi che non supportano exist_ok
    print(f"Directory già esistente: {str(fee)}")
    
except Exception as e:
    # Gestione generica di altri errori
    print(f"Errore imprevisto: {str(e)}")
'''
os.makedirs() vs os.mkdir():

Copia
# mkdir crea solo l'ultima directory del percorso
# makedirs crea tutto l'albero delle directory mancanti
os.mkdir("a/b/c")       # Fallisce se a/b non esiste
os.makedirs("a/b/c")    # Crea a, poi b, poi c
Parametro mode avanzato:

Copia
# Imposta i permessi 755 (rwxr-xr-x)
os.makedirs("mio_dir", mode=0o755, exist_ok=True)
Best practice per percorsi complessi:

Copia
# Risolve automaticamente ../ e ~/
percorso = os.path.expanduser("~/documents/../projects")
# Normalizza il percorso: /home/user/projects
percorso_normalizzato = os.path.normpath(percorso)  
Esempio pratico di output:

Copia
Inserisci la directory principale: /home/user
Struttura creata: /home/user/progetto/docs/reports
Casi d'errore tipici:

FileExistsError: Se una delle directory intermedie è un file
PermissionError: Se mancano i permessi di scrittura
NotADirectoryError: Se un componente del percorso non è una directory
'''    
