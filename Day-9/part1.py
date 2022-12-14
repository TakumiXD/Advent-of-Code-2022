with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

    head = [0,0]
    tail = [0,0]
    visited = set()

    for line in inputs:
        direction, steps = line.split(" ")
        for i in range(int(steps)):
            if direction == "L":
                head[1] -= 1
            elif direction == "R":
                head[1] += 1
            elif direction == "U":
                head[0] += 1
            else:
                head[0] -= 1

            if tail[0] - head[0] == -2:
                tail[0] += 1
                if tail[1] < head[1]:
                    tail[1] += 1
                elif tail[1] > head[1]:
                    tail[1] -= 1
            elif tail[0] - head[0] == 2:
                tail[0] -= 1
                if tail[1] < head[1]:
                    tail[1] += 1
                elif tail[1] > head[1]:
                    tail[1] -= 1         
            elif tail[1] - head[1] == -2:
                tail[1] += 1
                if tail[0] < head[0]:
                    tail[0] += 1
                elif tail[0] > head[0]:
                    tail[0] -= 1
            elif tail[1] - head[1] == 2:
                tail[1] -= 1
                if tail[0] < head[0]:
                    tail[0] += 1
                elif tail[0] > head[0]:
                    tail[0] -= 1

            visited.add((tail[0], tail[1]))

    print(len(visited))