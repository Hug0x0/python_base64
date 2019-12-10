"""
6
"""
# binary = "010100"
# decimal = 0
# for digit in binary:
#     decimal = decimal*2 + int(digit)
# print(decimal)
# depart = ["Q", "U", "J", "D", "R", "A", "=", "="]
# convert = ''.join(map(str, depart))
# print(convert)


def depart(list) -> list:

    depart = []
    for bits in list:
        depart.append(int(bits, 2))
    print(depart)


depart(["010000", "010100", "001001",
        "000011", "010001", "000000"])
