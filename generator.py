plot = {1: 1, 2: 1, 3: 0, 4: 0, 5: 0}
dia = {1: 2, 2: 3, 3: 6, 4: 2, 5: 2, 6: 12, 7: 11, 8: 1, 9: 0, 10: 4, 11: 3}
for i in range(5):
    i += 1
    for j in range(plot[i] + 1):
        print(f'plot_{i}_{j} = load("images\\\plot\\\plot_{i}_{j}.png")')

for i in range(11):
    i += 1
    for j in range(dia[i] + 1):
        print(f'dia_{i}_{j} = load("images\\\dia\\\dia_{i}_{j}.png")')