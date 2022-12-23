from order import Order
from calculate_shipping import CalculateShipping

# Criando instância da classe que calcula o frete
calculate_shipping = CalculateShipping()

# Criando instância da classe que faz o pedido
order = Order(500)

# Chamando a função que calcula o frete com base no pedido feito
calculate_shipping.execute_calculation(order, "Express")

# Chamando a função que calcula o frete com base no pedido feito
calculate_shipping.execute_calculation(order, "Default")
