import json  # Per gestire il database dei clienti
import os    # Per controllare l'esistenza del file JSON

# Nome del file per la persistenza dei dati
DB_FILE = 'fidelity_db.json'

def load_db():
    """Carica il database dei clienti da un file JSON."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_db(db):
    """Salva il database dei clienti su un file JSON."""
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)

def delete_db():
    """Elimina il database JSON e svuota il dizionario."""
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print("Database eliminato con successo.")
    else:
        print("Errore: il database non esiste.")

class FidelityCard:
    """Rappresenta la carta fedeltà di un cliente."""
    
    def __init__(self, customer_name, loyalty_card_type, points=0):
        self.customer_name = customer_name
        self.loyalty_card_type = loyalty_card_type
        self.points = points
    
    def get_tier_level(self):
        """Determina il livello della carta in base ai punti."""
        if self.loyalty_card_type != 'tiered':
            return None
        if self.points >= 1000:
            return 'Platinum'
        elif self.points >= 500:
            return 'Gold'
        elif self.points >= 200:
            return 'Silver'
        return 'Bronze'

    def add_points(self, points):
        """Aggiunge punti alla carta."""
        if points > 0:
            self.points += points
    
    def redeem_points(self, points):
        """Riscatta punti se disponibili."""
        if 0 < points <= self.points:
            self.points -= points
            return True
        return False
    
    def to_dict(self):
        """Converte l'oggetto in un dizionario per il salvataggio."""
        return {
            "customer_name": self.customer_name,
            "loyalty_card_type": self.loyalty_card_type,
            "points": self.points
        }
    
# Caricamento del database
fidelity_db = load_db()

# Menu interattivo
while True:
    cmd = input("comando: ")
    
    if cmd == 'chiudi':
        save_db(fidelity_db)
        exit()
    
    if cmd == 'aggiungi':
        name = input("  Nome cliente: ")
        card_type = input("  Tipo carta ('tiered' o altro): ")
        points = int(input("  Punti iniziali: "))
        if name not in fidelity_db:
            fidelity_db[name] = FidelityCard(name, card_type, points).to_dict()
            save_db(fidelity_db)
        else:
            print("Errore: cliente già esistente!")
    
    if cmd == 'mostra':
        print("--- Clienti registrati ---")
        for name, data in fidelity_db.items():
            card = FidelityCard(**data)
            print(f"Cliente: {card.customer_name}, Tipo: {card.loyalty_card_type}, Punti: {card.points}, Livello: {card.get_tier_level()}")
    
    if cmd == 'modifica':
        name = input("  Cliente da modificare: ")
        if name in fidelity_db:
            new_points = int(input("  Nuovi punti: "))
            fidelity_db[name]['points'] = new_points
            save_db(fidelity_db)
        else:
            print("Errore: cliente non trovato!")
    
    if cmd == 'elimina':
        name = input("  Cliente da eliminare: ")
        if name in fidelity_db:
            del fidelity_db[name]
            save_db(fidelity_db)
            print(f"Cliente '{name}' eliminato.")
        else:
            print("Errore: cliente non trovato!")
    
    if cmd == 'cancella_db':
        delete_db()
        fidelity_db = {}
