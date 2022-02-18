class CycleShop():
    def __init__(self, stock):
        self.stock = stock

    def DisplayCycle(self):
        print("Total cycle", self.stock)

    def CycleRent(self, q):

        if q <= 0:
            print("Enter the valid value")
        elif q > self.stock:
            print("Value out of stock")
        else:
            print("total price", q * 15)
            print("Cycle Left", self.stock - q)


while True:
    object = CycleShop(50)
    print("welcome to Sai Cycle shop")
    print("15 rs per Cycle")
    uc = (int(input('''
        1 Display Stock
        2 Rent Cycle
        3 Exit

        ''')))

    if uc == 1:
        object.DisplayCycle()
    elif uc == 2:
        n = int(input("enter the Qty: "))
        object.CycleRent(n)
    else:
        break

