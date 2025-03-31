import csv
import os
from django.conf import settings
from .models import Customer  # Assicurati che il modello Customer sia importato correttamente

def append_customer_to_csv(customer):
    # Percorso del file CSV
    csv_file_path = r'D:\250214Python\FidelityCardManager\fidelity_card_project\clienti_hair.csv'
    
    # Controlla se il file esiste, se non esiste, crea il file e aggiungi l'intestazione
    file_exists = os.path.isfile(csv_file_path)
    
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Scrivi l'intestazione se il file è nuovo
        if not file_exists:
            writer.writerow(['nomecognome', 'email'])  # Aggiungi intestazione
        
        # Scrivi i dati del nuovo cliente
        writer.writerow([customer.name, customer.email])

# Esempio di utilizzo dopo la registrazione di un cliente
def register_customer(name, email, password, loyalty_card_type):
    # Logica di registrazione del cliente
    new_customer = Customer(name=name, email=email, password=password, loyalty_card_type=loyalty_card_type)
    new_customer.save()  # Salva il cliente nel database
    
    # Aggiungi il cliente al CSV
    append_customer_to_csv(new_customer)

# Chiamata di esempio
# register_customer('Mario Rossi', 'mario.rossi@example.com', 'securepassword', 'points')
