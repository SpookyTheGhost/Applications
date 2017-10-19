// findIndexRange
// calculatevalue


#include "stdafx.h"
#include <thread>       
#include <chrono> 
#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <string>
#include <windows.h>
#include <cmath>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

double getVoltage() {
	double voltage;
	cin >> voltage;
	return voltage;
}

double lookupTable(double voltage) {
	map <double, double> lookup;
	lookup.insert({ 0, -40 });
	lookup.insert({ 0.3, 30 });
	lookup.insert({ 0.6, 60 });
	lookup.insert({ 1, 100 });

	if (lookup.count(voltage) > 0) {
		return lookup.at(voltage);
	}
	else {
		return -1; // out of range
	}
}

string lowercase(string s) {
	string output;
	transform(s.begin(), s.end(), output.begin(), ::tolower);
	return output;
}

bool compare(string a, string b) {
	return !(b.compare(a));
}

void activateAC() {}
void killAC() {}
void activateHeater() {}
void killHeater() {}
void activateHumidifier() {}
void killHumidifier() {}
void activateDehumidifier() {}
void killDehumidifier() {}

void temperatureAdjust(double currentTemperature, double requestedTemperature, string season, string status) {
	const long deviation = 2;

	if (currentTemperature == requestedTemperature || (abs(requestedTemperature - currentTemperature) < deviation)) return;

	string lower = lowercase(status);

	if (compare(season, "summer") && compare(status, "off") && (currentTemperature - requestedTemperature) < deviation) {
		return;  // do nothing, upper bound not reached
	}

	else if (compare(season, "summer") && compare(status, "off") && (requestedTemperature - currentTemperature) > deviation) {
		activateAC();
	}

	else if (compare(season, "summer") && compare(status, "off") && (currentTemperature - requestedTemperature) > deviation) {
		
	}

	else if (compare(season, "summer") && compare(status, "on") && (requestedTemperature - currentTemperature) < deviation) {
		return; // do nothing, lower bound not reached
	}
	else if (compare(season, "summer") && compare(status, "on") && (requestedTemperature - currentTemperature) > deviation) {
		killAC();
	}

	else if (compare(season, "winter") && compare(status, "off") && (currentTemperature - requestedTemperature) < deviation) {
		return;  // do nothing, upper bound not reached
	}

	else if (compare(season, "winter") && compare(status, "off") && (requestedTemperature - currentTemperature) > deviation) {
		activateAC();
	}

	else if (compare(season, "winter") && compare(status, "on") && (requestedTemperature - currentTemperature) < deviation) {
		return; // do nothing, lower bound not reached
	}
	else if (compare(season, "winter") && compare(status, "on") && (requestedTemperature - currentTemperature) > deviation) {
		killHeater();
	}
}

void humidityAdjust(double currentHumidity, double requestedHumidity, string season, string status) {
	const long deviation = 2;

	if (currentHumidity == requestedHumidity || (abs(requestedHumidity - currentHumidity) < deviation)) return;

	string lower = lowercase(status);

	if (compare(season, "summer") && compare(status, "off") && (currentHumidity - requestedHumidity) < deviation) {
		return;  // do nothing, upper bound not reached
	}

	else if (compare(season, "summer") && compare(status, "off") && (requestedHumidity - currentHumidity) > deviation) {
		activateHeater();
	}

	else if (compare(season, "summer") && compare(status, "on") && (requestedHumidity - currentHumidity) < deviation) {
		return; // do nothing, lower bound not reached
	}
	else if (compare(season, "summer") && compare(status, "on") && (requestedHumidity - currentHumidity) > deviation) {
		killAC();
	}

	else if (compare(season, "winter") && compare(status, "off") && (currentHumidity - requestedHumidity) < deviation) {
		return;  // do nothing, upper bound not reached
	}

	else if (compare(season, "winter") && compare(status, "off") && (requestedHumidity - currentHumidity) > deviation) {
		activateAC();
	}

	else if (compare(season, "winter") && compare(status, "on") && (requestedHumidity - currentHumidity) < deviation) {
		return; // do nothing, lower bound not reached
	}
	else if (compare(season, "winter") && compare(status, "on") && (requestedHumidity - currentHumidity) > deviation) {
		killHeater();
	}
}

int main(){
	double d = lookupTable(0.5);
	cout << d << endl;
	
/*
double requestedTemperature;
cin >> requestedTemperature;
double requestedHumidity;
cin >> requestedHumidity;
string season;
cin >> season;
string HCstatus;
string Hstatus;
cin >> HCstatus;
cin >> Hstatus;

int count = 0;
for (int i = 0;; i++) {
double currentVoltage = getVoltage();
double value = lookupTable(currentVoltage);
temperatureAdjust(value, requestedTemperature, season, HCstatus);
if (count = 5) {
count = 0;
humidityAdjust(value, requestedHumidity, season, Hstatus);
}
count++;
}
*/
	Sleep(500);
	return 0;
}
