from order import Order
from calculate_shipping_strategy import CalculateShippingStrategy
from shippings import Default, Express

# Criando instância da classe que calcula o frete
calculate_shipping = CalculateShippingStrategy()

# Criando instância da classe que faz o pedido
order = Order(500)

# Chamando a função que calcula o frete com base no pedido feito
calculate_shipping.execute_calculation(order, Default().calculate)

# Chamando a função que calcula o frete com base no pedido feito
calculate_shipping.execute_calculation(order, Express().calculate)
