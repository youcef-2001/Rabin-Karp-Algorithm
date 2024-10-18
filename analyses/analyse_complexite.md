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