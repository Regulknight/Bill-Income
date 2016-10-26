def is_into(dot, rect):
    if dot[0] < rect[0][0] or dot[0] > rect[0][0] + rect[1][0] or dot[1] < rect[0][1] or dot[1] > rect[0][1] + rect[1][1]:
        return False
    return True

rect = (0.5, 0.5), (1, 1)

mas = []

for i in range(0, 20, 1):
    line = []
    for j in range(0, 20, 1):
        line.append(is_into((i/10, j/10), rect))
    mas.append(line)
for i in mas:
    print(i)
