# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256

# pat -> pattern
# txt -> text
# q -> A prime number


def search(pat, txt, q,d=256):
	"""
	le programme suivant est une implementation de l'algorithme Rabin-Karp
	pat -> pattern a rechercher
	txt -> le texte dans leqel chercher
	q -> est un nombre de preference premier necessaire a la fonction de hashage
	d -> est le nombre de caractere dans l'alphabet d'input a ne pas confondre avec le texte auquel rechercher
	"""
	
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 # hash a rechercher
	t = 0 # hash de la plage dans le texte
	h = 1
	
	# h = d.puiss(M-1) mod q
	for i in range(M-1):
		h = (h*d) % q
	# Calculate the hash value of pattern and first window
	
	for i in range(M):
		p = (d*p + ord(pat[i])) % q
		t = (d*t + ord(txt[i])) % q
	# Slide the pattern over text one by one
	for i in range(N-M+1):
		# si le hash du pattern et de la fenetre  sont equal verifier que les caractere correspondent correctement
		if p == t:
			# Check for characters one by one
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else:
					j += 1
			# if pat[0...M-1] = txt[i, i+1, ...i+M-1]
			if j == M:
				print("Pattern found at index " + str(i))
		# Calculate hash value for next window of text: Remove
		# leading digit, add trailing digit
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
			# We might get negative values of t, converting it to
			# positive
			if t < 0:
				t = t+q



