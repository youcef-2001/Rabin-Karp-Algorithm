## Algorithme de Recherche de Motif - Rabin-Karp (Approche Naïve en Une Fonction )

Cette implémentation présente une version simple et efficace de l'algorithme de Rabin-Karp, une méthode utilisée pour rechercher un motif dans un texte. Elle se base sur le calcul de hachages pour comparer les sous-chaînes du texte avec le motif recherché. Bien que l'algorithme soit conçu pour être plus rapide que la recherche brute en comparant directement les chaînes, cette version adopte une approche naïve et facile à comprendre, en utilisant une seule fonction.

### Fonctionnement
L'algorithme Rabin-Karp repose sur les étapes suivantes :

Le calcul d'un hachage pour le motif (pat) et pour chaque sous-chaîne de longueur équivalente dans le texte (txt).
Si les hachages correspondent, on effectue une vérification caractère par caractère pour s'assurer que la sous-chaîne du texte correspond bien au motif.
Le hachage est mis à jour de manière incrémentale pour chaque nouvelle fenêtre de sous-chaîne, rendant l'algorithme plus efficace que les comparaisons directes répétées.
Caractéristiques
Une seule fonction : La fonction search(pat, txt, q, d=256) regroupe toutes les étapes, de l'initialisation au calcul du hachage et à la recherche du motif.
####  Paramètres :
pat : le motif à rechercher dans le texte.
txt : le texte dans lequel la recherche est effectuée.
q : un nombre premier utilisé pour limiter les collisions de hachage.
d : la taille de l'alphabet (par défaut 256 pour le jeu de caractères ASCII).
Complexité : Bien que l'algorithme soit théoriquement O(N + M) en moyenne, cette version naïve effectue un passage caractère par caractère lors des collisions de hachages, rendant son utilisation plus intuitive mais potentiellement moins optimisée.
Exemple d'utilisation
```python 
pat = "test"
txt = "ceci est un simple test dans un texte"
q = 101  # Nombre premier
utilisé pour le hachage
```

### Appel de la fonction
    positions = search(pat, txt, q)

print("Motif trouvé aux positions :", positions)
Résultat attendu
La fonction retourne une liste des indices dans le texte où le motif est trouvé. Si aucune correspondance n'est trouvée, la liste est vide.

## Algorithme de Recherche de Motif - Rabin-Karp (Approche POO)

Cette implémentation présente une version organisée et modulaire de l'**algorithme de Rabin-Karp**, une méthode utilisée pour rechercher un **motif** dans un **texte**. En divisant le processus en deux classes distinctes, **`Hasher`** et **`Searcher`**, cette approche facilite la réutilisation des composants et améliore la lisibilité du code.

### Classes

#### Classe `Hasher`

**Responsabilité** : Calculer tous les hachages pour chaque fenêtre du texte en fonction de la taille du motif, et calculer le hachage d'un motif spécifique.

**Méthodes** :

- `__init__(self, txt, q, M, d=256)` : Initialise l'objet `Hasher`, prépare le texte pour la recherche et pré-calcule certaines valeurs (comme `h` qui est le multiplicateur pour faire glisser les fenêtres de manière efficace).
  
- `calculHashes(self)` : Calcule le hachage pour toutes les fenêtres du texte.
  
- `calculHash(self, pat)` : Calcule le hachage d'un motif donné (`pat`).

#### Classe `Searcher`

**Responsabilité** : Utiliser les hachages calculés par `Hasher` pour effectuer la recherche du motif dans le texte.

**Méthodes** :

- `__init__(self, hasher, pat)` : Initialise un objet `Searcher` à partir d'un objet `Hasher` et du motif à rechercher.

- `searchPattern(self)` : Parcourt les hachages calculés, compare le hachage du motif avec ceux des sous-chaînes du texte et vérifie si les sous-chaînes correspondent au motif.

### Avantages de cette approche

- **Séparation des responsabilités** : La classe `Hasher` est responsable du calcul des hachages, tandis que la classe `Searcher` se concentre sur l'acte de recherche du motif. Cela améliore la lisibilité et permet de mieux structurer l'algorithme.
  
- **Réutilisabilité** : Vous pouvez réutiliser l'objet `Hasher` pour différents motifs sans recalculer tous les hachages du texte, ce qui optimise l'utilisation des ressources si plusieurs recherches doivent être effectuées dans le même texte.

- **Modularité** : Les deux classes peuvent être facilement modifiées ou étendues sans impacter l'autre. Par exemple, vous pouvez optimiser `Hasher` sans changer `Searcher`.

### Suggestions d'amélioration



1. **Ajout de tests et d'erreurs** :
   - Vous pouvez ajouter une gestion des erreurs pour vérifier si le motif est plus grand que le texte, ou si les paramètres donnés à la classe `Hasher` sont valides (par exemple, si `M > N`, il n'y a pas besoin de lancer la recherche).

2. **Optimisation potentielle** :
   - Vous pouvez envisager de stocker les hachages de manière plus compacte (par exemple, dans une liste) au lieu d'un dictionnaire, à moins que vous ne prévoyiez des recherches non séquentielles dans le texte.

## Exemple d'utilisation

```python
from implementations.implem import Hasher, Searcher

txt = "ceci est un simple test dans un texte de test"
pat = "test"
q = 101  # Nombre premier utilisé pour le hachage

# Crée un Hasher et calcule les hachages pour toutes les fenêtres du texte
hasher = Hasher(txt, q, len(pat))
hasher.calculHashes()

# Crée un Searcher pour chercher le motif dans le texte
searcher = Searcher(hasher, pat)
positions = searcher.searchPattern()

print("Motif trouvé aux positions :", positions)
