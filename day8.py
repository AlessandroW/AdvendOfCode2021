test = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def parser(input):
    return [{"signals": sorted(line.split(" | ")[0].split(" "), key=len),
             "digits": line.split(" | ")[1].split(" ")}
            for line in input.split("\n")
            if len(line) > 0]

def intersection(*args):
    result = set(args[0])
    for arg in args:
        result = result & set(arg)
    return result

def convert(signals):
    two_segments = list(filter(lambda x: len(x) == 2, signals))  # 1
    three_segments = list(filter(lambda x: len(x) == 3, signals))  # 7
    four_segments = list(filter(lambda x: len(x) == 4, signals))  # 4
    five_segments = list(filter(lambda x: len(x) == 5, signals))  # 2, 3, 5
    six_segments  = list(filter(lambda x: len(x) == 6, signals))  # 0, 6, 9
    seven_segments  = list(filter(lambda x: len(x) == 7, signals))  # 8

    segments = {}
    taken = []
    segments["c"] = two_segments[0]
    segments["f"] = segments["c"]
    taken.extend(segments["f"])

    segments["a"] = [char for char in three_segments[0]
                     if char not in taken][0]
    taken.append(segments["a"])
    segments["b"] = list(char for char in four_segments[0]
                         if char not in taken)
    segments["d"] = next(char for char in segments["b"]
                         if char in set(four_segments[0]) & intersection(*five_segments))
    taken.append(segments["d"])
    segments["b"] = next(char for char in segments["b"]
                         if char not in segments["d"])
    taken.extend(segments["b"])
    segments["c"] = next(char for char in segments["c"]
                         if all(char in segment for segment in
                                # 2, 3
                                filter(lambda x: segments["b"]
                                       not in x, five_segments)))
    segments["f"] = next(char for char in segments["f"]
                         if char != segments["c"])

    segments["g"] = next(char for char in "abcdefg"
                         if char not in taken and
                         all(char in signal for signal in five_segments))
    taken.append(segments["g"])
    segments["e"] = next(char for char in "abcdefg"
                         if char not in taken)
    taken.append(segments["e"])
    assert len(taken) == 7, sorted(segments.keys())
    return segments


def encode(signal, segments={key: key for key in "abcdefg"}):
    segments = {v: k for k, v in segments.items()}
    converted = "".join(sorted(segments[s] for s in signal))
    if converted == "abcefg":
        return 0
    elif converted == "cf":
        return 1
    elif converted == "acdeg":
        return 2
    elif converted == "acdfg":
        return 3
    elif converted == "bcdf":
        return 4
    elif converted == "abdfg":
        return 5
    elif converted == "abdefg":
        return 6
    elif converted == "acf":
        return 7
    elif converted == "abcdefg":
        return 8
    elif converted == "abcdfg":
        return 9
    else:
        raise ValueError(converted, signal)


assert encode("abcefg") == 0
assert encode("cf") == 1

with open("day8.txt") as f:
    input = f.read()

parsed_text = parser(input)
converted_segments = [convert(text["signals"]) for text in parsed_text]
result = [encode(signal, segments) for segments, text
          in zip(converted_segments, parsed_text)
          for signal in text["digits"]]

part1 = sum(1 for number in result if number in [1,4,7,8])
print(part1)

result = [int("".join([str(encode(signal, segments))
                       for signal in text["digits"]]))
          for segments, text
          in zip(converted_segments, parsed_text)
          ]
part2 = sum(number for number in result)
print(part2)
