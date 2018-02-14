/*
** Florian BACHO, 2018
** Quadripod
** File description:
** An Interface for the quadripod that the AI will control
*/

#pragma once

#include <cstdint>

namespace Quadripod {

	// Possible action for each motor
	enum Action {
		UP = 0,
		DOWN,
		NONE
	};

	using QPair = std::pair<std::vector<uint8_t>, Action>; // Pair state / action
	using QReinforcement = std::pair<QPair, float>; // Reinforcement earned during a try

	class IQuadripod {
	public:
		virtual void learn() = 0;
		virtual std::vector<QReinforcement> makeTry() = 0;

	protected:
		virtual uint8_t getPosition(uint8_t idx) = 0; // 0 <= idx <= nb_motor
		virtual void setPosition(uint8_t idx, uint8_t position) = 0;
	};
}
