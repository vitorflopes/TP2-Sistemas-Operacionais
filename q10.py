def contar_livros_impares(fila):
    contador = 0
    
    for numero in fila:
        # Verificação manual para número ímpar: subtraindo 2 até que o número chegue a 0 ou 1
        n = numero
        while n > 1:
            n = n - 2  # Subtrai 2 até reduzir o número a 0 (par) ou 1 (ímpar)
        
        if n == 1:  # Se restar 1, o número é ímpar
            contador += 1
            
    return contador

# Exemplo de uso
fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contar_livros_impares(fila))
