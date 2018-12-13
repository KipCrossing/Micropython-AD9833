from ad9833 import AD9833

# DUMMY classes for testing without board

class SBI(object):
    def __init__(self):
        pass
    def send(self,data):
        print(data)

class Pin(object):
    def __init__(self):
        pass
    def low(self):
        print("                0")
    def high(self):
        print("                1")


# Code

SBI1 = SBI()
PIN3 = Pin()

wave = AD9833(SBI1,PIN3)

wave.set_freq(14500)
wave.set_type(2)
wave.send()
print(wave.shape_type)
