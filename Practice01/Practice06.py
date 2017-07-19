class Gadget():
    def __init__(self, gadgetName, brand):
        self.gadgetName = gadgetName
        self.brand = brand

class Tao:
    def __init__(self, pangalan, gadgetName, brand):
        self.pangalan = pangalan
        self.gadget = Gadget(gadgetName, brand)

    def gayagaya(self, kalaban):
        self.pangalan = kalaban.pangalan

        return  self.pangalan

tao1 = Tao("Lando", "Sagwen", "Samsung")
tao2 = Tao("Kevin", "Tablet", "Kopiko")

tao1.gayagaya(tao2)
print tao1.pangalan