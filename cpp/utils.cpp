#include "utils.h"
#include <fstream>
#include <string>

std::vector<std::string> Utilities::ReadAllLinesInFile(const std::filesystem::path& Path){
    std::vector<std::string> AllLines;
    std::ifstream FileStream{Path};
    std::string CurrentLine;
    while (std::getline(FileStream, CurrentLine)) {
        AllLines.push_back(CurrentLine);
    }
    return AllLines;
}
