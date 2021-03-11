
class parentClass:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

class childClass(parentClass):
    def test(self):
        print("child")    
