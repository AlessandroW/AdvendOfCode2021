#include <vector>
#include <iostream>
#include <fstream>

int main(int argc, char **argv){
std::ifstream infile("day1.txt");

int result = 0;
int prevNumber = -1;
int currentNumber;

while (infile >> currentNumber)
{
    if (prevNumber != -1 && currentNumber > prevNumber){
       ++result;
    }
    prevNumber = currentNumber;
}
  std::cout << result << '\n';
}
