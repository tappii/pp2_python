class animal:
    def __init__(self, type, paw):
          self.type = type
          self.paw = paw
    def getinfo(self):
        print(self.type,self.paw)
chicken = animal("chicken", 2)
chicken.getinfo()