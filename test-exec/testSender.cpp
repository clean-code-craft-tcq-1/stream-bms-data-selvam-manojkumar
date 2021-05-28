#include "stdafx.h"


#include<iostream>
#include <stdlib.h>
#include <sstream>
#include "../sender/bms_sender.h"
#include "catch.hpp"


TEST_CASE("validate input data") {
	class BMS_Data_generator * obj = new class BMS_Data_generator;
	BMS_DATA testData;
	testData = obj->pushToTest(obj->Output_JSON_Data());
	REQUIRE(BMS_Data_generator::Validate_Range(testData.SOC, MIN_SOC, MAX_SOC));
	REQUIRE(BMS_Data_generator::Validate_Range(testData.temperature, MIN_TEMP, MAX_TEMP));
}

TEST_CASE("data generation test") {

	class BMS_Data_generator * obj = new class BMS_Data_generator;
	BMS_DATA testData;
	for (int noOfIter = 0; noOfIter < 50; noOfIter++) 
	{
		testData = obj->pushToTest(obj->Output_JSON_Data());
		REQUIRE(BMS_Data_generator::Validate_Range(testData.SOC, MIN_SOC, MAX_SOC));
		REQUIRE(BMS_Data_generator::Validate_Range(testData.temperature, MIN_TEMP, MAX_TEMP));
	}
}
