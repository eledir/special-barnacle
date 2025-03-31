# interfaccia delle sequenze
class Biblioteca:
    def __init__(self):
        self.libri = []
    
    def aggiungi_libro(self, titolo):
        self.libri.append(titolo)
    
    def __iter__(self):
        return iter(self.libri)

# Creiamo un'istanza della biblioteca
biblioteca = Biblioteca()
biblioteca.aggiungi_libro("1984")
biblioteca.aggiungi_libro("Il Signore degli Anelli")
biblioteca.aggiungi_libro("Il Nome della Rosa")

# Iteriamo sui libri disponibili nella biblioteca
print("Libri disponibili in biblioteca:")
for libro in biblioteca:
    print("-", libro)

# Formattazione stringhe con diversi metodi
prezzo = 12.99
titolo = "1984"
quantita = 2

# Usando f-string
scontrino_f = f"Hai acquistato {quantita} copie di '{titolo}' per un totale di {prezzo * quantita:.2f} euro."
print(scontrino_f)

# Usando format()
scontrino_format = "Hai acquistato {} copie di '{}' per un totale di {:.2f} euro.".format(quantita, titolo, prezzo * quantita)
print(scontrino_format)

# Usando stile C con %
scontrino_percent = "Hai acquistato %d copie di '%s' per un totale di %.2f euro." % (quantita, titolo, prezzo * quantita)
print(scontrino_percent)
'''
Ora lo script include anche tre metodi diversi per formattare una stringa, simulando una ricevuta di acquisto per i libri. 

'''