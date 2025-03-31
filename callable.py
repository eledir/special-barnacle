def mia_funzione():
    print("Ciao!")

mia_funzione() # Chiamare la funzione
print(callable(mia_funzione)) # Verifica se un oggetto è chiamabile

class MioOggettoChiamabile:
    def __call__(self):
        print("Oggetto chiamato!")

oggetto = MioOggettoChiamabile()
oggetto() # Chiamare l'oggetto
print(callable(oggetto))

print(callable(list)) # Anche i tipi (classi) sono chiamabili (per creare istanze)