/*
** EPITECH PROJECT, 2018
** Quadripod
** File description:
** ExperienceMemory Structure declaration
*/

#pragma once

#include <cstdint>
#include <vector>

namespace Quadripod {
	struct ExperienceMemory {
		std::vector<uint8_t> state;
		std::vector<uint8_t> reachedState;
		std::vector<Action> actions;
		float reinforcement;
	};
}
