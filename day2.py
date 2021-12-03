#!/usr/bin/env python3

with open("day2.txt") as f:
    input = f.read().split("\n")

horizontal = 0
depth = 0
aim = 0

for line in input[:-1]:
    value = int(line.split()[-1])
    if "forward" in line:
        horizontal += value
        depth += aim * value
    elif "down" in line:
        aim += value
    elif "up" in line:
        aim -= value
print("Part 1")
print(horizontal * aim)
print("Part 2")
print(horizontal * depth)
