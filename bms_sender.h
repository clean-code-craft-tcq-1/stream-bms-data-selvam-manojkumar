#pragma once

#include<string.h>

//Temperature

#define MIN_TEMP    0.0
#define MAX_TEMP    100.0

//SOC
#define MIN_SOC     0.0
#define MAX_SOC     100.0

typedef struct{
	float temperature;
	float SOC;
}BMS_DATA;


class BMS_Data_generator
{

public:
	float Generate_temperature();
	float Generate_SOC();
	int randomGenerator(int min_value, int max_value);
	std::stringstream Output_JSON_Data();
	void pushToConsole(std::stringstream outputData);// print on console
	BMS_DATA pushToTest(std::stringstream TestData);
};


