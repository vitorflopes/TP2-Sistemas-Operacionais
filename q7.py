def contar_pedidos_pares(pilha_de_pedidos):
    # Inicializa o contador de pedidos pares
    contador_pares = 0

    # Percorre cada pedido na pilha
    for i in range(len(pilha_de_pedidos)):
        # Acessa o pedido atual
        pedido = pilha_de_pedidos[i]

        # Verifica se o número de identificação é par
        if pedido % 2 == 0:
            contador_pares += 1

    # Retorna o total de pedidos com número par
    return contador_pares

# Exemplo de uso
pilha_de_pedidos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contar_pedidos_pares(pilha_de_pedidos))
