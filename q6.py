def contar_pedidos_impares(pilha_de_pedidos):
    # Inicializa o contador de pedidos ímpares
    contador_impares = 0

    # Percorre cada pedido na pilha
    for i in range(len(pilha_de_pedidos)):
        # Acessa o pedido atual
        pedido = pilha_de_pedidos[i]

        # Verifica se o número de identificação é ímpar
        if pedido % 2 != 0:
            contador_impares += 1

    # Retorna o total de pedidos com número ímpar
    return contador_impares

# Exemplo de uso
pilha_de_pedidos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contar_pedidos_impares(pilha_de_pedidos))


