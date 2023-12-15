#  Escribe un programa que genere una lista de 10 números aleatorios. Luego, 
#  ordena esta lista en orden ascendente y descendente, y finalmente imprime ambas versiones.
# **Instrucciones:**
#	1. Genera una lista de 10 números aleatorios.
#	2. Ordena la lista en orden ascendente y guárdala en una variable.
#	3. Ordena la lista en orden descendente y guárdala en otra variable.
#	4. Imprime la lista original y ambas listas ordenadas.

import random
random_numbers = [random.randint(0, 10) for x in range(10)]
print(f"Lista Original: ", random_numbers)
numMenor_Mayor = sorted(random_numbers)
print(f"Lista en orden Ascendente: ", numMenor_Mayor)
numMayor_Menor = sorted(random_numbers, reverse= True)
print(f"Lista en orden descendente: ", numMayor_Menor)
