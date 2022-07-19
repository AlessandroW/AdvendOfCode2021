import numpy as np

test = "16,1,2,0,4,2,7,1,2,14"

with open("./day7.txt") as f:
    input = f.read().split("\n")[0]

def parse(input):
    numbers = list(map(int, input.split(",")))
    return np.array(numbers)

def part1(input):
    numbers = parse(input)
    median = np.median(numbers)
    cost = sum(abs(number - median) for number in numbers)
    print(median, cost)

def part2(input):
    numbers = parse(input)
    gausssum = lambda n: (n*(n+1))/2
    loss = lambda x, target: gausssum(abs(x - target))
    calculate_loss = lambda target: sum(loss(x, target) for x in numbers)
    candidates = [calculate_loss(candidate)
                  for candidate in range(min(numbers), max(numbers)+1)]
    print(min(candidates))

part1(input)
part2(input)
