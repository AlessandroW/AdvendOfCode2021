#include <array>
#include <bits/c++config.h>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

void checkCandidates(std::vector<std::string> &input,
                     std::vector<int> &candidates, int position, char value) {
  // Remove all candidates that don't have the value at the position.
    if (candidates.size() == 1){
        std::cout << "Final " << input[0] << "\n";
        return;
    }
  std::vector<int>::iterator candidate;
  std::cout << "Size " << candidates.size() << " value " << value << "\n";
  for (candidate = candidates.begin(); candidate != candidates.end();) {
    if (input[*candidate][position] != value) {
      std::cout << *candidate << " " << input[*candidate] << "\n";
      std::cout << "removing"
                << "\n";
      candidate = candidates.erase(candidate);
    } else {
      ++candidate;
    }
  }
}

int main() {
  const std::size_t bits{5};
  std::ifstream infile("day3.txt");
  std::array<std::array<int, 2>, bits> data{};
  std::vector<std::string> input{};
  std::string line;
  std::vector<int> co2Candidates{};
  std::vector<int> o2Candidates{};
  int gamma{0};
  int epsilon{0};
  char mostCommon;
  char leastCommon;

  // Counting
  int lineNumber{0};
  // TODO create a most common / least common function based on the remaining candidates
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
    mostCommon = '1';
    leastCommon = '0';
    if (data[i][1] > data[i][0]) {
      gamma += pow(2, bits - i - 1);
    } else if (data[i][0] > data[i][1]) {
      epsilon += pow(2, bits - i - 1);
      mostCommon = '0';
      leastCommon = '1';
    }
    checkCandidates(input, o2Candidates, i, mostCommon);
    // checkCandidates(input, co2Candidates, i, leastCommon);
  }

  std::cout << "Result " << o2Candidates[0] << " " << co2Candidates[0] << "\n";
  std::cout << "Result " << gamma * epsilon << "\n";
}
