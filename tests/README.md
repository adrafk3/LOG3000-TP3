# Module `tests`

## Raison d'etre
Ce module contient les tests automatises de l'application. Son objectif est de detecter rapidement les regressions et de confirmer les bogues fonctionnels.

## Fichiers principaux
- `test_operators.py`: verifie le contrat attendu des operations arithmetiques (`+`, `-`, `*`, `/`).

## Couverture actuelle
Les tests couvrent:
- addition standard;
- soustraction standard (`a - b`);
- multiplication standard (`a * b`);
- division reelle (`a / b`);
- gestion de la division par zero.

## Comment executer les tests
Depuis la racine du projet:

```bash
python -m unittest discover -s tests -v
```

Alternative (un seul fichier):

```bash
python -m unittest tests/test_operators.py -v
```

## Interpretation des resultats
- `OK`: tous les comportements testes correspondent aux attentes.
- `FAILED`: au moins un comportement implemente ne respecte pas le contrat attendu d'une calculatrice standard. Ces echecs doivent etre traces via des issues GitHub.
