with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    cycle = 0
    X = 1

    for line in lines:
        if (cycle % 40 == 0):
            print('\n', end='')
        if abs(X - cycle) <= 1:
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        cycle = cycle % 40
        if line[:4] == "addx":
            if (cycle % 40 == 0):
                print('\n', end='')
            if abs(X - cycle) <= 1:
                print('#', end='')
            else:
                print('.', end='')
            addVal = int(line.split(" ")[1])
            X += addVal
            cycle += 1
            cycle = cycle % 40
    
