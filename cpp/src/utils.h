#pragma once
#include <vector>
#include <string>
#include <filesystem>

class Utilities {
   public:
      static std::vector<std::string> read_all_lines_in_file(const std::filesystem::path& Path);
};

