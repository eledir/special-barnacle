# shutil.copy(src, dst)
import shutil
import os
import datetime

def gestione_copia_file():
    """Simula la copia di file per backup o gestione."""

    print("Simulazione di copia file con shutil.copy()")

    file_da_copiare = input("Inserisci il percorso completo del file che vuoi copiare: ")

    if not os.path.isfile(file_da_copiare):
        print(f"Errore: Il file '{file_da_copiare}' non esiste o non è un file valido.")
        return

    destinazione = input("Inserisci il percorso completo della destinazione (cartella o nuovo nome file): ")

    try:
        if os.path.isdir(destinazione):
            # Se la destinazione è una cartella, il file verrà copiato lì con lo stesso nome
            nome_file = os.path.basename(file_da_copiare)
            destinazione_completa = os.path.join(destinazione, nome_file)
            shutil.copy(file_da_copiare, destinazione_completa)
            print(f"File '{nome_file}' copiato con successo in '{destinazione}'.")
        else:
            # Se la destinazione non è una cartella, viene interpretata come il nuovo nome del file
            shutil.copy(file_da_copiare, destinazione)
            print(f"File '{os.path.basename(file_da_copiare)}' copiato con successo come '{os.path.basename(destinazione)}'.")

    except FileNotFoundError:
        print(f"Errore: Il file sorgente '{file_da_copiare}' non è stato trovato.")
    except PermissionError:
        print(f"Errore: Non hai i permessi necessari per leggere il file sorgente o scrivere nella destinazione.")
    except OSError as e:
        print(f"Si è verificato un errore durante la copia: {e}")
    finally:
        print("Operazione di copia completata.")

def scenario_backup():
    """Simula uno scenario di backup di file."""

    cartella_da_backuppare = input("Inserisci il percorso della cartella di cui vuoi fare il backup: ")
    cartella_backup = input("Inserisci il percorso della cartella di backup: ")

    if not os.path.isdir(cartella_da_backuppare):
        print(f"Errore: La cartella sorgente '{cartella_da_backuppare}' non esiste o non è una cartella valida.")
        return
    if not os.path.isdir(cartella_backup):
        try:
            os.makedirs(cartella_backup, exist_ok=True)
            print(f"Cartella di backup '{cartella_backup}' creata.")
        except OSError as e:
            print(f"Errore durante la creazione della cartella di backup: {e}")
            return

    data_backup = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    cartella_backup_data = os.path.join(cartella_backup, f"backup_{data_backup}")

    try:
        os.makedirs(cartella_backup_data)
        print(f"\nCreazione cartella di backup: '{cartella_backup_data}'")

        for nome_file in os.listdir(cartella_da_backuppare):
            percorso_completo_sorgente = os.path.join(cartella_da_backuppare, nome_file)
            percorso_completo_destinazione = os.path.join(cartella_backup_data, nome_file)
            if os.path.isfile(percorso_completo_sorgente):
                shutil.copy(percorso_completo_sorgente, percorso_completo_destinazione)
                print(f"Copiato: '{nome_file}'")

        print("\nBackup completato con successo!")

    except FileNotFoundError:
        print(f"Errore: Una delle cartelle non è stata trovata.")
    except PermissionError:
        print("Errore: Problemi di permessi durante il backup.")
    except OSError as e:
        print(f"Si è verificato un errore durante il backup: {e}")
    finally:
        print("Operazione di backup terminata.")

if __name__ == "__main__":
    while True:
        print("\nScegli un'operazione:")
        print("1. Copia un singolo file")
        print("2. Simula un backup di una cartella")
        print("3. Esci")

        scelta = input("Inserisci il numero dell'operazione: ")

        if scelta == '1':
            gestione_copia_file()
        elif scelta == '2':
            scenario_backup()
        elif scelta == '3':
            print("Uscita.")
            break
        else:
            print("Scelta non valida. Riprova.")