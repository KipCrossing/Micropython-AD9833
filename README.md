# Micropython-AD9833
This script is written in python 3.x for interfacing the AD9833 with microcontrollers with micropython (specifically the PyBoard) over SPI.

## Usage

Import
```
from AD9833 import AD9833
from pyb import Pin
from pyb import SPI
```
Choose SS pin
```
ss = Pin('X5', Pin.OUT_PP)
```

Choose SPI
```
spi = SPI(1, SPI.MASTER, baudrate=9600, polarity=1, phase=0,firstbit=SPI.MSB)
```

Takes 2 arguments: sbi and ss
```
wave = AD9833(sbi,ss)
```

Set the frequency
```
wave.set_freq(14500)
```
Set the wave type:
0 for sin
1 for square
2 for triangle
```
wave.set_type(2)
```

Finally, send command to the AD9833
```
wave.send()
```

You can also get some useful information
```
print(wave.shape_type)
print(wave.freq)
```

![Alt text](/LoPy-connections.gif?raw=true "Optional Title")
