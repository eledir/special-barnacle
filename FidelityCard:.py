class FidelityCard:
    """Rappresenta la carta fedeltà di un cliente con un sistema a livelli."""

    def __init__(self, customer_name, loyalty_card_type, points=0):
        """
        Inizializza la carta fedeltà con i dettagli del cliente.

        :param customer_name: Nome del cliente.
        :param loyalty_card_type: Tipo di carta fedeltà ('tiered' o altri tipi).
        :param points: Punti iniziali sulla carta (predefinito è 0).
        """
        self.customer_name = customer_name  # Memorizza il nome del cliente
        self.loyalty_card_type = loyalty_card_type  # Memorizza il tipo di carta fedeltà
        self.points = points  # Memorizza il numero di punti sulla carta

    def get_tier_level(self):
        """Restituisce il livello della carta fedeltà in base ai punti accumulati."""
        if self.loyalty_card_type != 'tiered':  # Controlla se la carta è di tipo 'tiered'
            return None  # Se non è di tipo 'tiered', non ha livelli
        
        # Determina il livello della carta in base ai punti accumulati
        if self.points >= 1000:
            return 'Platinum'  # Livello massimo
        elif self.points >= 500:
            return 'Gold'  # Livello oro
        elif self.points >= 200:
            return 'Silver'  # Livello argento
        else:
            return 'Bronze'  # Livello base

    def add_points(self, points):
        """
        Aggiunge punti alla carta fedeltà.

        :param points: Numero di punti da aggiungere.
        """
        if points > 0:  # Verifica che i punti da aggiungere siano validi
            self.points += points  # Aggiunge i punti alla carta

    def redeem_points(self, points):
        """
        Permette di riscattare punti dalla carta fedeltà.

        :param points: Numero di punti da riscattare.
        :return: True se il riscatto è riuscito, False altrimenti.
        """
        if 0 < points <= self.points:  # Verifica che ci siano abbastanza punti per il riscatto
            self.points -= points  # Sottrae i punti dalla carta
            return True  # Conferma il successo del riscatto
        return False  # Se i punti non sono sufficienti, restituisce False

    def __str__(self):
        """Restituisce una rappresentazione in stringa della carta fedeltà."""
        return (f"Cliente: {self.customer_name}, "  # Nome del cliente
                f"Tipo Carta: {self.loyalty_card_type}, "  # Tipo di carta
                f"Punti: {self.points}, "  # Numero di punti
                f"Livello: {self.get_tier_level()}")  # Livello della carta

# Esempio di utilizzo:
card = FidelityCard("Alice", "tiered", 600)  # Crea una carta con 600 punti
print(card)  # Stampa i dettagli della carta (dovrebbe essere Gold)
card.add_points(500)  # Aggiunge 500 punti alla carta
print(card.get_tier_level())  # Ora dovrebbe essere Platinum
