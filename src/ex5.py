"""
5
"""
depart = "01000001010000100100001101000100"
n = 6
j = 1

tab = []
for i in range(0, len(depart), 6):
    tab.append(depart[i:i+6])
    if len(depart) % 6 != 0:
        rip_last = tab.pop()
        dif = 6 - (len(depart % 6))
        solution = rip_last + ("0" * dif)
        tab.append(solution)
print(tab)
