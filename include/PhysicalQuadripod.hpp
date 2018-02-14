/*
** Florian BACHO, 2018
** Quadripod
** File description:
** Physical Quadripod class declaration
*/

#pragma once

#include "AQuadripod.hpp"

namespace Quadripod {
	class PhysicalQuadripod final : public AQuadripod {
	public:
		PhysicalQuadripod(const std::string &memoryFilename,
				  const std::string &annFilename);

	protected:
		uint8_t getPosition(uint8_t idx) override;
		void setPosition(uint8_t idx, uint8_t position) override;
	};
}
