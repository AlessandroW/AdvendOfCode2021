#include "day2.h"
#include "utils.h"
#include <stdexcept>
#include <string_view>
#include <string>
#include <iostream>

Day2::Day2() {
    // Parse puzzle input
    for (std::string_view line : Utilities::read_all_lines_in_file("../../data/day2.txt")) {
        if (std::string::size_type pos = line.find(' '); pos != std::string::npos) {
            char direction = line[0];
            int unit = std::stoi(std::string(line.substr(pos + 1, line.size())));
            Day2::puzzle.emplace_back(direction, unit);
        }
    }
};

void Day2::print_solution_1(){
    int h_position = 0;
    int depth = 0;
    for (const auto& line : Day2::puzzle) {
        switch (line.first) {
            case 'f':
                h_position += line.second;
                break;
            case 'u':
                depth -= line.second;
                break;
            case 'd':
                depth += line.second;
                break;
            default:
                throw std::invalid_argument("Invalid direction!");
                break;
        }
    }
    std::cout << "Part 1: " << h_position * depth << "\n";
}

void Day2::print_solution_2() {
    int h_position = 0;
    int depth = 0;
    int aim = 0;
    for (const auto& line : Day2::puzzle) {
        switch (line.first) {
            case 'f':
                h_position += line.second;
                depth += aim * line.second;
                break;
            case 'u':
                aim -= line.second;
                break;
            case 'd':
                aim += line.second;
                break;
            default:
                throw std::invalid_argument("Invalid direction!");
                break;
        }
    }
    std::cout << "Part 2: " << h_position * depth << "\n";
}
