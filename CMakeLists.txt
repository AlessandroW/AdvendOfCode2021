# From https://github.com/onqtam/doctest/blob/master/examples/installed_doctest_cmake/executable/CMakeLists.txt
cmake_minimum_required(VERSION 3.0)

project(main VERSION 0.0.1 LANGUAGES CXX)

# require C++17
set(CMAKE_CXX_STANDARD 17)

# Add dependencies using CPM.cmake
# https://github.com/cpm-cmake/CPM.cmake
# mkdir -p cmake
# wget -O cmake/CPM.cmake https://github.com/cpm-cmake/CPM.cmake/releases/latest/download/get_cpm.cmake
include(cmake/CPM.cmake)
cpmaddpackage("gh:onqtam/doctest#2.4.5")
cpmaddpackage("gh:fmtlib/fmt#8.0.1")

add_executable(${PROJECT_NAME} day3.cpp ParseHelper.h)
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)
target_link_libraries(${PROJECT_NAME} PRIVATE doctest::doctest)
target_link_libraries(${PROJECT_NAME} PRIVATE fmt::fmt)
