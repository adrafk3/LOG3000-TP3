# Module `templates`

## Raison d'etre
Ce module contient les gabarits HTML rendus par Flask. Il definit la structure de l'interface utilisateur et les interactions client minimales (composition de l'expression et soumission au serveur).

## Fichiers principaux
- `index.html`: page unique de la calculatrice. Contient:
  - le formulaire `POST` vers la route `/`;
  - le champ `display` utilise pour envoyer l'expression au backend;
  - les boutons numeriques et operateurs;
  - des fonctions JavaScript locales pour modifier/vider l'affichage.

## Dependances et hypotheses
- Depend de Flask/Jinja (`{{ url_for(...) }}` et `{{ result }}`).
- Suppose qu'une route backend accepte `GET`/`POST` sur `/` et retourne `result`.
- Suppose que le fichier CSS `static/style.css` est servi correctement par Flask.
- Le nom du champ de formulaire `display` doit rester coherent avec `app.py`.
