#include <LiquidCrystal.h>

int moisture = 0;

LiquidCrystal lcd_1(7, 6, 5, 4, 3, 2);

void setup()
{
  pinMode(A0, OUTPUT);
  pinMode(A1, INPUT);
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  
  lcd_1.begin(16, 2); // Set up the number of columns and rows on the LCD.

  // Print a message to the LCD.
  lcd_1.print("DERRICK!");
}

void loop()
{
  digitalWrite(A0, HIGH);
  delay(10);
  moisture = analogRead(A1);
  // set the cursor to column 0, line 1
  // note: line 1 is the second row, since counting
  // begins with 0):
  lcd_1.setCursor(0, 1);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(A0, LOW);
  lcd_1.print(moisture);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  if (moisture < 200) {
    digitalWrite(12, HIGH);
  } else {
    if (moisture < 400) {
      digitalWrite(11, HIGH);
    } else {
      if (moisture < 600) {
        digitalWrite(10, HIGH);
      } else {
        if (moisture < 800) {
          digitalWrite(9, HIGH);
        } else {
          digitalWrite(8, HIGH);
        }
      }
    }
  }
  delay(100);
}
