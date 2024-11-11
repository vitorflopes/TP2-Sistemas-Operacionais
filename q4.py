def ordenar_pilha(pilha):
    # Cria uma pilha auxiliar vazia
    pilha_ordenada = []

    # Processa até que a pilha original esteja vazia
    while pilha:
        # Remove o elemento do topo da pilha original
        temp = pilha.pop()
        
        # Transfere elementos da pilha ordenada para a pilha original 
        # até encontrar a posição correta do elemento temporário
        while pilha_ordenada and pilha_ordenada[-1] > temp:
            pilha.append(pilha_ordenada.pop())

        # Coloca o elemento temporário na posição correta da pilha ordenada
        pilha_ordenada.append(temp)
    
    # Retorna a pilha ordenada
    return pilha_ordenada

# Exemplo de uso
pilha = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(ordenar_pilha(pilha))

