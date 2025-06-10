if [ $1 = "p" ]
then
    python3 main.py
else
    g++ -std=c++14 main.cpp
    ./a.out
    rm a.out
fi
