# os.remove(file) → Elimina un file.
import os

def elimina_file_sicuro():
    """Simula l'eliminazione sicura di un file."""

    percorso_file = input("Inserisci il percorso completo del file che vuoi eliminare: ")

    if not os.path.exists(percorso_file):
        print(f"Errore: Il file '{percorso_file}' non esiste.")
        return

    if not os.path.isfile(percorso_file):
        print(f"Errore: '{percorso_file}' non è un file.")
        return

    conferma = input(f"Sei sicuro di voler eliminare il file '{percorso_file}'? (sì/no): ").lower()

    if conferma == 'sì':
        try:
            os.remove(percorso_file)
            print(f"File '{percorso_file}' eliminato con successo.")
        except PermissionError:
            print(f"Errore: Non hai i permessi necessari per eliminare il file '{percorso_file}'.")
        except FileNotFoundError:
            # Questo caso è improbabile dato il controllo iniziale, ma è buona pratica includerlo
            print(f"Errore: Il file '{percorso_file}' non è stato trovato durante il tentativo di eliminazione.")
        except OSError as e:
            print(f"Si è verificato un errore durante l'eliminazione del file: {e}")
    else:
        print("Eliminazione annullata.")
    finally:
        print("Operazione di eliminazione completata.")

if __name__ == "__main__":
    elimina_file_sicuro()