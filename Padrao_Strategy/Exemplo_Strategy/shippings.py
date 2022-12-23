class Default():
    def calculate(self, order):
        total = order.value * 0.05
        return total


class Express():
    def calculate(self, order):
        total = order.value * 0.1
        return total