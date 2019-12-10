""" 
Exo 7
"""
n2ch = "".join([
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789-_",
])
ch2n = dict(zip(n2ch, range(len(n2ch))))


def depart(int_list) -> list:

    depart = []
    for integer in int_list:
        depart.append(
            list(ch2n.keys())[list(ch2n.values()).index(integer)])
    print(depart)


depart([16, 20, 9, 3, 17, 0])


# depart = [16, 20, 9, 3, 17, 0]
# for integer in depart:
#     depart.append(
#         list(ch2n.keys())[list(ch2n.values()).index(integer)])
#     print(depart)
