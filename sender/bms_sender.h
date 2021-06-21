/* ***********************************************************************************************************
* File Name   :	bms_sender.h
* Author      : Manoj Kumar Selvam
* Description : bms_sender.h is implementation of BMS_Data_generator.
* Functions   :
* *********************************************************************************************************** */
#pragma once

#include<string.h>

//Temperature

#define MIN_TEMP    0.0
#define MAX_TEMP    100.0

//SOC
#define MIN_SOC     0.0
#define MAX_SOC     100.0

#define TEMP_JSON_INDEX 1
#define SOC_JSON_INDEX 3

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
};


class BMS_generator_tester : public BMS_Data_generator
{
public:
	BMS_DATA pushToTest(std::stringstream TestData);
	bool Validate_Range(float current_value, int min_value, int max_value);
};
