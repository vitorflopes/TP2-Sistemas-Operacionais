def inverter_fila(fila):
    inicio = 0
    fim = len(fila) - 1
    
    # Continuamos até que o índice do inicio seja menor que o do fim
    while inicio < fim:
        # Troca os elementos de início e fim
        temp = fila[inicio]
        fila[inicio] = fila[fim]
        fila[fim] = temp
        
        # Move o índice inicio para a direita e fim para a esquerda
        inicio += 1
        fim -= 1
    
    return fila

# Exemplo de uso
fila = [1, 2, 3, 4, 5]
print(inverter_fila(fila))


