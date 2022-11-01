// DHT library import 
#include "DHT.h"

// define on which pin the information given by the dht sensor will be read
DHT dht(2, DHT11);

// sensor setup
void setup() {
	dht.begin();
  Serial.begin(9600) // exchange rate of data : 9600 bits/s 
}

// read and display info given by dht
void loop() {
	 float h = dht.readHumidity() ;
	float t = dht.readTemperature() ;

	Serial.print("Humidity :") ;
	Serial.printIn(h) ;
	Serial.print("Temperature :") ;
	Serial.printIn(t) ;
}
