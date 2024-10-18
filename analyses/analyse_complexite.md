## Analyse de la Complexité
L'algorithme de Rabin-Karp a une complexité qui dépend de la taille du motif (M) et du texte (N), avec une distinction importante entre le cas moyen et le pire cas.

#### Pré-calcul du hachage :
Le calcul initial du hachage pour le motif (pat) et pour la première fenêtre du texte prend un temps O(M), où M est la longueur du motif.
#### Recherche dans le texte :
Dans chaque nouvelle fenêtre de taille M, l'algorithme met à jour le hachage en O(1) et le compare avec le hachage du motif. S'il y a correspondance de hachage, une vérification caractère par caractère est effectuée, ce qui prend un temps O(M) dans le pire cas (si tous les caractères doivent être comparés).
L'algorithme glisse sur N-M+1 fenêtres dans le texte, donc le coût pour parcourir le texte est O(N) dans le meilleur et le cas moyen. Cependant, si le hachage du motif est égal au hachage de nombreuses fenêtres, chaque fenêtre nécessitera une comparaison caractère par caractère, ce qui peut amener la complexité à O(N * M) dans le pire cas.
#### Cas moyen :
Dans la majorité des cas, les collisions de hachage sont rares, et le test caractère par caractère ne se produit pas souvent. Par conséquent, la complexité moyenne de l'algorithme est O(N + M), ce qui est beaucoup plus efficace que la recherche brute O(N * M) dans les scénarios habituels.
#### Pire cas :
Le pire cas de l'algorithme se produit lorsque les hachages des sous-chaînes du texte sont égaux à celui du motif mais que les sous-chaînes ne correspondent pas, forçant ainsi des vérifications caractère par caractère pour presque chaque fenêtre. Dans ce cas, la complexité est O(N * M), car chaque fenêtre pourrait nécessiter une comparaison complète de M caractères.


## Analyse de la Complexité pour la version POO: 

#### Classe Hasher :
Initialisation et calcul des hachages (calculHashes) : Le calcul initial des hachages prend un temps O(N), où N est la longueur du texte, car chaque caractère du texte est traité pour toutes les fenêtres possibles de taille M. Le calcul du hachage de chaque fenêtre est incrémental, donc il est O(1) par fenêtre.
Le calcul du hachage d'un motif (calculHash) prend O(M).
#### Classe Searcher :
La recherche dans le texte prend O(N) dans le meilleur cas, puisque chaque hachage est comparé directement. En cas de collision de hachage, une vérification caractère par caractère est effectuée, ce qui peut augmenter la complexité dans le pire cas à O(N * M).
En résumé, cette approche garde la complexité similaire à celle de l'algorithme Rabin-Karp classique, avec O(N + M) dans la plupart des cas et O(N * M) dans le pire cas.

#### Conclusion

Cette approche modulaire de l'algorithme de Rabin-Karp améliore la lisibilité et la maintenabilité du code tout en préservant les performances de l'algorithme. Les classes Hasher et Searcher permettent une utilisation efficace et réutilisable de l'algorithme pour diverses applications de recherche de motifs.