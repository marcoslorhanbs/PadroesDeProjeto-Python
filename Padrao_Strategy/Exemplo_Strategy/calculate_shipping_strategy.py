class CalculateShippingStrategy():

    def execute_calculation(self, order, shipping):
        total = shipping(order)
        print(total)