# Micropython-AD9833

This script is written in python 3.x for interfacing the AD9833 with micropython microcontrollers over SPI.

## Usage

Import

```python
from ad9833 import AD9833
from pyb import Pin
from pyb import SPI
```

Choose SS pin

```python
ss = Pin('X5', Pin.OUT_PP)
```

Choose SPI

```python
spi = SPI(1, SPI.MASTER, baudrate=9600, polarity=1, phase=0,firstbit=SPI.MSB)
```

Takes 2 arguments: sbi and ss

```python
wave = AD9833(spi,ss)
```

Set the frequency

```python
wave.set_freq(14500)
```

Set the wave type: 0 for sin 1 for square 2 for triangle

```python
wave.set_type(2)
```

Finally, send command to the AD9833

```python
wave.send()
```

You can also get some useful information

```python
print(wave.shape_type)
print(wave.freq)
```
