#ifndef UTILS_H_
#define UTILS_H_

#include <vector>
#include <string>
#include <filesystem>

class Utilities {
   public:
      static std::vector<std::string> ReadAllLinesInFile(const std::filesystem::path& Path);
};

#endif // UTILS_H_
