#Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário. O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.

valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

def calcular_pedido(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago):

  totalHamburgueres = valorHamburguer * quantidadeHamburguer

  totalBebidas = valorBebida * quantidadeBebida

  precoTotal = totalHamburgueres + totalBebidas

  troco = valorPago - precoTotal

  mensagem = f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}."

  print(mensagem)

calcular_pedido(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago)