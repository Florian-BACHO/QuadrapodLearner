/*
** EPITECH PROJECT, 2018
** Quadripod
** File description:
** Abstract Quadripod Class definition
*/

#include <iostream>
#include <exception>
#include "AQuadripod.hpp"

using namespace Quadripod;

static const std::array<uint, 3> layersDescriptor = {AQuadripod::nbMotor,
						     24,
						     1};

AQuadripod::AQuadripod(const std::string &filename)
{
	try {
		loadQValuesFromFile(filename);
	} catch (std::ios_base::failure &e) {
		std::cout << "No trained QValue file. Creating one." <<
			std::endl;
	}
}

void AQuadripod::loadQValuesFromFile(const std::string &filename)
{
	std::ifstream file(filename);
	uint64_t nbQValues;
	std::string tmp;

	if (!file.is_open())
		throw std::ios_base::failure("Cannot open file");
	file >> nbQValues;
	std::cout << "QValue file found." << std::endl <<
		"Number of learned QValues: " << nbQValues << std::endl <<
		"Loading QValues..." << std::endl;
	for (auto i = 0u; i < nbQValues; i++)
		loadQValue(file);
	file.close();
}

void AQuadripod::loadQValue(std::ifstream &file)
{
	std::vector<uint8_t> state;
	uint8_t idx;
        uint8_t tmp;
	float ftmp;
	QPair stateAction;

	file >> idx;
	for (auto i = 0u; i < AQuadripod::nbMotor; i++) {
		file >> tmp;
		state.push_back(tmp);
	}
	file >> tmp;
	stateAction = std::make_pair(state, static_cast<Action>(tmp));
	file >> ftmp;
	_learnedQValues[idx][stateAction] = ftmp;
	std::cout << "Learned QValues loaded." << std::endl;
	annLearnQValues();
}

std::vector<QReinforcement> AQuadripod::makeTry()
{
	return (std::vector<QReinforcement>());
}

void AQuadripod::learn()
{

}

void AQuadripod::createAnn()
{
}

void AQuadripod::annLearnQValues()
{
	createAnn();
}
