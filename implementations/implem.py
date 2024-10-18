"""calcul de tout les hash pour les fenetre du texte a rechercher"""
class Hasher :
    def __init__(self,txt,q,M, d =256):
        self.N = len(txt)
        self.dic = dict(enumerate((self.N-M+2)*[0]))
        # The value of h would be "pow(d, M-1)%q"
        self.h = 1
        for i in range(M-1):
            self.h = (self.h*d) % q
        self.txt = txt
        self.q = q
        self.d = d
        self.M = M


    def calculHashes(self):
        """rempli le dictionnaire de lobjet en calculant un hash pour toutees les fenetres"""
        for i in range(self.M):
            self.dic[0] = (self.d*self.dic[0] + ord(self.txt[i])) % self.q
        for i in range(self.N-self.M+1):
            if i < self.N-self.M:
                self.dic[i+1] = (self.d*(self.dic[i]-ord(self.txt[i])*self.h) + ord(self.txt[i+self.M])) % self.q
			# We might get negative values of dic[i], converting it to
			# positive
            if self.dic[i+1] < 0:
                self.dic[i+1] = self.dic[i+1]+self.q

    def calculHash(self,pat):
        """return le hash du pattern"""
        p=0
        for i in range(self.M):
            p = (self.d*p + ord(pat[i])) % self.q
        return p





"""Object pour chercher et tester les hash de toutes les fenetres avec le pattern"""

class Searcher:

    def __init__(self,hasher : Hasher,pat):
        self.p = hasher.calculHash(pat)
        self.N = hasher.N
        self.M = hasher.M
        self.dico = hasher.dic
        self.txt = hasher.txt
        self.pattern = pat
		

        
        
    def searchPattern(self)  :
        res = []
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
                    res.append(i)
        return res 


