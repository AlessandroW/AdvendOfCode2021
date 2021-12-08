from pprint import pprint as print
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
            for line in input.split("\n")]


def convert(signals):
    segments = {}
    taken = []
    segments["c"] = list(filter(lambda x: len(x) == 2, signals))[0]
    segments["f"] = segments["c"]
    taken.extend(segments["f"])
    segments["a"] = [char for char in list(filter(lambda x: len(x) == 3, signals))[0]
                     if char not in taken][0]
    taken.append(segments["a"])
    five_segments = list(filter(lambda x: len(x) == 5, signals))
    segments["b"] = list(char for char in list(filter(lambda x: len(x) == 4, signals))[0]
                         if char not in taken)
    # TODO
    segments["d"] = list(char for char in segments["b"]
                         if char in filter(
                                 # Number 3
                                 lambda signal: all(char in signal
                                                    for char in segments["c"]),
                                 five_segments))
    # taken.append(segments["d"])
    segments["b"] = next(char for char in segments["b"]
                         if char not in segments["d"])
    taken.extend(segments["b"])
    segments["g"] = next((char for char in "abcdefg"
                          if char not in taken and
                          all(char in signal for signal in five_segments)))
    taken.append(segments["g"])
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

parsed_text = parser(test)
print([convert(text["signals"]) for text in parsed_text])
