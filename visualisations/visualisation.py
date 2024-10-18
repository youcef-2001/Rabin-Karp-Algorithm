

import time
import random
import string
import matplotlib.pyplot as plt

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





def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def measure_performance(text_length, pattern_length, num_trials=10):
    total_time = 0
    pattern = generate_random_string(pattern_length)
    for _ in range(num_trials):
        text = generate_random_string(text_length)
        hasher = Hasher(text, q=101, M=pattern_length)
        hasher.calculHashes()
        start_time = time.time()
        searcher = Searcher(hasher, pattern)
        searcher.searchPattern()
        total_time += (time.time() - start_time)
    return total_time / num_trials

# Configurations pour le graphique
text_sizes = [100,250, 500, 1000,2500, 5000, 10000, 100000,200000, 300000]
pattern_length = 15
execution_times = []

# Mesure des performances
for text_size in text_sizes:
    avg_time = measure_performance(text_size, pattern_length)
    execution_times.append(avg_time)

# Tracer les résultats
plt.figure(figsize=(10, 10))
plt.plot(text_sizes, execution_times, marker='o')
plt.title("Performance de l'Algorithme Rabin-Karp")
plt.xlabel("Taille du texte (N)")
plt.ylabel("Temps d'exécution moyen (secondes)")
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.xticks(text_sizes)
plt.show()