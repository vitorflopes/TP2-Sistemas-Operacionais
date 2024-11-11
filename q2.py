def merge_sort(lista):
    # Se a lista tiver apenas um elemento ou estiver vazia, ela já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Encontra o ponto médio para dividir a lista em duas metades
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Ordena as duas metades recursivamente
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    # Combina as duas metades ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Combina as duas listas enquanto ambas têm elementos
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes, se houver, das duas metades
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

# Exemplo de uso
lista = [5, 3, 8, 6, 2, 7, 4, 1]
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)
