
/* ***********************************************************************************************************
* File Name   :	sender_app.cpp
* Author      : Manoj Kumar Selvam
* Description : sender_app.cpp is implementation of main.
* Functions   :
* *********************************************************************************************************** */

#include<iostream>
#include <stdlib.h>
#include <sstream>
#include <unistd.h>
#include "bms_sender.h"

int main()
{
	class BMS_Data_generator * obj = new class BMS_Data_generator;
	while (1)
	{
		obj->pushToConsole(obj->Output_JSON_Data());
		Sleep(500);
	}
	return 0;
}
