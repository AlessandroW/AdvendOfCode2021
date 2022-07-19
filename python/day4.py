class Board():
    def __init__(self, input):
        self.board = [row.split() for row in input.split("\n") if row]

    def __str__(self):
        return "\n".join([" ".join(map(lambda element: f"{element:>2}", row)) for row in self.board])

    def check(self, number):
        for row in self.board:
            if number in row:
                for index, element in enumerate(row):
                    if element == number:
                        row[index] = "X"
        for row in self.board:
            if sum(1 for element in row if element == "X") == 5:
                return True

        for column in range(len(self.board[0])):
            if sum(1 for row in self.board if row[column] == "X") == 5:
                return True
        return False

    def count(self):
        return sum(sum(map(lambda x: int(x) if x != "X" else 0, row)) for row in self.board)


def part1():
    numbers = file[0].split(",")
    boards = [Board(input) for input in file[1:]]

    for number in numbers:
        for board in boards:
            if (board.check(number)):
                print("BINGO!")
                print(board.count() * int(number))
                return

def part2():
    numbers = file[0].split(",")
    boards = [Board(input) for input in file[1:]]
    point = None
    for number in numbers:

        if len(boards) == 1:
            if point is None:
                point = int(number)
            if boards[0].check(number):
                print("BINGO!")
                print(boards[0].count() * point)
                return
        else:
            boards = [board for board in boards if not board.check(number)]


with open("day4.txt") as f:
    file = f.read().split("\n\n")

part1()
part2()
