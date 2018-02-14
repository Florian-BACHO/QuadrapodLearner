/*
** Florian BACHO, 2018
** Quadripod
** File description:
** An Abstract class that inherit from the Quadripod Interface
*/

#pragma once

#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <fann.h>
#include <fann_cpp.h>
#include "IQuadripod.hpp"
#include "ExperienceMemory.hpp"

namespace Quadripod {

	// Description of a motor, his id and limits of positions
        struct motorDescriptor {
		int id;
		float minLimit;
		float maxLimit;
	};

	class AQuadripod : public IQuadripod {
	public:
		AQuadripod(const std::string &memoryFilename,
			   const std::string &annFilename);
		~AQuadripod();
		void learn() override;
		std::vector<ExperienceMemory> makeTry() override; // Execute a try of nbActionPerTry actions
		static const uint8_t nbMotor = 12;
		static const uint8_t positionPerMotor = 5;
		static const uint32_t nbActionPerTry = 10;
		static const uint8_t nbAction = 3;

	protected:
		virtual uint8_t getPosition(uint8_t idx) = 0; // 0 <= idx <= nbMotor
		virtual void setPosition(uint8_t idx, uint8_t position) = 0;

	private:
		void loadMemoryFromFile(const std::string &filename);
		void loadMemory(std::ifstream &file);
		void saveMemoryToFile(const std::string &filename) const;
		void saveMemory(std::ofstream &file,
				const ExperienceMemory &toSave) const;
		void loadAnnFromFile(const std::string &filename);
		void saveAnnToFile(const std::string &filename);
		void createAnn(void);

		std::string _memoryFilename;
		std::string _annFilename;
		std::vector<ExperienceMemory> _memory;
		FANN::neural_net _ann;
	};
}
