import time
from implementations.implem1 import search
from implementations.implem import Searcher , Hasher
from ressources.chaines import texte1 , texte2 , texte3

if __name__ == '__main__':
	pat = "hey"		
	# les args 
	# A prime number
	q = 101

		# Function Call
	print("Resultat avec l'algo fonctionnel :")
	start = time.time()
	print (search(pat, texte2, q))
	end = time.time()
	timeT = end- start
	print("time" , timeT)


	print("Resultat avec l'algo POO :")
	#Function Call with POO 
	start = time.time()
	hasher = Hasher(texte2, q, len(pat))
	hasher.calculHashes()# rempli le dictionnaire des hash 
	searcher = Searcher(hasher , pat)
	print(searcher.searchPattern())
	end = time.time()
	timeT= end-start
	print("time" ,timeT )
	



pat = "hey"
hasher = Hasher(texte2, 101, len(pat))
assert (not hasher == None)
hasher.calculHashes()# rempli le dictionnaire des hash 
searcher = Searcher(hasher , pat)
assert(not searcher == None)
assert(searcher.searchPattern() ==[15, 45, 54, 222, 240, 270, 279, 447])

assert ( not hasher.calculHash("salut") ==  hasher.calculHash("lutsa"))

