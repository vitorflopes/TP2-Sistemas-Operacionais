def tarefa_no_topo(pilha_de_tarefas):
    # Verifica se a pilha está vazia; se sim, retorna None ou uma mensagem
    if len(pilha_de_tarefas) == 0:
        return None  # Ou podemos retornar "Pilha vazia"

    # Retorna o elemento no topo sem removê-lo
    topo = pilha_de_tarefas[len(pilha_de_tarefas) - 1]
    return topo

# Exemplo de uso
pilha_de_tarefas = [1, 2, 3, 4, 5]
print(tarefa_no_topo(pilha_de_tarefas))


