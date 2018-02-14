/*
** EPITECH PROJECT, 2018
** Quadripod
** File description:
** Neuron class declaration
*/

#pragma once

#include <vector>

namespace Quadripod {
	class Neuron {
	public:
		Neuron(uint32_t nbEntry, bool isOut); //Initialize randomly
		void activate(const std::vector<Neuron> &prevLayer);
		void setActivation(float value);
		float getActivation() const;
		void calculateGradient(); // For output neurons
		void calculateGradient(std::vector

	private:
		std::vector<float> _weights;
		bool _isOut;
		float _activation;
		float _gradient;
	};
}
