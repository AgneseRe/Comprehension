# ***** ESERCIZI DICTIONARIES COMPREHENSION PARTE 1 *****
import math

# *** FUNCTION FOR DICTIONARY ***
def calcola_circonferenza(raggio):
    return 2 * math.pi * raggio
    
# 1. Creare un dizionario che a ciascun numero (compreso tra 1 e 30) associ il suo successivo
diz_successivi = {i:i+1 for i in range(1, 31)}    
print("RESULT 1: ", diz_successivi)

# 2. Creare un dizionario che a ciascun valore del raggio (compreso tra 1 e 10) associ l'area
#       del cerchio corrispondente (math.pi * (r ** 2))
diz_aree = {i:math.pi * (i ** 2) for i in range(1, 11)}
print("RESULT 2: ", diz_aree)

# 3. Date due liste, una contenente i nomi di persona e una contenente le età delle persone,
#       creare un dizionario che associ a ciasscuna persona la corrispondente età
nomi = ["Adele", "Anastasia", "Beatrice", "Carlo", "Edoardo"]
età = [38, 50, 18, 21, 35]
diz_persone = {nomi[i]:età[i] for i in range(0, len(nomi))}    # oppure range(len(età))
print("RESULT 3: ", diz_persone)

# 4. Creare un dizionario che ad ogni numero (compreso tra 1 e 10) associa la lunghezza della
#    circonferenza con quel dato numero come raggio (2*math.pi*r)
# 4b. Realizzare una funzione che, passato il raggio del cerchio come parametro, calcoli la 
#   lunghezza della circonferenza relativa. La lunghezza della Crf deve essere ritornata (return)
diz_circonferenze = {i:calcola_circonferenza(i) for i in range(1, 11)}   # str("{:.3f}".format(2*math.pi*i))
print("RESULT 4: ", diz_circonferenze)