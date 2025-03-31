import json  # Importazione della libreria per la gestione JSON

# Classe per rappresentare la PosContributiva
class PosContributiva:
    def __init__(self, codice, descrizione):
        self.codice = codice  # Codice della PosContributiva
        self.descrizione = descrizione  # Descrizione associata

    def to_dict(self):
        return {"codice": self.codice, "descrizione": self.descrizione}  # Converti in dizionario

# Classe per rappresentare la DenunciaIndividuale
class DenunciaIndividuale:
    def __init__(self, tipo_regolarizz, cod_ente_redattore):
        self.tipo_regolarizz = tipo_regolarizz  # Tipo di regolarizzazione
        self.cod_ente_redattore = cod_ente_redattore  # Codice ente redattore

    def to_dict(self):
        return {"tipo_regolarizz": self.tipo_regolarizz, "cod_ente_redattore": self.cod_ente_redattore}  

# Classe per rappresentare la Qualifica
class Qualifica:
    def __init__(self, codice, descrizione):
        self.codice = codice  # Codice della qualifica
        self.descrizione = descrizione  # Descrizione della qualifica

    def to_dict(self):
        return {"codice": self.codice, "descrizione": self.descrizione}  

# Dizionario per mappare codici e descrizioni di PosContributiva
pos_contributiva_dict = {
    "CP": "Denuncia completa",
    "FP": "Denuncia frazionata parziale",
    "FC": "Denuncia frazionata di completamento",
    "NS": "Non specificato",
    "AN": "Denuncia anticipata",
    "41": "Pagamento Diretto SR41"
}

# Dizionario per mappare codici e descrizioni del Tipo di Regolarizzazione
tipo_regolarizz_dict = {
    "RS": "Regolarizzazione spontanea",
    "CM": "Conciliazione monocratica",
    "PE": "Regolarizzazione PEGASO",
    "VE": "Regolarizzazione per differenze retributive",
    "VN": "Regolarizzazione per lavoratore in nero",
    "SS": "Regolarizzazione per differenze retributive (sentenza)",
    "SN": "Regolarizzazione per lavoratore in nero (sentenza)",
    "RM": "Regolarizzazione da compliance - Morosità",
    "RE": "Regolarizzazione da compliance - Evasione"
}

# Dizionario per mappare codici e descrizioni degli Enti Redattori
cod_ente_redattore_dict = {
    "01": "D.T.L.",
    "02": "I.N.A.I.L.",
    "03": "G.D.F.",
    "04": "A.S.L.",
    "05": "Agenzia delle Entrate",
    "06": "P.S.",
    "07": "Carabinieri"
}

# Dizionario per mappare codici e descrizioni delle Qualifiche
qualifica_dict = {
    "1": "Operaio",
    "2": "Impiegato",
    "3": "Dirigente",
    "4": "Apprendista non soggetto all’assicurazione infortuni (fino al 31/12/2006)",
    "5": "Apprendista soggetto all’assicurazione infortuni",
    "6": "Lavoratore a domicilio",
    "7": "Equiparato o intermedio considerato impiegato ai fini della contribuzione",
    "8": "Viaggiatore o piazzista",
    "9": "Dirigenti di aziende industriali assunti dall’01.01.2003",
    "A": "Atipica ex INPDAI",
    "B": "Lavoratore domestico dipendente da agenzia di lavoro interinale",
    "C": "Apprendista non professionalizzante mantenuto in servizio come operaio",
    "D": "Apprendista non professionalizzante mantenuto in servizio come impiegato",
    "E": "Pilota (fondo volo)  ",
    "F": "Pilota in addestramento (primi 12 mesi)",
    "G": "Pilota collaudatore",
    "H": "Tecnico di volo",
    "I": "Lavoratori in esodo art 41 comma 5-bis D.lgs 14 settembre 2015, n. 148. Circ. n. 48/2021",
    "L": "Tecnico di volo in addestramento (primi 12 mesi)",
    "M": "Tecnico di volo per i collaudi",
    "N": "Assistente di volo",
    "P": "Giornalista professionista, praticante o pubblicista iscritto all’INPGI",
    "Q": "Lavoratore con qualifica di quadro",
    "R": "Apprendista mantenuto in servizio come impiegato (art. 7 comma 9 T.U. dell’Apprendistato, circ. n. 128/2012)",
    "S": "Lavoratore autonomo dello spettacolo. (msg n.10025/2010). Convenzionalmente, per tali lavoratori, gli elementi <Qualifica2> e <Qualifica3> dovranno essere impostati rispettivamente a “F” e “D”.",
    "T": "Lavoratori per i quali viene versata la contribuzione figurativa correlata all’esodo. Circ. n. 62/2017.",
    "U": "Lavoratore autonomo sportivo professionista. Convenzionalmente, per tali lavoratori, gli elementi <Qualifica2> e <Qualifica3> dovranno essere impostati rispettivamente a “F” e “D”.",
    "V": "Lavoratori in esodo ex art. 4 legge n. 92/2012. Domanda presentata a decorrere dal 1° maggio 2015",
    "W": "Apprendista mantenuto in servizio come operaio (art. 7 comma 9 T.U. dell’Apprendistato, circ. n. 128/2012)",
    "Z": "Lavoratore escluso da contribuzione INPS previdenziale ed assistenziale, OTD o OTI dipendente di azienda agricola in genere ovvero OTD dipendente da cooperativa L.240/84 per il quale possono essere versate le quote di pensione oppure poste a conguaglio somme a titolo di donazione sangue e midollo osseo."
}

# Creazione di liste di oggetti a partire dai dizionari
pos_contributiva = [PosContributiva(k, v) for k, v in pos_contributiva_dict.items()]
denuncia_individuale = [DenunciaIndividuale(k, v) for k, v in tipo_regolarizz_dict.items()]
qualifiche = [Qualifica(k, v) for k, v in qualifica_dict.items()]

# Funzione di ricerca
def ricerca(codice, lista):
    for elemento in lista:
        if elemento.codice == codice:
            return elemento
    return None

# Funzione di aggiornamento
def aggiorna(codice, nuova_descrizione, lista):
    for elemento in lista:
        if elemento.codice == codice:
            elemento.descrizione = nuova_descrizione
            return True
    return False

# Converti tutto in JSON
dati_json = json.dumps({
    "PosContributiva": [obj.to_dict() for obj in pos_contributiva],
    "DenunciaIndividuale": [obj.to_dict() for obj in denuncia_individuale],
    "Qualifiche": [obj.to_dict() for obj in qualifiche]
}, indent=4)



