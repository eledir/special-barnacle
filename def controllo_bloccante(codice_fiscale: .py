def controllo_bloccante(codice_fiscale: str, trimestre: int, ultimo_mese: int, iva_esigibile: float, iva_detratta: float) -> tuple[bool, float, float]:
    """
    Verifica se il controllo bloccante deve essere attivato e calcola IvaDovuta e IvaCredito.
    
    :param codice_fiscale: Stringa contenente il codice fiscale.
    :param trimestre: Intero che indica il trimestre della comunicazione (1, 2, 3, 4).
    :param ultimo_mese: Intero che indica il valore di UltimoMese.
    :param iva_esigibile: Importo dell'IVA esigibile.
    :param iva_detratta: Importo dell'IVA detratta.
    :return: Una tupla contenente lo stato del controllo bloccante, il valore di IvaDovuta e quello di IvaCredito.
    """
    if len(codice_fiscale) == 16:
        return True, 0, 0  # Blocco attivo se il codice fiscale è lungo 16 caratteri
    
    condizioni_bloccanti = {
        1: 12,  # Primo trimestre con UltimoMese 12
        2: 3,   # Secondo trimestre con UltimoMese 3
        3: 6,   # Terzo trimestre con UltimoMese 6
        4: 9    # Quarto trimestre con UltimoMese 9
    }
    
    if trimestre in condizioni_bloccanti and ultimo_mese == condizioni_bloccanti[trimestre]:
        return True, 0, 0  # Blocco attivo se la combinazione trimestre/UltimoMese è vietata
    
    # Calcolo di A (IvaEsigibile - IvaDetratta)
    A = iva_esigibile - iva_detratta
    
    # Determinazione dei valori di IvaDovuta e IvaCredito
    if A > 0:
        iva_dovuta = A
        iva_credito = 0
    elif A < 0:
        iva_dovuta = 0
        iva_credito = -A
    else:
        iva_dovuta = 0
        iva_credito = 0
    
    return False, iva_dovuta, iva_credito  # Nessuna condizione bloccante soddisfatta

# Esempi di test
print(controllo_bloccante("ABCDEF12G34H567I", 1, 12, 1000, 800))  # (True, 0, 0), codice fiscale di 16 caratteri
print(controllo_bloccante("ABCDEFG12345", 1, 12, 1000, 800))     # (True, 0, 0), primo trimestre con UltimoMese 12
print(controllo_bloccante("ABCDEFG12345", 2, 5, 2000, 2500))      # (False, 0, 500), IvaCredito calcolato
'''
spiegazione>
ultimo_mese == condizioni_bloccanti[trimestre]
L'espressione ultimo_mese == condizioni_bloccanti[trimestre] serve a verificare se il valore di ultimo_mese corrisponde a quello bloccante per il trimestre specificato.
Spiegazione dettagliata:
Dizionario delle condizioni bloccanti
condizioni_bloccanti = {
    1: 12,  # Primo trimestre con UltimoMese 12
    2: 3,   # Secondo trimestre con UltimoMese 3
    3: 6,   # Terzo trimestre con UltimoMese 6
    4: 9    # Quarto trimestre con UltimoMese 9
}
Qui definiamo un dizionario in cui la chiave è il trimestre (1, 2, 3, 4) e il valore associato è il valore di ultimo_mese che, se presente, deve attivare il blocco.
Verifica della condizione bloccante
if trimestre in condizioni_bloccanti and ultimo_mese == condizioni_bloccanti[trimestre]:
trimestre in condizioni_bloccanti verifica se il valore di trimestre è una chiave del dizionario (per evitare errori di lookup).
ultimo_mese == condizioni_bloccanti[trimestre] confronta il valore di ultimo_mese con quello associato al trimestre nel dizionario.

Esempio pratico
Supponiamo di chiamare la funzione con:
controllo_bloccante("ABCDEFG12345", 1, 12, 1000, 800)
trimestre = 1
ultimo_mese = 12
Dal dizionario, condizioni_bloccanti[1] restituisce 12
Poiché ultimo_mese == 12, la condizione è vera e il controllo bloccante viene attivato.

Riassunto
Questa logica permette di verificare in modo semplice e chiaro se una specifica combinazione di trimestre e ultimo_mese corrisponde a una condizione bloccante, evitando l'uso di più condizioni if separate.
'''