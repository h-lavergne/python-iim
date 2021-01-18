# Membres du groupe
- Benjamin Lebon
- Maxime Bonnet
- Hugo Lavergne

## Channel TD 11

# Bubble sort
```
Bubble Sort est l'algorithme de tri le plus simple qui fonctionne en échangeant à plusieurs reprises les éléments adjacents s'ils sont dans le mauvais ordre.

## Resultats:
Série: 35;5;14;233;7;9;20;15;3;8;895
Résultat: 3;5;7;8;9;14;15;20;35;233;895
Nb de comparaison : 27
Nb iteration : 55
Temps (sec) : 0.0s
```

# Selection Sort
```
L'algorithme de tri par sélection trie un tableau en trouvant à plusieurs reprises l'élément minimum (en tenant compte de l'ordre croissant) de la partie non triée et en le plaçant au début. L'algorithme gère deux sous-tableaux dans un tableau donné.

1) Le sous-tableau qui est déjà trié.
2) Sous-matrice restante non triée.

À chaque itération du tri par sélection, l'élément minimum (en tenant compte de l'ordre croissant) du sous-tableau non trié est sélectionné et déplacé vers le sous-tableau trié.

## Resultats:
Série: 35;5;14;233;7;9;20;15;3;8;895
Résultat: 3;5;7;8;9;14;15;20;35;233;895
Nb de comparaison : 8
Nb iteration : 55
Temps (sec) : 0.0s
```

# Insertion Sort
```
Le tri par insertion est un algorithme de tri simple qui fonctionne de la même manière que vous triez les cartes à jouer entre vos mains. Le tableau est virtuellement divisé en une partie triée et une partie non triée. Les valeurs de la pièce non triée sont sélectionnées et placées à la bonne position dans la pièce triée.

## Resultats:
Série: 35;5;14;233;7;9;20;15;3;8;895
Résultat: 3;5;7;8;9;14;15;20;35;233;895
Nb de comparaison : 27
Nb iteration : 10
Temps (sec) : 0.0s
```

# Merge Sort
```
Merge Sort est un algorithme 'Divide and Conquer'. Il divise le tableau d'entrée en deux moitiés, appelle lui-même les deux moitiés et fusionne ensuite les deux moitiés triées. La fonction merge () est utilisée pour fusionner deux moitiés. La fusion (arr, l, m, r) est un processus clé qui suppose que arr [l..m] et arr [m + 1..r] sont triés et fusionne les deux sous-tableaux triés en un seul.

## Resultats:
Série: 35;5;14;233;7;9;20;15;3;8;895
Résultat: 3;5;7;8;9;14;15;20;35;233;895
Nb de comparaison : 39
Nb iteration : N/A
Temps (sec) : 0.0s
```

# Quick Sort
```
Comme Merge Sort, QuickSort est un algorithme Divide and Conquer. Il sélectionne un élément comme pivot et partitionne le tableau donné autour du pivot sélectionné. Il existe de nombreuses versions de quickSort qui sélectionnent le pivot de différentes manières.

 - Toujours choisir le premier élément comme pivot.
 - Toujours choisir le dernier élément comme pivot (implémenté ci-dessous)
 - Choisir un élément aléatoire comme pivot.
 - Choisir la médiane comme pivot.

## Resultats:
Série: 35;5;14;233;7;9;20;15;3;8;895
Résultat: 35;5;14;233;7;9;20;15;3;8;895
Nb de comparaison : 34
Nb iteration : N/A
Temps (sec) : 0.0s
```

# Shell Sort
```
Le shell sort est un algorithme qui trie d'abord les éléments éloignés les uns des autres et réduit successivement l'intervalle entre les éléments à trier. C'est une version généralisée du tri par insertion.

Dans le sheel sort, les éléments à un intervalle spécifique sont triés. L'intervalle entre les éléments est progressivement diminué en fonction de la séquence utilisée. Les performances du shell sort dépendent du type de séquence utilisé pour un tableau d'entrée donné.

## Resultats:
Série: 35;5;14;233;7;9;20;15;3;8;895
Résultat: 3;5;7;8;9;14;15;20;35;233;895
Nb de comparaison : 15
Nb iteration : 25
Temps (sec) : 0.0s
```

# Comb Sort 
```
Le tri en peigne est une variante du tri à bulles. Le tri en peigne augmente l'écart utilisé dans les comparaisons et les échanges. Dans le tri à bulles, lorsque deux éléments sont comparés, ils ont toujours un écart (distance l'un de l'autre) de 1. L'idée de base du tri en peigne est que l'écart peut être bien supérieur à 1.

## Resultats:
Série: 35;5;14;233;7;9;20;15;3;8;895
Résultat: 3;5;7;8;9;14;15;20;35;233;895
Nb de comparaison : 5
Nb iteration : 7
Temps (sec) : 0.0s
```


## Étude comparative

```
D'après les résultats retournés par les différentes méthodes de tri, nous pouvons voir que # Comb Sort effectue très peu de comparaison et d'itération ce qui prouve son efficacité.
```