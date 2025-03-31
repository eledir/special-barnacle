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
        if val is None:
            if tb is None:
                raise typ
            val = typ()
        if tb is not None:
            val = val.with_traceback(tb)
        raise val

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

class WaiterCoroutine(Coroutine):
    def __init__(self, table_number):
        super().__init__()
        self.table_number = table_number
        self.current_task = None
        self.order = None

    def send(self, food):
        # Simula la ricezione del cibo dalla cucina
        if self.status == "waiting_for_food":
            print(f"Cameriere {self.table_number}: Consegno il cibo {food} al tavolo.")
            self.status = "serving"
            return food
        raise StopIteration("Nessun ordine in attesa")

    def throw(self, exception, value=None, traceback=None):
        # Gestisce un problema al tavolo
        if isinstance(exception, ValueError):
            print(f"Cameriere {self.table_number}: Problema con l'ordine - {value}")
            self.status = "resolving_issue"
            return "risolto"
        raise exception

    def take_order(self, order):
        # Prende l'ordine dal tavolo
        self.order = order
        self.status = "waiting_for_food"
        print(f"Cameriere {self.table_number}: Ordine ricevuto - {order}")
        return order

    def close(self):
        # Chiude il servizio per il tavolo
        print(f"Cameriere {self.table_number}: Tavolo completato. Pulizia in corso.")
        self.status = "free"
        self.order = None
        super().close()

# Esempio di utilizzo
def ristorante_simulator():
    # Creiamo due camerieri per due tavoli diversi
    cameriere_tavolo1 = WaiterCoroutine(1)
    cameriere_tavolo2 = WaiterCoroutine(2)

    # Simulazione delle interazioni
    ordine1 = cameriere_tavolo1.take_order("Pizza Margherita")
    
    try:
        # Simulazione di un problema con l'ordine
        cameriere_tavolo1.throw(ValueError, "Pizza troppo fredda")
    except Exception as e:
        print(f"Errore gestito: {e}")

    # Simulazione della consegna del cibo
    cameriere_tavolo1.send("Pizza Margherita calda")
    
    # Chiusura del servizio per il tavolo
    cameriere_tavolo1.close()

# Esecuzione del simulatore
if __name__ == "__main__":
    ristorante_simulator()