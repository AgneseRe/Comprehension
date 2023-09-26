# ***** ESERCIZI LIST COMPREHENSION PARTE 2 *****
prodotti = ["Biscotti", "spaghetti", "Speck", "Mele renette", "Sale grosso", "Sale fine"]

# 1. Creare una lista che contenga i soli prodotti il cui nome inizia per S oppure s
#   ["spaghetti", "Speck", "Sale grosso", "Sale fine"]
prodotti_s1 = [prodotto for prodotto in prodotti if prodotto[0] == 'S' or prodotto[0] == 's']
prodotti_s2 = [prodotto for prodotto in prodotti if prodotto.startswith('S') or prodotto.startswith('s')]
prodotti_s3 = [prodotto for prodotto in prodotti if prodotto.upper()[0] == 'S']     # prodotto.lower()[0] == 's'
print("RESULT 1: ", prodotti_s3)

# 2. Creare una lista che contenga i soli prodotti il cui nome è costituito da due parole
# (cosa restituisce il metodo .split ?) ["Mele renette", "Sale grosso", "Sale fine"]
prodotti_2parole = [prodotto for prodotto in prodotti if len(prodotto.split(" ")) == 2]
prodotti_2parole2 = [prodotto for prodotto in prodotti if " " in prodotto]  # prende anche quelle da 3, 4 ... parole
prodotti_2parole3 = [prodotto for prodotto in prodotti if prodotto.count(" ") == 1]
print("RESULT 2: ", prodotti_2parole3)

# 3. Creare una lista che contenga i soli prodotti che hanno lunghezza è 9
#   ["spaghetti", "Sale fine"]
prodotti9 = [prodotto for prodotto in prodotti if len(prodotto) == 9]
print("RESULT 3: ", prodotti9)

# 4. Creare una lista che contenga i prodotti scritti in maiuscolo se la loro lunghezza è 9, altrimenti in minuscolo.
#   ["biscotti", "SPAGHETTI", "speck", "mele renette", "sale grosso", "SALE FINE"]
prodotti_maiusc_minusc = [prodotto.upper() if len(prodotto) == 9 else prodotto.lower() 
                            for prodotto in prodotti]
print("RESULT 4: ", prodotti_maiusc_minusc)

# 5. Creare una lista che contenga i prodotti scritti in maiuscolo se la loro lunghezza è 9, altrimenti in minuscolo.
#    Si prendono solo i prodotti il cui nome è costituito da una sola parola (no spazi all'interno)
#   ["biscotti", "SPAGHETTI", "speck"]
prodotti_maiusc_minusc_nove = [prodotto.upper() if len(prodotto) == 9 else prodotto.lower() 
                                for prodotto in prodotti if len(prodotto.split(" ")) == 1]
print("RESULT 5: ", prodotti_maiusc_minusc_nove)

# 6. Creare tutte le possibili combinazioni ottenute lanciando due dadi a 6 facce
combinazioni = [[dado1, dado2] for dado1 in range(1, 7) for dado2 in range(1, 7)]
print("RESULT 6: ", combinazioni)