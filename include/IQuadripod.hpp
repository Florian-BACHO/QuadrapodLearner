/*
** Florian BACHO, 2018
** Quadripod
** File description:
** An Interface for the quadripod that the AI will control
*/

#pragma once

#include <cstdint>

namespace Quadripod {

	struct ExperienceMemory;

	// Possible action for each motor
	enum Action {
		UP = 0,
		DOWN,
		NONE
	};

	class IQuadripod {
	public:
		virtual void learn() = 0;
		virtual std::vector<ExperienceMemory> makeTry() = 0;

	protected:
		virtual uint8_t getPosition(uint8_t idx) = 0; // 0 <= idx <= nb_motor
		virtual void setPosition(uint8_t idx, uint8_t position) = 0;
	};
}
