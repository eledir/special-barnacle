class FourDigitYearConverter:
    def __init__(self):
        """
        Inizializza la classe chiedendo all'utente di inserire un anno valido (quattro cifre numeriche).
        """
        while True:
            user_input = input("Inserisci anno (quattro cifre numeriche): ")
            if user_input.isdigit() and len(user_input) == 4:
                self.regex = user_input
                break  # Esce dal loop se l'input è valido
            else:
                print("Errore: Devi inserire solo quattro cifre numeriche. Riprova.")

    def to_python(self, value):
        """
        Converte una stringa numerica in un intero.
        """
        return int(value)

    def check_regex(self):
        """
        Verifica se l'attributo regex è valutato come True o False.
        """
        if self.regex:
            print(f"regex '{self.regex}' è valutata come True")
        else:
            print("regex è valutata come False")


# Creiamo un'istanza della classe (qui viene richiesto l'input)
converter = FourDigitYearConverter()

# Stampiamo il valore della regex e verifichiamo se è valutata come True
print(f"Valore inserito: {converter.regex}")
converter.check_regex()

  