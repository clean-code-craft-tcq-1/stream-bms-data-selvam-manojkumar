#include<iostream>
#include <stdlib.h>
#include <sstream>
#include "../sender/bms_sender.h"
#include "catch.hpp"


TEST_CASE("validate input data") {
	class BMS_generator_tester * tester_obj = new class BMS_generator_tester;
	BMS_DATA testData;
	testData = tester_obj->pushToTest(obj->Output_JSON_Data());
	REQUIRE(tester_obj->Validate_Range(testData.SOC, MIN_SOC, MAX_SOC));
	REQUIRE(tester_obj->Validate_Range(testData.temperature, MIN_TEMP, MAX_TEMP));
}

TEST_CASE("data generation test") {

	class BMS_generator_tester * tester_obj = new class BMS_generator_tester;
	BMS_DATA testData;
	for (int noOfIter = 0; noOfIter < 50; noOfIter++) 
	{
		testData = tester_obj->pushToTest(obj->Output_JSON_Data());
		REQUIRE(tester_obj->Validate_Range(testData.SOC, MIN_SOC, MAX_SOC));
		REQUIRE(tester_obj->Validate_Range(testData.temperature, MIN_TEMP, MAX_TEMP));
	}
}
