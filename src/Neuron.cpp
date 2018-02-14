/*
** EPITECH PROJECT, 2018
** Quadripod
** File description:
** Neuron class definition
*/

#include <cstdlib>
#include <ctime>
#include <math>
#include "Neuron.hpp"

using namespace Quadripod;

Neuron::Neuron(uint32_t nbEntry)
{
	std::srand(std::time(nullptr));

	for (auto i = 0u; i < nbEntry + 1; i++)
		_weights.push_back((static_cast<float>(std::rand()) / RAND_MAX)
				   - 0.5f);
}

void Neuron::activate(const std::vector<Neuron> &prevLayer)
{
	float in = 0.0f;

	for (auto i = 0u; i < prevLayer.size(); i++)
		in += _weights[i] * prevLayer[i].getActivation();
	_activation = _isOut ? in : 1.0f / (1.0f + exp(-in))
}

void Neurone::setActivation(float value)
{
	_activation = value;
}

float Neuron::getActivation() const
{
	return (_activation);
}
