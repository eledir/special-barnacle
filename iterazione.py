class Biblioteca:
    """
    Questa classe rappresenta una biblioteca, in grado di contenere e gestire una collezione di libri.
    """
    def __init__(self):
        """
        Il costruttore della classe Biblioteca.
        Inizializza un elenco vuoto chiamato 'libri' che conterrà i titoli dei libri presenti nella biblioteca.
        """
        self.libri = []

    def aggiungi_libro(self, titolo):
        """
        Questo metodo permette di aggiungere un nuovo libro alla biblioteca.

        Args:
            titolo (str): Il titolo del libro da aggiungere.
        """
        self.libri.append(titolo)

    def __iter__(self):
        """
        Questo metodo speciale rende l'oggetto BibliotecaIterable, ovvero in grado di essere iterato.
        Restituisce un iteratore per l'elenco dei libri. Questo permette di utilizzare un ciclo 'for' direttamente sull'oggetto Biblioteca.
        """
        return iter(self.libri)

# Creiamo un'istanza della biblioteca
biblioteca = Biblioteca()
# Aggiungiamo alcuni libri alla biblioteca utilizzando il metodo aggiungi_libro
biblioteca.aggiungi_libro("1984")
biblioteca.aggiungi_libro("Il Signore degli Anelli")
biblioteca.aggiungi_libro("Il Nome della Rosa")

# Iteriamo sui libri disponibili nella biblioteca
print("Libri disponibili in biblioteca:")
# Grazie al metodo __iter__, possiamo iterare direttamente sull'oggetto 'biblioteca'
for libro in biblioteca:
    # Ad ogni iterazione, la variabile 'libro' conterrà un titolo dalla lista 'self.libri'
    print("-", libro)