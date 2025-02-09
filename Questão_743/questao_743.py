import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Inicializa as distâncias com infinito para todos os nós (índice 0 não é utilizado)
        dist = [math.inf] * (n + 1)
        dist[k] = 0  # A distância do nó de partida para ele mesmo é 0

        # Relaxa todas as arestas por (n - 1) iterações
        for i in range(n - 1):
            # Flag para detectar se houve alguma atualização nesta iteração
            updated = False
            for u, v, w in times:
                # Se o nó u já foi alcançado e podemos melhorar a distância para v
                if dist[u] != math.inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            # Se não houve atualizações, já temos os caminhos mínimos
            if not updated:
                break

        # Verifica a maior distância entre os nós alcançados (desconsidera o índice 0)
        max_time = max(dist[1:])
        # Se algum nó não foi alcançado, retorna -1; caso contrário, retorna o tempo máximo
        return max_time if max_time != math.inf else -1