/* ***********************************************************************************************************
* File Name   :	bms_sender.cpp
* Author      : Manoj Kumar Selvam
* Description : BMS_sender.cpp is implements intefaces to send the BMS datas like temperature and State of Charging
* Functions	  :
* *********************************************************************************************************** */
#include<iostream>
#include <stdlib.h>
#include <sstream>
#include "bms_sender.h"

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
	outputData << "{\"Temperature\": "<< bms_params.temperature << ", \"SOC\": " << bms_params.SOC <<"}";
	return outputData;
}

void BMS_Data_generator::pushToConsole(std::stringstream outputData)
{
	std::cout << outputData.str() << std::endl;
}

BMS_DATA BMS_Data_generator::pushToTest(std::stringstream TestData)
{
	BMS_DATA bms_params;
	return bms_params;
}

