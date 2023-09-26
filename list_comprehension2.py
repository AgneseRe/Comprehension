# ***** ESERCIZI LIST COMPREHENSION PARTE 1 *****
import math

# Creare una lista che contenga i soli numeri pari compresi tra 1 e 10 inclusi
numeri_pari = [i for i in range(1, 11, 2)]
print(numeri_pari)

# Creare una lista che contenga la tabellina del 5
numeri5 = [i for i in range(5, 51, 5)]
print(numeri5)

# Data la lista targhe = ["BN000RT", "FA789WE", "HC090YT", "AA456QB"], creare
# una lista che contenga le sole due lettere iniziali di ciascuna targa
#   es. ["BN", "FA", "HC", "AA"]
targhe = ["BN000RT", "FA789WE", "HC090YT", "AA456QB", "HP381GG"]
iniziali = [targa[:2] for targa in targhe]
print(iniziali)

# Creare una lista che contenga le radici quadrate dei numeri compresi tra 30 e 50 (usare math.sqrt())
radici = [math.sqrt(i) for i in range(30, 51)]
print(radici)

# Creare una lista che contenga le sole targhe che iniziano per H
targhe_H = [targa for targa in targhe if targa[0] == 'H']   # if targa.startswith('H')
print(targhe_H)

# Creare una lista che contenga le sole targhe il cui primo numero è uno 0
targhe_0 = [targa for targa in targhe if targa[2] == '0']   # ATTENZIONE AGLI APICI
print(targhe_0)

# Creare una lista che contenga le prime due lettere della targa se la targa inizia per 'H',
# altrimenti che contenga i tre numeri centrali. Result ["000", "789", "HC", "456", "HP"]
targhe_letters_or_numbers = [targa[:2] if targa.startswith('H') else targa[2:5] for targa in targhe]
print(targhe_letters_or_numbers)

# Creare una lista di booleani che contenga True se la targa inizia per H, altrimenti False
# Il risultato deve essere del tipo [False, False, True, False, True]
targhe_booleane = [True if targa.startswith('H') else False for targa in targhe]
print(targhe_booleane)
