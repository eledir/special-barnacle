#!/usr/bin/env python
import os
import django

# Configurazione dell'ambiente Django
# Imposta la variabile d'ambiente per il modulo di impostazione di Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fidelity_card_project.settings')
# Inizializza Django
django.setup()

# Importa il modello Reward dal modulo loyalty
from loyalty.models import Reward

# Lista dei premi di bellezza Hair da aggiungere
# Ogni premio è rappresentato come un dizionario con nome, descrizione, punti richiesti e percentuale di sconto
beauty_rewards = [
    {
        'name': 'Shampoo Ristrutturante alla Keratina',
        'description': 'Deterge e rinforza i capelli fragili.',
        'points_required': 1500,
        'discount_percentage': 0
    },
    {
        'name': 'Maschera Nutriente all\'Olio di Argan',
        'description': 'Idrata in profondità e dona lucentezza.',
        'points_required': 2000,
        'discount_percentage': 0
    },
    {
        'name': 'Taglio & Piega Professionale',
        'description': 'Un look fresco e alla moda con i migliori hairstylist.',
        'points_required': 5000,
        'discount_percentage': 0
    },
    {
        'name': 'Trattamento alla Cheratina Lisciante',
        'description': 'Capelli lisci e setosi per settimane.',
        'points_required': 8000,
        'discount_percentage': 0
    },
    {
        'name': 'Colore Professionale Senza Ammoniaca',
        'description': 'Colore vibrante e senza danni.',
        'points_required': 7000,
        'discount_percentage': 0
    },
    {
        'name': 'Extension Capelli Naturali',
        'description': 'Volume e lunghezza in un attimo!',
        'points_required': 10000,
        'discount_percentage': 0
    },
    {
        'name': 'Spray Volumizzante alla Biotina',
        'description': 'Dona corpo e volume ai capelli sottili.',
        'points_required': 1800,
        'discount_percentage': 0
    },
    {
        'name': 'Spazzola Termica Professionale',
        'description': 'Perfetta per uno styling facile e veloce.',
        'points_required': 3500,
        'discount_percentage': 0
    },
    {
        'name': 'Trattamento Detox per il Cuoio Capelluto',
        'description': 'Purifica e riequilibra la cute.',
        'points_required': 4000,
        'discount_percentage': 0
    },
    {
        'name': 'Gift Card Bronze Salone di Bellezza',
        'description': 'Un trattamento personalizzato a tua scelta!',
        'points_required': 12000,
        'discount_percentage': 0
    },
]

def add_beauty_rewards():
    # Funzione per aggiungere i premi al database
    rewards_added = 0  # Contatore per i premi aggiunti
    rewards_updated = 0  # Contatore per i premi aggiornati
    
    for reward_data in beauty_rewards:
        # Verifica se il premio esiste già usando il nome come identificatore
        reward, created = Reward.objects.update_or_create(
            name=reward_data['name'],  # Usa il nome come chiave primaria
            defaults={
                'description': reward_data['description'],  # Descrizione del premio
                'points_required': reward_data['points_required'],  # Punti richiesti per riscattare
                'discount_percentage': reward_data['discount_percentage'],  # Percentuale di sconto
                'is_active': True  # Imposta il premio come attivo
            }
        )
        
        if created:  # Se il premio è stato creato
            rewards_added += 1  # Incrementa il contatore dei premi aggiunti
            print(f"Aggiunto: {reward.name}")  # Stampa il nome del premio aggiunto
        else:  # Se il premio esisteva già
            rewards_updated += 1  # Incrementa il contatore dei premi aggiornati
            print(f"Aggiornato: {reward.name}")  # Stampa il nome del premio aggiornato
    
    # Stampa un riepilogo dell'operazione
    print(f"\nOperazione completata. Aggiunti {rewards_added} nuovi premi, aggiornati {rewards_updated} premi esistenti.")

if __name__ == '__main__':
    # Punto di ingresso principale del programma
    print("Aggiunta premi di bellezza Hair al catalogo...")
    add_beauty_rewards()  # Chiama la funzione per aggiungere i premi