class TabelaHash:
    def __init__(self, tamanho):
        # Inicializa a tabela hash com uma lista de listas vazias para cada índice
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        # Função hash simples que calcula o índice usando o hash da chave e o tamanho da tabela
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        # Calcula o índice da chave na tabela usando a função hash
        indice = self._hash(chave)
        
        # Verifica se a chave já existe no índice para atualizar o valor
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor  # Atualiza o valor existente
                return
        
        # Se a chave não existe, insere um novo par (chave, valor) na lista da posição
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        # Calcula o índice da chave
        indice = self._hash(chave)
        
        # Procura a chave na lista de colisões do índice
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]  # Retorna o valor associado à chave
        return None  # Retorna None se a chave não for encontrada

    def remover(self, chave):
        # Calcula o índice da chave
        indice = self._hash(chave)
        
        # Procura a chave na lista de colisões do índice
        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                del self.tabela[indice][i]  # Remove o par (chave, valor) da lista
                return True  # Indica que a remoção foi bem-sucedida
        return False  # Indica que a chave não foi encontrada

# Cria uma tabela hash com tamanho 10
tabela = TabelaHash(10)

# Insere pares de chave e valor na tabela
tabela.inserir("nome", "Alice")
tabela.inserir("idade", 30)
tabela.inserir("cidade", "São Paulo")

# Busca valores associados às chaves
print(tabela.buscar("nome"))
print(tabela.buscar("idade"))
print(tabela.buscar("cidade"))
print(tabela.buscar("pais"))

# Remove uma chave da tabela
tabela.remover("idade")

# Tenta buscar a chave removida
print(tabela.buscar("idade"))