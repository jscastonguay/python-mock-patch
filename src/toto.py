from device import Device

class Toto():
    def __init__(self) -> None:
        self.d = Device()
    
    def getNumber(self, x : int) -> int:
        return 3
    
    def operation(self, x : int):
        return self.d.do(2 * x) * self.d.param
