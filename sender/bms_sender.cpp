/* ***********************************************************************************************************
* File Name   :	bms_sender.cpp
* Author      : Manoj Kumar Selvam
* Description : BMS_sender.cpp is implements intefaces to send the BMS datas like temperature and State of Charge
* Functions	  :
* *********************************************************************************************************** */
#include<iostream>
#include <stdlib.h>
#include <sstream>
#include "bms_sender.h"


bool BMS_generator_tester::Validate_Range(float current_value, int min_value, int max_value)
{
	return((current_value >= min_value) && (current_value <= max_value));
}

int BMS_Data_generator::randomGenerator(int min_value, int max_value)
{
	return (rand() % (min_value - max_value + 1)) + min_value;
}

float BMS_Data_generator::Generate_temperature()
{

	return randomGenerator(MIN_TEMP, MAX_TEMP);;
}

float BMS_Data_generator::Generate_SOC()
{
	return randomGenerator(MIN_SOC, MAX_SOC);
}

std::stringstream BMS_Data_generator::Output_JSON_Data()
{
	BMS_DATA bms_params;
	bms_params.temperature = Generate_temperature();
	bms_params.SOC = Generate_SOC();
	std::stringstream outputData;
	outputData << "{\"Temperature\": "<< bms_params.temperature << " ,\"SOC\": " << bms_params.SOC <<" }";
	return outputData;
}

void BMS_Data_generator::pushToConsole(std::stringstream outputData)
{
	std::cout << outputData.str() << std::endl;
}

BMS_DATA BMS_generator_tester::pushToTest(std::stringstream testData)
{
	BMS_DATA bms_params;
	std::string subString[5];
	for(int iter=0; iter < 5; iter++)
	{
		testData >> subString[iter];
	}
	bms_params.temperature = std::stof(subString[TEMP_JSON_INDEX]);
	bms_params.SOC = std::stof(subString[SOC_JSON_INDEX]);
	return bms_params;
}

