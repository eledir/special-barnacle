import os

def interazione_apertura_file():
    """Simula l'interazione di apertura di un file nella vita reale."""

    nome_file = input("Inserisci il nome del file che vuoi aprire: ")

    # Verifica se il file esiste nella directory corrente
    if not os.path.exists(nome_file):
        print(f"Errore: Il file '{nome_file}' non esiste nella directory corrente.")
        return

    modalita = input("Inserisci la modalità di apertura (lettura 'r', scrittura 'w', append 'a', lettura e scrittura 'r+', ecc.): ")

    try:
        with open(nome_file, modalita) as file:
            print(f"File '{nome_file}' aperto con successo in modalità '{modalita}'.")

            if modalita == 'r':
                contenuto = file.read()
                print("\nContenuto del file:")
                print(contenuto)
            elif modalita == 'w':
                nuovo_contenuto = input("\nInserisci il testo che vuoi scrivere nel file (sovrascriverà il contenuto esistente): ")
                file.write(nuovo_contenuto)
                print("Testo scritto nel file.")
            elif modalita == 'a':
                nuovo_contenuto = input("\nInserisci il testo che vuoi aggiungere al file: ")
                file.write(nuovo_contenuto + "\n") # Aggiunge una nuova linea per chiarezza
                print("Testo aggiunto al file.")
            elif modalita == 'r+':
                print("\nPuoi leggere e scrivere nel file. Ricorda che la posizione del cursore influenzerà le operazioni.")
                # Qui si potrebbero aggiungere ulteriori interazioni per lettura e scrittura
            else:
                print("\nModalità non gestita specificamente in questo esempio.")

    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non è stato trovato (anche se la verifica iniziale è fallita, questo è un controllo aggiuntivo).")
    except PermissionError:
        print(f"Errore: Non hai i permessi necessari per aprire il file '{nome_file}' in modalità '{modalita}'.")
    except Exception as e:
        print(f"Si è verificato un errore inaspettato: {e}")
    finally:
        print("Operazione di apertura/chiusura file completata.")

if __name__ == "__main__":
    interazione_apertura_file()