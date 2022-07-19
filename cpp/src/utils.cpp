#include "utils.h"
#include <fstream>
#include <string>

std::vector<std::string> Utilities::read_all_lines_in_file(const std::filesystem::path& path){
    std::vector<std::string> all_lines;
    std::ifstream FileStream{path};
    std::string current_line;
    while (std::getline(FileStream, current_line)) {
        all_lines.emplace_back(std::move(current_line));
    }
    return all_lines;
}
