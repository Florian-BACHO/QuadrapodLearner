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

static const uint32_t layersDescriptor[] = {AQuadripod::nbMotor,
					    24,
					    AQuadripod::nbAction *
					    AQuadripod::nbMotor};
static const uint32_t nbLayer = 3;

AQuadripod::AQuadripod(const std::string &memoryFilename,
		       const std::string &annFilename)
	: _memoryFilename(memoryFilename), _annFilename(annFilename)
{
	try {
		loadMemoryFromFile(memoryFilename);
	} catch (std::ios_base::failure &e) {
		std::cout << "No Memory file. " <<
			"It will be created at memory save." << std::endl;
	}
	try {
		loadAnnFromFile(annFilename);
	} catch (std::ios_base::failure &e) {
		std::cout << "No Artificial Neural Network file." << std::endl;
		createAnn();
	}
}

AQuadripod::~AQuadripod()
{
	saveMemoryToFile(_memoryFilename);
	saveAnnToFile(_annFilename);
}

void AQuadripod::loadMemoryFromFile(const std::string &filename)
{
	std::ifstream file(filename);
	uint64_t memorySize;
	std::string tmp;

	std::cout  << "Loading Memory..." << std::endl;
	if (!file.is_open())
		throw std::ios_base::failure("Cannot open memory file");
	file >> memorySize;
	for (auto i = 0u; i < memorySize; i++)
		loadMemory(file);
	file.close();
	std::cout << "Done." << std::endl;
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
	std::cout << "Done." << std::endl;
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
	std::cout << "Creating Artificial Neural Network..." << std::endl;
	if (!_ann.create_standard_array(nbLayer, layersDescriptor))
		throw std::ios_base::failure("Cannot create ANN");
	_ann.randomize_weights(-1.0f, 1.0f);
	_ann.set_activation_function_hidden(FANN::SIGMOID);
	_ann.set_activation_function_output(FANN::LINEAR);
}

void AQuadripod::loadAnnFromFile(const std::string &filename)
{
	std::cout << "Loading Artificial Neural Network..." << std::endl;
	if (!_ann.create_from_file(filename))
		throw std::ios_base::failure("Cannot open ANN file");
	std::cout << "Done." << std::endl;
}

void AQuadripod::saveAnnToFile(const std::string &filename)
{
	std::cout << "Saving Artificial Neural Network..." << std::endl;
	if (!_ann.save(filename))
		throw std::ios_base::failure("Cannot save ANN file");
	std::cout << "Done." << std::endl;
}
