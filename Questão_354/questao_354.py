class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key=lambda x: (x[0], -x[1])) #ordena os envelopes pela largura e altura 
        
        heights = [h for _, h in envelopes] #define a lista de alturas
        
        lis = [] #cria uma lista vazia para armazenar a maior subsequência crescente
        
        #para cada altura, encontra a posição correta na lista lis e insere a altura
        for h in heights:
            pos = bisect.bisect_left(lis, h) #encontra a posição correta para inserir a altura
            if pos == len(lis):#se a posição for igual ao tamanho da lista, insere a altura no final
                lis.append(h)
            else: #se não insere a altura na posição correta
                lis[pos] = h
        
        return len(lis) #retorna o tamanho da lista lis