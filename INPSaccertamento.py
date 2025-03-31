

import datetime  # Importazione del modulo datetime per la gestione delle date

# Altre funzioni e codice...

def view_tasks():
    """Visualizza la to-do list."""
    if not to_do_list:
        print("La to-do list è vuota.")  # Messaggio se la lista è vuota
    else:
        for i, task in enumerate(to_do_list, start=1):
            # Converte la data di scadenza da stringa a oggetto datetime
            due_date = datetime.datetime.strptime(task['due_date'], '%d/%m/%Y')  
            # Stampa il numero, il task e la data di scadenza formattata
            print(f"{i}. {task['task']} - Scadenza: {due_date.strftime('%d/%m/%Y')}")

# Altre funzioni e codice...

if __name__ == "__main__":
    to_do_list = []  # Inizializza una lista vuota per i task

    while True:
        # Stampa il menu delle opzioni
        print("\nMenu:")
        print("1. Aggiungi un nuovo task")
        print("2. Visualizza la to-do list")
        print("3. Rimuovi un task")
        print("4. Inizializza la to-do list per l'avviso di addebito INPS")
        print("5. Esci")
        
        option = input("Seleziona un'opzione (1-5): ")  # Richiesta di input all'utente

        if option == "1":
            # Opzione per aggiungere un nuovo task
            task = input("Inserisci il nuovo task: ")
            due_date = input("Inserisci la data di scadenza (gg/mm/aaaa): ")
            to_do_list.append({"task": task, "due_date": due_date})  # Aggiunge il task alla lista
            print("Task aggiunto correttamente.")
        elif option == "2":
            # Opzione per visualizzare la to-do list
            view_tasks()
        elif option == "3":
            # Opzione per rimuovere un task
            view_tasks()  # Mostra la lista dei task
            task_num = int(input("Inserisci il numero del task da rimuovere: "))  # Richiesta di input
            if 0 < task_num <= len(to_do_list):
                to_do_list.pop(task_num - 1)  # Rimuove il task dalla lista
                print("Task rimosso correttamente.")
            else:
                print("Numero del task non valido.")  # Messaggio di errore se il numero non è valido
        elif option == "4":
            # Opzione per inizializzare la to-do list per l'avviso di addebito INPS
            to_do_list = [
                {"task": "Controlla la notifica di addebito", "due_date": "31/03/2025"},
                {"task": "Verifica i dettagli dell'addebito", "due_date": "07/04/2025"},
                {"task": "Contatta l'INPS per chiarimenti", "due_date": "14/04/2025"},
                {"task": "Effettua il pagamento", "due_date": "21/04/2025"},
                {"task": "Conferma l'avvenuto pagamento", "due_date": "28/04/2025"}
            ]
            print("To-do list per l'avviso di addebito INPS inizializzata correttamente.")
        elif option == "5":
            print("Uscita dal programma.")  # Messaggio di uscita
            break  # Esce dal ciclo
        else:
            print("Opzione non valida. Riprova.")  # Messaggio di errore per opzione non valida



