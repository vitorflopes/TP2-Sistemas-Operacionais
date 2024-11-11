def ordenar_fila(fila):
    n = len(fila)
    
    # Realiza múltiplas passagens pela lista
    for i in range(n):
        # Percorre a lista até o último elemento não ordenado
        for j in range(0, n - i - 1):
            # Se o elemento atual é maior que o próximo, troca-os
            if fila[j] > fila[j + 1]:
                # Troca de elementos
                temp = fila[j]
                fila[j] = fila[j + 1]
                fila[j + 1] = temp
    
    return fila

# Exemplo de uso
fila = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(ordenar_fila(fila))


