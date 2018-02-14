/*
** Florian BACHO, 2018
** Quadripod
** File description:
** Main
*/

#include <iostream>
#include <string>
#include "PhysicalQuadripod.hpp"

using namespace Quadripod;

int main()
{
	try {
		PhysicalQuadripod quad("test");
	} catch (std::exception &e) {
		std::cout << std::string(e.what()) << std::endl;
		return (1);
	}
	return (0);
}
