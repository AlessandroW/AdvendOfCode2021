#include <fstream>
#include <string>
#include <iostream>
#include <sstream>

int main() {
  std::ifstream infile("day2.txt");
  std::string line;
  int horizontal {0};
  int depth {0};
  int aim {0};
  while (std::getline(infile, line)) {
    std::istringstream iss(line);
    std::string command;
    int value;

    if(!(iss >> command >> value)) { break;}
    if (command == "forward"){
      horizontal += value;
      depth += aim * value;
    } else if (command == "down") {
      aim += value;
    } else if (command == "up") {
      aim -= value;
    }
  }

  std::cout << "Part 1: " << horizontal * aim << "\n";
  std::cout << "Part 2: " << horizontal * depth << "\n";
}
