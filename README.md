# Arduino-realtime-temperature-datalogger-with-python

Arduino Uno temperature datalogger with LCD display and set temperature LED indicator and live graphical output using Arduino and python.

The standard pyfirmata file that translates the python code to the Arduino needs modifying in order to utilise the liquid crystal display.

Instructions:

Upload the pyfirmataLCD.ino file to the Arduino using the arduino IDE

Connect the Arduino as follows:

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

Connect the Arduino to a laptop via USB and use the Python temperature_live_datalogger.py code to run. Ensure you enter the desired path within the code to save the data

See the video for operation 
