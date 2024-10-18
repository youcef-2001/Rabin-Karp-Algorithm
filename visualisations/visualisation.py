

import time
import random
import string
import matplotlib.pyplot as plt

from ..implementations.implem import Hasher
from ..implementations.implem import Searcher


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
text_sizes = [100, 500, 1000, 5000, 10000]
pattern_length = 10
execution_times = []

# Mesure des performances
for text_size in text_sizes:
    avg_time = measure_performance(text_size, pattern_length)
    execution_times.append(avg_time)

# Tracer les résultats
plt.figure(figsize=(10, 6))
plt.plot(text_sizes, execution_times, marker='o')
plt.title("Performance de l'Algorithme Rabin-Karp")
plt.xlabel("Taille du texte (N)")
plt.ylabel("Temps d'exécution moyen (secondes)")
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.xticks(text_sizes)
plt.show()