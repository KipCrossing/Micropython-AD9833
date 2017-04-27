'''
Written by Kipling Crossing
This sample code was written in python 3 for micropython
for interfacing between the Pyboard (or other) and the 
AD9833 over SPI. 

This code was inspired by Arduion code by sinneb
www.sinneb.net/?p=562

The connections between the AD9833 and PyBoard are:

VCC -> Vin (any)
DGND -> GND (any)
SDATA -> MOSI (X8)
SCLK -> SCK (X6)
FSYNC -> ss (X5)
MCLK -> Timer (X4)
AGND -> GND (any)


'''

from pyb import Pin
from pyb import SPI
from pyb import ADC
import time
from pyb import Timer



# Define frequency in Hz
Freq =10000  

# Clock Frequency
ClockFreq = 25000000

# Note: some AD9833 PCBs do not include a MCLK pin and therefore you should check its clock rate - mine is 25 MHz

p = Pin('X4') # X4 has TIM9, CH2
tim = Timer(9, freq=ClockFreq)
ch = tim.channel(2, Timer.PWM, pin=p)
ch.pulse_width_percent(50)

# Calculate frequency word to send
word = hex(round((Freq*2**28)/ClockFreq))

# Split frequency word onto its seperate bytes
MSB = (int(word) & 0xFFFC000)>>14
LSB = int(word) & 0x3FFF


# Set control bits DB15 = 0 and DB14 = 1; for frequency register 0
MSB |= 0x4000
LSB |= 0x4000

# Allocate X5 as ss for FSYNC
p_out = Pin('X5', Pin.OUT_PP)

# Initiate SPI bus
spi = SPI(1, SPI.MASTER, baudrate=9600, polarity=1, phase=0,firstbit=SPI.MSB)

#function for splitting hex into high and low bits
def bytes(integer):
    return divmod(integer, 0x100)

# This is the function that sends the data
def Send(data):
    high, low = bytes(data)
    p_out.low()

    spi.send(high)
    spi.send(low)

    p_out.high()


Send(0x2100)

#Set the frequency
Send(LSB)    #lower 14 bits
Send(MSB)    #Upper 14 bits

#phase
#Send(0&0xC000)    # Place holder for now - does nothing. 
#shape
Send(0x2000)    # square: 0x2020, sin: 0x2000, triangle: 0x2002


'''
adc = ADC(Pin('X19'))
while True:
    print(adc.read())     # read value, 0-4095

'''
# For observing the wave using pin X19 ADC
adc = pyb.ADC(pyb.Pin.board.X19)    # create an ADC on pin X19
buf = bytearray(1000)                # create a buffer of 1000 bytes
adc.read_timed(buf, 1000000)             # read analog values into buf at 1000000Hz

for val in buf:                     # loop over all values
    print(val)                      # print the value out



