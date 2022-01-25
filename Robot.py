import troykahat


class Motor():
    def __init__(self, pinE, pinD):
        self.pinE = pinE
        self.pinD = pinD
        self.ap = troykahat.analog_io()
        self.ap.pinMode(self.pinE, self.ap.OUTPUT)
        self.ap.pinMode(self.pinD, self.ap.OUTPUT)

    def run(self, dir: str, speed: int):
        if dir == 'forward':
            self.ap.analogWrite(self.pinE, speed)
            self.ap.digitalWrite(self.pinD, True)
        elif dir == 'backward':
            self.ap.analogWrite(self.pinE, speed)
            self.ap.digitalWrite(self.pinD, False)
        elif dir == 'stop':
            self.ap.analogWrite(self.pinE, 0)
            self.ap.digitalWrite(self.pinD, False)
