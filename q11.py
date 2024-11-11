class FilaAtendimento:
    def __init__(self):
        # Inicializamos a fila como uma lista vazia
        self.fila = []
        self.inicio = 0  # Apontador para o início da fila

    def adicionar_cliente(self, nome):
        # Adiciona um cliente ao final da fila
        self.fila.append(nome)

    def atender_cliente(self):
        # Verifica se há clientes para atender
        if self.inicio < len(self.fila):
            # Obtém o cliente no início da fila
            cliente = self.fila[self.inicio]
            # Move o ponteiro de início para o próximo cliente na fila
            self.inicio += 1
            # Exibe o cliente que está sendo atendido
            print(f"Atendendo cliente: {cliente}")
            return cliente
        else:
            print("Nenhum cliente na fila para atender.")
            return None

    def tamanho_fila(self):
        # Calcula o tamanho da fila baseado no ponteiro de início
        return len(self.fila) - self.inicio

# Cria uma nova fila de atendimento
fila = FilaAtendimento()

# Adiciona clientes à fila
fila.adicionar_cliente("Cliente 1")
fila.adicionar_cliente("Cliente 2")
fila.adicionar_cliente("Cliente 3")

# Atende o primeiro cliente da fila
fila.atender_cliente()

# Verifica o tamanho da fila
print(f"Tamanho da fila: {fila.tamanho_fila()}")

# Atende o próximo cliente
fila.atender_cliente()

# Verifica o tamanho da fila novamente
print(f"Tamanho da fila: {fila.tamanho_fila()}")
