def calcola_importi(iva_dovuta, iva_credito, debito_precedente,
                     interessi_dovuti, crediti_imposta, credito_periodo_precedente,
                     credito_anno_precedente, versamenti_auto, acconto,
                     trimestre, subfornitura):
    """
    Funzione che calcola l'importo da versare e l'importo a credito
    in base alle regole del controllo bloccante.
    """
    # Calcolo della variabile A sulla base delle voci contabili
    A = (iva_dovuta - iva_credito + debito_precedente +
         interessi_dovuti - crediti_imposta - credito_periodo_precedente -
         credito_anno_precedente - versamenti_auto - acconto)
    
    # Controllo sull'eccezione: Se Trimestre = 5 e Subfornitura è presente, il controllo è disattivato
    if trimestre == 5 and subfornitura:
        return None  # Il controllo non viene applicato
    
    # Se Trimestre = 5 e Subfornitura non è presente, gli importi non devono essere presenti
    if trimestre == 5 and not subfornitura:
        return "Errore: Gli importi non devono essere presenti quando Trimestre è 5 senza Subfornitura"
    
    # Calcolo degli importi secondo il valore di A
    if A > 0:
        importo_da_versare = A
        importo_a_credito = 0
    elif A < 0:
        importo_da_versare = 0
        importo_a_credito = -A  # Il credito è il valore assoluto di A
    else:
        importo_da_versare = 0
        importo_a_credito = 0
    
    return {
        "ImportoDaVersare": importo_da_versare,
        "ImportoACredito": importo_a_credito
    }

# Esempio di utilizzo
dati_esempio = calcola_importi(
    iva_dovuta=1000,
    iva_credito=500,
    debito_precedente=200,
    interessi_dovuti=50,
    crediti_imposta=100,
    credito_periodo_precedente=150,
    credito_anno_precedente=50,
    versamenti_auto=200,
    acconto=100,
    trimestre=3,
    subfornitura=False
)

print(dati_esempio)