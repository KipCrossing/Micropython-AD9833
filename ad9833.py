# By Kipling Crossing
class AD9833(object):

    # Clock Frequency
    ClockFreq = 25000000
    freq = 10000
    shape_word =  0x2000

    def __init__(self,spi,ss):
        self.spi = spi
        self.ss = ss

    #function for splitting hex into high and low bits
    def _bytes(self,integer):
        return divmod(integer, 0x100)

    def _send(self, data):
        high, low = self._bytes(data)
        self.ss.low()

        self.spi.send(high)
        self.spi.send(low)

        self.ss.high()


    def set_freq(self,freq):
        self.freq = freq

    def set_type(self,inter):
        if inter == 1:
            self.shape_word = 0x2020
        elif inter == 2:
            self.shape_word = 0x2002
        else:
            self.shape_word = 0x2000

    @property
    def shape_type(self):
        if self.shape_word == 0x2020:
            return "Square"
        elif self.shape_word == 0x2002:
            return "Triangle"
        else:
            return "Sine"

    def send(self):
        # Calculate frequency word to send
        word = hex(int(round((self.freq*2**28)/self.ClockFreq)))

        # Split frequency word onto its seperate bytes
        MSB = (int(word,16) & 0xFFFC000) >> 14
        LSB = int(word,16) & 0x3FFF

        # Set control bits DB15 = 0 and DB14 = 1; for frequency register 0
        MSB |= 0x4000
        LSB |= 0x4000

        self._send(0x2100)
        #Set the frequency
        self._send(LSB)    #lower 14 bits
        self._send(MSB)    #Upper 14 bits
        #phase
        #Send(0&0xC000)    # Place holder for now - does nothing.
        #shape
        self._send(self.shape_word)    # square: 0x2020, sin: 0x2000, triangle: 0x2002
