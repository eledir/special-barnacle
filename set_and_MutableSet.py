insieme_frutta = {"mela", "banana", "arancia"}
print("mela" in insieme_frutta) # Verifica di appartenenza
print(len(insieme_frutta))      # Ottenere il numero di elementi

altro_insieme = {"banana", "kiwi"}
unione = insieme_frutta | altro_insieme   # Unione
intersezione = insieme_frutta & altro_insieme # Intersezione
differenza = insieme_frutta - altro_insieme  # Differenza

insieme_mutabile = {1, 2, 3}
insieme_mutabile.add(4)
insieme_mutabile.remove(2)