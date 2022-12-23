class CalculateShipping():

    def execute_calculation(self, order, shipping):
        if shipping == "Default":
            total = order.value * 0.05
        elif shipping == "Express":
            total = order.value * 0.1
        print(total)
        