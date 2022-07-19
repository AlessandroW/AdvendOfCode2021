#pragma once

#include <string>
#include <vector>
#include <utility>
#include "utils.h"

class Day2 {
    public:
        Day2();
        void print_solution_1();
        void print_solution_2();
    private:
        std::vector<std::pair<char, int>> puzzle;
};
