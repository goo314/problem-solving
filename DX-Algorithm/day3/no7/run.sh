g++ -std=c++14 -c main.cpp
g++ -std=c++14 -c solution.cpp
g++ -std=c++14 -o a.out main.o solution.o

./a.out
rm a.out *.o
