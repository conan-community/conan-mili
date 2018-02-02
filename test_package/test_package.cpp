#include <iostream>
#include "mili/mili.h"

using namespace mili;

int main()
{
    Select<true, int, float>::result n = 1;
    std::cout << n << std::endl;
    return 0;
}