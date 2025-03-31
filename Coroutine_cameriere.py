class Coroutine:
    def __init__(self):
        # Inizializza lo stato della coroutine come "libera"
        self.status = "free"

    def send(self, value):
        """Invia un valore nella coroutine.
        Restituisce il prossimo valore o solleva StopIteration.
        """
        # Questo metodo deve essere implementato dalle sottoclassi per definire il comportamento di invio
        raise NotImplementedError("Sottoclassi devono implementare send()")

    def throw(self, typ, val=None, tb=None):
        """Solleva un'eccezione nella coroutine.
        Restituisce il prossimo valore o solleva StopIteration.
        """
        # Gestisce la creazione e il sollevamento di un'eccezione
        if val is None:
            if tb is None:
                raise typ
            val = typ()
        if tb is not None:
            val = val.with_traceback(tb)
        raise val

    def close(self):
        """Solleva GeneratorExit all'interno della coroutine."""
        # Tenta di sollevare GeneratorExit per segnalare la chiusura
        try:
            self.throw(GeneratorExit)
        except (GeneratorExit, StopIteration):
            # Ignora GeneratorExit e StopIteration durante la chiusura
            pass
        else:
            # Se la coroutine non gestisce GeneratorExit, solleva un RuntimeError
            raise RuntimeError("coroutine ignored GeneratorExit")

    def __await__(self):
        """Rende la coroutine awaitable."""
        # Permette di utilizzare la coroutine con 'await'
        yield self

class WaiterCoroutine(Coroutine):
    def __init__(self, table_number):
        # Chiama il costruttore della classe genitore (Coroutine)
        super().__init__()
        # Memorizza il numero del tavolo assegnato a questo cameriere
        self.table_number = table_number
        # Memorizza l'attività corrente del cameriere (potrebbe essere None)
        self.current_task = None
        # Memorizza l'ordine corrente preso dal tavolo (potrebbe essere None)
        self.order = None

    def send(self, food):
        # Simula la ricezione del cibo dalla cucina
        if self.status == "waiting_for_food":
            # Stampa un messaggio indicando che il cameriere sta consegnando il cibo
            print(f"Cameriere {self.table_number}: Consegno il cibo {food} al tavolo.")
            # Aggiorna lo stato del cameriere a "serving"
            self.status = "serving"
            # Restituisce il cibo consegnato
            return food
        # Se il cameriere non sta aspettando cibo, solleva un'eccezione
        raise StopIteration("Nessun ordine in attesa")

    def throw(self, exception, value=None, traceback=None):
        # Gestisce un problema al tavolo
        if isinstance(exception, ValueError):
            # Se l'eccezione è un ValueError (es. problema con l'ordine), stampa un messaggio
            print(f"Cameriere {self.table_number}: Problema con l'ordine - {value}")
            # Aggiorna lo stato del cameriere a "resolving_issue"
            self.status = "resolving_issue"
            # Indica che il problema è stato gestito
            return "risolto"
        # Se l'eccezione non è un ValueError, la rilancia
        raise exception

    def take_order(self, order):
        # Prende l'ordine dal tavolo
        # Memorizza l'ordine
        self.order = order
        # Aggiorna lo stato del cameriere a "waiting_for_food"
        self.status = "waiting_for_food"
        # Stampa un messaggio indicando che l'ordine è stato ricevuto
        print(f"Cameriere {self.table_number}: Ordine ricevuto - {order}")
        # Restituisce l'ordine
        return order

    def close(self):
        # Chiude il servizio per il tavolo
        # Stampa un messaggio indicando che il tavolo è completato
        print(f"Cameriere {self.table_number}: Tavolo completato. Pulizia in corso.")
        # Aggiorna lo stato del cameriere a "free"
        self.status = "free"
        # Resetta l'ordine corrente
        self.order = None
        # Chiama il metodo close della classe genitore
        super().close()

# Esempio di utilizzo
def ristorante_simulator():
    # Creiamo due camerieri per due tavoli diversi
    cameriere_tavolo1 = WaiterCoroutine(1)
    cameriere_tavolo2 = WaiterCoroutine(2)

    # Simulazione delle interazioni
    # Il cameriere del tavolo 1 prende un ordine
    ordine1 = cameriere_tavolo1.take_order("Pizza Margherita")

    try:
        # Simulazione di un problema con l'ordine sollevando un'eccezione
        cameriere_tavolo1.throw(ValueError, "Pizza troppo fredda")
    except Exception as e:
        # Gestisce l'eccezione stampando un messaggio
        print(f"Errore gestito: {e}")

    # Simulazione della consegna del cibo inviando il cibo alla coroutine
    cameriere_tavolo1.send("Pizza Margherita calda")

    # Chiusura del servizio per il tavolo
    cameriere_tavolo1.close()

# Esecuzione del simulatore
if __name__ == "__main__":
    ristorante_simulator()