""" 
Exo 8
"""


def depart(list) -> list:
    depart = list
    while len(depart) % 4 != 0:
        depart.append("=")
    print(depart)


depart(["Q", "U", "J", "D", "R", "A"])
