from django.db import models

class Reporter(models.Model):
    # Campo per il nome completo del reporter
    # - CharField: Campo per stringhe di testo
    # - max_length=70: Lunghezza massima di 70 caratteri
    full_name = models.CharField(max_length=70)

    def __str__(self):
        # Metodo speciale che restituisce una rappresentazione leggibile dell'oggetto
        # Viene utilizzato quando si stampa l'oggetto o lo si visualizza nell'admin di Django
        # NOTA: C'è un piccolo errore di battitura qui ('full_nam' invece di 'full_name')
        return self.full_nam  # <-- Questo è un errore, dovrebbe essere 'full_name'