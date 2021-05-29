
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
	class BMS_Data_generator * sender_obj = new class BMS_Data_generator;
	for(int count =0;count<100;count++)
	{
		sender_obj->pushToConsole(sender_obj->Output_JSON_Data());
		sleep(500);
	}
	return 0;
}
