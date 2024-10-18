from Hasher import Hasher
class Searcher:

    def __init__(self,hasher : Hasher,pat):
        self.p = hasher.calculHash(pat)
        self.N = hasher.N
        self.M = hasher.M
        self.dico = hasher.dic
        self.txt = hasher.txt
        self.pattern = pat
		

        
        
    def serachPattern(self)  :
        for i in range(self.N-self.M+1):
		# si le hash du pattern et de la fenetre  sont equal verifier que les caractere correspondent correctement
            if self.p == self.dico[i]:
                # Check for characters one by one
                for j in range(self.M):
                    if self.txt[i+j] != self.pattern[j]:
                        break
                    else:
                        j += 1
                # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
                if j == self.M:
                    print("Pattern found at index " + str(i))
