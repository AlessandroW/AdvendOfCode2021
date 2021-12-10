test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

def is_open(char):
    return char in "([{<"

def is_closing(char):
    return char in ")]}>"

def closes(char, closing):
    return (char == "[" and closing == "]") \
        or (char == "(" and closing == ")") \
        or (char == "<" and closing == ">") \
        or (char == "{" and closing == "}") \

def part1(input):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    result = []

    for line in input.split("\n"):
        stack = []
        for char in line:
            if is_open(char):
                stack.append(char)
            elif closes(stack[-1], char):
                del stack[-1]
            else:
                result.append(points[char])
                break
    print(sum(result))

with open("day10.txt") as f:
    input = f.read()

part1(input)

def part2(input):
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    scores = []
    for line in input.split("\n"):
        stack = []
        for char in line:
            if is_open(char):
                stack.append(char)
            elif closes(stack[-1], char):
                del stack[-1]
            else:
                break
        else:
            if stack:
                score = 0
                for element in reversed(stack):
                    score *= 5
                    score += points[element]
                scores.append(score)
    scores = sorted(scores)
    print(scores[len(scores) // 2])

part2(input)
