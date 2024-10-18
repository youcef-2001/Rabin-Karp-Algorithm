

from implementations.implem import Hasher , Searcher
from ressources.chaines import texte1 , texte2 , texte3


pat = "hey"
hasher = Hasher(texte2, 101, len(pat))
hasher.calculHashes()# rempli le dictionnaire des hash 
searcher = Searcher(hasher , pat)
assert(searcher.searchPattern() ==[15, 45, 54, 222, 240, 270, 279, 447])

assert (not hasher.calculHash("salut") ==  hasher.calculHash("lutsa"))