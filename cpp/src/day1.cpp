#include "day1.h"
#include "utils.h"
#include <iostream>

Day1::Day1(){
    auto input = Utilities::read_all_lines_in_file("../../data/day1.txt");
    for (const auto& line : input) {
        puzzle.emplace_back(std::stoi(line));
    }
}

void Day1::print_solution_1(){
    int increases = 0;
    for (size_t i = 1; i < puzzle.size(); ++i) {
        if (puzzle[i] > puzzle[i-1]){
            ++increases;
        }
    }
    std::cout << "Part 1: " << increases << "\n";
}

void Day1::print_solution_2(){
    int increases = 0;
    for (size_t i = 3; i < puzzle.size(); ++i) {
        if (puzzle[i] > puzzle[i-3]){
            ++increases;
        }
    }
    std::cout << "Part 2: " << increases << "\n";

}
