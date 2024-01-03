## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

```bash
cd /path/to/put/project/in
git clone https://github.com/DaGuinci/Orange-County-Lettings.git
```

#### Créer l'environnement virtuel

```bash
cd /path/to/Python-OC-Lettings-FR
python -m venv venv
```

* Activer l'environnement 
  
```bash
source venv/bin/activate
```

* Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
```bash
which python
```

* Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure
```bash
python --version
```

* Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel
```bash
which pip
```
  
Pour désactiver l'environnement
```bash
deactivate
```

#### Exécuter le site

```bash
cd /path/to/Python-OC-Lettings-FR
source venv/bin/activate
pip install --requirement requirements.txt
python manage.py runserver
```
* Aller sur `http://localhost:8000` dans un navigateur.


#### Linting

```bash
cd /path/to/Python-OC-Lettings-FR
source venv/bin/activate
flake8
```


#### Tests unitaires

```bash
cd /path/to/Python-OC-Lettings-FR
source venv/bin/activate
pytest --cov=.
```

#### Panel d'administration

* Aller sur `http://localhost:8000/admin`
* Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`


## Accéder au rapport d'erreurs Sentry

https://sentry.io/organizations/daguincicode/projects/python-django/?project=4506503864451072