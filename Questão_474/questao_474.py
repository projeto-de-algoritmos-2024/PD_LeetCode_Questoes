class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Inicializa matriz DP com zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Itera sobre cada string da entrada
        for s in strs:
            # Conta zeros e uns na string atual
            zeros = s.count('0')
            ones = s.count('1')
            
            # Itera de trás para frente para evitar usar a mesma string múltiplas vezes
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        return dp[m][n]