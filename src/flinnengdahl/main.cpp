#include <iostream>
#include "fe.h"

int main(void)
{
	FlinnEngdahl fe;
	fe.read("../numbered-names-intl.txt");
	for (int ilat = -100; ilat <= 100; ilat++) {
		for (int ilon = -1000; ilon <= 1000; ilon++) {
			int n = fe.number(ilat+0.5, ilon+0.5);
			std::cout << n << " " << fe.name(n) << std::endl;
		}
	}

	fe.setCategory("de");
	std::cout << fe.name(127) << std::endl;
	std::cout << fe.name(50, 10) << std::endl;
	fe.setCategory("xy");
}
