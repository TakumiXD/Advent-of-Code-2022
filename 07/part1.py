from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    path = []
    sizes = defaultdict(int)

    for line in lines:
        if line[:4] == "$ cd":
            dir = line.split(" ")[2]
            if dir == '..':
                path.pop()
            else:
                path.append(dir)
        elif line[:4] != "$ ls" and line[:4] != "dir ":
            size = int(line.split(" ")[0])
            for i in range(len(path)):
                sizes['/'.join(path[:i+1])] += size

    res = 0
    for key, value in sizes.items():
        if value <= 100000:
            res += value

    print(res)