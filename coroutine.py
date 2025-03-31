class Coroutine:
    def __init__(self):
        self.status = "free"

    def send(self, value):
        """Invia un valore nella coroutine.
        Restituisce il prossimo valore o solleva StopIteration.
        """
        raise NotImplementedError("Sottoclassi devono implementare send()")

    def throw(self, typ, val=None, tb=None):
        """Solleva un'eccezione nella coroutine.
        Restituisce il prossimo valore o solleva StopIteration.
        """
        # Assicurati che typ sia una sottoclasse di BaseException
        if not isinstance(typ, type) or not issubclass(typ, BaseException):
            raise TypeError("L'eccezione deve essere una sottoclasse di BaseException")

        # Gestione del valore dell'eccezione
        if val is None:
            # Se nessun valore è fornito, crea un'istanza dell'eccezione
            exception = typ()
        elif isinstance(val, typ):
            # Se val è già un'istanza del tipo di eccezione
            exception = val
        elif isinstance(val, str):
            # Se val è una stringa, usa come messaggio dell'eccezione
            exception = typ(val)
        else:
            # Altrimenti, converti val in stringa come messaggio
            exception = typ(str(val))

        # Aggiunta della traceback se presente
        if tb is not None:
            exception = exception.with_traceback(tb)

        # Solleva l'eccezione
        raise exception

    def close(self):
        """Solleva GeneratorExit all'interno della coroutine."""
        try:
            self.throw(GeneratorExit)
        except (GeneratorExit, StopIteration):
            pass
        else:
            raise RuntimeError("coroutine ignored GeneratorExit")

    def __await__(self):
        """Rende la coroutine awaitable."""
        yield self

# Esempio di sottoclasse di Coroutine
class ExampleCoroutine(Coroutine):
    def send(self, value):
        if value > 10:
            print(f"Received value greater than 10: {value}")
            return f"Processed: {value}"
        else:
            print(f"Received value: {value}")
            return f"Acknowledged: {value}"

# Esempio di utilizzo delle funzionalità di throw
def example_usage():
    print("Esempio 1: Sollevare un'eccezione con valore stringa")
    coro = Coroutine()
    try:
        # Sollevare un'eccezione ValueError con un messaggio stringa
        coro.throw(ValueError, "Qualcosa è andato storto!")
    except ValueError as e:
        print(f"Eccezione catturata: {e}")

    print("\nEsempio 2: Sollevare un'eccezione senza valore")
    try:
        # Sollevare un TypeError senza un valore specifico
        coro.throw(TypeError)
    except TypeError as e:
        print(f"Eccezione catturata: {e}")

    print("\nEsempio 3: Sollevare un'eccezione con valore numerico")
    try:
        # Sollevare un ValueError con un valore numerico
        coro.throw(ValueError, 42)
    except ValueError as e:
        print(f"Eccezione catturata: {e}")

    print("\nEsempio 4: Tentativo di sollevare un'eccezione non valida")
    try:
        # Tentativo di sollevare un'eccezione non valida (che dovrebbe generare un TypeError)
        coro.throw("Non è un'eccezione")
    except TypeError as e:
        print(f"Eccezione catturata: {e}")

if __name__ == "__main__":
    example_usage()
'''
I principali miglioramenti in questa versione sono:

Gestione più flessibile della creazione dell'eccezione:

Supporta passare una stringa come messaggio
Supporta passare un valore numerico o altro che verrà convertito in stringa
Gestisce correttamente il caso in cui venga passata già un'istanza dell'eccezione


Aggiunta di più esempi di utilizzo:

Sollevare un'eccezione con un messaggio stringa
Sollevare un'eccezione senza un valore specifico
Sollevare un'eccezione con un valore numerico
Gestire un tentativo di sollevare un'eccezione non valida



Quando eseguito, lo script mostrerà:

Come sollevare eccezioni in una coroutine
Come gestire diversi tipi di input per il messaggio dell'eccezione
Come prevenire tentativi di sollevare oggetti non validi come eccezioni

L'output dimostrerà la flessibilità del metodo throw() nel gestire diversi tipi di input e nel sollevare eccezioni in modo coerente.
La logica principale ora è:

Verificare che il tipo di eccezione sia valido
Creare l'eccezione in modo flessibile:

Nessun valore: istanza vuota
Stringa: usata come messaggio
Altro valore: convertito in stringa come messaggio


Aggiungere traceback se presente....if val is None::

Questo è il primo blocco if.
La condizione val is None verifica se l'argomento val (che rappresenta il valore associato all'eccezione) è None.
Se val è effettivamente None, significa che chi ha chiamato throw non ha fornito un'istanza specifica dell'eccezione o un valore da associare ad essa. In questo caso, dobbiamo potenzialmente crearne una.
if tb is None::

Questo è un blocco if annidato all'interno del primo if.
Viene eseguito solo se la condizione del blocco if esterno (val is None) è vera.
La condizione tb is None verifica se l'argomento tb (che rappresenta l'oggetto traceback) è None.
Se anche tb è None (e val era None), significa che non abbiamo né un valore specifico per l'eccezione né una traceback. In questa situazione, solleviamo direttamente il tipo di eccezione (typ) fornito. Questo creerà un'istanza predefinita dell'eccezione.
val = typ():

Questa riga si trova all'interno del primo blocco if ma fuori dal blocco if annidato.
Viene eseguita se val era None ma tb non era None.
In questo caso, creiamo un'istanza dell'eccezione specificata in typ senza passare argomenti al costruttore (utilizzando ()). Questa istanza viene quindi assegnata a val. L'obiettivo è avere un'istanza di eccezione a cui poter aggiungere la traceback.
if tb is not None::

Questo è il secondo blocco if principale (non annidato nel primo).
La condizione tb is not None verifica se l'argomento tb (l'oggetto traceback) ha un valore (cioè, non è None).
Questo blocco viene eseguito se è stata fornita una traceback.
val = val.with_traceback(tb):

Questa riga si trova all'interno del secondo blocco if.
Chiama il metodo with_traceback() sull'oggetto eccezione val. Questo metodo restituisce una nuova istanza dell'eccezione con la traceback tb impostata. L'oggetto risultante viene riassegnato a val.
In sintesi, la struttura if nel metodo throw gestisce diversi scenari in base a quali argomenti (valore dell'eccezione e traceback) sono stati forniti quando il metodo è stato chiamato, assicurando che l'eccezione venga sollevata correttamente con le informazioni appropriate.
'''    