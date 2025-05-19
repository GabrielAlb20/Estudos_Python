"""
Tipos em Python na prática


nomes = list = ['Geek', 'University']

versoes: tuple = (3, 4, 7)

opcoes: dict = {'ar': True, 'banco_couro': True}

valores: set = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)




from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Geek', 'University']

versoes: Tuple[int, int, int] = (3, 7, 4)

opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}

valores: Set[int] = {3, 4, 5, 6}

print(__annotations__)

"""

import random


# https://www.alt-codes.net/suit-cards.php
NAIPES = '♠ ♥ ♣ ♦ ♤ ♢ ♡ ♧ ♢'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


# PAREI NO MINUTO 12:57 AULA 165.