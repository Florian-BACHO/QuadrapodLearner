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
						     AQuadripod::nbAction *
						     AQuadripod::nbMotor};

AQuadripod::AQuadripod(const std::string &filename)
	: _memoryFilename(filename)
{
	try {
		loadMemoryFromFile(filename);
	} catch (std::ios_base::failure &e) {
		std::cout << "No Memory file. Creating one." <<
			std::endl;
	}
}

AQuadripod::~AQuadripod()
{
	saveMemoryToFile(_memoryFilename);
}

void AQuadripod::loadMemoryFromFile(const std::string &filename)
{
	std::ifstream file(filename);
	uint64_t memorySize;
	std::string tmp;

	if (!file.is_open())
		throw std::ios_base::failure("Cannot open memory file");
	file >> memorySize;
	std::cout << "Memory file found." << std::endl <<
		"Memory size: " << memorySize << std::endl <<
		"Loading Memory..." << std::endl;
	for (auto i = 0u; i < memorySize; i++)
		loadMemory(file);
	file.close();
}

void AQuadripod::loadMemory(std::ifstream &file)
{
	ExperienceMemory mem;
	uint8_t utmp;

	for (auto i = 0u; i < AQuadripod::nbMotor; i++) {
		file >> utmp;
		mem.state.push_back(utmp);
	}
	for (auto i = 0u; i < AQuadripod::nbMotor; i++) {
		file >> utmp;
		mem.actions.push_back(static_cast<Action>(utmp));
	}
	for (auto i = 0u; i < AQuadripod::nbMotor; i++) {
		file >> utmp;
		mem.reachedState.push_back(utmp);
	}
	file >> mem.reinforcement;
	_memory.push_back(mem);
}

void AQuadripod::saveMemory(std::ofstream &file,
			    const ExperienceMemory &toSave) const
{
	for (auto i : toSave.state)
		file << i << " ";
	file << std::endl;
	for (auto i : toSave.actions)
		file << static_cast<uint8_t>(i) << " ";
	file << std::endl;
	for (auto i : toSave.reachedState)
		file << i << " ";
	file << std::endl;
	file << toSave.reinforcement;
}

void AQuadripod::saveMemoryToFile(const std::string &filename) const
{
	std::ofstream file(filename, std::ios::trunc);

	if (!file.is_open())
		throw std::ios_base::failure("Cannot open memory file");
	file << _memory.size() << std::endl;
	std::cout << "Memory file created and cleared." << std::endl <<
		"Saving " << _memory.size() << " memory..." << std::endl;
	for (const auto &it : _memory)
		saveMemory(file, it);
	file.close();
}

std::vector<ExperienceMemory> AQuadripod::makeTry()
{
	return (std::vector<ExperienceMemory>());
}

void AQuadripod::learn()
{

}

void AQuadripod::createAnn()
{

}
