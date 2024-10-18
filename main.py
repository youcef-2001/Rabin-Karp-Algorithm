import time
from implementations.implem1 import search
from implementations.implem import Searcher , Hasher



if __name__ == '__main__':
	pat = input("quelle patterne rechercher? ")	
	texte = input("Le texte dans lequel recherchez")
	# nombre premier
	q = 101

	# Function Call
	print("Resultat avec l'algo fonctionnel :")
	start = time.time()
	print (search(pat, texte, q))
	end = time.time()
	timeT = end- start
	print("time" , timeT,"s")



	print("Resultat avec l'algo POO :")
	#Function Call with POO 
	start = time.time()
	hasher = Hasher(texte, q, len(pat))
	hasher.calculHashes()# rempli le dictionnaire des hash 
	searcher = Searcher(hasher , pat)
	print(searcher.searchPattern())
	end = time.time()
	timeT= end-start
	print("time" ,timeT , "s")
	




