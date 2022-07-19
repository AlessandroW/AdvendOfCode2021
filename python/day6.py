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

state = [0] * 7
for fish in parse(text):
    state[fish] += 1

day = 0
planner = [0, 0, 0]
while (day < 256 + 1):
    today = day % 7
    state[(day + 6) % 7] += planner[0]
    planner[0] = planner[1]
    planner[1] = planner[2]
    planner[2] = 0
    if state[today] != 0:
        planner[-1] += state[today]
    day += 1
print(sum(state) + sum(planner[:-1]))  # ignore the last day as these are planned for tomorrow
