# Installazione di neonctl su Windows

import os
import subprocess

def check_neonctl():
    """Verifica se neonctl è installato e disponibile."""
    try:
        result = subprocess.run(["neonctl", "--version"], capture_output=True, text=True, check=True)
        print(f"NeonCTL versione trovata: {result.stdout.strip()}")
    except FileNotFoundError:
        print("Errore: 'neonctl' non trovato. Assicurati di installarlo.")
        exit(1)

if __name__ == "__main__":
    check_neonctl()
    print("Esecuzione dell'applicazione...")
