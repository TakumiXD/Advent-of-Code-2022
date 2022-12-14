with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    rope = [ [0,0] for i in range(10) ]

    visited = set()

    for line in inputs:
        direction, steps = line.split(" ")
        for i in range(int(steps)):
            if direction == "L":
                rope[0][1] -= 1
            elif direction == "R":
                rope[0][1] += 1
            elif direction == "U":
                rope[0][0] += 1
            else:
                rope[0][0] -= 1

            for j in range(1,10):
                if rope[j][0] - rope[j-1][0] == -2:
                    rope[j][0] += 1
                    if rope[j][1] < rope[j-1][1]:
                        rope[j][1] += 1
                    elif rope[j][1] > rope[j-1][1]:
                        rope[j][1] -= 1
                elif rope[j][0] - rope[j-1][0] == 2:
                    rope[j][0] -= 1
                    if rope[j][1] < rope[j-1][1]:
                        rope[j][1] += 1
                    elif rope[j][1] > rope[j-1][1]:
                        rope[j][1] -= 1         
                elif rope[j][1] - rope[j-1][1] == -2:
                    rope[j][1] += 1
                    if rope[j][0] < rope[j-1][0]:
                        rope[j][0] += 1
                    elif rope[j][0] > rope[j-1][0]:
                        rope[j][0] -= 1
                elif rope[j][1] - rope[j-1][1] == 2:
                    rope[j][1] -= 1
                    if rope[j][0] < rope[j-1][0]:
                        rope[j][0] += 1
                    elif rope[j][0] > rope[j-1][0]:
                        rope[j][0] -= 1


            visited.add((rope[9][0], rope[9][1]))

    print(len(visited))