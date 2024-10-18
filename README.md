## Algorithme de Recherche de Motif - Rabin-Karp 

Cette implémentation présente une version simple et efficace de l'algorithme de Rabin-Karp, une méthode utilisée pour rechercher un motif dans un texte. Elle se base sur le calcul de hachages pour comparer les sous-chaînes du texte avec le motif recherché. Bien que l'algorithme soit conçu pour être plus rapide que la recherche brute en comparant directement les chaînes, cette version adopte une approche naïve et facile à comprendre, en utilisant une seule fonction.

### Fonctionnement
L'algorithme Rabin-Karp repose sur les étapes suivantes :

Le calcul d'un hachage pour le motif (pat) et pour chaque sous-chaîne de longueur équivalente dans le texte (txt).
Si les hachages correspondent, on effectue une vérification caractère par caractère pour s'assurer que la sous-chaîne du texte correspond bien au motif.
Le hachage est mis à jour de manière incrémentale pour chaque nouvelle fenêtre de sous-chaîne, rendant l'algorithme plus efficace que les comparaisons directes répétées.
Caractéristiques
Une seule fonction : La fonction search(pat, txt, q, d=256) regroupe toutes les étapes, de l'initialisation au calcul du hachage et à la recherche du motif.


