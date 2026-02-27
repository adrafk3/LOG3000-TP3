# Module `static`

## Raison d'etre
Ce module contient les ressources statiques de l'interface. Son role est de definir l'apparence visuelle de la calculatrice et l'organisation du layout.

## Fichiers principaux
- `style.css`: styles globaux de la page, styles du conteneur de calculatrice, grille des boutons, et etats visuels (hover/active).

## Dependances et hypotheses
- Le CSS est charge depuis le template via `url_for('static', filename='style.css')`.
- Les classes/identifiants CSS (`.calculator`, `.buttons`, `.btn`, `.operator`, `#display`) doivent rester alignes avec le HTML de `templates/index.html`.
- Aucun preprocesseur CSS n'est utilise (CSS natif uniquement).
