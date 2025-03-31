class TwoDigitMonthConverter:
    def __init__(self):
        #definiamo mesi  01-12 solo cifre usiamo while True
        while True:
            mese_input = input("mese 2 cifre 01-12:  ")
            if mese_input.isdigit() and len(mese_input) == 2 and 1 <= int(mese_input) <= 12:
                self.regex = mese_input
            else:
                print("Errore: solo 2 cifre! ")  
    def to_python(self):
        return int(self.regex)
converter = TwoDigitMonthConverter()
print(f"Valore inserito: {converter.regex}")




                                    
'''
class TwoDigitMonthConverter:
    def __init__(self):
        """
        Inizializza la classe chiedendo all'utente di inserire un mese valido (due cifre numeriche).
        """
        while True:
            user_input = input("Inserisci mese (due cifre numeriche, es. '01' per Gennaio): ")
            if user_input.isdigit() and len(user_input) == 2 and 1 <= int(user_input) <= 12:
                self.regex = user_input
                break  # Esce dal loop se l'input è valido
            else:
                print("Errore: Devi inserire esattamente due cifre numeriche tra 01 e 12. Riprova.")

    def to_python(self):
        """
        Converte la stringa numerica in un intero.
        """
        return int(self.regex)

    def check_regex(self):
        """
        Verifica se l'attributo regex è valutato come True o False.
        """
        if self.regex:
            print(f"regex '{self.regex}' è valutata come True")
        else:
            print("regex è valutata come False")


# Creiamo un'istanza della classe (qui viene richiesto l'input)
converter = TwoDigitMonthConverter()

# Stampiamo il valore della regex e verifichiamo se è valutata come True
print(f"Valore inserito: {converter.regex}")
converter.check_regex()

'''