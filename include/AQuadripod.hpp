/*
** Florian BACHO, 2018
** Quadripod
** File description:
** An Abstract class that inherit from the Quadripod Interface
*/

#pragma once

#include <vector>
#include <utility>
#include <map>
#include <string>
#include <fstream>
#include <fann.h>
#include <fann_cpp.h>
#include "IQuadripod.hpp"

namespace Quadripod {

	// Description of a motor, his id and limits of positions
        struct motorDescriptor {
		int id;
		float minLimit;
		float maxLimit;
	};

	using QValue = std::map<QPair, float>;

	class AQuadripod : public IQuadripod {
	public:
		AQuadripod(const std::string &filename); // Filename is the file where all learned QValues will be saved
		void learn() override;
		std::vector<QReinforcement> makeTry() override; // Execute a try of nbActionPerTry actions
		static const uint8_t nbMotor = 12;
		static const uint8_t positionPerMotor = 5;
		static const uint32_t nbActionPerTry = 10;

	protected:
		virtual uint8_t getPosition(uint8_t idx) = 0; // 0 <= idx <= nbMotor
		virtual void setPosition(uint8_t idx, uint8_t position) = 0;

	private:
		void loadQValuesFromFile(const std::string &filename);
		void loadQValue(std::ifstream &file);
		void saveQValuesToFile(const std::string &filename) const;
		void createAnn();
		void annLearnQValues();

		std::map<uint8_t, QValue> _learnedQValues; // Each motor have a QValue map
		FANN::neural_net _ann;
	};
}
