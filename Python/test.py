'''a = "ab cd ef gh"
print(a.split())'''

'''class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

comp1 = Computer()   #---> This is object
print(type(comp1))

# Computer.config(comp1)
comp1.config()'''


class ComputerConfig:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config of your computer is", self.cpu, self.ram)

comp1 = ComputerConfig("i5", "8GB")
comp2 = ComputerConfig("Ryzen 5", "16GB")

comp1.config()
comp2.config()
