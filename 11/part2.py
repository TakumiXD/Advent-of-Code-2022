from operator import add, mul
from functools import partial
from math import lcm

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    lines = [line.strip() for line in lines]

    NUM_OF_MONKEYS = 8
    i = 0

    numOfInspections = [ 0 for i in range(NUM_OF_MONKEYS) ]
    items = []
    operation = []
    function = lambda a, b, op: {"+": add, "*": mul} [op](a, b)
    testDivisibleBy = []
    divisibleThen = []
    notDivisibleThen = []

    for monkeyNum in range(NUM_OF_MONKEYS):
        i += 1
        itemsForMonkey = lines[i].replace("Starting items: ", '').split(", ")
        itemsForMonkey = [int(x) for x in itemsForMonkey]
        items.append(itemsForMonkey)

        i += 1
        operationLine = lines[i].replace("Operation: new = ", '')
        if (operationLine == "old * old"):
            operation.append(lambda x: x * x)
        else:
            _, op, arg = operationLine.split(" ")
            operation.append(partial(function, b=int(arg), op=op))

        i += 1
        testDivisibleBy.append(int(lines[i][-2:]))

        i += 1
        divisibleThen.append(int(lines[i][-1]))

        i += 1
        notDivisibleThen.append(int(lines[i][-1]))
        
        i += 2

    i = 0
    lcmOfDivisors = lcm(*testDivisibleBy)

    for i in range(10000):
        for j in range(NUM_OF_MONKEYS):
            while items[j]:
                numOfInspections[j] += 1
                worryLevel = operation[j](items[j].pop(0))
                worryLevel = worryLevel % lcmOfDivisors
                if (worryLevel % testDivisibleBy[j]) == 0:
                    items[divisibleThen[j]].append(worryLevel)
                else:
                    items[notDivisibleThen[j]].append(worryLevel)

    numOfInspections.sort(reverse=True)
    print(numOfInspections[0] * numOfInspections[1])