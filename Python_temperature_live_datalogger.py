"""
Created on Fri Oct 15 18:18:51 2021

@author: Steven Daniels
"""
from pyfirmata import Arduino, util, STRING_DATA
import pyfirmata
import time
import csv
import matplotlib.pyplot as plt
from drawnow import drawnow


#class to calculate elapsed time
class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start the timer"""
        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, return time passed"""
        elapsed_time = time.perf_counter() - self._start_time       
        return elapsed_time


#send the datapoint to the LCS
def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )
        
#save the data to a file        
def file():
    row = [xs,ys]
    with open('C:/add_your_filepath_here.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)


#plotting the graph
def make_fig():
    plt.ylabel("Temperature (C)")
    plt.xlabel("Time (Seconds)")
    plt.plot(xs,ys)
    plt.show()


#initialise the graph 
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#initilise the arduino board
board = Arduino('COM3')
board.send_sysex( STRING_DATA, util.str_to_two_byte_iter('Hello!') )    

#begon arduino iterator
it = pyfirmata.util.Iterator(board)
it.start()

#assign arduino pins
analog_input = board.get_pin('a:0:i')
LED4 = board.get_pin('d:10:o')
LED3 = board.get_pin('d:9:o')
LED2 = board.get_pin('d:8:o')

#set all LEDs to begin in the off position 
LEDs=[LED4,LED3,LED2]
for LED in LEDs:
        LED.write(0)
      

#temperature to decide when to turn on LED indicators
baseline_temp=20    
#call timer class
t = Timer()
#start timer class
t.start()
xs = []
ys = []
for i in range(200):
#read the voltage and conver to temperature using manufacturers values
    analog_value = analog_input.read()
    
    if analog_value == None:
       pass
    else:
       voltage=(analog_value*5)
       temp=(voltage-0.50)*100
       temp=round(temp,2)
       
#send temperature datapoint to the LCD
       msg("Temp= "+ str(temp) + " C")
       
#add datapoint to the lists
       xs.append(round(t.stop()))
       ys.append(float(temp))
       
#update graph
       drawnow(make_fig)
       
#turn on LED temperature indicators at set points       
#temperature 20C or less
       if temp < baseline_temp:
           LED4.write(0)
           LED4.write(0)
           LED4.write(0)
#temperature between 23-25C
       elif temp >= baseline_temp + 3 and temp < baseline_temp +5:   
           LED4.write(1)
           LED3.write(0)
           LED2.write(0)
#temperature between 25-27
       elif temp >= baseline_temp + 5 and temp < baseline_temp +7: 
           LED4.write(1)
           LED3.write(1)
           LED2.write(0)
#temperature >27
       elif temp >= baseline_temp +7: 
           LED4.write(1)
           LED3.write(1)
           LED2.write(1)   
    time.sleep(1)
#after collection, turn off all LEDs and blank the LCD, exit the 
#serial connection and save the data to a file
for LED in LEDs:
        LED.write(0)   
board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( " " ) )
board.exit()  
file()