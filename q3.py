def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

# Exemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(encontrar_duplicados_forca_bruta(lista))

#----------------------------------------------------------

def encontrar_duplicados_com_conjunto(lista):
    encontrados = set()
    duplicados = []
    for numero in lista:
        if numero in encontrados:
            if numero not in duplicados:
                duplicados.append(numero)
        else:
            encontrados.add(numero)
    return duplicados

# Exemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(encontrar_duplicados_com_conjunto(lista))
