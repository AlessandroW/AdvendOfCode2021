cmake_minimum_required(VERSION 3.14)
project(aoc2021)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(EXECUTABLE_NAME aoc)
add_executable(${EXECUTABLE_NAME}
  src/utils.h src/utils.cpp
  src/day1.h src/day1.cpp
  src/day2.h src/day2.cpp
  src/main.cpp)
target_compile_features(${EXECUTABLE_NAME} PRIVATE cxx_std_20)
target_compile_options(${EXECUTABLE_NAME} PRIVATE -Wall -Wextra -Wconversion -pedantic -Wfatal-errors)
