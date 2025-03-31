from datetime import datetime

class Caso:
    def __init__(self, name, case_number, account, status, priority, case_type, created_on, is_active):
        """Inizializza un nuovo caso con i dettagli forniti."""
        self.name = name                  # Nome del cliente o del caso
        self.case_number = case_number    # Numero identificativo del caso
        self.account = account            # Account associato al caso
        self.status = status              # Stato del caso (es. aperto, chiuso)
        self.priority = priority          # Priorità del caso (es. alta, media, bassa)
        self.case_type = case_type        # Tipo di caso (es. richiesta, reclamo)
        self.created_on = created_on      # Data di creazione del caso
        self.is_active = is_active        # Indica se il caso è attivo o meno

    @property
    def days_open(self):
        """Calcola il numero di giorni da quando il caso è stato creato."""
        return (datetime.now() - self.created_on).days

    def __str__(self):
        """Restituisce una rappresentazione in forma di stringa del caso."""
        return (f"Nome: {self.name}, "
                f"Numero Caso: {self.case_number}, "
                f"Account: {self.account}, "
                f"Stato: {self.status}, "
                f"Priorità: {self.priority}, "
                f"Tipo di Caso: {self.case_type}, "
                f"Creato il: {self.created_on.date()}, "
                f"Giorni Aperti: {self.days_open}, "
                f"Attivo: {'Sì' if self.is_active else 'No'}")

# Creazione di alcuni casi
caso1 = Caso("Mario Rossi", "C001", "Account A", "Aperto", "Alta", "Richiesta", datetime(2025, 3, 1), True)
caso2 = Caso("Giulia Bianchi", "C002", "Account B", "Chiuso", "Media", "Reclamo", datetime(2025, 2, 15), False)
caso3 = Caso("Luca Verdi", "C003", "Account C", "Aperto", "Bassa", "Richiesta", datetime(2025, 3, 10), True)

# Stampa dei dettagli dei casi
print(caso1)  # Dettagli di caso1
print(caso2)  # Dettagli di caso2
print(caso3)  # Dettagli di caso3

# Filtraggio dei casi attivi
casi_attivi = [caso for caso in [caso1, caso2, caso3] if caso.is_active]
print("\nCasi attivi:")
for caso in casi_attivi:
    print(caso)
