/*
** Florian BACHO, 2018
** Quadripod
** File description:
** Physical Quadripod class definition
*/

#include "PhysicalQuadripod.hpp"

using namespace Quadripod;

PhysicalQuadripod::PhysicalQuadripod(const std::string &filename)
	: AQuadripod(filename)
{}

uint8_t PhysicalQuadripod::getPosition(uint8_t)
{
	return (0);
}

void PhysicalQuadripod::setPosition(uint8_t, uint8_t)
{

}
