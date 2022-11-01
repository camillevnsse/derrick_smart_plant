// library imports (for the DHT11 sensor and the LCD display) 
#include "DHT.h"
#include "LiquidCrystal_I2C.h"
#include "Wire.h"

// components setup
DHT dht(2, DHT11);
LiquidCrystal_I2C LCD(0x27,16,2);

// sensor setup
void setup() {
	LCD.init();
   	LCD.backlight();
	dht.begin() ;
	// Serial.begin(9600) ; // exchange rate of data : 9600 bits/s 
}

void loop() {
	// read data from the DHT11
	float h = dht.readHumidity() ;
	float t = dht.readTemperature() ;
	
	// humidity display
	LCD.setCursor(0,0); // top-left
	LCD.print("Humidity: ");
	LCD.print(h);
	
	// temperature display
	LCD.setCursor(0,1); // bottom-left
	LCD.print("Temperature: ");
	LCD.print(t);
	
	// refresh
	delay(1000);
	LCD.clear();

	// Serial.print("Humidity :") ;
	// Serial.printIn(h) ;
	// Serial.print("Temperature :") ;
	// Serial.printIn(t) ;
}
