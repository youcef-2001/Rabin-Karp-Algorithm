class Hasher :
    def __init__(self,txt,q,M, d =256):
        self.N = len(txt)
        self.dic = enumerate(self.N * [0])
        # The value of h would be "pow(d, M-1)%q"
        self.h = 1
        for i in range(M-1):
            self.h = (self.h*d) % q
        self.txt = txt
        self.q = q
        self.d = d
        self.M = M


    def calculHashes(self):
        for i in range(self.M):
            self.dic[0] = (self.d*self.dic[0] + ord(self.txt[i])) % self.q
        for i in range(self.N-self.M+1):
            if i < self.N-self.M:
                self.dic[i+1] = (self.d*(self.dic[i]-ord(self.txt[i])*self.h) + ord(self.txt[i+self.M])) % self.q
			# We might get negative values of t, converting it to
			# positive
            if self.dic[i+1] < 0:
                self.dic[i+1] = self.dic[i+1]+self.q