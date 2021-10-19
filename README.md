# Arduino-realtime-temperature-datalogger
Arduino temperature datalogger with LCD display and set temperature LED indicator using pyfirmata

Pyfirmata file needs modifying by including the liquid crystal function below to operate the LCD:

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int lastLine = 1;

void stringDataCallback(char *stringData){
   if ( lastLine ) {
     lastLine = 0;
     lcd.clear();
   } else {
     lastLine = 1;
     lcd.setCursor(0,1);
   }
   lcd.print(stringData);
}

LCD pin assignment:
16(LED-) to -ve
15(LED+) via 220ohm resitor to +ve
14(DB7) to arduino digital pin 2
13(DB6) to arduino digital pin 3
12(DB5) to arduino digital pin 4
11(DB4) to arduino digital pin 5
10(DB3) no connection
9(DB2) no connection
8(DB1) no connection
7(DB0) no connection
6(E) to arduino digital pin 11
5(RW) to -ve
4(RS) to arduino digital pin 12
3(VO) to potentiometer center pin (left pin of potentiometer to +ve and right to -ve)
2(VDD) to +ve
1(VSS) to -ve

On the Arduino:
Analogue pin A0 to center pin of TMP36 temperature sensor (from flat side facing the left pin to +ve, right pin to -ve)
Digital pin 8, 9 and 10 each connect to the long side of an LED, then the cathode (short pin) of the LED connects via a 220ohm resistor to ground
