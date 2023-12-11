import networkx as nx

# Criar um grafo direcionado
G = nx.DiGraph()

class Comando:
    def jump(self):
        print('TesteJump')

    def nothing(self):
        print('Testenada')

    def stop(self):
        print('TestePARar')

    def back(self):
        print('Voltar')

# Criar uma instância da classe
comandos = Comando()

for method_name in dir(comandos):
    # Obter o atributo (método) da instância
    method = getattr(comandos, method_name)
    # Verificar se o atributo é um método chamável e não um método especial (começa e termina com __)
    if callable(method) and not method_name.startswith('__'):
        method()




# Adicionar nós ao grafo
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")
# G.add_node("D")

# # Adicionar arestas ao grafo
# G.add_edge("A", "B")
# G.add_edge("A", "C")
# G.add_edge("B", "D")
# G.add_edge("C", "D")


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#      # Isso é apenas para visualizar a ordem de visita
    
#     for neighbor in graph.neighbors(start):
#         print(neighbor)
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)
#     return visited

# # Chamar DFS a partir do nó 'A'
# visited_nodes = dfs(G, 'A')
