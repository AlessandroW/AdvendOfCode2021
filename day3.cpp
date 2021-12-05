#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#define DOCTEST_CONFIG_IMPLEMENT
#include <doctest/doctest.h>

void checkCandidates(std::vector<std::string> &input,
                     std::vector<int> &candidates, int position, char value) {
  // Remove all candidates that don't have the value at the position.
  if (candidates.size() == 1) {
    return;
  }
  std::vector<int>::iterator candidate;
  for (candidate = candidates.begin(); candidate != candidates.end();) {
    if (input[*candidate][position] != value) {
      candidate = candidates.erase(candidate);
    } else {
      ++candidate;
    }
  }
}

char getMostCommon(std::vector<std::string> &input,
                   std::vector<int> &candidates, int position) {
  std::size_t sum{0};
  for (auto candidate : candidates) {
    if (input[candidate][position] == '1') {
      ++sum;
    }
  }
  if (sum >= candidates.size() - sum) {
    return '1';
  }
  return '0';
}

char getLeastCommon(std::vector<std::string> &input,
                   std::vector<int> &candidates, int position) {
  std::size_t sum{0};
  for (auto candidate : candidates) {
    if (input[candidate][position] == '1') {
      ++sum;
    }
  }
  if (sum >= candidates.size() - sum) {
    return '0';
  }
  return '1';
}

int toBinary(std::string number) {
  int result = 0;
  for (auto i = 0; i < number.size(); ++i) {
    if (number[i] == '1') {
      result += pow(2, number.size() - i - 1);
    }
  }
  return result;
}

int main(int argc, char **argv) {
  doctest::Context context;
  context.applyCommandLine(argc, argv);

  int res = context.run(); // run doctest

  // important - query flags (and --exit) rely on the user doing this
  if (context.shouldExit()) {
    // propagate the result of the tests
    return res;
  }

  const std::size_t bits{12};
  std::string filename = "../day3.txt";
  if (argc > 1) {
    filename = argv[1];
  }
  std::ifstream infile(filename);
  std::array<std::array<int, 2>, bits> data{};
  std::vector<std::string> input{};
  std::string line;
  std::vector<int> co2Candidates{};
  std::vector<int> o2Candidates{};
  int gamma{0};
  int epsilon{0};
  int o2{0};
  int co2{0};
  char mostCommon;
  char leastCommon;

  // Counting
  int lineNumber{0};
  while (std::getline(infile, line)) {
    co2Candidates.push_back(lineNumber);
    o2Candidates.push_back(lineNumber);
    input.push_back(line);
    ++lineNumber;
    for (auto i = 0; i < line.size(); ++i) {
      if (line[i] == '0') {
        data[i][0] += 1;
      } else {
        data[i][1] += 1;
      }
    }
  }

  // Convert binary to decimal
  for (int i = 0; i < bits; ++i) {
    if (data[i][1] > data[i][0]) {
      gamma += pow(2, bits - i - 1);
    } else {
      epsilon += pow(2, bits - i - 1);
    }
  }

  std::cout << "Part 1 " << gamma * epsilon << "\n";

  // Part II

  for (auto i = 0; i < bits; ++i) {
    mostCommon = getMostCommon(input, o2Candidates, i);
    checkCandidates(input, o2Candidates, i, mostCommon);

    leastCommon = getLeastCommon(input, co2Candidates, i);
    checkCandidates(input, co2Candidates, i, leastCommon);
  }

  o2 = toBinary(input[o2Candidates[0]]);
  co2 = toBinary(input[co2Candidates[0]]);

  std::cout << "Part 2 " << o2 * co2 << "\n";
}

TEST_CASE("Test: get most/least common bit.") {
  std::vector<std::string> input{{"10000"},
                                 {"11110"},
                                 {"11100"},
                                 {"11000"}};
  std::vector<int> candidates{0, 1, 2, 3};
  CHECK(getMostCommon(input, candidates, 0) == '1');
  CHECK(getMostCommon(input, candidates, 1) == '1');
  CHECK(getMostCommon(input, candidates, 2) == '1');
  CHECK(getMostCommon(input, candidates, 3) == '0');
  CHECK(getMostCommon(input, candidates, 4) == '0');

  CHECK(getLeastCommon(input, candidates, 0) == '0');
  CHECK(getLeastCommon(input, candidates, 1) == '0');
  CHECK(getLeastCommon(input, candidates, 2) == '0');
  CHECK(getLeastCommon(input, candidates, 3) == '1');
  CHECK(getLeastCommon(input, candidates, 4) == '1');

}

TEST_CASE("Test: binary conversion") {
  CHECK(toBinary("0000") == 0);
  CHECK(toBinary("0001") == 1);
  CHECK(toBinary("0011") == 3);
  CHECK(toBinary("1011") == 11);
}
