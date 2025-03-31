from typing import Callable, Type
from types import FunctionType

# Usa l'Ellipsis built-in invece di importarlo da typing
class CallableGenericAlias:
    """
    Rappresenta un alias generico per Callable[argtypes, resulttype].
    
    Gestisce la creazione e la rappresentazione di tipi Callable con argomenti e tipo di ritorno.
    Estende il comportamento base di GenericAlias per i tipi Callable.
    """

    # Utilizzo di __slots__ per ottimizzazione della memoria
    __slots__ = ()

    def __new__(cls, origin, args):
        """
        Metodo di creazione personalizzato per CallableGenericAlias.
        
        Args:
            origin: La classe base (Callable)
            args: Una tupla contenente gli argomenti e il tipo di ritorno
        
        Raises:
            TypeError: Se gli argomenti non sono nel formato corretto
        """
        # Verifica che args sia una tupla di esattamente 2 elementi
        if not (isinstance(args, tuple) and len(args) == 2):
            raise TypeError(
                "Callable deve essere usato come Callable[[arg, ...], result].")
        
        # Separa gli argomenti e il tipo di ritorno
        t_args, t_result = args
        
        # Se t_args è una tupla o lista, appiattisci la struttura
        if isinstance(t_args, (tuple, list)):
            args = (*t_args, t_result)
        # Verifica che t_args sia un'espressione di parametro valida
        elif not is_param_expr(t_args):
            raise TypeError(f"Atteso una lista di tipi, un ellipsis, "
                            f"ParamSpec, o Concatenate. Ricevuto {t_args}")
        
        # Chiama il costruttore della classe base
        return super().__new__(cls, origin, args)

    def __repr__(self):
        """
        Genera una rappresentazione testuale personalizzata dell'alias.
        
        Gestisce casi speciali come ParamSpec e fornisce una 
        visualizzazione leggibile dei tipi Callable.
        """
        # Se è un caso speciale (ParamSpec), usa la rappresentazione base
        if len(self.__args__) == 2 and is_param_expr(self.__args__[0]):
            return super().__repr__()
        
        # Genera una rappresentazione dettagliata dei tipi di argomenti e ritorno
        return (f'collections.abc.Callable'
                f'[[{", ".join([_type_repr(a) for a in self.__args__[:-1]])}], '
                f'{_type_repr(self.__args__[-1])}]')

    def __reduce__(self):
        """
        Supporto per la serializzazione dell'oggetto.
        
        Gestisce casi speciali durante la riduzione/serializzazione.
        """
        args = self.__args__
        # Se non è un caso speciale, raggruppa gli argomenti
        if not (len(args) == 2 and is_param_expr(args[0])):
            args = list(args[:-1]), args[-1]
        return CallableGenericAlias, (Callable, args)

    def __getitem__(self, item):
        """
        Gestisce la sostituzione di TypeVar e la creazione di nuovi alias.
        
        Personalizza il comportamento di getitem per mantenere la struttura 
        specifica di Callable.
        """
        # Converti l'item in una tupla se non lo è già
        if not isinstance(item, tuple):
            item = (item,)

        # Ottiene i nuovi argomenti dalla classe base
        new_args = super().__getitem__(item).__args__

        # Gestisce casi speciali come Z[[int, str, bool]]
        if not isinstance(new_args[0], (tuple, list)):
            t_result = new_args[-1]
            t_args = new_args[:-1]
            new_args = (t_args, t_result)
        
        # Restituisce un nuovo CallableGenericAlias
        return CallableGenericAlias(Callable, tuple(new_args))

def is_param_expr(obj):
    """
    Verifica se l'oggetto è un'espressione di parametro valida.
    
    Args:
        obj: Oggetto da verificare
    
    Returns:
        bool: True se l'oggetto è un'espressione di parametro valida
    """
    # Controlla se è un ellipsis
    if obj is Ellipsis:
        return True
    
    # Controlla se è una lista
    if isinstance(obj, list):
        return True
    
    # Ottiene il tipo dell'oggetto
    obj = type(obj)
    
    # Nomi dei tipi speciali da verificare
    names = ('ParamSpec', '_ConcatenateGenericAlias')
    
    # Verifica se il tipo appartiene al modulo 'typing' 
    # e corrisponde a uno dei nomi specificati
    return obj.__module__ == 'typing' and any(obj.__name__ == name for name in names)

def _type_repr(obj):
    """
    Genera una rappresentazione testuale di un tipo.
    
    Gestisce casi speciali come tipi built-in, Ellipsis, funzioni.
    
    Args:
        obj: Oggetto di cui generare la rappresentazione
    
    Returns:
        str: Rappresentazione testuale dell'oggetto
    """
    # Gestisce tipi
    if isinstance(obj, type):
        # Per tipi built-in, usa solo il nome della classe
        if obj.__module__ == 'builtins':
            return obj.__qualname__
        # Per altri tipi, include il modulo
        return f'{obj.__module__}.{obj.__qualname__}'
    
    # Gestisce Ellipsis
    if obj is Ellipsis:
        return '...'
    
    # Gestisce funzioni
    if isinstance(obj, FunctionType):
        return obj.__name__
    
    # Usa la rappresentazione standard per altri oggetti
    return repr(obj)

# Esempio di utilizzo
def esempio():
    # Esempio di utilizzo di un tipo Callable
    def somma(a: int, b: int) -> int:
        return a + b
    
    # Tipo Callable che accetta due interi e restituisce un intero
    tipo_somma = Callable[[int, int], int]
    
    print(f"Tipo della funzione somma: {tipo_somma}")
    print(f"Tipo della funzione: {type(somma)}")

if __name__ == "__main__":
    esempio()
'''
Nella vita reale, un file `Callable.py` (o più precisamente, il concetto di "callable" implementato in Python in un file con qualsiasi nome) è utile in moltissime occasioni in cui si desidera trattare una porzione di codice (una funzione, un metodo di una classe, o un oggetto di una classe che implementa `__call__`) come un'entità che può essere passata, memorizzata ed eseguita in un secondo momento.

Ecco alcuni scenari comuni nella vita reale in cui i callable sono ampiamente utilizzati:

**1. Funzioni di Callback (Event Handling, Asincronicità):**

* **Interfacce grafiche (GUI):** Quando si preme un pulsante, si seleziona un elemento da un menu, o si verifica un altro evento in un'applicazione GUI (come quelle create con Tkinter, PyQt, Kivy), si utilizzano delle *funzioni di callback*. Queste funzioni vengono registrate per essere chiamate quando l'evento specifico si verifica. Il sistema GUI non sa in anticipo quale funzione deve eseguire, quindi si affida a un callable fornito dallo sviluppatore.
* **Programmazione asincrona (asyncio):** In contesti di I/O concorrente (operazioni di rete, lettura/scrittura di file), si usano spesso callback (o concetti simili come le coroutine) per essere notificati quando un'operazione asincrona è completata. Invece di bloccare l'esecuzione, il programma continua a fare altro e la callback viene chiamata al termine dell'operazione.
* **Gestione di segnali (signal handling):** Nei sistemi operativi, è possibile registrare delle funzioni (callable) per essere eseguite quando il programma riceve determinati segnali (ad esempio, SIGINT per l'interruzione da tastiera).

**2. Funzioni come Argomenti (Higher-Order Functions):**

* **Ordinamento personalizzato:** Funzioni come `sorted()` in Python accettano un argomento `key` che è una funzione (un callable). Questa funzione viene applicata a ciascun elemento della lista prima del confronto, permettendo di definire criteri di ordinamento complessi. Ad esempio, ordinare una lista di stringhe in base alla loro lunghezza o al numero di vocali.
* **Filtraggio e trasformazione di dati:** Funzioni come `map()`, `filter()`, e list comprehensions (che internamente utilizzano concetti simili) prendono una funzione (un callable) come input per applicare una trasformazione o un filtro a una sequenza di dati. Ad esempio, raddoppiare tutti i numeri in una lista o selezionare solo i numeri pari.
* **Decoratori:** I decoratori in Python (`@decorator`) sono una sintassi elegante per avvolgere una funzione con un'altra funzione (il decoratore). Il decoratore è un callable che prende la funzione originale come argomento e restituisce una versione modificata della funzione. Questo è ampiamente usato per aggiungere funzionalità come logging, gestione degli errori, o misurazione del tempo di esecuzione.

**3. Astrazione e Flessibilità:**

* **Strategie di algoritmi:** In alcuni casi, si può voler rendere un algoritmo flessibile permettendo all'utente di specificare una particolare "strategia" o operazione da eseguire all'interno dell'algoritmo. Questo può essere fatto passando una funzione (un callable) come argomento. Ad esempio, un algoritmo di ricerca potrebbe accettare una funzione di confronto personalizzata.
* **Sistemi di plugin:** Un'applicazione complessa potrebbe utilizzare un sistema di plugin in cui funzionalità aggiuntive possono essere caricate dinamicamente. Questi plugin potrebbero registrare delle funzioni (callable) che vengono poi invocate dall'applicazione principale in determinate circostanze.

**4. Oggetti Callable (Classi con `__call__`)**

* **Oggetti funzione con stato:** A volte è utile avere un oggetto che si comporta come una funzione ma che mantiene anche uno stato interno. Implementando il metodo `__call__` in una classe, gli oggetti di quella classe diventano callable. Questo può essere utile per creare "funzioni" che hanno una configurazione o una memoria interna. Ad esempio, un oggetto che conta quante volte è stato chiamato.
* **Creazione di astrazioni più complesse:** Gli oggetti callable possono essere utilizzati per incapsulare logiche più complesse rispetto a una semplice funzione, pur mantenendo la sintassi di chiamata di una funzione.

**Esempi concreti:**

* **Un bot di Telegram:** Potrebbe usare delle funzioni di callback per gestire i comandi degli utenti (es. `/start`, `/help`). Quando un utente invia un comando, la funzione di callback associata a quel comando viene eseguita.
* **Un framework web (Django, Flask):** Utilizzano i callable (le view functions) per definire la logica che deve essere eseguita quando un utente visita una specifica URL.
* **Un sistema di logging:** Potrebbe permettere di registrare diverse "handler" (che potrebbero essere callable) per decidere come gestire i messaggi di log (stamparli a schermo, scriverli su file, inviarli a un server remoto).

In sintesi, i callable sono uno strumento fondamentale in Python (e in molti altri linguaggi di programmazione) per rendere il codice più modulare, flessibile, riutilizzabile e reattivo agli eventi. Permettono di trattare il codice eseguibile come dati, aprendo la strada a pattern di progettazione potenti e a una programmazione più dinamica.
'''    