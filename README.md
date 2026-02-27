# LOG3000 TP3 - Calculatrice Web Flask

## Equipe
Equipe 36

## But et portee du projet
Ce projet est une application web de calculatrice construite avec Flask. L'objectif est de fournir une interface simple permettant d'entrer une expression arithmetique binaire (deux operandes, un operateur) et d'obtenir un resultat via un backend Python.

Le projet sert aussi de base pedagogique pour:
- la documentation du code et des modules;
- l'ajout de tests automatises;
- la collaboration Git (branches, pull requests, issues).

## Structure du depot
- `app.py`: point d'entree Flask, routage HTTP, validation et evaluation des expressions.
- `operators.py`: fonctions de calcul appelees par `app.py`.
- `templates/index.html`: template principal de l'interface.
- `static/style.css`: styles CSS de l'application.
- `tests/test_operators.py`: tests unitaires des operations arithmetiques.
- `templates/README.md`: documentation du module de presentation.
- `static/README.md`: documentation du module de styles.
- `tests/README.md`: documentation du module de tests.

## Pre-requis
- Git
- Python 3.10+ (3.11 recommande)
- pip

## Installation (etape par etape)
1. Cloner le depot:
```bash
git clone <url-du-repo>
```

2. Aller dans le dossier du projet:
```bash
cd TP3---LOG3000
```

3. Creer un environnement virtuel:
```bash
python -m venv .venv
```

4. Activer l'environnement virtuel:
- Windows PowerShell:
```bash
.\.venv\Scripts\Activate.ps1
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

5. Installer les dependances minimales:
```bash
pip install flask
```

## Utilisation
1. Demarrer l'application:
```bash
python app.py
```

2. Ouvrir un navigateur a l'adresse:
```text
http://127.0.0.1:5000
```

3. Utiliser les boutons de l'interface pour composer une expression, puis appuyer sur `=`.

4. Le resultat (ou un message d'erreur) est affiche dans le champ principal.

## Comportement fonctionnel actuel
Le comportement ci-dessous reflete l'implementation actuelle:
- une seule operation binaire est acceptee par expression;
- `+` effectue une addition standard;
- `-` effectue `b - a`;
- `*` effectue `a ** b`;
- `/` effectue `a // b`.

Ces details sont documentes dans `operators.py` pour garder une trace claire de l'etat courant du code.

## Tests
Le depot contient une suite de tests unitaires dans `tests/`.

Execution de toute la suite:
```bash
python -m unittest discover -s tests -v
```

Execution d'un fichier specifique:
```bash
python -m unittest tests/test_operators.py -v
```

## Flux de contribution
1. Creer une branche depuis `main`:
```bash
git checkout -b docs/<sujet>
```

2. Faire des commits atomiques avec messages explicites:
```bash
git add .
git commit -m "docs: decrire le module templates"
```

3. Pousser la branche:
```bash
git push -u origin docs/<sujet>
```

4. Ouvrir une Pull Request vers `main`:
- decrire le probleme;
- decrire la solution;
- lier l'issue correspondante (`Closes #<id>` si applicable).

5. Faire la revue de code avant fusion.

## Gestion des issues
- Utiliser une issue par besoin (bug, dette technique, amelioration).
- Ajouter un titre clair, des etapes de reproduction (si bug), et un resultat attendu.
- Assigner la branche/PR associee a l'issue pour garder la tracabilite.
