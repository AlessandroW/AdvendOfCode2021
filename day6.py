# each latern fish creates a new one every 7 days
# one number represents the number of das until the fish creates a new one
import numpy as np

test = "3,4,3,1,2"

with open("day6.txt") as f:
    text = f.read().split("\n")[0]

def parse(input):
    return np.array(list(map(int, input.split(","))))

def day(state):
    new_fish = np.array([9 for i in range(np.count_nonzero(state==0))])
    state = np.concatenate((state, new_fish), axis=None)
    state = np.where(state == 0, 7, state)
    state -= 1
    return state

state = parse(text)
for i in range(80):
    state = day(state)
print(len(state))

state = {i: 0 for i in range(7)}
stack = []
for fish in parse(test):
    state[fish] += 1

day = 0
while (day < 10):
    if state[day % 7] != 0:
        stack.append(0)
        stack.append(0)
        stack.append(state[day % 7])
        print("zero at day", day)
    day += 1

print(state)
