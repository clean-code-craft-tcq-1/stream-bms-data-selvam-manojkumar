// bms_sender.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include <stdlib.h>
#include <sstream>
#include <windows.h>
#include "bms_sender.h"

int main()
{
		class BMS_Data_generator * obj = new class BMS_Data_generator;
		BMS_DATA testData;
		testData = obj->pushToTest(obj->Output_JSON_Data());
	while (1)
	{
		obj->pushToConsole(obj->Output_JSON_Data());
		Sleep(500);
	}
	return 0;
}