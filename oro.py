from django.db import models

class Operazione(models.Model):
    ora_operazione = models.DateTimeField(auto_now_add=True)
    numero_scheda = models.CharField(max_length=50, unique=True)
    dati_cliente = models.TextField()
    descrizione_oggetto = models.TextField()
    valore_stimato = models.DecimalField(max_digits=10, decimal_places=2)
    quotazione_metallo = models.DecimalField(max_digits=10, decimal_places=2)
    importo_corrisposto = models.DecimalField(max_digits=10, decimal_places=2)
    MODALITA_PAGAMENTO = [
        ('contanti', 'Contanti'),
        ('bonifico', 'Bonifico Bancario'),
        ('assegno', 'Assegno Non Trasferibile')
    ]
    modalita_pagamento = models.CharField(max_length=20, choices=MODALITA_PAGAMENTO)
    ricevuta_rilasciata = models.BooleanField(default=True)
    copia_ricevuta_archiviata = models.BooleanField(default=True)
    foto_acquisite = models.BooleanField(default=True)
    note_anomalie = models.TextField(blank=True, null=True)
    segnalazione_uif = models.BooleanField(default=False)
    riferimento_uif = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Operazione {self.numero_scheda} - {self.ora_operazione}"
