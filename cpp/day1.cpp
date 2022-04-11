#include "day1.h"
#include "utils.h"
#include <iostream>

Day1::Day1(){
    auto Input = Utilities::ReadAllLinesInFile("../day1.txt");
    for (const auto& line : Input) {
        Puzzle.push_back(std::stoi(line));
    }
}

void Day1::PrintSolution1(){
    int Increases = 0;
    for (int i = 1; i < Puzzle.size(); ++i) {
        if (Puzzle[i] > Puzzle[i-1]){
            ++Increases;
        }
    }
    std::cout << "Part 1: " << Increases << "\n";
}

void Day1::PrintSolution2(){
    int Increases = 0;
    for (int i = 3; i < Puzzle.size(); ++i) {
        if (Puzzle[i] > Puzzle[i-3]){
            ++Increases;
        }
    }
    std::cout << "Part 2: " << Increases << "\n";

}
