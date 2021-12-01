#include <iostream>
#include <fstream>
#include <queue>

int main(int argc, char **argv){
std::ifstream infile("day1.txt");

int result = 0;
int i = 0;
int currentNumber;
std::queue<int> prevNumbers {};


while (infile >> currentNumber)
{
    prevNumbers.push(currentNumber);
    ++i;
    if (i >= 4){
        if(currentNumber > prevNumbers.front()) ++result;
        prevNumbers.pop();
    }
}

  std::cout << result << '\n';
}
